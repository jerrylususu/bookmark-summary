Title: Maybe the Fastest Disk Usage Program on macOS

URL Source: https://healeycodes.com/maybe-the-fastest-disk-usage-program-on-macos

Published Time: Fri, 01 Aug 2025 07:09:40 GMT

Markdown Content:
I set out to write the fastest `du -sh` clone on macOS and I think I've done it. On a large benchmark, [dumac](https://github.com/healeycodes/dumac) is 6.4x faster than `du` and 2.58x faster than [diskus](https://github.com/sharkdp/diskus) with a warm disk cache.

The odds were certainly in my favor as `diskus` does not use macOS-specific syscalls and instead uses standard POSIX APIs. As I'll go on to explain, I used [tokio tasks](https://docs.rs/tokio/latest/tokio/task/) and [getattrlistbulk](https://man.freebsd.org/cgi/man.cgi?query=getattrlistbulk&sektion=2&manpath=macOS+13.6.5) to be faster than the current crop of `du -sh` clones that run on macOS.

The Challenge
-------------

My benchmark is a directory with 12 levels, 100 small files per level, with a branching factor of two — 4095 directories, 409500 files.

`du -sh` (disk usage, summarize, human-readable) works out the total size of a directory by traversing all the files and subdirectories. It must list every file and retrieve each file's size (in blocks) to sum the total.

On Unix-like systems a directory listing, like `readdir`, or the `fts` family of traversal functions, only provide filenames and inode numbers. It doesn't provide file sizes. So `du` needs to call `lstat` on every single file and hardlink it comes across.

In my benchmark this means making 4k+ syscalls for the directories and 400k+ syscalls for the files.

The traditional `du` (from GNU coreutils or BSD) is typically single-threaded and processes one file at a time. It doesn't use multiple CPU cores, or overlapping I/O operations, meaning the work is handled sequentially.

On my Apple M1 Pro, the CPU is not saturated and the majority of the time is spent waiting on each sequential syscall.

time du -sh ./deep

1.6G ./deep

du -sh ./deep 0.04s user 1.08s system 43% cpu 2.570 total

The performance of disk usage programs depends on the filesystem and the underlying hardware. Benchmarks for these projects are usually done on Linux with a cold or warm disk cache. For the cold runs, the disk cache is cleared between each run.

I couldn't find a reliable way of clearing the disk cache on macOS. However, on macOS with modern Apple hardware, I found that the performance of disk usage programs with a warm disk cache strongly correlates with cold disk cache performance. So to make my life easier, warm disk cache results are the only thing I'm measuring and comparing.

Concurrency
-----------

Previously, when I wrote about [beating the performance of grep with Go](https://healeycodes.com/beating-grep-with-go), I found that just adding goroutines was enough to outperform the stock `grep` that comes with macOS.

My first attempt to write a faster `du -sh` in Go did not go so well. I expected that my quick prototype, focused on the core problem of traversing and summing the block size, would be faster.

var sem = make(chan struct{}, 16)

func handleDir(rootDir string, ch chan int64) {

size := int64(0)

// open()

dir, err := os.Open(rootDir)

if err != nil {

panic(err)

}

defer dir.Close()

// getdirentries64()

files, err := dir.Readdir(0)

if err != nil {

panic(err)

}

for _, file := range files {

sem <- struct{}{}

if file.IsDir() {

childCh := make(chan int64)

go handleDir(filepath.Join(rootDir, file.Name()), childCh)

childSize := <-childCh

size += childSize

} else {

// lstat64()

size += file.Sys().(*syscall.Stat_t).Blocks * 512

}

<-sem

}

ch <- size

}

It was slower than `du -sh`. It took twice as long on my benchmark.

./goroutines temp/deep 0.30s user 3.12s system 68% cpu 4.987 total

I ran a System Trace with macOS's Instruments to see what it was doing.

![Image 1: A list of system calls made by ./goroutines.](https://healeycodes.com/_next/image?url=%2Fposts%2Fmaybe-the-fastest-disk-usage-program-on-macos%2Fsyscalls.png&w=1920&q=100)

The high amount of `lstat64` calls is expected. That's fetching the attributes of each file. The `open` and `close` calls are also expected, roughly one per directory.

`getdirentries64` calls is twice the number of directories in my benchmark. This is because it's designed to read directory entries into a buffer until it gets an empty result. This is the syscall that Go's `Readdir` uses under the hood on macOS.

The other syscalls here are related to the scheduling of goroutines and channels. I tried a few different designs (and different sized semaphores on the I/O) but it didn't affect performance that much.

I ran a CPU profile with pprof and saw that the majority of the time was spent doing the syscalls I saw above.

![Image 2: A Go CPU profile.](https://healeycodes.com/_next/image?url=%2Fposts%2Fmaybe-the-fastest-disk-usage-program-on-macos%2Fgo-profile.png&w=1920&q=100)

My understanding at this point was that there is an inherent system resource cost to getting this information out, with some bandwidth/contention limitations, and some per-syscall Go overhead too.

I went looking for a more efficient method of getting this information out of the kernel without making a syscall for each file.

getattrlistbulk
---------------

macOS has a syscall called [getattrlistbulk(2)](https://man.freebsd.org/cgi/man.cgi?query=getattrlistbulk&sektion=2&manpath=macOS+13.6.5) which allows you to read multiple directory entries and their metadata in one go. It's like a combined "readdir + stat" that returns a batch of file names along with requested attributes like file type, size, etc.

Instead of calling `stat` for every file, one `getattrlistbulk` call can return dozens or hundreds of entries at once. This means far fewer syscalls for my benchmark!

First you open a directory (one `open` call) and then make a `getattrlistbulk` call which will retrieve an amount of entries that fits in the passed buffer (128KB was optimal in my testing), along with the attributes you need to do the same work as `du -sh` like name, inode, type, and size. You loop and call it again until the directory is fully read (it returns `0` when done).

I found some background on this syscall in a [mailing list](https://lists.apple.com/archives/filesystem-dev/2014/Dec/msg00004.html):

> Also note that as of Yosemite, we have added a new API: getattrlistbulk(2), which is like getdirentriesattr(), but supported in VFS for all filesystems. getdirentriesattr() is now deprecated.
> 
> 
> The main advantage of the bulk call is that we can return results in most cases without having to create a vnode in-kernel, which saves on I/O: HFS+ on-disk layout is such that all of the directory entries in a given directory are clustered together and we can get multiple directory entries from the same cached on-disk blocks.

My first attempt at wiring up this syscall used CGO. I wrote a C function that took a directory file descriptor and called `getattrlistbulk` in a loop until it had all the file info, and then returned the list of files and their attributes to Go.

// File info structure to track size and inode

typedef struct {

long blocks;

uint64_t inode;

} file_info_t;

// Directory information and subdirectory names

typedef struct {

file_info_t *files;

int file_count;

char **subdirs;

int subdir_count;

} dir_info_t;

// Get directory info (called from Go)

dir_info_t* get_dir_info(int dirfd) {

struct attrlist attrList = {0};

// Describe what we want back

attrList.bitmapcount = ATTR_BIT_MAP_COUNT;

attrList.commonattr = ATTR_CMN_RETURNED_ATTRS | ATTR_CMN_NAME | ATTR_CMN_ERROR | ATTR_CMN_OBJTYPE | ATTR_CMN_FILEID;

attrList.fileattr = ATTR_FILE_ALLOCSIZE;

// Set buffer size (affects number of calls required)

char attrBuf[128 * 1024];

int file_capacity = INITIAL_FILE_CAPACITY;

file_info_t *files = (file_info_t *)malloc(file_capacity * sizeof(file_info_t));

int file_count = 0;

int subdir_capacity = INITIAL_SUBDIR_CAPACITY;

char **subdirs = (char **)malloc(subdir_capacity * sizeof(char*));

int subdir_count = 0;

for (;;) {

int retcount = getattrlistbulk(dirfd, &attrList, attrBuf, sizeof(attrBuf), 0);

if (retcount == 0) {

break;

}

char *entry = attrBuf;

for (int i = 0; i < retcount; i++) {

// .. parsing code

The Go-side of this looks quite similar to my initial prototype. The C types are automatically generated on the Go-side in my editor and during `go build`. To turn the C pointers into a Go slice or struct, you use `unsafe` functions.

You also need to then free the C memory by calling into CGO again.

package main

// #cgo CFLAGS: -O3 -march=native -Wall -flto

// #include "lib.h"

import "C"

// ..

func handleDir(rootDir string) int64 {

dir, err := os.Open(rootDir)

// ..

info := C.get_dir_info(C.int(dir.Fd()))

// Free the C objects' memory

defer C.free_dir_info(info)

size := int64(0)

// Process files

if info.file_count > 0 {

files := (*[1 << 30]C.file_info_t)(unsafe.Pointer(info.files))[:info.file_count:info.file_count]

for _, file := range files {

size += int64(file.blocks) * 512

}

}

// Process subdirectories recursively

if info.subdir_count > 0 {

var wg sync.WaitGroup

var totalSize int64

subdirs := (*[1 << 30]*C.char)(unsafe.Pointer(info.subdirs))[:info.subdir_count:info.subdir_count]

for i, subdir := range subdirs {

wg.Add(1)

go func(index int) {

defer wg.Done()

childSize := handleDir(filepath.Join(rootDir, C.GoString(subdir)))

atomic.AddInt64(&totalSize, childSize)

}(i)

}

wg.Wait()

size += atomic.LoadInt64(&totalSize)

}

return size

}

The results were great. My Go program was now ~3x faster than `du -sh` for my benchmark.

./cgo temp/deep 0.07s user 3.70s system 443% cpu 0.850 total

I ran another CPU profile with pprof and saw that the majority of the time was spent in CGO, running my fairly optimized C code.

![Image 3: A Go CPU profile.](https://healeycodes.com/_next/image?url=%2Fposts%2Fmaybe-the-fastest-disk-usage-program-on-macos%2Fcgo-profile.png&w=1920&q=100)

This was where I wanted to spend CPU time: setting up the `getattrlistbulk` call, making it, and parsing the result. I optimized the buffer size (KB) and also tuned some of the memory allocations but then I hit a dead end. I couldn't get any faster without changing the overall design.

I had spent a few hours to get this far and now I wanted to go all the way. I knew that using CGO was suboptimal here because of the [overhead of calling into C from Go](https://groups.google.com/g/golang-dev/c/XSkrp1_FdiU). I've seen some sources suggest that the cost is 40ns for trivial calls. Along with some extra allocations on the Go side that I was having trouble getting rid of, I suspected the per-directory overhead to be higher.

I wanted to go all the way and see how fast I could push the performance here. So I ported my program to Rust.

Rust
----

By using Rust, I avoid a context switch between runtimes. I'm making the same C function call underneath, `libc::getattrlistbulk`, but it's a zero-cost abstraction. My program calls into the kernel many times from Rust, but without bouncing back and forth between Go and C on each directory.

I also needed a new concurrency primitive. An alternative to Go's goroutines. I picked [tokio tasks](https://docs.rs/tokio/latest/tokio/task/) as I understand them to be fairly analogous — light-weight, multiplexed green threads, and cheap to spawn.

// Calculate total size recursively

fn calculate_size(root_dir: String) -> Pin<Box<dyn Future<Output = Result<i64, String>> + Send>> {

Box::pin(async move {

// Get directory contents

let dir_info = tokio::task::spawn_blocking({

let root_dir = root_dir.clone();

// Make the libc::getattrlistbulk call

move || get_dir_info(&root_dir)

}).await.map_err(|_| "task join error".to_string())??;

let mut total_size = 0i64;

// Process files in this directory, deduplicating by inode

for file in &dir_info.files {

total_size += check_and_add_inode(file.inode, file.blocks);

}

// Process subdirectories concurrently with limiting

if !dir_info.subdirs.is_empty() {

let semaphore = Arc::new(Semaphore::new(MAX_CONCURRENT));

let futures: Vec<_> = dir_info.subdirs.into_iter()

.map(|subdir| {

let semaphore = semaphore.clone();

let subdir_path = Path::new(&root_dir).join(&subdir).to_string_lossy().to_string();

tokio::spawn(async move {

let _permit = semaphore.acquire().await.unwrap();

calculate_size(subdir_path).await

})

})

.collect();

// Collect all results

for future in futures {

match future.await {

Ok(Ok(size)) => total_size += size,

// ..

}

}

}

Ok(total_size)

})

}

Similar to my original Go prototype, it's a recursive traversal. I experimented with some concurrency limiting to avoid thrashing system resources and the overhead of context-switching and contention of threads. It didn't yield much performance improvements. Maybe 10% or so. I settled with a semaphore of 64.

`du -sh` deduplicates hardlinks so, while working concurrently, every time we sum the block size of a file, we need to lock and check whether we've seen the inode before.

I used a sharded inode set for this to lower the lock contention overhead.

// Sharded inode tracking

const SHARD_COUNT: usize = 128;

// Global sharded inode set for hardlink deduplication

static SEEN_INODES: LazyLock<[Mutex<HashSet<u64>>; SHARD_COUNT]> = LazyLock::new(|| {

std::array::from_fn(|_| Mutex::new(HashSet::new()))

});

In my final benchmark results, I've included diskus — a delightfully simple (and fast!) `du -sh` clone. It doesn't use macOS native APIs so it's a bit of an unfair comparison but it is the fastest `du -sh` clone I could find aside from my final Rust program which I've called dumac.

hyperfine --warmup 3 --min-runs 3 'du -sh temp/deep' 'diskus temp/deep' './goroutines temp/deep' './cgo temp/deep' './target/release/dumac temp/deep'

Benchmark 1: du -sh temp/deep

Time (mean ± σ): 3.330 s ± 0.220 s [User: 0.040 s, System: 1.339 s]

Range (min … max): 3.115 s … 3.554 s 3 runs

Benchmark 2: diskus temp/deep

Time (mean ± σ): 1.342 s ± 0.068 s [User: 0.438 s, System: 7.728 s]

Range (min … max): 1.272 s … 1.408 s 3 runs

Benchmark 3: ./goroutines temp/deep

Time (mean ± σ): 6.810 s ± 0.010 s [User: 0.290 s, System: 3.380 s]

Range (min … max): 6.799 s … 6.816 s 3 runs

Benchmark 4: ./cgo temp/deep

Time (mean ± σ): 564.6 ms ± 19.5 ms [User: 51.1 ms, System: 2634.2 ms]

Range (min … max): 542.6 ms … 591.0 ms 5 runs

Benchmark 5: ./target/release/dumac temp/deep

Time (mean ± σ): 521.0 ms ± 24.1 ms [User: 114.4 ms, System: 2424.5 ms]

Range (min … max): 493.2 ms … 560.6 ms 6 runs

Summary

./target/release/dumac temp/deep ran

1.08 ± 0.06 times faster than ./cgo temp/deep

2.58 ± 0.18 times faster than diskus temp/deep

6.39 ± 0.52 times faster than du -sh temp/deep

13.07 ± 0.61 times faster than ./goroutines temp/deep

I was able to remove ~43ms by moving from Go/CGO to Rust.

If my program is a success, it's because I've tried to reduce the cost of all of the work that is not optimal syscalls.

The time spent on syscalls is ~91% of the time in the below flamegraph. Locking for the inode deduplication is ~1.5% and the remaining time is the scheduling overhead of tokio.

![Image 4: The result of cargo flamegraph](https://healeycodes.com/_next/image?url=%2Fposts%2Fmaybe-the-fastest-disk-usage-program-on-macos%2Fflamegraph.png&w=1920&q=100)

Further Reading
---------------

I have [a version](https://github.com/healeycodes/dumac/blob/main/previousattamps/gosyscall/main.go) where I called `getattrlistbulk` from within Go like:

syscall.RawSyscall6(

SYS_GETATTRLISTBULK,

uintptr(fd),

uintptr(unsafe.Pointer(&attrList)),

uintptr(unsafe.Pointer(&attrBuf[0])),

uintptr(len(attrBuf)),

0, // options

0, // unused

)

But it was actually slower than using CGO.

The [dumac repository](https://github.com/healeycodes/dumac) contains the source code for [my attempts](https://github.com/healeycodes/dumac/tree/main/previousattamps) as I iterated towards my final Rust program.

I was inspired by the work behind [dut](https://codeberg.org/201984/dut) ([Show HN: Dut –a fast Linux disk usage calculator](https://codeberg.org/201984/dut)) which is sadly Linux-only. I'm fairly confident that some of the ideas behind it could be ported to macOS native APIs and supersede the performance of my program. Especially when it comes to reducing the overhead of tokio's scheduler.

There are also some fast disk usage programs that show useful, and in some cases interactive, terminal output like [dust](https://github.com/bootandy/dust) and [dua](https://github.com/Byron/dua-cli).

A fairly up-to-date blog post on the performance of reading directories on macOS is [Performance considerations when reading directories on macOS](https://blog.tempel.org/2019/04/dir-read-performance.html).

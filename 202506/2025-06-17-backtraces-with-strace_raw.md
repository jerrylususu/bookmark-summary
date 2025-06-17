Title: Backtraces with strace

URL Source: https://shane.ai/posts/backtraces-with-strace/

Published Time: 2023-11-06 16:22:00 -0700 -0700

Markdown Content:
I discovered [strace](https://man7.org/linux/man-pages/man1/strace.1.html) somewhere between my first part time web development part time job in 2005 and my first full time “software engineering” job in 2008, and it seemed like a superpower giving me x-ray vision into running infrastructure. When a process was stuck, or existing after a cryptic error message, instead of grepping around I could get a pretty good timeline of what the process was up to.

It has some fatal flaws, the `ptrace` based technology can cause performance issues so it’s mostly not suited to running in production (unless you were one of my personal heros: the old mysql@facebook team which liked to live dangerously and often used `ptrace` based debuggers to obtain life profiling data). If you’re intro history of performance engineering before `perf` and `ebpf` and friends, I highly recommend reading up on [poor mans profiler](https://dom.as/2010/10/08/more-on-pmp/).

After 15+ years I thought I knew most of the useful features, but last month I found a new incredibly useful flag: `--stack-traces`. It appears it was added in 2014 and I’m just finding out about it now! When you specify the `--stack-traces` flag strace will print the stack trace that resulted in the system call. I was debugging some complex signal handling interactions between Go and Cgo and while I knew someone was messing with the signal I didn’t know who. After a couple hours of grepping the entire codebase I just wasn’t sure how the code ended up doing what it did.

But I did something that works surprisingly often on the internet: I imagined the feature I wanted existed and googled for it (or looked at the man page), so after a quick look for “strace stack traces” I found the feature existed! When enabled it will cause `strace` to print stacktraces so you can see how the code got where it got. Let’s look at an example with a small `go` program to just get a feel for how a single DNS resolution is handled and how `--stack-traces` can help us understrand the architecture of an application.

stracing the pure go DNS resolver[⌗](https://shane.ai/posts/backtraces-with-strace/#stracing-the-pure-go-dns-resolver)
----------------------------------------------------------------------------------------------------------------------

Here is a simple go program that looks up the IP addresses associated with the `shane.ai` domain.

```
import (
        "net"
        "fmt"
)
func main() {
        names, err := net.LookupHost("shane.ai")
        if err != nil {
                panic(err)
        }
        for _, name := range names {
                fmt.Printf("%s\n", name)
        }
}
```

Now let’s inspect what this program does using strace. Today I want to know when it `connects` to a service and what code paths lead there. I’m going to use the Go DNS resolver as an example because Go ships with 2 DNS resolvers that we can compare via stack traces:

1.   A pure Go resolver (generally used when static linking and cross compiling) where go handles all I/O and incidentally avoids a [common](https://httptoolkit.com/blog/configuring-nodejs-dns/) issue with evented runtimes and libc dns
2.   A cgo based resolver which uses libc

First lets look at the highlights from the pure Go version. We see a couple of `SOCK_DGRAM` sockets opened in non-blocking mode (which makes sense since Go’s big thing is kind of non-blocking network I/O). We connect to `127.0.0.53` which is the system configured resolver on my machine. Note that my `main` function isn’t in the stack trace, so Go uses a separate goroutine for the lookup. My current understanding is this is part of ipv6 support and the [happy eyeballs](https://en.wikipedia.org/wiki/Happy_Eyeballs) algorithm which involves concurrent lookups for ipv4 & ipv6.

```
export GOMACPROCS=1
export GODEBUG=netdns=go
go build -trimpath -o dnscheck .
strace -fze socket,connect --stack-trace ./dnscheck 2>&1 | sed -e 's|/home/shane/src/||g' | head -50
```

```
strace: Process 88648 attached
strace: Process 88649 attached
strace: Process 88650 attached
strace: Process 88651 attached
strace: Process 88652 attached
[pid 88647] socket(AF_INET, SOCK_DGRAM|SOCK_CLOEXEC|SOCK_NONBLOCK, IPPROTO_IP) = 3
 > dnscheck/dnscheck(runtime/internal/syscall.Syscall6+0xe) [0x3aee]
 > dnscheck/dnscheck(syscall.RawSyscall+0x15) [0x7b5f5]
 > dnscheck/dnscheck(syscall.socket+0x25) [0x7afa5]
 > dnscheck/dnscheck(syscall.Socket+0x3d) [0x79f7d]
 > dnscheck/dnscheck(net.sysSocket+0x3a) [0xad65a]
 > dnscheck/dnscheck(net.socket+0x65) [0xadc25]
 > dnscheck/dnscheck(net.internetSocket+0xf1) [0xa77f1]
 > dnscheck/dnscheck(net.(*sysDialer).dialUDP+0xa5) [0xb1145]
 > dnscheck/dnscheck(net.(*sysDialer).dialSingle+0x2b2) [0x9a2b2]
 > dnscheck/dnscheck(net.(*sysDialer).dialSerial+0x248) [0x99b88]
 > dnscheck/dnscheck(net.(*sysDialer).dialParallel+0x3e5) [0x99245]
 > dnscheck/dnscheck(net.(*Dialer).DialContext+0x6de) [0x98c9e]
 > dnscheck/dnscheck(net.(*Resolver).dial+0xa5) [0xa96a5]
 > dnscheck/dnscheck(net.(*Resolver).exchange+0x36a) [0x9bbea]
 > dnscheck/dnscheck(net.(*Resolver).tryOneName+0x466) [0x9cd06]
 > dnscheck/dnscheck(net.(*Resolver).goLookupIPCNAMEOrder.func3.1+0x85) [0xa0165]
 > dnscheck/dnscheck(net.(*Resolver).goLookupIPCNAMEOrder.func3.2+0x27) [0xa00a7]
 > dnscheck/dnscheck(runtime.goexit.abi0+0x1) [0x65201]
[pid 88647] connect(3, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("127.0.0.53")}, 16) = 0
 > dnscheck/dnscheck(runtime/internal/syscall.Syscall6+0xe) [0x3aee]
 > dnscheck/dnscheck(syscall.Syscall+0x46) [0x7b646]
 > dnscheck/dnscheck(syscall.connect+0x29) [0x7ab49]
 > dnscheck/dnscheck(syscall.Connect+0x46) [0x79bc6]
 > dnscheck/dnscheck(net.(*netFD).connect+0x78) [0xa1958]
 > dnscheck/dnscheck(net.(*netFD).dial+0x3b2) [0xae2f2]
 > dnscheck/dnscheck(net.socket+0x294) [0xade54]
 > dnscheck/dnscheck(net.internetSocket+0xf1) [0xa77f1]
 > dnscheck/dnscheck(net.(*sysDialer).dialUDP+0xa5) [0xb1145]
 > dnscheck/dnscheck(net.(*sysDialer).dialSingle+0x2b2) [0x9a2b2]
 > dnscheck/dnscheck(net.(*sysDialer).dialSerial+0x248) [0x99b88]
 > dnscheck/dnscheck(net.(*sysDialer).dialParallel+0x3e5) [0x99245]
 > dnscheck/dnscheck(net.(*Dialer).DialContext+0x6de) [0x98c9e]
 > dnscheck/dnscheck(net.(*Resolver).dial+0xa5) [0xa96a5]
 > dnscheck/dnscheck(net.(*Resolver).exchange+0x36a) [0x9bbea]
 > dnscheck/dnscheck(net.(*Resolver).tryOneName+0x466) [0x9cd06]
 > dnscheck/dnscheck(net.(*Resolver).goLookupIPCNAMEOrder.func3.1+0x85) [0xa0165]
 > dnscheck/dnscheck(net.(*Resolver).goLookupIPCNAMEOrder.func3.2+0x27) [0xa00a7]
 > dnscheck/dnscheck(runtime.goexit.abi0+0x1) [0x65201]
[pid 88650] socket(AF_INET, SOCK_DGRAM|SOCK_CLOEXEC|SOCK_NONBLOCK, IPPROTO_IP) = 7
 > dnscheck/dnscheck(runtime/internal/syscall.Syscall6+0xe) [0x3aee]
 > dnscheck/dnscheck(syscall.RawSyscall+0x15) [0x7b5f5]
 > dnscheck/dnscheck(syscall.socket+0x25) [0x7afa5]
 > dnscheck/dnscheck(syscall.Socket+0x3d) [0x79f7d]
 > dnscheck/dnscheck(net.sysSocket+0x3a) [0xad65a]
```

stracing the cgo libc DNS resolver[⌗](https://shane.ai/posts/backtraces-with-strace/#stracing-the-cgo-libc-dns-resolver)
------------------------------------------------------------------------------------------------------------------------

Let’s see the difference when we use `cgo` on this ubuntu machine using systemd. `libc.so` ’s `getaddrinfo` is in the stack trace now. Also notice that it’s using a `AF_UNIX` unix domain socket for some communication. It looks like on my machine it’s an unused part of glibc where system dns can be accessed via a unix domain socket: `/var/run/nscd/socket`. There’s an explanation of [glibc’s behaviour here](https://jameshfisher.com/2018/02/05/dont-use-nscd/).

So after glibc wastes some time looking for a service that’s not running, it also opens up some `SOCK_DGRAM` sockets and as expected they are in blocking mode. Which means that like node, when Go uses the system resolver it has to use a threadpool instead of just using evented I/O. This has generally annoyed people because Go’s home rolled DNS resolver isn’t 100% compatible with glibc and sometimes that breaks things. Skipping glibc tends to annoy system administrators.

However accessing the “system” resolver via blocking `cgo` calls by default causes unexpected resource issues. People are often not really prepared for their Go programs to be running tons of threads, usually Go keeps threads near `GOMAXPROCS` which is by default equal to the number of cores on your machine. Having an outage due to thread pools where you expected to see a handful but instead saw 10k tends to annoy developers and users.

```
export GOMACPROCS=1
export GODEBUG=netdns=cgo
go build -trimpath -o dnscheck .
strace -fze socket,connect --stack-trace ./dnscheck 2>&1 | sed -e 's|/home/shane/src/||g' | head -50
```

```
strace: Process 90067 attached
strace: Process 90068 attached
strace: Process 90069 attached
strace: Process 90070 attached
strace: Process 90071 attached
[pid 90066] socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 3
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__socket+0xb) [0x12031b]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(svc_run+0x38b1) [0x169301]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(svc_run+0x3f01) [0x169951]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(svc_run+0x4397) [0x169de7]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(svc_run+0x1dea) [0x16783a]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(getaddrinfo+0x1b92) [0x103f42]
 > dnscheck/dnscheck(runtime.text+0x3b) [0x103b]
[pid 90066] socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 3
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__socket+0xb) [0x12031b]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(svc_run+0x38b1) [0x169301]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(svc_run+0x45d7) [0x16a027]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(svc_run+0x1f07) [0x167957]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(getaddrinfo+0x1b92) [0x103f42]
 > dnscheck/dnscheck(runtime.text+0x3b) [0x103b]
[pid 90066] socket(AF_INET, SOCK_DGRAM|SOCK_CLOEXEC|SOCK_NONBLOCK, IPPROTO_IP) = 3
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__socket+0xb) [0x12031b]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__res_randomid+0x199) [0x1473a9]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__res_context_send+0x2bf) [0x147e6f]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__res_context_query+0x1c1) [0x145de1]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__res_context_search+0x472) [0x146ac2]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(_nss_dns_gethostbyname4_r+0x251) [0x13e781]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(getaddrinfo+0x1ec0) [0x104270]
 > dnscheck/dnscheck(runtime.text+0x3b) [0x103b]
[pid 90066] connect(3, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("127.0.0.53")}, 16) = 0
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__connect+0x4b) [0x11fd2b]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__res_randomid+0xfd) [0x14730d]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__res_context_send+0x2bf) [0x147e6f]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__res_context_query+0x1c1) [0x145de1]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__res_context_search+0x472) [0x146ac2]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(_nss_dns_gethostbyname4_r+0x251) [0x13e781]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(getaddrinfo+0x1ec0) [0x104270]
 > dnscheck/dnscheck(runtime.text+0x3b) [0x103b]
[pid 90066] socket(AF_NETLINK, SOCK_RAW|SOCK_CLOEXEC, NETLINK_ROUTE) = 3
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__socket+0xb) [0x12031b]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__idna_from_dns_encoding+0x25b) [0x13be6b]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(getaddrinfo+0x1273) [0x103623]
 > dnscheck/dnscheck(runtime.text+0x3b) [0x103b]
[pid 90066] socket(AF_INET, SOCK_DGRAM|SOCK_CLOEXEC, IPPROTO_IP) = 3
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__socket+0xb) [0x12031b]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(getaddrinfo+0xd53) [0x103103]
 > dnscheck/dnscheck(runtime.text+0x3b) [0x103b]
[pid 90066] connect(3, {sa_family=AF_INET, sin_port=htons(0), sin_addr=inet_addr("185.199.111.153")}, 16) = 0
 > /usr/lib/x86_64-linux-gnu/libc.so.6(__connect+0x4b) [0x11fd2b]
 > /usr/lib/x86_64-linux-gnu/libc.so.6(getaddrinfo+0xa93) [0x102e43]
```

Wrap up[⌗](https://shane.ai/posts/backtraces-with-strace/#wrap-up)
------------------------------------------------------------------

That’s all folks. I hope that you don’t need it, but if you ever do find yourself asking: “what code is touching that thing!?” `strace --stack-traces` I hope you’ll land on this post and find that `strace` is at your service.

Maybe in the future I’ll look at converting `strace --stack-traces` output to something compatible with [mozilla’s trace viewer](https://profiler.firefox.com/). That sounds fun.

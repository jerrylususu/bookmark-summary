Title: Can You Get Root With Only a Cigarette Lighter?

URL Source: https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html

Markdown Content:
_By David Buchanan, 7th October 2024_

Spoiler alert: **Yes**.

![A regular bright-orange cigarette/barbecue lighter](blob:https://www.da.vidbuchanan.co.uk/98b5578b91a50c5457e165fd2dd60b0e) _the elite hacking tool they don't want you to know you already own_

Before you can write an exploit, you need a bug. When there are no bugs, we have to get creative—that's where [Fault Injection](https://en.wikipedia.org/wiki/Fault_injection) comes in. Fault injection can take many forms, including software-controlled data corruption, power glitching, clock glitching, electromagnetic pulses, lasers, and more.

Hardware fault injection is something that typically requires specialized (and expensive) equipment. The costs stem from requiring a high degree of precision in terms of both _when_ and _where_ the fault is injected. There are many valiant attempts at bringing down the costs, with notable projects ranging from the RP2040-based [PicoEMP](https://github.com/newaetech/chipshouter-picoemp), all the way to ["Laser Fault Injection for The Masses"](https://blog.fraktal.fi/laser-fault-injection-for-the-masses-1860afde5a26). (The RP2040 crops up a lot due to its low cost combined with the ["PIO"](https://www.raspberrypi.com/news/what-is-pio/) peripheral, which can do I/O with tight timings and latency)

A while back I read about using a [piezo-electric](https://en.wikipedia.org/wiki/Piezo_ignition) [BBQ Igniter](https://hackaday.com/2022/01/29/blast-chips-with-this-bbq-lighter-fault-injection-tool/) coupled to an inductor as a low-budget tool for electro-magnetic fault injection (EMFI), and I was captivated. I wondered, how far can you take such a primitive tool? At the time, the best thing I could come up with was exploiting a software implementation of AES running on an Arduino, using [DFA](https://github.com/SideChannelMarvels/Deadpool/blob/master/README_dfa.md)—it worked!

But I wasn't fully satisfied. I wanted to exploit something more "real," but I was out of ideas for the time being.

Fast forward to a couple of weeks ago, and the announcement of the Nintendo Switch 2 is [on the horizon](https://old.reddit.com/r/GamingLeaksAndRumours/comments/1fjp352/photos_of_switch_2_factory_prototypes_have_leaked/). We anticipate the Switch 2 will run largely the same system software as the Switch 1, and we're all out of software bugs. So, I was inspired to brush up on my hardware exploitation skills, and revisited my thoughts on low-budget EMFI.

[The Test Subject](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#the-test-subject)
-----------------------------------------------------------------------------------------

Like any self-respecting hacker, I own a pile of junk laptops. I picked out a Samsung S3520, equipped with an Intel i3-2310M CPU and 1GB of DDR3 RAM. Manufactured in 2011, it's new enough that it can comfortably run a lightweight desktop Linux distro (I picked Arch), but crappy enough that I wasn't worried about bricking it.

**My goal is to write a local-privilege-escalation exploit that works based on injected hardware faults.**

I decided that the most physically vulnerable part of the laptop was the DDR bus that connects the DRAM memory to the rest of the system.

If you've ever looked at a laptop memory module (SODIMM), you'll notice it has a whole lot of pins. Among them are 64 "DQ" pins (numbered DQ0 to DQ63) that transfer data bits in either direction (read or write). I figured that if I could inject faults on one of these pins, I could do _something_ interesting.

After a lot of fiddling around, here's the hardware setup I came up with:

![a DDR3 SODIMM with a wire soldered to one of the data lines](blob:https://www.da.vidbuchanan.co.uk/0af0164657decdecca10f173801c8caf) _If I counted right, this corresponds to pin 67, aka DQ26_

It's just one resistor (15 ohms) and one wire, soldered to DQ26. The wire acts like an antenna, picking up any nearby EM interference and dumping it straight onto the data bus. The resistor (which might be entirely unnecessary) is just there to make sure that the interference isn't so great as to disturb normal operation of the memory—I only want glitches to happen on-demand, not all the time.

![a laptop running memtest86+, showing two errors](blob:https://www.da.vidbuchanan.co.uk/80cbb34482ea206255ace4d848fdd9e5) _Ignore the random electrical tape; this laptop has been through a lot._

I found that clicking a regular piezo-electric lighter (no inductor coils needed) in the vicinity of the antenna wire was enough to reliably induce memory errors, shown here under memtest. Note that the errors shown both correspond to bit 29 being flipped.

Why bit 29, when I soldered to DQ26? Honestly, I'm not entirely sure; either I miscounted the pins or my laptop's motherboard swaps some of the data lines around. As far as I can tell, swapping data lines like that _is_ allowable (it can make signal routing easier).

We don't have much control over _when_ we inject the fault (to the resolution of my finger's reaction speed), but whenever it happens we can be fairly certain it will always flip the same bit of any particular 64-bit read or write.

[Exploiting Bit-flips in CPython](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#exploiting-bitflips-in-cpython)
----------------------------------------------------------------------------------------------------------------------

As a starting point, I wanted to try writing a "sandbox escape" exploit for CPython. This is purely academic since CPython isn't even sandboxed in the first place and you can just do `os.system("/bin/sh")`, but I needed something easy to get started with and I'm already familiar with CPython's internals. My explanation for this exploit is going to be a bit hand-wavey because the specifics aren't that interesting, it's the overall strategy that I want to convey.

For exploiting CPython, I actually used a wire soldered to DQ7 instead of the DQ26 pictured earlier, for reasons that will become more obvious shortly.

CPython objects live on a garbage-collected heap. An object has a header that contains its refcount, then a pointer to its type object, followed by other type-specific fields. There are two object types of particular interest to us, `bytes` and `bytearray`. `bytes` objects are immutable and `bytearray` objects are mutable.

A `bytes` object has a length field, followed by the data itself (as part of the same heap allocation).

A `bytearray` object has a length field followed by a _pointer_ to the actual data storage buffer.

The core idea of my exploit strategy is to instantiate a `bytes` object that contains a fake `bytearray` structure within it. The fake `bytearray` object is just data, we can't _do_ anything with it, but if we trick CPython into giving us a reference (pointer) to this fake object, then we can construct an arbitrary memory read/write primitive (since we chose the `bytearray`'s length and pointer fields ourselves).

So how do we get a reference to the fake object? Recall that our initial "exploit primitive" is the ability to flip bit 7 of a 64-bit word. This is equivalent to either adding or subtracting 128 (27) from a pointer. If our fake `bytearray` object was at an offset of +128 bytes within the `bytes` object, then glitching a pointer to the `bytes` object will transform it into a pointer to the crafted `bytearray` object (with 50% probability).

So the big question is, how do we glitch that specific pointer, as opposed to everything else? If we accidentally glitch some important data we'll probably crash the whole OS, which is obviously not good.

Something important to remember is that we're glitching the memory _bus_, not the memory _contents_ (as in something like [Rowhammer](https://googleprojectzero.blogspot.com/2015/03/exploiting-dram-rowhammer-bug-to-gain.html)). We only glitch the read and write operations, the data "at rest" is mostly safe. The solution here is to spam memory accesses of the pointer we want to glitch. If 99% of bus activity is saturated with exploitable operations, then a randomly timed glitch has (in theory) a 99% chance of landing somewhere we want it to.

If we read the same pointer in a loop, almost nothing would happen. This is because the CPU caches the data to avoid unnecessary DRAM accesses (cache is fast, DRAM is comparatively slow and high-latency).

My solution was to fill up a big array (larger than the 3MiB cache this CPU has) with references to the same object. Then I can access the array items sequentially in a loop, forcing the CPU to fetch them from DRAM each time, and check to see if their value changed. The inner loop looks like this:

\# "victim" is the prepared \`bytes\` object described earlier
spray \= (victim,) \* 0x100\_0000 \# I actually use a tuple instead of an array, same idea

for obj in spray:
    if obj is not victim: \# under non-glitchy conditions, this is always false
        print("Found corrupted ptr!")
        assert(type(obj) is bytearray)

Most of the time this won't work, so the whole thing is done from inside another big loop, until it does work (or until the system crashes 🙃).

Python's `is` keyword comes in handy here, it's essentially a pointer comparison operation, allowing us to check if the pointer changed. Visualising the objects in memory, it looks like this:

![](blob:https://www.da.vidbuchanan.co.uk/bc45692bb7b59362f88918e59483d5c6)

A "glitched" pointer is shown in red, which is now able to access the fake bytearray object. The glitch itself could occur during _either_ a write or a read, the net result is the same either way. The rest of the exploit isn't especially interesting; I set up a repeatable read/write primitive and then craft a Function object that jumps to shellcode. You can see the full source [here](https://github.com/DavidBuchanan314/dram_emfi/blob/ccd7f254e0a2bc8ba02708d6228ea03e16330de7/ddr3_dq7.py). The script also has an option (the `TESTING` variable) to induce simulated bit-flips through software, which is useful for testing without any hardware setup.

[Exploiting Bit-flips in Linux](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#exploiting-bitflips-in-linux)
------------------------------------------------------------------------------------------------------------------

Now that we've warmed up, it's time for a proper security boundary crossing. Can we get from an unprivileged Linux user, to root? There are three core concepts we need to understand first:

*   Memory caching (which I already touched on)
*   Virtual Memory and Page Tables
*   The Translation Lookaside Buffer (TLB)

### [Memory Caching](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#memory-caching)

As I mentioned earlier, DRAM is (relatively) slow and high-latency. So the CPU has on-die caches, which are faster. These caches have multiple tiers (L1, L2, L3) with different size/locality/latency trade-offs, but for our purposes we only have to care about the L3 cache (the largest layer, 3MiB in this case). If data currently resides in cache (a "cache hit"), the CPU won't need to access DRAM to read it. If there's a "cache miss" on the other hand, the CPU will have to reach out to DRAM.

The smallest unit of memory from the caching perspective is a ["cache line"](https://stackoverflow.com/a/3947435), and on my laptop that's a 64-byte chunk. That means that if you read even a single byte that isn't cached, a whole 64-byte DRAM read operation takes place. You may recall that the DRAM data bus itself was only 64 _bits_ wide, which means the read happens in a "burst" of 8 sequential accesses.

The precise policy the CPU uses to decide which data to keep in the cache, and when to "evict" it, is effectively a vendor-proprietary secret. But as a reasonable approximation we can model it as a LRU cache: least-recently-used cache lines get evicted first.

### [Virtual Memory](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#virtual-memory)

Back in the old days, simple CPUs like the [MOS 6502](https://en.wikipedia.org/wiki/MOS_Technology_6502) had a "flat" address space. If your program tried to read from address `0xcafe`, then the CPU would physically set the 16-bit address bus pins to `0xcafe` (`0b1100101011111110`) and read back a byte from that location. Aside from hardware tricks like [bank switching](https://en.wikipedia.org/wiki/Bank_switching), the address you requested was the address you got data back from. Simple as!

![](blob:https://www.da.vidbuchanan.co.uk/94912be3a9ca375caac1a5186773116d) _My 6502 computer, built many years ago (the USB-C port is a contemporary addition). Note the D0-D7 data pins and A0-A15 address pins._

Fast forward a number of years, and we want to run more than one program at once on our CPUs. Furthermore, each program should be tricked into believing it has the whole address space all to itself. This is useful for a lot of reasons, including that it stops one process from being able to clobber another process's memory (accidentally or otherwise).

In the modern era, we call this trick Virtual Memory. Virtual Memory means that there's a layer of indirection between the address a program tries to access (the virtual address), and the underlying physical address space. Each process can have its own virtual-\>physical mappings, keeping different processes isolated from each other.

On x86-64 (and most other modern architectures), this indirection is implemented using the concept of [Paging](https://wiki.osdev.org/Paging).

The virtual address space is split up into 4KiB _Pages_, and a tree-structured hierarchy of _Page Tables_ dictates how the CPU (specifically the [MMU](https://en.wikipedia.org/wiki/Memory_management_unit)) decodes virtual addresses and maps them onto physical pages. On this platform there are 4 layers of Page Tables. Officially the 4 layers all have different names, but I'm going to call them "level 3" to "level 0", with level 3 being the root of the tree. A Page Table is itself a 4KiB page, containing an array of 512 Page Table Entries (PTEs), each a 64-bit structure. A PTE either points to the physical address of the next-level Page Table (in the case of levels 3 to 1), or the physical address of the "destination" page (in the case of level 0).

The physical address of the root page table is stored in the CR3 CPU register.

The PTEs themselves have the following layout (diagram via osdev wiki)

![](blob:https://www.da.vidbuchanan.co.uk/72d98aa44aef6f2a5e2cd443d3e540d5)

The only part that we need to care about is the address portion, in the middle. When you mask off all the flag bits, you're left with a physical memory address (since pages are 4K-aligned, the low bits are always zero).

For a probably-better explanation along with some diagrams, check out [this article](https://os.phil-opp.com/page-tables/) from "Writing an OS in Rust" (note that they number the levels 4 to 1, which is probably more conventional 😅).

### [The Translation Lookaside Buffer](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#the-translation-lookaside-buffer)

If the process of traversing page tables to resolve a virtual address sounds expensive, that's because it is. That's where the [TLB](https://en.wikipedia.org/wiki/Translation_lookaside_buffer) comes in. It's a specialized piece of hardware inside the CPU that efficiently caches virtual-to-physical page mappings. The TLB has a finite size, and I don't actually know the size for my laptop but from what I can tell, it's somewhere on the order of 1024 entries (note that each entry corresponds to a whole page-sized mapping).

[Exploit Strategy](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#exploit-strategy)
-----------------------------------------------------------------------------------------

My exploit strategy was inspired by elements of Mark Seaborn's [Rowhammer exploit](https://googleprojectzero.blogspot.com/2015/03/exploiting-dram-rowhammer-bug-to-gain.html). The main goal is to get a Page Table for our own process mapped into user-accessible memory. Once we have that, we can modify the PTEs within it to grant ourselves access to arbitrary physical memory, which is essentially the keys to the kingdom.

Rather than try to control the layout of structures in physical memory (A physical-memory version of [heap feng shui](https://en.wikipedia.org/wiki/Heap_feng_shui), I suppose?), my strategy is to fill up (aka "spray") as much of physical memory as possible with level-0 page tables. In practice I fill exactly 50% of physical memory.

Once the spray is complete, I sit in a loop trying to access a bunch of R/W mappings in a way that bypasses the TLB (because the number of mappings exceeds the TLB size), forcing a page table traversal on each access. I want to glitch the memory bus during that traversal in order to corrupt bit-29 of a level-0 PTE read. If I'm lucky (with about 50% odds) the glitch will offset the physical address that the PTE points to, making it point to one of the level-0 page tables that we sprayed earlier.

This should theoretically work with bit-flips in any bit position between 29 (corresponding to a 512MiB offset) and 12 (corresponding to a 4KiB offset). It just matters that the PTE ends up pointing "somewhere else," and because we've filled up ~50% of physical memory with exploitable page tables, we have a good chance of success. Therefore, soldering the antenna wire perhaps isn't totally necessary, if you can generate strong enough electromagnetic interference (although you'd have much higher chances of crashing or even bricking the whole system that way).

Here's a visualisation of how the fault affects the page tables:

![](blob:https://www.da.vidbuchanan.co.uk/045af254b278526e6cc8ccf0dba3754b)

Each of the blocks in this diagram represent a 4K page of physical memory. Their locations within memory are more or less random, and aren't relevant to the exploit logic. What does matter is what points to what. The glitched PTE (in red) is supposed to point to the R/W page, but now it points to another level-0 page table, providing access to it _as if_ it were a regular R/W page. In practice there are thousands more of these level-0 pages, and the glitched PTE could've ended up pointing to any one of them, but I can only fit so many on the diagram.

So how do I spray so many level-0 page tables?

First, I create a [memfd](https://man7.org/linux/man-pages/man2/memfd_create.2.html), which is a relatively modern Linux feature. It fills the same role as the `/dev/shm/` file in Mark Seaborn's exploit, but without having to touch the filesystem at all. Then I use the [mmap](https://man7.org/linux/man-pages/man2/mmap.2.html) syscall to map this same buffer into memory, many times over. I use the `MAP_FIXED` option to force each mapping to be 2MiB-aligned in virtual memory, which guarantees the creation of a new level-0 page table each time. Linux has a ~216 limit to the number of mappings (VMAs, Virtual Memory Areas) that each process is allowed, so I make each mapping 32MiB long. This means each one generates 16 level-0 page tables. Although each mapping takes up 32MiB of virtual memory space, the PTEs all point to the exact same underlying physical pages. The physical memory cost of each mapping consists _only_ of the level-0 page tables, and therefore I can spray as many of them as I want, until memory is full.

As I said before, we attempt to access the R/W mappings in a loop, waiting for a fault to happen. We can detect a fault because an unexpected value will come back, and if it was successful then the data should look like a PTE. If so, we now have R/W access to a page table. The next step is to figure out which virtual address this page table corresponds to. I do this by modifying the PTE to point at physical address 0 (which is an arbitrary choice, any address should work really) and then scanning the R/W mappings again to see which one changed, if any.

The MMU won't immediately "notice" edits to the PTE, because the virtual-\>physical address mappings are cached by the TLB. Every time we change it, we need to flush the TLB. There's no direct way of doing this from userspace (that I know of?) so instead I just access a few thousand of the R/W mappings in a loop, forcing the TLB to fill up with new values and evict the old ones.

At this point, we have full read/write access to all of physical memory! There are a bunch of strategies we could use from this point onwards, and again I took inspiration from the Rowhammer exploit. I open the `/usr/bin/su` executable (which is [setuid root](https://en.wikipedia.org/wiki/Setuid)) nominally in read-only mode (I don't have write permissions!) and mmap the first page of it. Then, I scan through all of physical memory until I find that same page. Once I've found the physical page, I have full write access to it, and I replace it with my own tiny (<4KiB) ELF [program](https://github.com/DavidBuchanan314/dram_emfi/blob/ccd7f254e0a2bc8ba02708d6228ea03e16330de7/payload/gimme_shell.c) that spawns a root shell. This effectively poisons Linux's page cache.

The next time someone (me) tries to invoke the `su` binary, Linux knows it already has the first page in memory and doesn't try to read it from disk again. So it re-uses that cached page, and starts executing our injected ELF instead. Game over!

My injected ELF also flushes the page cache (`echo 1 > /proc/sys/vm/drop_caches`), so the _next_ time someone invokes `su` it functions normally again.

My full exploit source can be found [here](https://github.com/DavidBuchanan314/dram_emfi/blob/ccd7f254e0a2bc8ba02708d6228ea03e16330de7/linux_x86_64_lpe.c).

Here's a demo video (sorry it's a bit blurry):

I was unusually lucky on this run, normally it takes several clicks of the lighter to get a good glitch. Not shown are the several previous attempts that crashed the whole system! I'm not sure what the overall exploit reliability is, I haven't tried to measure it rigorously. When the laptop's screen is off and I'm SSHed in it feels like it's around 50%. But when I'm at a graphical shell like in the demo, it's maybe closer to 20% reliability. This system has integrated graphics, so perhaps the GPU's memory accesses interfere with the exploit. There are also various background services running (pipewire, sshd, systemd stuff etc.), and swap is enabled too. I wanted it to be a fairly realistic desktop Linux environment, and disabling all these things would probably increase reliability.

If the laptop had more RAM installed, I'd be able to fill an even higher percentage of it with page tables, which should also increase the overall exploit reliability.

[Practical Uses](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#practical-uses)
-------------------------------------------------------------------------------------

As cool as my Linux LPE is, I already had root on that laptop because it's mine. Is there anything more "useful" we can do with it?

I'm not much of a PC gamer (more of a Nintendo fanboy), but I'm always irked when I see "anti-cheat" software that uses technologies like TPM to restrict the software you're allowed to run on the rest of your system. Perhaps a reliable EMFI Windows LPE would let gamers take back control of their PCs without interfering with TPM attestation status.

Imagine a future where "Gaming RAM" sticks have a RP2040 on board to automate the whole exploit (and also drive the RGB LEDs, of course).

There's a similar story with Android devices and SafetyNet/Play Integrity checking, although fitting a glitching modchip into a phone would be more of a challenge.

[Thoughts](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#thoughts)
-------------------------------------------------------------------------

On a conceptual level, I've known about page tables and TLBs for a long time. But even when working on low-level performance optimizations, that knowledge has never actually _mattered_ to me (Caching on the other hand becomes relevant all the time!) But in this exploit, all of it absolutely does matter, and it's been very satisfying to finally test that theoretical knowledge.

Actually seeing and interacting with the structures that maintain the illusion of virtual memory felt a bit like escaping the matrix.

[Open Questions](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html#open-questions)
-------------------------------------------------------------------------------------

*   Does it work on DDR4, DDR5? (I don't see any reason why not!)
*   Does it work on ARM? (Likewise)
*   To what extent do the various types of ECC mitigate this? (DDR5 Link-ECC in particular)
*   What's the simplest way to trigger similar faults electronically? (say, with an RP2040)
*   Can you use this to break out of a hypervisor?
*   Can I write a Webkit exploit with this?
*   Can I write a Nintendo Switch kernel exploit with this?

I'm going to be looking into these in the future—stay tuned!

Finally, I'd like to thank JEDEC for paywalling all of the specification documents that were relevant to conducting this research.

Title: The Linux Boot Process: From Power Button to Kernel

URL Source: https://www.0xkato.xyz/linux-boot/

Published Time: 2025-10-25T13:37:00+00:00

Markdown Content:
*   [Home](https://www.0xkato.xyz/)
*   [Blog](https://www.0xkato.xyz/blog)
*   [Research](https://www.0xkato.xyz/projects)
*   [About](https://www.0xkato.xyz/about)
*   [Portfolio](https://github.com/0xkato/Portfolio/tree/main)

Saturday. October 25, 2025 -  15 mins

Part 1 — From power button to the kernel’s first breath
-------------------------------------------------------

You press the power button. A second later a wall of text scrolls by, or a logo fades in, and eventually Linux appears. What happens in between is not magic. It is a careful handshake between tiny programs and a very literal CPU. This part follows that handshake until the very first line of C code inside the Linux kernel runs.

### The very first instruction

When power stabilizes, the CPU resets itself to a tiny, old‑fashioned mode called real mode. Real mode dates back to the original 8086 chip. The rules are simple on purpose. Memory addresses are built from two values the CPU keeps in special fast storage called registers. You combine a segment and an offset like this:

`physical_address = (segment << 4) + offset`

If you see numbers like `0xFFFFFFF0`, that is hexadecimal. Hex is base 16. We write `0x` in front to make that clear. `0x10` is 16 in everyday counting. `0x100000` is 1 megabyte. Hex lines up nicely with how hardware stores bits, which is why you see it everywhere in low‑level code.

Right after reset the CPU jumps to a special address called the reset vector at `0xFFFFFFF0`. Think of it as a permanent bookmark that says “start here.” There is room for almost nothing at that address, so manufacturers put a far (long) jump there that passes control to the firmware on your motherboard.

**Tiny explainer: register** A register is a tiny slot inside the CPU. It holds a number the CPU is using right now. Names like CS and IP are register names. CS means “code segment,” which marks the current neighborhood for instructions. IP means “instruction pointer,” which marks which instruction comes next.

### BIOS and UEFI

The firmware is a small starter program baked into your board.

BIOS stands for Basic Input Output System. It is the older style. BIOS does a quick health check called POST, looks at the boot order, and tries each device. If it finds a disk whose very first 512‑byte sector ends with the marker bytes `0x55` and `0xAA`, it treats that device as bootable. BIOS copies that sector to memory at `0x7C00` and jumps there. That sector is tiny, so it usually knows only how to load the next, larger piece.

UEFI is the modern replacement. It still starts the machine, but it understands filesystems directly and can load bigger boot programs without the old “first sector” dance. UEFI also passes richer information to the operating system. Different path, same goal: hand control to a boot program that can load Linux.

### Meet the bootloader

The bootloader is the usher that gets the operating system into place. GRUB is a popular choice on PCs. It reads its configuration, shows a menu if you installed one, and loads the Linux kernel into memory. The Linux kernel file actually contains two things:

*   a small setup program that still runs in real mode
*   the larger compressed kernel that will be unpacked a little later

GRUB also fills out a small structure called the setup header with useful facts: where it placed the kernel, where the command line lives, where the initrd is if you have one. Then it jumps into the setup program.

### The setup program makes a safe room

Before Linux can do anything interesting, the setup code creates a predictable workspace.

It lines up the segment registers so memory copies behave the same way every time. Names you’ll see here are CS for code, DS for data, and SS for stack. It also clears a single CPU bit called the “direction flag” so copy instructions move forward through memory.

It creates a stack. The stack is a last‑in, first‑out workbench where functions store temporary values. SS says which segment the stack uses. SP is the pointer to the current top of the stack.

It clears a region called BSS. BSS is where global variables that must start as zero live. C code assumes BSS is zero. The setup program writes zeros over that entire span to keep that promise.

If you passed `earlyprintk` on the kernel command line, the setup code also programs the serial port so it can print very early messages. This is useful when graphics are not ready yet.

Finally the setup program asks the firmware “how much usable RAM do we really have and where are the holes.” On old BIOS this is a call people often nickname e820, which returns a simple list of usable and reserved ranges. The kernel will use that list to avoid stepping on the firmware’s toes.

With that done, the setup code calls its first C function, which is literally named `main`. We are still in the small old real mode at this point. The next job is to leave it.

**Tiny explainer: interrupt** An interrupt is a hardware or software “excuse me” that pauses what the CPU is doing and runs a small handler for something urgent. A timer tick is an interrupt. A key press is an interrupt. There are two flavors here. Maskable interrupts follow your rules and can be temporarily blocked so they do not fire during delicate moments. Non‑maskable interrupts, often called NMI, always cut in because they usually report serious hardware issues. We will control both while switching modes so nothing surprises us halfway through.

Part 2 — Leaving real mode, stepping through 32‑bit land, and arriving in 64‑bit
--------------------------------------------------------------------------------

Modern Linux on PCs runs in long mode, which is the 64‑bit mode of x86_64. You cannot jump there directly from real mode. The path is real mode to protected mode and then protected mode to long mode. This part covers that path and explains the vocabulary on the way.

### Protected mode, without the jargon haze

Protected mode is the 32‑bit world introduced to get past the limits of the 1980s. It adds two central ideas.

The Global Descriptor Table, or GDT, is a short list of segment descriptions. A description says “this segment starts here, covers this much, and is allowed to do these things.” Linux keeps this simple. It uses a flat model, which means the base is zero and the size covers the whole 32‑bit space. When everything is flat, addresses look like plain numbers again.

The Interrupt Descriptor Table, or IDT, is a directory of “phone numbers” for emergency calls. If an interrupt arrives, the CPU looks up the entry in the IDT and jumps to the handler listed there. During the switch we load a tiny placeholder IDT because we are about to block interrupts anyway. The full‑featured IDT arrives later once the real kernel is in charge.

### The careful switch

The setup code turns off the noisy parts first. It disables maskable interrupts with a single instruction. It quiets the old PIC chips so hardware interrupts are fully blocked for a moment. It opens the A20 line. This is a historical quirk. Early PCs made addresses wrap at 1 megabyte. Opening A20 removes that wrap so higher addresses work like you expect. It resets the math coprocessor so the floating point state is clean.

Then it loads a tiny GDT with only what we need right now and a tiny IDT. Finally it sets a single bit named PE in a control register named CR0 and performs a far jump. That jump reloads the code segment from the GDT and locks in protected mode. It reloads the data and stack segments and fixes the stack pointer to match the new flat world.

We are now in 32‑bit protected mode.

**Tiny explainer: control registers** The CPU has a few special registers for on off switches. CR0 turns on protected mode. CR3 holds the address of the top of the page tables, which we will need in a second. CR4 enables a set of extended features such as larger page table entries.

### Why we still are not done

Linux wants 64‑bit. That is long mode. Two things are needed.

Paging must be on. Paging is the translator between virtual addresses and physical addresses. Programs use virtual addresses. The hardware reads and writes physical memory. Page tables map one to the other in fixed‑size chunks called pages. On PCs a normal page is 4 kilobytes. There are also bigger pages. Early in boot the kernel uses 2 megabyte pages to describe low memory quickly.

A single bit named LME in a special register called EFER must be set to allow long mode. EFER is a model specific register, which is a fancy way of saying “a register used for certain CPU features.”

### Building just enough paging

The 32‑bit prologue builds a small set of page tables that say “for this region, virtual equals physical.” That is called an identity map. It is enough to flip paging on safely.

To make this work the code enables PAE in CR4 so larger entries are used. It builds a minimal set of tables that cover low memory in 2 megabyte chunks. It writes the address of the top table into CR3. Paging is now ready.

Finally it sets LME in EFER and performs a far return into a label that is written as 64‑bit code. Long mode is now active. Segments are still “flat,” but addresses and registers are 64‑bit wide.

**Why all the extra care** Switching modes while a live system runs is like changing a car tire while rolling. The code blocks interruptions, prepares the minimum needed tables, flips the bit, and only then invites interrupts back. Slow and steady prevents weird half‑switched states.

Part 3 — Unpacking the real kernel, fixing addresses, and why Linux sometimes moves itself
------------------------------------------------------------------------------------------

We have a 64‑bit CPU with paging on and a compressed kernel in memory. Now the small 64‑bit stub does the practical work: get out of the way if needed, unpack the kernel, fix addresses if the kernel is not at its default spot, and jump.

### Clearing a path and setting safety nets

The stub first figures out where it is actually running. Early code is linked as if it lived at address zero and then computes its real base at runtime. If the planned destination for the decompressed kernel would overlap the stub, it copies itself to a safe place.

It clears its own BSS so global state starts clean.

It loads a minimal IDT with two handlers. One for page fault and one for NMI. A page fault happens when the CPU cannot find a mapping for a virtual address it just tried to use. In our early identity‑mapped world, the tiny page fault handler can add the missing mapping on the fly and continue. The NMI handler is there so a non‑maskable interrupt does not crash the machine while we are still bringing things up.

It also builds identity mappings for the regions it will touch next. That includes the future home of the kernel, the small boot parameters page the bootloader filled in, and the command line buffer.

### Decompressing Linux…

A C function commonly named `extract_kernel` takes over. It sets aside a tiny heap for temporary buffers, prints the classic line, and unpacks the kernel using whatever algorithm the kernel was built with. gzip, xz, zstd, lzo, and others all plug into the same wrapper.

When the bytes are out, the decompressor reads the kernel’s ELF headers. ELF, short for Executable and Linkable Format, is both a file format and a map. It says which chunks are code, which are data, and exactly where each chunk wants to live. The decompressor copies each chunk where it belongs.

If the kernel is being loaded at a different address than it was built for, the decompressor applies relocations. A relocation is a small fix‑up that adjusts a pointer or an instruction that contains an address. The decompressor walks a list of these and patches each place so it points to the right spot in the address space we are actually using.

When everything is in place, the decompressor returns the entry point of the real kernel and jumps there, passing a pointer to the boot parameters. From that moment you are in the full kernel. The first function you meet is `start_kernel`, and the big initialization begins.

### Why the kernel sometimes moves itself on purpose

You may see kASLR mentioned in kernel logs. That stands for Kernel Address Space Layout Randomization. The idea is simple. If attackers do not know where the kernel lives in memory, certain attacks get a lot harder.

Early in boot, if kASLR is enabled, the decompressor chooses two “bases” at random:

*   a physical base, which is where the bytes will live in RAM
*   a virtual base, the starting virtual address the kernel will use once full paging is set up

How does it choose without breaking anything

It builds a do not touch list. That includes the decompressor itself, the compressed image, the initial ramdisk, the boot parameters page, and the command line buffer. It can also include ranges you reserve with a `memmap=` option on the command line.

It scans the memory map from firmware to find large free regions. For each free region it counts how many aligned “slots” of the right size would fit. It draws a random number using the best early entropy source it has. On modern CPUs that might be a hardware random instruction. It reduces the number to the total number of slots and picks the matching slot. That becomes the physical base. The virtual base is chosen the same way, but within the kernel’s virtual address window.

If nothing suitable exists, the code falls back to the default addresses and prints a small warning. If you pass `nokaslr` on the command line, the randomization step is skipped by design.

* * *

A quick glossary you can bookmark
---------------------------------

**Hexadecimal.** Base 16 numbers written with `0x`. `0x10` is 16. `0x100000` is 1 megabyte. Hex maps cleanly to bits, which is why low‑level code uses it.

**Register.** A tiny slot inside the CPU that holds a number right now. Examples: CS, DS, SS, IP, SP.

**Segment and offset.** The two pieces used to build real‑mode addresses. Physical address equals segment times 16 plus offset.

**BIOS.** Older firmware that starts the machine, checks hardware, and loads the first boot sector into memory.

**UEFI.** Modern firmware that understands filesystems and loads larger boot programs directly.

**Bootloader.** The usher that places the kernel in memory and passes facts about the system to it. GRUB is a common one.

**Stack.** A last‑in, first‑out workbench for functions. SS selects its segment. SP points at the current top.

**BSS.** A region where global variables that must start as zero live. The kernel setup code clears it before C runs.

**Interrupt.** A fast “excuse me” from hardware or software. The CPU pauses, runs a small handler, then resumes. Maskable interrupts can be blocked for a moment. NMI cannot.

**GDT.** Global Descriptor Table. Short list of segment descriptors. Linux sets it to a simple flat model.

**IDT.** Interrupt Descriptor Table. Directory of interrupt handlers. Early boot uses a minimal one. The full kernel installs the real one later.

**A20 line.** Historical switch that must be opened to address above 1 megabyte correctly on old PCs.

**Protected mode.** 32‑bit mode that introduces the GDT and IDT and allows paging.

**Long mode.** 64‑bit mode on x86_64. Requires paging and a bit named LME set in the EFER register.

**Paging.** The translator from virtual addresses to physical memory. Implemented with page tables.

**Page tables.** The data structure that maps virtual pages to physical pages. Early boot uses identity maps. Normal pages are 4 KB. Early boot often uses 2 MB pages to cover ground quickly.

**CR0, CR3, CR4.** Control registers. CR0 turns on protected mode. CR3 points to the top of the page tables. CR4 enables extended features such as PAE.

**EFER.** A model‑specific register that holds Long Mode Enable among other bits.

**ELF.** The kernel’s on‑disk format with a built‑in map of what belongs where.

**Relocation.** A fix‑up that adjusts addresses when code is loaded at a different base than it was built for.

**kASLR.** Randomizes kernel base addresses at boot to make exploitation harder.

Feedback is extremely welcomed! You can reach out to me on X [@0xkato](https://x.com/0xkato)
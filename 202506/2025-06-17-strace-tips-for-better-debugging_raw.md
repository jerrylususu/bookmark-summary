Title: strace tips for better debugging

URL Source: https://rrampage.github.io/2025/06/13/strace-tips-for-better-debugging/

Published Time: 2025-06-13T19:08:50+05:30

Markdown Content:
Recently, I have been building software without libc to better understand Linux syscalls and internals better. So far, I have built a [minimal shell](https://gist.github.com/rrampage/5046b60ca2d040bcffb49ee38e86041f), [terminal Snake game](https://gist.github.com/rrampage/2a781662645dc2fcba45784eb584cbdc), pure ARM64 assembly [HTTP server](https://gist.github.com/rrampage/d31e75647a77badb3586ebae1e414cb6) and [threads implementation](https://gist.github.com/rrampage/43c56d4a56f8f73320d17ff7b3a49be6). I have been using [`strace`](https://man7.org/linux/man-pages/man1/strace.1.html) extensively while debugging.

Useful options and flags
------------------------

I use a version of the following command:

```
strace -fintrCDTYyy -o strace.log -v -s128 ./binary
```

This looks like an alphabet soup of options! Here’s what they do and how they are useful:

*   `-f`: Follow child processes/threads. This is especially useful when dealing with spawning processes or threads as otherwise, strace will only trace the parent process.
*   `-v`: Print unabbreviated versions of environment, stat, termios and other structs in syscalls. I found this invaluable in conjunction with `-s` when doing assembly programming to check if the structs were being initialized correctly and if certain arguments were being sent in little/big endian format
*   `-s NUM`: Specify the maximum string size to print. Useful for large structs
*   `-o`: Save strace output to a log file. It is always better to do this to investigate the output of the original process and strace separately without each cluttering the other
*   `-yy`: Print all available information associated with file descriptors. This is great for expanding the file descriptor to either its full path in case of a file or TCP address in case of sockets
*   `-Y`: Print command names for PIDs. I found this useful when building the shell to check if the correct program is being executed
*   `-t`: Print current timestamp in log
*   `-T`: Show time spent in syscalls. Useful for some basic profiling although strace heavily slows down the process.
*   `-r`: Print a relative timestamp upon entry to each system call
*   `-n`: Print syscall number. Great to quickly find out syscall numbers on new architectures.
*   `-i`: Print instruction pointer at the time of syscall. Found this useful when debugging assembly code to check rough location of errors.
*   `-C`: Print summary of syscall count, time, errors at the end of regular output

Print stack traces
------------------

The `-k` or `--stack-trace` prints the stacktrace along with the syscall. This is useful if your program is compiled with with `-g`. [This post](https://shane.ai/posts/backtraces-with-strace/) is a good read on using strace to show backtraces for a Golang program compiled with `GODEBUG`.

Selectively tracing syscalls
----------------------------

By default, strace traces all syscalls. We can be very selective in tracing calls by using the `-e` option. It allows us to trace families of syscalls e.g `-e t=%net` will trace all network related syscalls while `-e t=%mem` will trace memory related syscalls.

We can also trace only syscalls which succeed using `-z` option or fail using `-Z` option. Another useful option is `-P` which can be used to only trace syscalls which access a particular path e.g `strace -f -P /usr/bin/ls sh -c ls`.

Tampering with syscalls!
------------------------

strace is very powerful and can do stuff like inject faults for particular syscalls e.g `strace -e inject=%file:error=ENOENT:when=3+ ls` which fails the all file related syscalls after 2 successful invocations. We can also make syscalls return a particular value using `retval` or send signal using `signal` or delay at beginning or end of syscall using `delay_enter` and `delay_exit` with `-e inject`.

I found this useful when debugging failure cases in code for the syscalls. The strace output will have lines like `openat(AT_FDCWD, "/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory) (INJECTED)` which have `INJECTED` marked in them. This is useful to differentiate genuine syscall errors from the injected ones.

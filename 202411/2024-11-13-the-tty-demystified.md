# The TTY demystified
- URL: https://www.linusakesson.net/programming/tty/
- Added At: 2024-11-13 14:38:07

## TL;DR
文章详细介绍了Linux和UNIX系统中的TTY子系统，包括其历史、使用场景、进程管理、信号处理、流控制和设备配置。通过解释TTY驱动、终端模拟、作业控制等概念，帮助开发者深入理解这一复杂系统。文章还提供了相关的手册页和glibc文档以供进一步学习。

## Summary
1. **Introduction**:
   - The TTY subsystem is central to Linux and UNIX design.
   - Its importance is often overlooked, and good introductory articles are scarce.
   - Understanding TTYs is essential for developers and advanced users.
   - The TTY subsystem is a complex system with many special cases.

2. **History**:
   - **Stock Ticker (1869)**: An electro-mechanical machine for real-time stock price distribution.
   - **Teletypes**: Evolved from stock tickers, used ASCII and were part of the Telex network.
   - **Computers and Teletypes**: Early computers used teletypes as input/output devices.
   - **UNIX Development**: The UNIX approach was to handle low-level details in the kernel, leaving advanced features to applications.
   - **Modern Times**: Physical teletypes are extinct; modern TTYs are emulated.

3. **Use Cases**:
   - **Physical Teletype**: Connected to a UART (Universal Asynchronous Receiver and Transmitter) via wires.
   - **UART Driver**: Manages byte transmission, including parity checks and flow control.
   - **Line Editing**: The operating system provides an editing buffer and basic editing commands (backspace, erase word, clear line, reprint).
   - **Session Management**: The TTY driver manages multiple programs, foreground/background jobs, and job control signals.
   - **Linux Console**: Emulates a video terminal in software, rendered to a VGA display.
   - **Pseudo Terminals (PTY)**: Facilitate terminal emulation in userland, used by applications like `xterm` and `ssh`.

4. **Processes**:
   - **Process States**: Running, Uninterruptible Sleep, Interruptible Sleep, Stopped, Zombie.
   - **Job Control**: Job control is managed by the session leader (shell) using signals and system calls.
   - **Jobs and Sessions**: Jobs are process groups, managed by the session leader. Examples include suspending a program with `^Z` or running a program in the background with `&`.

5. **Signals**:
   - **Signal Types**: SIGHUP, SIGINT, SIGQUIT, SIGPIPE, SIGCHLD, SIGSTOP, SIGCONT, SIGTSTP, SIGTTIN, SIGTTOU, SIGWINCH.
   - **Signal Actions**: Terminate, Core Dump, Ignore, Function Call.
   - **Signal Examples**:
     - **SIGHUP**: Sent to the entire session on hangup, default action is termination.
     - **SIGINT**: Sent to the foreground job on `^C`, default action is termination.
     - **SIGQUIT**: Similar to SIGINT but with a core dump.
     - **SIGPIPE**: Sent to processes writing to a pipe with no readers.
     - **SIGCHLD**: Sent to the parent process when a child process changes state.
     - **SIGSTOP**: Unconditionally suspends the recipient.
     - **SIGCONT**: Resumes a stopped process.
     - **SIGTSTP**: Suspends the process on `^Z`.
     - **SIGTTIN/SIGTTOU**: Sent to background jobs attempting to read/write to the TTY.
     - **SIGWINCH**: Sent to the foreground job when the terminal size changes.

6. **Flow Control and Blocking I/O**:
   - **Blocking I/O**: The pseudo terminal can only buffer a certain amount of data. When full, write operations block the process.
   - **Flow Control**: The TTY can be explicitly put in a blocking state using control characters (`^S` and `^Q`).

7. **Configuring the TTY Device**:
   - **TTY Configuration**: Can be read or modified using `ioctl(2)` or POSIX wrappers (`termios(3)`).
   - **Command Line Tool**: `stty(1)` is used to manipulate TTY devices.

8. **Conclusion**:
   - The article provides a comprehensive understanding of TTY drivers, line disciplines, terminals, line editing, and job control.
   - Further details can be found in various man pages and the glibc manual.

9. **Discussion and Feedback**:
   - Readers appreciate the article for its clarity and depth.
   - Some readers provide corrections and additional information.
   - The article remains relevant and informative over the years.

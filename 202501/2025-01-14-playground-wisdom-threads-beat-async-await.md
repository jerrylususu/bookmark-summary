# Playground Wisdom: Threads Beat Async/Await
- URL: https://lucumr.pocoo.org/2024/11/18/threads-beat-async-await/
- Added At: 2025-01-14 14:17:29

## TL;DR
Armin Ronacher认为async/await在大多数编程语言中是不良抽象，主张使用线程作为更好的并发模型。他指出async/await存在背压处理不足、函数着色、未解决Promise等问题，而线程提供了更灵活的挂起能力和并发处理。作者推崇Java的Project Loom等虚拟线程实现，并认为结构化并发和通道是未来并发编程的关键方向。

## Summary
1. **作者观点**：作者Armin Ronacher认为async/await是大多数编程语言中的不良抽象，主张使用线程作为更好的替代方案。

2. **历史背景**：
   - 作者几年前曾讨论过async/await系统在处理背压（back pressure）方面的不足。
   - 现在，作者认为async/await的问题并未得到显著改善，反而更加确信其不适合大多数语言。

3. **引用与参考**：
   - **Bob Nystrom的《What Color is Your Function》**：讨论了两种函数类型（同步和异步）的单向兼容性问题。
   - **Ron Pressler的《Please stop polluting our imperative languages with pure concepts》**：批评了在命令式语言中引入纯函数概念的做法。
   - **Nathaniel J. Smith的《Notes on structured concurrency, or: Go statement considered harmful》**：阐述了结构化并发的重要性。

4. **Scratch编程的启示**：
   - **Scratch的并发模型**：Scratch通过“精灵”（sprites）实现了类似actor模型的并发编程，孩子们可以轻松理解并发。
   - **与传统编程的对比**：传统编程语言（如Python、C#）通常将线程和并发视为复杂和高级的概念，而Scratch则将其简化为自然的过程。

5. **命令式编程的优势**：
   - **命令式编程并非低劣**：作者认为命令式编程语言并不逊色于函数式编程语言，尽管后者在数学和逻辑上有其优势。
   - **等待机制**：命令式语言和函数式语言在处理“等待”时有不同的方式，作者通过JavaScript的Promise和async/await展示了这种差异。

6. **async/await的问题**：
   - **阻塞与挂起**：async/await剥夺了函数自由挂起的能力，导致代码表达力下降。
   - **未解决的Promise**：async/await引入了未解决Promise的问题，可能导致资源泄漏和调试困难。
   - **背压问题**：async/await系统难以有效处理背压，导致缓冲区膨胀。

7. **线程的优势**：
   - **线程的挂起能力**：线程允许函数在任何地方挂起，这是处理并发和背压的强大工具。
   - **线程的灵活性**：线程可以是操作系统线程，也可以是虚拟线程（如协程或纤程），开发者无需关心其具体实现。

8. **不同语言的async/await实现**：
   - **JavaScript**：单线程语言，async/await是对Promise的语法糖，没有真正的线程支持。
   - **Python**：已有操作系统级线程，但受GIL限制，async/await基于协程实现，存在复杂的同步问题。
   - **C#**：有真正的线程支持，async/await主要用于UI线程的非阻塞操作。
   - **Rust**：基于轮询的async/await系统，适合无运行时的系统编程。

9. **async/await的局限性**：
   - **锁和同步**：async/await并未消除对锁和同步的需求，反而引入了新的复杂性。
   - **GIL问题**：在Python中，async/await并未解决GIL的限制。
   - **内存访问阻塞**：即使是非阻塞操作，内存访问仍可能阻塞，async/await无法完全解决这一问题。

10. **线程的未来**：
    - **Java的Project Loom**：通过虚拟线程实现了轻量级的并发，开发者只需使用传统的线程API。
    - **结构化并发**：作者认为结构化并发（如Trio的nursery概念）是未来并发编程的关键，线程应知道其父子关系，并能传递上下文。

11. **结论**：
    - **async/await的利弊**：async/await虽然缓解了回调地狱，但也带来了函数着色、背压问题和未解决Promise等新问题。
    - **线程的回归**：作者认为线程是更好的并发模型，尤其是像Java的Project Loom这样的虚拟线程实现，能够提供更直观和高效的并发编程体验。

12. **未来展望**：
    - **结构化并发和通道**：作者认为结构化并发和通道（channels）是未来并发编程的重要方向，能够简化线程间的通信和同步。
    - **语言设计的启示**：未来的编程语言设计应注重轻量级的协程和线程支持，同时提供结构化并发和通道等高级抽象。

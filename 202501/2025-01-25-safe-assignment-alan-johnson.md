# Safe Assignment | Alan Johnson
- URL: https://nalanj.dev/posts/safe-assignment/
- Added At: 2025-01-25 21:54:21
- [Link To Text](2025-01-25-safe-assignment-alan-johnson_raw.md)

## TL;DR
Alan Johnson 讨论了 JavaScript 中新的安全赋值操作符（?=）提案，旨在简化 try/catch 块中的错误处理。他实现了一个 `tryCatch` 函数，支持同步和异步操作，减少代码冗余。虽然不确定是否会实际使用，但他认为这次探索很有趣，并邀请读者反馈。

## Summary
1. **文章背景**：Alan Johnson 讨论了 JavaScript 中新的安全赋值操作符（?=）的提案，并分享了他对如何处理 try/catch 块中常见问题的看法。

2. **安全赋值操作符提案**：
   - **功能描述**：新的 ?= 操作符将尝试在 try/catch 块中执行赋值操作，并返回一个数组。数组的第一个元素是错误（如果有），第二个元素是赋值的结果（如果没有错误）。
   - **示例代码**：
     ```javascript
     const [error, value] ?= maybeThrows();
     ```

3. **try/catch 块的常见问题**：
   - **代码冗余**：在 try/catch 块中定义变量时，必须在块外部声明变量，导致代码冗长。
   - **示例代码**：
     ```javascript
     let errorMsg;
     try {
       maybeThrow();
     } catch (e) {
       errorMsg = "An error message";
     }
     ```

4. **非异步函数的实现**：
   - **函数实现**：Alan 实现了一个名为 `tryCatch` 的函数，用于处理非异步函数中的 try/catch 逻辑。
   - **功能描述**：`tryCatch` 函数在 try/catch 块中调用函数，并返回一个数组，包含错误和结果。
   - **示例代码**：
     ```javascript
     function tryCatch(fn, ...args) {
       try {
         return [undefined, fn.apply(null, args)];
       } catch (e) {
         return [e, undefined];
       }
     }
     ```

5. **异步函数的实现**：
   - **挑战**：处理异步函数时，需要额外的逻辑来处理 Promise。
   - **函数实现**：Alan 扩展了 `tryCatch` 函数，使其能够处理异步函数。
   - **功能描述**：如果函数返回一个 Promise，`tryCatch` 会返回一个新的 Promise，并在 Promise 解析时返回错误或结果。
   - **示例代码**：
     ```javascript
     function tryCatch(fn, ...args) {
       try {
         const result = fn.apply(null, args);
         if (result.then) {
           return new Promise(resolve => {
             result
               .then(v => resolve([undefined, v]))
               .catch(e => resolve([e, undefined]));
           });
         }
         return [undefined, result];
       } catch (e) {
         return [e, undefined];
       }
     }
     ```

6. **Promise 处理逻辑**：
   - **检查 Promise**：通过 `if (result.then)` 检查函数是否返回了 Promise。
   - **解析 Promise**：如果返回了 Promise，则返回一个新的 Promise，并在解析时返回错误或结果。
   - **示例代码**：
     ```javascript
     if (result.then) {
       return new Promise(resolve => {
         result
           .then(v => resolve([undefined, v]))
           .catch(e => resolve([e, undefined]));
       });
     }
     ```

7. **总结**：
   - **使用场景**：Alan 提到他经常遇到需要 try/catch 的情况，但显式的 try/catch 块显得冗长且繁琐。
   - **探索意义**：虽然不确定是否会实际使用这个实现，但这次探索让他感到有趣。

8. **反馈与讨论**：Alan 邀请读者分享对这篇文章的看法，可以通过 comments@nalanj.dev 联系他。

# How to convert a Node.js stream of event callback functions into an Async Iterator
- URL: https://www.jbernier.com/p?id=nodejs-stream-async-iterator
- Added At: 2024-08-16 14:37:10

## TL;DR
本文介绍了如何将基于事件回调的流处理代码转换为使用`for await`循环的异步迭代器，通过封装异步生成器函数实现。示例展示了如何处理CSV文件流，并比较了两个排序后的CSV文件。最后指出`csv-parse`库已有异步迭代器API，简化了实现过程。

## Summary
1. **问题描述**：如何将基于事件回调的流处理代码转换为使用`for await`循环的异步迭代器。
   - **背景**：假设有一个流（例如内存中的文件读取），但唯一可用的API是一系列事件处理回调。
   - **示例**：使用`csv-parse`库的流API，通过事件回调处理数据。

2. **转换动机**：
   - **代码美观性**：`for await`循环看起来更简洁。
   - **功能需求**：如果需要同时程序化地迭代多个流（例如逐行比较多个文件），使用回调几乎不可能实现。

3. **解决方案**：将回调代码封装在一个**异步生成器函数**中。
   - **实现步骤**：
     - 创建一个异步生成器函数`createCsvParseStream`。
     - 使用`Promise`和`resolve`、`reject`函数处理事件回调。
     - 在`while`循环中等待`Promise`，并通过`yield*`返回结果。

4. **具体实现**：
   ```javascript
   async function* createCsvParseStream(parser) {
       let results = [];
       let done = false;
       let resolve, reject;
       let promise = new Promise((res, rej) => {
           resolve = res;
           reject = rej;
       });

       parser.on('readable', () => {
           let record;
           while ((record = parser.read()) !== null) {
               results.push(record);
               resolve();
               promise = new Promise((res, rej) => {
                   resolve = res;
                   reject = rej;
               });
           }
       });

       parser.on('error', (err) => {
           console.error(err.message);
           done = true;
           reject();
       });

       parser.on('end', () => {
           done = true;
           resolve();
       });

       while (!done) {
           await promise;
           yield* results;
           results = [];
       }
   }
   ```

5. **使用示例**：
   ```javascript
   const asyncIterable = createCsvParseStream(inputStream);

   for await (const input of asyncIterable) {
       console.log(input);
   }
   ```

6. **条件迭代多个流**：
   - **示例**：比较两个排序后的CSV文件，找出添加或删除的行。
   ```javascript
   const iter = asyncIterable1[Symbol.asyncIterator]();
   const iter2 = asyncIterable2[Symbol.asyncIterator]();

   let [res1, res2] = await Promise.all([iter.next(), iter2.next()]);

   while (!res1.done && !res2.done) {
     console.log("do stuff", res1, res2);
     
     if (...) {
       ...
       res1 = await iter.next();
     } else if (...) {
       ...
       res2 = await iter2.next();
     } else {
       ...
       [res1, res2] = await Promise.all([iter.next(), iter2.next()]);
     }
   }
   ```

7. **`for await`循环定义**：
   - **等价实现**：
     ```javascript
     const iter = parser[Symbol.asyncIterator]();
     let res = await iter.next();

     while (!res.done) {
       console.log("res", res.value);
       res = await iter.next();
     }
     ```

8. **备注**：`csv-parse`库实际上有[异步迭代器API](https://csv.js.org/parse/api/async_iterator/)，因此不需要上述复杂的实现。

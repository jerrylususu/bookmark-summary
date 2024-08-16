# One Thing Nobody Explained To You About TypeScript
- URL: https://kettanaito.com/blog/one-thing-nobody-explained-to-you-about-typescript
- Added At: 2024-08-16 14:32:04
- [Link To Text](2024-08-16-one-thing-nobody-explained-to-you-about-typescript_raw.md)

## TL;DR
作者分享了使用TypeScript的经验，特别是在`tsconfig.json`配置上的误解和解决方法。通过创建多个`tsconfig.json`文件并正确使用`references`属性，解决了类型冲突问题，提高了开发效率。

## Summary
1. **TypeScript经验**：
   - 作者使用TypeScript超过四年，认为它提高了生产力，尤其是在编写类型和以类型优先解决问题时。
   - 尽管作者自认为对TypeScript有一定了解，但仍有一些误解，特别是在`tsconfig.json`的使用上。

2. **`tsconfig.json`的误解**：
   - 作者最初认为`tsconfig.json`是一个配置文件，用于配置TypeScript，但实际上它的作用更为复杂。
   - `tsconfig.json`不仅是一个配置文件，它还决定了TypeScript如何理解和处理项目中的文件。

3. **示例项目**：
   - 创建一个简单的纯TypeScript前端应用，不使用框架和依赖。
   - 代码中使用`document`对象，TypeScript通过加载默认的`lib.dom`定义库来识别`document`。

4. **测试框架引入**：
   - 为了添加自动化测试，引入了Vitest测试框架。
   - 编写测试代码时，TypeScript报错提示找不到`it`，需要安装类型定义。

5. **解决测试框架类型问题**：
   - 通过修改`tsconfig.json`，添加`vitest/globals`到`compilerOptions.types`，使TypeScript加载额外的类型定义。
   - 修改后，测试通过，但发现了一个潜在问题。

6. **潜在问题**：
   - 在`app.ts`中引用一个不存在的全局变量`test`，TypeScript没有报错，反而提供了类型建议。
   - 这表明TypeScript加载了错误的类型定义，导致潜在的运行时错误。

7. **配置文件的作用**：
   - `tsconfig.json`的`include`选项控制哪些模块应用该配置。
   - 如果模块不在`include`指定的目录中，`tsconfig.json`对该模块无效。

8. **配置文件的误用**：
   - 将`test`目录添加到`include`中，导致测试框架的类型定义泄露到所有`src`模块中。
   - 这会导致类型冲突和整体使用体验的下降。

9. **解决方案**：
   - 为每个运行环境创建单独的`tsconfig.json`文件。
   - 使用`references`属性，使TypeScript能够处理嵌套配置，确保每个模块只受其特定配置的影响。

10. **具体配置示例**：
    - 创建多个`tsconfig.json`文件，如`tsconfig.src.json`、`tsconfig.test.json`等。
    - 使用`references`属性在根级`tsconfig.json`中引用这些配置文件。

11. **总结**：
    - TypeScript的配置不仅限于简单的配置文件，它涉及到如何组织和理解项目中的代码。
    - 通过正确使用`tsconfig.json`和相关配置，可以避免类型冲突和提高开发效率。

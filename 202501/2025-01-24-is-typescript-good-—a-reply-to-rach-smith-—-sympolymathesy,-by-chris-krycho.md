# Is TypeScript Good?—A Reply to Rach Smith — Sympolymathesy, by Chris Krycho
- URL: https://v5.chriskrycho.com/journal/is-typescript-good/
- Added At: 2025-01-24 13:55:18
- [Link To Text](2025-01-24-is-typescript-good-—a-reply-to-rach-smith-—-sympolymathesy,-by-chris-krycho_raw.md)

## TL;DR
文章讨论了TypeScript在JavaScript开发中的实用性，强调了其错误捕捉、代码可持续性和系统“库存”提升的价值。作者Chris Krycho认同TypeScript可能引发“聪明代码”陷阱，但也指出其在提高代码质量和未来扩展能力方面的优势。文章建议在引入TypeScript时平衡短期功能交付和长期维护投入，强调其对代码库长期可持续性的重要性。

## Summary
1. **文章背景**：
   - **目标读者**：主要面向对TypeScript感兴趣的JavaScript开发者，讨论TypeScript的实用性，而非深入技术细节或哲学争议。
   - **作者背景**：作者Chris Krycho在过去6年半中深入研究了TypeScript的优缺点，观点较为成熟。

2. **Rach Smith的观点**：
   - **初始感受**：Rach最初对TypeScript感到不适应，认为编写速度慢且笨重，尤其是在大部分代码库仍然是JavaScript的情况下。
   - **逐渐接受**：经过6个月的使用，她开始喜欢TypeScript，尤其是能够“看到事物的类型”这一特性。
   - **担忧**：她担心自己对TypeScript的喜爱可能只是“曝光效应”（Mere Exposure Effect），并指出TypeScript可能让人过于追求“聪明”的代码，导致代码难以维护。

3. **Chris Krycho的回应**：
   - **认同与补充**：Chris认同Rach关于TypeScript可能引发“聪明代码”陷阱的观点，但也认为TypeScript的价值不仅限于此。
   - **TypeScript的陷阱**：
     - **拼图效应**：TypeScript的类型系统可能让开发者陷入长时间的拼图式调试，虽然解决后很有成就感，但并不总是值得。
     - **正确性最大化**：开发者可能过度追求代码的正确性，导致时间浪费在不必要的细节上。
   - **适用场景**：
     - **高安全性需求**：如TLS实现或基础库开发时，最大化正确性是必要的。
     - **普通应用代码**：大多数应用代码应尽量减少类型注解，依赖类型推断，保持代码简洁。

4. **TypeScript的价值**：
   - **错误捕捉**：TypeScript转换过程中常常暴露JavaScript代码中的潜在错误，提升代码质量。
   - **代码可持续性**：即使转换后功能不变，TypeScript也能通过显式化隐式复杂性，提升代码的可读性和可维护性。
   - **系统“库存”提升**：TypeScript通过提供类型信息和强大的重构工具，增强了代码库的“库存”（即未来交付新功能的能力）。

5. **总结**：
   - **平衡投资**：在代码库中引入TypeScript需要平衡短期功能交付和长期代码维护的投入。
   - **未来价值**：TypeScript不仅改善了当前代码质量，还为未来的功能扩展和修改提供了更好的基础。

6. **引用与扩展**：
   - **博客文化**：Chris引用Brad East的观点，强调博客的对话性和实验性，认为博客是思想的碰撞和交流。
   - **代码质量与软件质量**：引用Mark Seeman的观点，强调代码质量对软件长期可持续性的重要性。
   - **系统思维**：借用Donella Meadows的“系统思维”概念，将代码库的“库存”与“流动”类比，强调对代码库的长期投资。

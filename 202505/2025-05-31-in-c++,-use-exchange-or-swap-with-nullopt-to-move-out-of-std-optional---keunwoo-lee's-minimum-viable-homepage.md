# In C++, use exchange or swap with nullopt to move out of std::optional - Keunwoo Lee's Minimum Viable Homepage
- URL: https://keunwoo.com/notes/cpp-moving-std-optional/
- Added At: 2025-05-31 10:19:29
- [Link To Text](2025-05-31-in-c++,-use-exchange-or-swap-with-nullopt-to-move-out-of-std-optional---keunwoo-lee's-minimum-viable-homepage_raw.md)

## TL;DR


使用`std::exchange`可安全转移`std::optional`的值并将其置为`nullopt`，避免残留engaged状态引发未定义行为。单纯移动对象或其值会导致原对象仍显示有效但内部为空，需手动`.reset()`修复，但不如`exchange`直接。优先选用`exchange`确保安全简洁；仅在性能敏感场景考虑`std::swap`，但需注意代码可读性。测试表明`exchange`和`swap`能有效重置原optional，其他方法不可取。

## Summary


1. **推荐做法**  
使用`std::exchange`将`std::optional`交换为`std::nullopt`以安全转移值：  
- `auto dest = std::exchange(src, std::nullopt);`  
- 原`src`变为`nullopt`，表达式返回原`optional`的值；若原值非空，可直接通过`.value()`或`*`获取。  
- 类似Rust的`Option::take`方法。  

**替代方案**：`std::swap`需预先声明变量（如`swap_dest`），虽可能因特例化优化更高效，但可读性较差：  
- `std::swap(swap_src, swap_dest);`  

2. **错误用法及问题**  
- **仅移动`std::optional`**：  
  `auto only_moved_to = std::move(moved_from_optional);`  
  - 原`moved_from_optional`仍处于“已移动（engaged）”状态（`has_value()`为真），内部值为空或未定义，易引发逻辑错误。  
- **仅移动内部值**：  
  `auto moved_value = std::move(moved_from_value.value());`  
  - 同样导致原`optional`保持engaged状态，需额外手动调用`.reset()`修正。  

3. **补救措施**  
- 移动后追加`.reset()`：  
  `move_then_reset.reset();`  
  - 虽可使原`optional`变为`nullopt`，但不如`std::exchange`简洁直接。  

4. **注意事项**  
- 移动后原`optional`若未显式置为`nullopt`，残留engaged状态可能引发未定义行为（如误用`.value()`）。  
- `std::exchange`是更安全且简洁的解决方案，优先选择；仅在性能敏感场景评估`std::swap`。  

5. **附录验证代码**  
完整示例代码输出显示：  
- `exchange`和`swap`后原`optional`变为`nullopt`。  
- 直接移动或仅移值后原`optional`仍非空，内部值为空字符串。

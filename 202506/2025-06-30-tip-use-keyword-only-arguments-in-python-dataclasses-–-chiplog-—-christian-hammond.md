# Tip: Use keyword-only arguments in Python dataclasses – ChipLog — Christian Hammond
- URL: https://chipx86.blog/2025/06/29/tip-use-keyword-only-arguments-in-python-dataclasses/
- Added At: 2025-06-30 13:30:30
- [Link To Text](2025-06-30-tip-use-keyword-only-arguments-in-python-dataclasses-–-chiplog-—-christian-hammond_raw.md)

## TL;DR


Python数据类通过设置`kw_only=True`强制使用关键字参数，提升可维护性。该参数使生成的`__init__()`含`*`，所有参数需显式指定，避免字段排序变动引发错误。同时允许子类自由添加必要字段，不受父类默认值顺序限制，推荐库开发者使用以确保扩展性。需Python3.10+支持，旧版本需动态设置装饰器参数但子类仍受限制，建议手动添加默认值。

## Summary


Python数据类通过设置`kw_only=True`强制使用关键字参数传入，提升可维护性。  
具体实现：在`@dataclass`装饰器中添加`kw_only=True`，生成的`__init__()`方法会包含`*`，要求后续参数必须用关键字指定。  

**优势**：  
1. 字段重新排序不影响调用者，避免因位置参数变化导致意外错误。例如，使用`MyDataClass(x=1, y='foo')`比`MyDataClass(1, 'foo')`更稳定。  
2. 子类可自由添加必要字段。当父类存在默认值字段时，子类新增的无默认值字段不会因位置参数顺序受限制。  

**适用场景**：  
主要推荐给库作者，以确保向后兼容性和未来扩展性。例如在Review Board项目中，需平衡维护与功能扩展的需求。  

**兼容性注意**：  
`kw_only`仅支持Python 3.10+。若需兼容旧版本，可用条件判断动态设置装饰器参数。但旧版本下子类仍受默认值字段顺序限制，需手动确保子类字段有默认值。  

示例兼容写法：  
```python
import sys
from dataclasses import dataclass

dataclass_kwargs = {'kw_only': True} if sys.version_info[:2] >= (3, 10) else {}

@dataclass(**dataclass_kwargs)
class MyDataClass:
    x: int
    y: str
    z: bool = True
```

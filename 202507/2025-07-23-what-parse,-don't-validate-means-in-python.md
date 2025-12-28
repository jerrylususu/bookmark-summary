# What "Parse, don't validate" means in Python?
- URL: https://www.bitecode.dev/p/what-parse-dont-validate-means-in
- Added At: 2025-07-23 13:35:18

## TL;DR


本文阐述Python中“Parse don’t validate”原则，指优先将外部数据（如命令行/JSON）解析为内部类型（如`int`或日期），而非依赖验证。解析过程中隐含类型验证（如转换失败早报错），而验证需分层规约业务条件。推荐通过`argparse`、`TypedDict`和Pydantic等工具在边界层处理数据，根据场景平衡解析复杂度，以提升安全性和容错性。

## Summary


本文探讨了Python中“Parse don't validate”原则的含义及实践方法。  
核心观点包括：  
1. **解析vs验证**：  
   - 解析是将低级/无结构数据转换为高级/结构化类型（如字符串转`int`、JSON转字典），隐含类型转换和验证失败（如`int(user_age)`捕获异常即为验证）。  
   - 验证更侧重检查数据是否满足特定条件（如年龄是否非负）。两者常交织出现，层层递进。  

2. **Python场景**：  
   - 输入通常为外部数据（命令行参数、表单、JSON文件），需在边界层处理。  
   - 示例：用`argparse`解析命令行参数，或用`datetime.fromisoformat()`将字符串转为日期对象。  

3. **如何决定解析程度**：  
   - 权衡投入与收益：更复杂的类型结构可增加代码信任度，但需更多初始工作。  
   - 依赖场景需求：脚本可简化，库需严格解析。  

4. **Python工具与技巧**：  
   - **Tip 1**：用`typing.NewType`标记类型，轻量表意（如`UserId = NewType('UserId', str)`）。  
   - **Tip 2**：使用`TypedDict`为字典添加结构约束。  
   - **Tip 3**：用Pydantic自动解析验证（如`BaseModel`定义对象模型）。  

5. **核心动机**：  
   - 通过早失败、结构化提取增强安全性与容错性，而非追求类型严格性。  

文中强调，解析是“附带理解的验证”，Python提供灵活手段在不同场景中平衡解析深度与开发成本。

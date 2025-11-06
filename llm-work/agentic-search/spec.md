## spec
用户可以输入一个问题，系统提供一系列 tool （关键词搜索、向量搜索、文本范围读取...），llm 可以根据需要自行调用工具，最后生成完整答案给用户（agentic search）

需要限制工具调用次数（例如10次内），以及最大对话 token 数（例如 60k 内）；搜索的时候可以指定 top_k，文本读取的时候需要限制长度（例如给行号区间？）避免爆 context

实现的时候分为core 和 interface，之间用 http 接口通信；初期的 interface 是 cli 便于本地调试，后期会有个 web 前端

实现 stage
1. 原型（直接 args 或者硬编码 query，验证能力，跑通就行）
2. core + http server（用 curl 自己验证）；考虑 fastapi？
3. cli interface
4. web interface

---

## guide
1. 记录文档的时候用中文（无论是设计文档还是实现记录）
2. 每次完成开发，或者是用户主动提示的时候，需要更新 impl_log.md
3. 每次只做用户要求的部分，不要做更多，不要过度设计
4. note.md 是你自己的，可以主动更新
5. python 用 venv 作为虚拟环境
6. 代码放在 /home/jerrylu/code/251028-bookmark-by-month/bookmark-summary/agentic-search 下

## resource
之前的实现可以看 /home/jerrylu/code/251028-bookmark-by-month/bookmark-summary/embedding_design.md 
/home/jerrylu/code/251028-bookmark-by-month/bookmark-summary/embed_usage.md
相关代码都是 *.py
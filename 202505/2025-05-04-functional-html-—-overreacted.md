# Functional HTML — overreacted
- URL: https://overreacted.io/functional-html/
- Added At: 2025-05-04 15:13:18
- [Link To Text](2025-05-04-functional-html-—-overreacted_raw.md)

## TL;DR


该技术通过函数化自定义标签和JSON结构化转换，实现全栈组件协作。支持异步数据处理、双向函数引用（客户端/服务端标记生成API或路径标识），并采用流式渲染和智能缓存，减少页面弹跳，提升性能。全栈组件闭环设计和灵活的渲染模式（延迟或渐进），优化了开发体验与效率。

## Summary


- 通过添加函数化的自定义标签<Server Tags>，允许用JavaScript函数扩展HTML标签，例如将<Greeting />自定义标签在序列化时替换为实际内容  
- 支持传递复杂对象作为组件属性<Attributes & Objects>，保持数据完整性，而非将对象转换为字符串  
- 通过定义JSON序列化格式<Objects>，HTML转化为JSON树结构，能表达原生HTML和对象，为全栈操作奠定基础  
- 实现异步数据获取<Async Server Tags>，将异步逻辑封装在标签函数中，执行时不影响主流程，如通过file读取用户数据  
- 事件处理引入客户端引用机制<Client References>，使用`'use client'`标记区分客户端函数，通过路径标识（如`/src/bundle.js#onLike`）替代字符串代码传递  
- 对应的服务器引用机制<Server References>，用`'use server'`标记函数生成API地址（如`/api?fn=onLike`），实现客户端调用服务端逻辑而不依赖手动路由配置  
- 客户端标签<Client Tags>允许将组件执行延迟到客户端，在结构化的JSON中保留组件标识和参数，支持渐进渲染或完全客户端渲染  
- 全栈标签<Full-Stack Components>结合服务端和客户端函数，例如服务端组件从文件加载数据后返回客户端组件，客户端组件绑定服务端函数形成闭环  
- 支持流式渲染<Streaming>，通过标记`HOLE`实现服务端内容按需填充，结合<Placeholder>组件控制渐进呈现，避免页面弹跳现象  
- 提升缓存能力<Caching>，结构化的JSON格式保留组件与数据的清晰边界，静态部分可独立缓存，动态内容通过占位符高效更新，优于传统HTML+脚本的混合模式  
- 最终形成一种<Functional HTML>编程模型：服务端执行标签函数生成数据，客户端执行标签实现交互，双向函数引用通过模块系统管理，实现组件化的全栈开发

# JSX Over The Wire — overreacted
- URL: https://overreacted.io/jsx-over-the-wire/#the-data-always-flows-down
- Added At: 2025-04-16 14:48:52
- [Link To Text](2025-04-16-jsx-over-the-wire-—-overreacted_raw.md)

## TL;DR


本文提出将React组件思维应用于后端数据交互，通过BFF架构设计屏幕专用API端点，分离后端与前端数据需求。利用组件化ViewModel结构和数据转换层减少REST API的冗余与耦合问题，进一步探索后端直接返回JSX组件的可能性，以提升前后端协同效率并降低开发复杂度。

## Summary


本文探讨了前端组件与后端数据交互的优化方法，提出通过将React组件概念引入后端数据传输过程来改善传统REST API的局限性。核心观点如下：

---

### 一、问题分析
1. **Model与ViewModel的矛盾**
   - **Model**：数据库中的原始数据（如帖子点赞记录），结构固定但无法直接用于界面呈现。
   - **ViewModel**：组件所需的特定数据格式（如总点赞数、好友点赞者列表），需聚合和个性化处理。若通过REST API返回通用资源（如`/api/posts`），存在两大问题：
     - **过度耦合**：需根据多个屏幕需求强制扩展Model，导致API设计混乱。
     - **冗余与缺失**：可能返回冗余数据或无法一次性获取所需数据（如需多请求拼接）。

2. **REST API的局限性**
   - 传统设计难以平衡模型存储与界面展示需求，导致演进困难：
     - 新增屏幕需求时需频繁调整API，影响现有消费者。
     - 数据获取需多次请求或过度“嵌套”字段，影响性能。

---

### 二、解决方案：BFF（Backend For Frontend）
1. **核心思想**
   - **屏幕驱动的API**：为每个界面设计专用端点（如`/screens/post-details/123`），返回该屏幕所需的完整ViewModel，避免冗余或缺失。
   - **数据转换层**：BFF层调用内部通用服务（如数据库、REST API），将原始数据构建成ViewModel。

2. **关键实践**
   - **代码复用**：
     - 将ViewModel拆解为可组合的函数（类似React组件树），例如：
       ```javascript
       async function LikeButtonViewModel({ postId }) {
         const [post] = await getPost(postId); // 获取基础点赞数据
         const friends = await getFriendLikes(postId); // 获取好友点赞数据
         return { // 返回组件props格式的数据
           totalLikeCount: post.totalLikeCount,
           isLikedByUser: post.isLikedByUser,
           friendLikes: friends.map(l => l.name)
         };
       }
       ```
     - 在更高层级组合这些函数，如：
       ```javascript
       async function PostDetailsViewModel({ postId }) {
         const post = await getPost(postId);
         const likes = await LikeButtonViewModel({ postId });
         return {
           title: post.title,
           author: post.author,
           likes // 直接引用子ViewModel的结果
         };
       }
       ```
   - **与React组件树对齐**：ViewModel的结构映射组件props，确保数据格式与组件需求严格一致，减少转换错误。

---

### 三、进阶：JSX Over the Wire
1. **更激进的实践**
   - **后端直接返回JSX组件**：在API中渲染组件并序列化为JSON：
     ```javascript
     app.get('/api/likes/:postId', async (req, res) => {
       const post = await getPost(req.params.postId);
       const json = <LikeButton 
         totalLikeCount={post.total} 
         isLiked={post.liked} 
         friends={friends} 
       />; // 使用JSX语法生成组件属性
       res.json(json);
     });
     ```
   - **优势**：
     - 避免数据到组件的转换步骤，减少错误。
     - 后端直接控制组件状态，符合“好莱坞原则”：*“别找我，我来找你”*（后端决定前端需要什么）。
   - **潜在挑战**：
     - 对组件的跨端（服务端/客户端）一致性有更高要求。
     - 需要处理跨域安全及序列化兼容性问题。

---

### 四、总结
- **BFF的价值**：
  - 屏幕专用端点减少过度设计，提升开发效率。
  - 组件化ViewModel降低代码重复，易于维护。
- **未来方向**：
  - 结合服务端渲染（SSR）和前端组件框架，进一步整合数据层与UI层。
  - 平衡性能（如大量组件时的传输开销）与开发体验。

通过将组件思维延伸到后端，该方法或为前后端分离架构提供新的可能性。

# Petnames: A humane approach to secure, decentralized naming
- URL: https://files.spritely.institute/papers/petnames.html
- Added At: 2024-11-23 13:41:57

## TL;DR
文章探讨了智能手机联系人列表中petnames系统的应用，用户通过分配本地化的有意义名称来管理联系人，系统自动更新和处理名称冲突，确保上下文相关性，提升用户体验。

## Summary
1. **智能手机联系人列表**：
   - 使用电话号码作为全局命名空间，但用户界面不直接显示电话号码。
   - 用户为每个联系人分配有意义的名称（petname），这些名称是本地化的，不具有全局意义。
   - UI通过这种映射来搜索和选择联系人，并在来电或查看通话记录时显示名称。
   - 如果petname更新，通话记录中的名称也会自动更新。

2. **智能手机联系人列表的局限**：
   - 虽然接近petnames系统，但还不够完善。
   - 需要进一步探讨如何完成这一系统。

3. **场景描述**：
   - Alyssa接到一个电话，显示为“Mom”，这是她为电话号码分配的petname。
   - 通话中，Alyssa的母亲Dr. Nym提到需要帮助组织一个数学讲座，并询问Alyssa的朋友是否感兴趣。
   - Alyssa推荐了她的朋友Ben Bitdiddle。

4. **Dr. Nym的联系人搜索**：
   - Dr. Nym在联系人列表中搜索“Ben”。
   - “personal contacts”部分显示她认识的人的petnames。
   - “network contacts”部分显示她本地存储的实体发布的edge names。
   - Dr. Nym看到“Alyssa ⇒ Ben Bitdiddle”，确认这是她女儿的朋友，并拨打电话。

5. **Ben的来电显示**：
   - Ben看到来电显示为“Alyssa ⇒ Jane Nym”，并有小字“Faculty ⇒ Dr. Nym”。
   - 尽管Ben没有保存Dr. Nym的本地petname，但他通过Alyssa和大学Faculty目录记住了Dr. Nym的身份。

6. **Ben保存Dr. Nym的联系信息**：
   - Ben决定将Dr. Nym的联系信息永久保存。
   - 在编辑界面中，系统建议本地名称为“Jane Nym”，Ben决定保留此名称。
   - Ben还决定将此联系信息作为edge name分享给其他联系人，并将edge name编辑为“Dr. Nym”。

7. **Dr. Nym订购披萨**：
   - Dr. Nym通过扫描QR码找到“Pizza Piano”的电话号码，并确认其身份后拨打电话订购披萨。
   - 她告知收银员Ben将负责取披萨，并提供Ben的电话号码。

8. **Ben接到披萨店的电话**：
   - Ben接到一个未保存的电话号码，Caller ID显示为“Pizza Piano.2”。
   - 由于Ben已与另一家Pizza Piano分店有过联系，系统将其标记为“Pizza Piano.2”。
   - Ben接听电话，披萨店员工告知他橄榄缺货，Ben同意更换为蘑菇。

9. **总结**：
   - 通过petnames系统，用户可以为联系人分配有意义的本地名称，并通过edge names共享信息。
   - 系统自动处理名称冲突，并提供上下文相关的名称建议，确保用户不会混淆。

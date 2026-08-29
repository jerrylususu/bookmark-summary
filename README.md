# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-08-29) [Is Having Agents in the Room Meant to Be Chaotic? — Raft](202608/2026-08-29-is-having-agents-in-the-room-meant-to-be-chaotic-%E2%80%94-raft.md)
  - 文章以计数游戏说明现有工作空间不适配代理：代理回合制导致推理与房间变化脱节。提出代理原生空间Raft与代理体验设计AX，通过“代理收件箱”和“保留草稿”让代理自主决定注意力与发送，并强调感知同理心与行动显式化两条原则。
  - Tags: #read #agent

- (2026-08-27) [Copy-on-write git worktrees](202608/2026-08-27-copy-on-write-git-worktrees.md)
  - 利用文件系统写时复制（reflink）特性，让多个 Git worktree 共享工作文件，从而节省磁盘空间。作者通过先  创建 worktree，再以 reflink 复制已有文件，最后检出完成，并封装为  工具。
  - Tags: #read #tips

- (2026-08-26) [The end of programming — Paul Dix](202608/2026-08-26-the-end-of-programming-%E2%80%94-paul-dix.md)
  - 作者判断传统“人手写代码、逐行审查”的软件开发模式正走向终结。Bun用AI主导重写超百万行Rust、GitHub代码量指数增长等表明，AI可产出并迭代复杂软件。未来开发者将转向定义问题、设计架构和构建验证闭环，只验收最终运行结果，而非阅读代码本身。
  - Tags: #read

- (2026-08-24) [Building a software factory for AI SDK](202608/2026-08-24-building-a-software-factory-for-ai-sdk.md)
  - Vercel团队为AI SDK构建“软件工厂”，用多个专职agent自动处理issue和PR，运行于隔离沙箱，人类保留最终审批。四周后，工厂贡献25-35%合并PR，关闭超75% issues，积压大幅下降，验证了以人为核心的自动化维护模式。
  - Tags: #read #agent

- (2026-08-24) [Human judgment doesn't leave the software factory. It relocates.](202608/2026-08-24-human-judgment-doesn%27t-leave-the-software-factory.-it-relocates..md)
  - 软件工厂将重复编码交给 AI，但人类判断并未消失，而是被重新定位到定义意图、设计系统、设定质量门槛、解读验证和最终上线负责。验证不是越多越好，认知带宽有限，需动态调整自主性并保留人类所有权。代码能上线，仍需人的品味与责任。
  - Tags: #read #agent

- (2026-08-24) [Your executable is a SQLite database](202608/2026-08-24-your-executable-is-a-sqlite-database.md)
  - 文章提出将Linux可执行文件从ELF换成SQLite数据库，原型SELF可运行，工具退化为SQL查询，支持去重、事务化与系统闭包，代价是启动延迟和文件略大。
  - Tags: #read #hack #deepdive

- (2026-08-24) [Anger, Anxiety and Agency](202608/2026-08-24-anger%2C-anxiety-and-agency.md)
  - 文章讨论面对AI不确定性时应持的态度：区分焦虑与愤怒，指出愤怒易错误归因，因为行业领导者同样迷茫。作者主张以好奇和实验替代愤怒，通过实践获得判断力与真实选择能力，而非虚假行动感，最终赢得能动性。
  - Tags: #read

- (2026-08-23) [Fast and Hard Code](202608/2026-08-23-fast-and-hard-code.md)
  - LLM降低了编程语言转换成本，使更多开发者敢于选择Rust、Zig等性能更好但更难的语言及DWARF、eBPF等底层技术。这可能带来两极分化：既产生更多低质量代码，也催生更多追求极致性能和小体积的开发者与项目。
  - Tags: #read #llm

- (2026-08-22) [Stop Making TUIs — Quarrelsome](202608/2026-08-22-stop-making-tuis-%E2%80%94-quarrelsome.md)
  - 文章认为，AI编程助手已让原生GUI开发变得容易，不应再继续构建终端用户界面（TUI）。作者逐一反驳TUI的密度、SSH、可访问性等优势，并展示用AI生成的macOS应用，呼吁开发者更新默认选择，转向原生GUI。
  - Tags: #read #ui

- (2026-08-21) [Introducing Dashboard Touch, a build-your-own version of Touch ID - Anil Dash](202608/2026-08-21-introducing-dashboard-touch%2C-a-build-your-own-version-of-touch-id---anil-dash.md)
  - Anil Dash 因不想受苹果键盘束缚，基于 tinyTouch 开发开源项目 Dashboard Touch，用低成本指纹传感器和微控制器自制 USB 指纹认证装置，模拟键盘自动输入密码。密码与指纹均存本地，仅适合安全环境个人使用。他也分享了动手制作的乐趣，希望社区改进。
  - Tags: #read

## Monthly Archive

- [2026-08](202608/monthly-index.md) (33 entries)
- [2026-07](202607/monthly-index.md) (30 entries)
- [2026-06](202606/monthly-index.md) (33 entries)
- [2026-05](202605/monthly-index.md) (70 entries)
- [2026-04](202604/monthly-index.md) (57 entries)
- [2026-03](202603/monthly-index.md) (70 entries)
- [2026-02](202602/monthly-index.md) (58 entries)
- [2026-01](202601/monthly-index.md) (67 entries)
- [2025-12](202512/monthly-index.md) (68 entries)
- [2025-11](202511/monthly-index.md) (78 entries)
- [2025-10](202510/monthly-index.md) (67 entries)
- [2025-09](202509/monthly-index.md) (40 entries)
- [2025-08](202508/monthly-index.md) (46 entries)
- [2025-07](202507/monthly-index.md) (77 entries)
- [2025-06](202506/monthly-index.md) (75 entries)
- [2025-05](202505/monthly-index.md) (65 entries)
- [2025-04](202504/monthly-index.md) (61 entries)
- [2025-03](202503/monthly-index.md) (49 entries)
- [2025-02](202502/monthly-index.md) (32 entries)
- [2025-01](202501/monthly-index.md) (41 entries)
- [2024-12](202412/monthly-index.md) (45 entries)
- [2024-11](202411/monthly-index.md) (57 entries)
- [2024-10](202410/monthly-index.md) (34 entries)
- [2024-09](202409/monthly-index.md) (46 entries)
- [2024-08](202408/monthly-index.md) (31 entries)
- [2024-07](202407/monthly-index.md) (12 entries)

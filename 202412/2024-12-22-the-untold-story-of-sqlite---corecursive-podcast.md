# The Untold Story of SQLite - CoRecursive Podcast
- URL: https://corecursive.com/066-sqlite-with-richard-hipp/
- Added At: 2024-12-22 07:37:01
- [Link To Text](2024-12-22-the-untold-story-of-sqlite---corecursive-podcast_raw.md)

## TL;DR
《CoRecursive》播客采访了SQLite开发者Richard Hipp，探讨了SQLite的起源、广泛应用及其独立开发和严格测试的成功之道。SQLite已成为全球核心基础设施，Richard通过自给自足的开发和高质量标准确保了其长期稳定性和可维护性。

## Summary
1. **播客简介**：
   - 播客名为《CoRecursive》，主持人是Adam Gordon Bell。
   - 每期节目邀请一位嘉宾分享某个软件背后的故事。
   - 本集主题是SQLite的开发者Richard Hipp，讨论他如何应对SQLite成为全球核心基础设施的挑战。

2. **SQLite的广泛应用**：
   - SQLite无处不在，存在于浏览器、手机、汽车、商用飞机等设备中。
   - 用于存储iMessages和WhatsApp消息。
   - 通过在电脑上搜索“*.db”文件，会发现许多SQLite数据库。

3. **SQLite的起源**：
   - Richard Hipp在为Bath Iron Works公司工作时，参与了DDG-79 Oscar Austin战舰的软件开发。
   - 项目涉及复杂的管道和阀门控制系统，数据存储在Informix数据库中。
   - Informix数据库的不稳定性导致应用程序频繁崩溃，Richard因此萌生了开发SQLite的想法。

4. **NP-Complete问题**：
   - 战舰的管道系统问题属于NP-Complete问题，需要使用启发式算法来快速找到近似解。
   - Informix数据库的不可靠性让Richard意识到需要一个更稳定的数据库解决方案。

5. **SQLite V1的开发**：
   - 2000年，Richard在政府合同暂停期间开始开发SQLite。
   - 他借鉴了编译器的经验，将SQL语句视为程序，编译成字节码并运行。
   - SQLite最初并未在战舰项目中使用，但后来被用于开发测试。

6. **SQLite的早期成功**：
   - SQLite发布后迅速吸引了大量关注，尤其是在Palm Pilot上运行SQL数据库的消息引发了广泛兴趣。
   - Richard持续改进SQLite，逐渐吸引了更多用户。

7. **与科技巨头的合作**：
   - **Motorola**：2001年，Motorola联系Richard，希望将SQLite集成到他们的手机操作系统中。Richard为Motorola开发了定制功能，并获得了8万美元的合同。
   - **America Online (AOL)**：AOL希望将SQLite集成到他们的CD中，Richard为此开发了一个临时索引功能，但后来发现该功能存在缺陷。
   - **Symbian OS和Nokia**：Nokia的Symbian OS团队邀请Richard到伦敦讨论合作，SQLite在他们的数据库引擎测试中胜出，Richard与Nokia签订了开发合同。

8. **SQLite Consortium的成立**：
   - 随着SQLite的广泛应用，用户要求提高“巴士因子”（即项目可持续性）。
   - Richard成立了SQLite Consortium，Mozilla基金会的Mitchell Baker提供了指导，建议开发者保持对项目的控制权。
   - 最终，Mozilla、Symbian和Adobe成为SQLite Consortium的创始成员。

9. **Android的崛起**：
   - 2005年，Richard与Google的Android团队合作，见证了Android的早期开发。
   - Android的快速迭代开发模式与传统手机制造商的缓慢开发周期形成鲜明对比，Richard意识到Android的潜力。

10. **SQLite的测试与质量保证**：
    - SQLite在Android设备上的广泛应用暴露了许多问题，Richard开始重视软件质量。
    - 他引入了航空标准的DO-178B质量标准，目标是实现100%的MCDC测试覆盖率。
    - 经过一年的努力，SQLite达到了100%的MCDC测试覆盖率，此后几乎没有再收到Android的错误报告。

11. **测试的规模**：
    - SQLite的测试套件包括TCL测试、TH3测试（100% MCDC覆盖）、SQL逻辑测试等。
    - 每次发布前，SQLite会运行数十亿次测试，确保代码的稳定性。

12. **SQLite的独立开发**：
    - Richard从零开始构建SQLite，没有依赖现有的数据库引擎或理论。
    - 他通过阅读Donald Knuth的《计算机程序设计艺术》学习B树算法，并自己实现了B树。
    - SQLite的解析器生成器Lemon和版本控制系统Fossil都是Richard自己开发的。

13. **自由与自给自足**：
    - Richard认为，自己构建所有工具和系统是一种自由，因为他不依赖第三方供应商。
    - 这种自给自足的开发方式让SQLite能够灵活应对各种需求，并保持长期的可维护性。

14. **总结**：
    - SQLite的成功不仅在于其广泛的应用，还在于Richard Hipp对软件质量的执着追求和自给自足的开发理念。
    - 通过严格的测试和独立开发，SQLite成为了全球核心基础设施的一部分，并持续为数百万设备提供支持。

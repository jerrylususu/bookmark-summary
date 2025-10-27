Title: Gamekeeper：像 Git 一样管理游戏存档 - 少数派

URL Source: https://sspai.com/post/102928

Published Time: 1970-01-01T00:00:00.000Z

Markdown Content:
Gamekeeper：像 Git 一样管理游戏存档 - 少数派

===============

[](https://sspai.com/)

[共创](https://sspai.com/create)

[PRIME](https://sspai.com/prime)

[Matrix](https://sspai.com/matrix)

[栏目](https://sspai.com/series)

Pi Store

 无需申请，自由写作 

任何用户都可使用写作功能。成功发布 3 篇符合基本规则的内容，可成为正式作者。[了解更多](https://manual.sspai.com/guide/init/)

共创 PRIME Matrix 栏目 Pi Store

![Image 8](https://cdnfile.sspai.com/2025/10/26/article/815f769b-722e-fc4e-b283-038a807cf8e9.jpeg?imageMogr2/auto-orient/thumbnail/!1420x708r/gravity/center/crop/1420x708/format/webp/ignore-error/1)[![Image 9](https://cdnfile.sspai.com//2020/07/15/03489f13d747077eafb9f844d842ed53.png)](javascript:;)

Gamekeeper：像 Git 一样管理游戏存档

主作者

[![Image 10: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!72x72r/gravity/center/crop/72x72/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 11](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 12](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

联合作者

[![Image 13: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!72x72r/gravity/center/crop/72x72/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 14](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 15](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

10/07 08:36

利益相关声明：作者与文中产品有直接的利益相关（开发者、自家产品等）

**Matrix 首页推荐**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

* * *

记得当年第一次玩到 3A 大作时，我在网吧刚刚结束了一场激烈的枪战，趁着「贤者时间」逛到了单机游戏区，阴差阳错地打开了一个名为《使命召唤 6：现代战争》的游戏。自此以后，CF 就从「小甜甜」变成了「牛夫人」。

如今十几年时间过去，我依旧保持着对单机游戏的热爱，单论 PC 平台上玩过的作品应该也有上百个了，但是这么多年以来，每次玩游戏时也总有一朵乌云萦绕在心头，那就是丢档。

第一次丢档事故发生在《孤岛惊魂 3》，那是我玩的第一款开放世界大作，直到现在我也不知道当初为什么会发生丢档，只知道一觉醒来什么都没了，那感觉真是从天堂到地狱，想死的心都有了。但没办法，那时候还是个初出茅庐的小白，云存档什么的完全没听说过，无奈转投《孤岛惊魂 4》——所以直到现在《孤岛惊魂 3》对我来说依旧是一段未尽的旅程，而这还不是这严重的一次。最严重的一次是因为折腾双系统，直接把操作系统搞没了，等电脑从售后拿回来，C 盘毫无意外地崭新如初。

那次到底丢了多少个档都已经算不清了，但也就是那次丢档事故之后，我开始认真研究起了存档管理。

Git 为什么不行
---------

存档管理这需求说复杂也不复杂，它本质就是文件备份和多平台同步。

所以早期我一直在尝试使用网盘搭配各种同步软件，比如 Synching、Goodsync 等，然后再自己写点脚本搞得更加自动化一点，也就差不多凑合用了。直到后来「那个男人」出现了——宫崎英高，老贼的魂游把我虐得死去活来却又欲罢不能，但魂学家们都知道老贼的游戏出了名地喜欢弱引导和多结局，不看攻略的话一不小心哪个结局就没了，不多玩几个周目根本下不来，像我这种强迫症直接横死当场。

这时我才意识到，存档管理这需求说简单还真没那么简单，现在的 3A 大作不多搞几个结局都不好意思叫 3A，外加存档机制被他们玩得飞起，连什么存档献祭玩法都来了，简单的线性存档管理显然已经不适用于当下的环境了。

怎么办呢？我第一时间就想到了那个程序员们家喻户晓的版本管理神器——Git，Git 天生就适合创建多分支，一个 Git 仓库几十上百个分支完全不在话下，再加上其分布式的仓库同步机制，多分支管理和多平台同步一起盘活了，那么 Git 会是最终答案吗？

![Image 16](https://cdnfile.sspai.com/2025/10/07/5fce0377f12d1c27b8882e1bd76d9080.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1/format/webp)
接下来的日子里，我一直用 Git 管理着我的游戏存档，也逐渐发现了 Git 的问题：

首先，Git 的使用太过复杂，想要在玩家圈子里普及开来几乎是不可能的；其次，Git 毕竟不是为存档管理而设计的，它不保存文件的创建时间、不保存空目录等特性在少数游戏上可能造成存档混乱；最后，我最理想的存档管理工具不仅仅只是存档管理，还包括诸如存档路径识别、存档分享、Mod 管理等等功能，这些东西都无法围绕 Git 进行构建。

虽然 Git 不是最终的答案，但我认为站在 Git 的肩膀上是绝对没问题的，既然 Git 不能满足需求，那咱们就给它改造一下，创造一个专为玩家设计的 Git，于是 Gamekeeper 这个独立开发项目就这么开始了。

**Gamekeeper 又如何做到**
--------------------

### **自动识别存档目录**

虽然玩家群体基本上都是懂电脑的，但游戏厂商实在是太能藏了，找游戏存档的位置依旧是个比较麻烦的活，好在社区的力量是无穷大的， [mtkennerly](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fmtkennerly) 大神开源项目 [ludusavi](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fmtkennerly%2Fludusavi) 会定期从 wiki 网站上抓取数量庞大的游戏数据，有了这些数据做支撑，寻找存档位置便不再那么棘手。

Gamekeeper 首次启动便会尝试下载 ludusavi 项目的全量数据文件 manifest.yaml：

![Image 17](https://cdnfile.sspai.com/2025/10/07/c44634a9e18bd4b260faac6566a4c41c.gif)
下载完成后，在新增游戏界面中，输入游戏的官方英文名称便可搜索到目标游戏，直接选中后，包括游戏的安装目录、启动文件、存档目录甚至游戏封面和图标都全部准备好了，紧接着点提交便添加完毕：

![Image 18](https://cdnfile.sspai.com/2025/10/07/3fa78c525c6d8e6e92ea79abbacb0eff.gif)

自动识别

### **多存档空间设计**

Gamekeeper 将游戏存档划分在一个个相互独立的存档空间内，所谓存档空间就是游戏内常说的存档槽位，因为现在的很多游戏都抛弃了存档槽机制，搞得大家只能一个存档玩到底，Gamekeeper 把这套机制重新加了回来，而且更上一层楼。

Gamekeeper 的存档空间没有数量上限，你像要多少个存档空间就创建多少存档空间，一个玩战士、一个玩法师，一个给自己玩、一个给女朋友玩：

![Image 19](https://cdnfile.sspai.com/2025/10/07/92739d7e1741e57d2840fe7633e2b238.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1/format/webp)

多存档空间

### **多分支存档管理**

多分支存档管理是 Gamekeeper 的开发重点。

首先软件的所有存档空间都需要创建一个初始存档，初始存档是一个空存档，它代表的是游戏尚未开始前的存档数据，是后续所有分支的起点；同时，Gamekeeper 参考 Git 设计了正在使用的存档的概念，它相当于 Git 中的 HEAD 指针，可以简单地理解为上一次保存的存档，在它的基础上提交新的存档和新的分支，就可以让存档空间内的分支图不断演进，最终形成一个由无数存档和分支组成的「分支树」：

![Image 20](https://cdnfile.sspai.com/2025/10/07/e434914eff9ac31e916c401421adb3fd.gif)

多分支存档管理

整个分支树在软件界面中井然有序，哪个存档属于哪个分支、谁先保存谁后保存，一目了然，可选择任意存档进行回档，再也不怕错过任何一个游戏结局。

### **差异存储模型**

现在的 3A 游戏容量是越来越膨胀，相应的存档容量也越来越膨胀，Gamekeeper 口号是不放过游戏中的任何一个精彩瞬间。以开放世界游戏举例，一个游戏玩完存档保存上千次都是常有的事，如果把这些存档全部保存下来，一个存档占用只有几 MB 的话，随着时间的推移也会达到以 GB 计算的程度。

Gamekeeper 参考 Git 和 SVN 的设计，采用差异存储模型保存存档，也就是每次只保存新旧存档之间产生变化的数据，而游戏每次覆写存档一般只改动少量数据，所以 Gamekeeper 所保存的存档数据，最终空间占用比较小，相应的软件所支持的存档数量便会直线上升。

![Image 21](https://cdnfile.sspai.com/2025/10/07/3029926e8af20c815813866258dd9069.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1/format/webp)

差异存储模型

**后续开发计划**
----------

Gamekeeper 目前还仅仅只是初版，围绕上面这些基础功能未来还计划开发新的玩法：

1.   利用网络存储服务进行多平台同步，即云存档功能
2.   存档分享，将自己的存档分享给他人或者获取他人分享的存档
3.   跟踪游戏进程进行存档监控，实现实时保存存档、定时保存存档等
4.   参考 Git 的 Tag 功能实现标签系统

对 Gamekeeper 感兴趣的用户可前往[官网](https://sspai.com/link?target=https%3A%2F%2Fgamekeeper.thinkuni.net%2F)免费下载并使用，详细说明请参考官网中的使用文档。

![Image 22](https://cdnfile.sspai.com/2025/10/07/2440e76a68d50ffae6558c8ed964d9e2.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1/format/webp)

官网截图

> 关注[少数派小红书](https://www.xiaohongshu.com/user/profile/63f5d65d000000001001d8d4)，感受精彩数字生活 🍃

> 实用、好用的 [正版软件](https://sspai.com/mall)，少数派为你呈现 🚀

[](https://sspai.com/s/JYjP)

66

19

[](https://service.weibo.com/share/share.php?url=https%3A%2F%2Fsspai.com%2Fpost%2F102928?ref=weibo&title=%E3%80%90Gamekeeper%EF%BC%9A%E5%83%8F%20Git%20%E4%B8%80%E6%A0%B7%E7%AE%A1%E7%90%86%E6%B8%B8%E6%88%8F%E5%AD%98%E6%A1%A3%E3%80%91%E7%AB%99%E5%9C%A8%20Git%20%E7%9A%84%E8%82%A9%E8%86%80%E4%B8%8A%EF%BC%8C%E5%88%9B%E9%80%A0%E4%B8%80%E4%B8%AA%E4%B8%93%E4%B8%BA%E7%8E%A9%E5%AE%B6%E8%AE%BE%E8%AE%A1%E7%9A%84%20Git%20%E5%BC%8F%E5%AD%98%E6%A1%A3%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7%E3%80%82%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdnfile.sspai.com%2F2025%2F10%2F26%2Farticle%2F815f769b-722e-fc4e-b283-038a807cf8e9.jpeg%3FimageMogr2%2Fauto-orient%2Fthumbnail%2F!1420x708r%2Fgravity%2Fcenter%2Fcrop%2F1420x708%2Fformat%2Fwebp%2Fignore-error%2F1&appkey=3196502474#)

扫码分享

目录 3

*   Git 为什么不行 
*   Gamekeeper 又如何做到 
    *   自动识别存档目录 
    *   多存档空间设计 
    *   多分支存档管理 
    *   差异存储模型 

*   后续开发计划 

 讨论 

我来说一句

发布

发表评论

发布

 本文责编：@ [克莱德](https://sspai.com/u/clyde)

[#游戏](https://sspai.com/tag/%E6%B8%B8%E6%88%8F)

[#应用推荐](https://sspai.com/tag/%E5%BA%94%E7%94%A8%E6%8E%A8%E8%8D%90)

[#App+1](https://sspai.com/tag/App+1)

66

[![Image 23: 清钰](https://cdnfile.sspai.com/2022/04/12/avatar/e8c3dc5934808a4ad70af0bf071b5e80.jpeg?imageMogr2/auto-orient/thumbnail/!32x32r/gravity/center/crop/32x32/format/webp/ignore-error/1)](https://sspai.com/u/har6qzrj/updates)

[![Image 24: dead_lee](https://cdnfile.sspai.com/2022/04/02/314dec5e1cd48e5ae7297e6f157b3f5b.jpeg?imageMogr2/auto-orient/thumbnail/!32x32r/gravity/center/crop/32x32/format/webp/ignore-error/1)](https://sspai.com/u/dead_lee/updates)

[![Image 25: XavierWu](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png?imageMogr2/auto-orient/thumbnail/!32x32r/gravity/center/crop/32x32/format/webp/ignore-error/1)](https://sspai.com/u/qhm7gylw/updates)

[![Image 26: Nikki](https://cdnfile.sspai.com/2022/04/14/2457aaab85a1e3fa81905363d255ac04.jpg?imageMogr2/auto-orient/thumbnail/!32x32r/gravity/center/crop/32x32/format/webp/ignore-error/1)](https://sspai.com/u/kq0ipti5/updates)

[![Image 27: LeBennington](https://cdnfile.sspai.com/2023/06/26/avatar/e88a105bc3266ea658f35e07752521d7?imageMogr2/auto-orient/quality/90/ignore-error/1)](https://sspai.com/u/lebennington/updates)

[清钰](https://sspai.com/u/har6qzrj/updates)、[dead_lee](https://sspai.com/u/dead_lee/updates)、[XavierWu](https://sspai.com/u/qhm7gylw/updates)等 66 人为本文章充电

[](https://service.weibo.com/share/share.php?url=https%3A%2F%2Fsspai.com%2Fpost%2F102928?ref=weibo&title=%E3%80%90Gamekeeper%EF%BC%9A%E5%83%8F%20Git%20%E4%B8%80%E6%A0%B7%E7%AE%A1%E7%90%86%E6%B8%B8%E6%88%8F%E5%AD%98%E6%A1%A3%E3%80%91%E7%AB%99%E5%9C%A8%20Git%20%E7%9A%84%E8%82%A9%E8%86%80%E4%B8%8A%EF%BC%8C%E5%88%9B%E9%80%A0%E4%B8%80%E4%B8%AA%E4%B8%93%E4%B8%BA%E7%8E%A9%E5%AE%B6%E8%AE%BE%E8%AE%A1%E7%9A%84%20Git%20%E5%BC%8F%E5%AD%98%E6%A1%A3%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7%E3%80%82%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdnfile.sspai.com%2F2025%2F10%2F26%2Farticle%2F815f769b-722e-fc4e-b283-038a807cf8e9.jpeg%3FimageMogr2%2Fauto-orient%2Fthumbnail%2F!1420x708r%2Fgravity%2Fcenter%2Fcrop%2F1420x708%2Fformat%2Fwebp%2Fignore-error%2F1&appkey=3196502474#)

扫码分享

[](http://www.instapaper.com/hello2?url=https%3A%2F%2Fsspai.com%2Fpost%2F102928&title=Gamekeeper%EF%BC%9A%E5%83%8F%20Git%20%E4%B8%80%E6%A0%B7%E7%AE%A1%E7%90%86%E6%B8%B8%E6%88%8F%E5%AD%98%E6%A1%A3&description=%E7%AB%99%E5%9C%A8%20Git%20%E7%9A%84%E8%82%A9%E8%86%80%E4%B8%8A%EF%BC%8C%E5%88%9B%E9%80%A0%E4%B8%80%E4%B8%AA%E4%B8%93%E4%B8%BA%E7%8E%A9%E5%AE%B6%E8%AE%BE%E8%AE%A1%E7%9A%84%20Git%20%E5%BC%8F%E5%AD%98%E6%A1%A3%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7%E3%80%82)

 举报本文章 

[![Image 28: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!84x84r/gravity/center/crop/84x84/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[Thinkuni](https://sspai.com/u/thinkuni/updates)

 还没有介绍自己 

 关注 

[![Image 29](https://cdnfile.sspai.com/10/14/2025/article/274b7794-c999-f092-c951-8b506fe91a35.png?imageMogr2/auto-orient/thumbnail/!1096x252r/gravity/center/crop/1096x252/format/webp/ignore-error/1)](https://sspai.com/a/nLgaEz)

 全部评论(19) 

热门排序

![Image 30](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png)

请在 登录 后评论...

[![Image 31: 郁闷人](https://cdnfile.sspai.com/2022/05/10/99b6d8c1eb738d65411780c2a9774db2.png?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/ko1zh3t9/updates)

[![Image 32](https://cdnfile.sspai.com/2022/05/10/99b6d8c1eb738d65411780c2a9774db2.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/ko1zh3t9)关注

郁闷人

[郁闷人 [![Image 33](https://cdnfile.sspai.com/2022/05/10/99b6d8c1eb738d65411780c2a9774db2.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/ko1zh3t9)关注 郁闷人](https://sspai.com/u/ko1zh3t9/updates)

昨天 15:22

好东西啊，之前调游戏存档的时候就发现，不同的游戏都有不同的风格，有的喜欢放自己的目录，有的喜欢放Windows游戏文件夹，有的放用户目录，千奇百怪也没什么官方文档

1 4 0 举报 昨天 15:22

[![Image 34: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 35](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 36](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

03:52

感谢支持，欢迎提意见

0 0 举报 03:52

[![Image 37: Eltrac](https://cdnfile.sspai.com/2024/01/25/3207de57c8b476d552ed7dc3376dddc8.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/8cubw13e/updates)

[![Image 38](https://cdnfile.sspai.com/2024/01/25/3207de57c8b476d552ed7dc3376dddc8.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/8cubw13e)关注

Eltrac

[Eltrac [![Image 39](https://cdnfile.sspai.com/2024/01/25/3207de57c8b476d552ed7dc3376dddc8.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/8cubw13e)关注 Eltrac](https://sspai.com/u/8cubw13e/updates)

03:04

看到只有 Windows 本来想问问会不会出 macOS 版本，随后立刻意识到自己拿 mac 打游戏这件事情本身就挺疯的

![Image 40](https://cdnfile.sspai.com/2025/10/27/99bcaf618f94f507faabb57046c97326.gif?imageMogr2/auto-orient/quality/90/ignore-error/1)

1 2 0 举报 03:04

[![Image 41: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 42](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 43](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

03:44

哈哈，linux都有打游戏的呢，有空了都会计划移植

0 0 举报 03:44

[![Image 44: TonY](https://cdnfile.sspai.com/2022/07/25/avatar/fd6b5cab997a88e7aec7e0603409c2ae.png?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/tony0624/updates)

[![Image 45](https://cdnfile.sspai.com/2022/07/25/avatar/fd6b5cab997a88e7aec7e0603409c2ae.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/tony0624)关注

TonY

[TonY [![Image 46](https://cdnfile.sspai.com/2022/07/25/avatar/fd6b5cab997a88e7aec7e0603409c2ae.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/tony0624)关注 TonY](https://sspai.com/u/tony0624/updates)

昨天 17:17

感觉这个需求还是不小，如果能有主机的解决方案就更好了

3 2 0 举报 昨天 17:17

[![Image 47: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 48](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 49](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

00:08

Steam deck那边可以计划一下，ps和xbox就要从长计议了

1 0 举报 00:08

[![Image 50: The_book](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/jylqbt2h/updates)

[![Image 51](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/jylqbt2h)关注

nuomi

[nuomi [![Image 52](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/jylqbt2h)关注 nuomi](https://sspai.com/u/jylqbt2h/updates)

回复

[Thinkuni [![Image 53](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

02:24

PS 和 Xbox 我感觉没戏啊，这俩平台连 Mod 都打不了。

0 0 举报 02:24

[![Image 54: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 55](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 56](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

回复

[nuomi [![Image 57](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/jylqbt2h)关注 nuomi](https://sspai.com/u/jylqbt2h/updates)

03:42

是啊，这两个平台太封闭，除非能得到官方支持

0 0 举报 03:42

[![Image 58: 为什么选](https://cdnfile.sspai.com/2022/06/15/263cbb6dae1f355641db67a7119e98a3.png?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/vuejs/updates)

[![Image 59](https://cdnfile.sspai.com/2022/06/15/263cbb6dae1f355641db67a7119e98a3.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/vuejs)关注

为什么选

[为什么选 [![Image 60](https://cdnfile.sspai.com/2022/06/15/263cbb6dae1f355641db67a7119e98a3.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/vuejs)关注 为什么选](https://sspai.com/u/vuejs/updates)

01:27

我派最近少有的，看完想立马下载的软件，平时的文章/教程都太复杂了，我只想简单直接高效

1 1 0 举报 01:27

[![Image 61: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 62](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 63](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

03:52

感谢支持，欢迎提意见

0 0 举报 03:52

[![Image 64: 黑猫Bon](https://cdnfile.sspai.com/2022/08/27/d1d91dcc9c8e19f1956795326c3152d6.jpeg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/cboqolkt/updates)

[![Image 65](https://cdnfile.sspai.com/2022/08/27/d1d91dcc9c8e19f1956795326c3152d6.jpeg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/cboqolkt)关注

黑猫Bon

少数派作者

[黑猫Bon [![Image 66](https://cdnfile.sspai.com/2022/08/27/d1d91dcc9c8e19f1956795326c3152d6.jpeg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/cboqolkt)关注 黑猫Bon 少数派作者](https://sspai.com/u/cboqolkt/updates)

昨天 14:44

是好东西啊，虽然我现在不玩游戏了

1 1 0 举报 昨天 14:44

[![Image 67: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 68](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 69](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

04:19

感谢认可

0 0 举报 04:19

[![Image 70: 臭烘烘奶茶](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png)](https://sspai.com/u/9gg1z56y/updates)

[![Image 71](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png)](https://sspai.com/u/9gg1z56y)关注

臭烘烘奶茶

[臭烘烘奶茶 [![Image 72](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png)](https://sspai.com/u/9gg1z56y)关注 臭烘烘奶茶](https://sspai.com/u/9gg1z56y/updates)

昨天 14:44

有点意思，个人感觉后续计划的第三条比较有用。这种工具软件最好做成自动化和无感操作的，玩个游戏还要像上班一样管理存档，任谁都要恼的。

1 1 0 举报 昨天 14:44

[![Image 73: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 74](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 75](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

00:10

会争取早日把饼烙出来(^_−)☆

0 0 举报 00:10

[![Image 76: The_book](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/The_book/updates)

[![Image 77](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/The_book)关注

The_book

[The_book [![Image 78](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/The_book)关注 The_book](https://sspai.com/u/The_book/updates)

10:27

看到这个就想起我曾经想基于git开发一个笔记软件，每次增删都自动触发一次提交，每次保存文件触发一次tag，然后还支持分支啥的。

0 0 0 举报 10:27

[![Image 79: eeee](https://cdnfile.sspai.com/2023/11/07/avatar/c3febe5f1208d7c49cb83cc2ef07d7c7?imageMogr2/auto-orient/quality/90/ignore-error/1)](https://sspai.com/u/drbakm5d/updates)

[![Image 80](https://cdnfile.sspai.com/2023/11/07/avatar/c3febe5f1208d7c49cb83cc2ef07d7c7?imageMogr2/auto-orient/quality/90/ignore-error/1)](https://sspai.com/u/drbakm5d)关注

eeee

新手上路

[eeee [![Image 81](https://cdnfile.sspai.com/2023/11/07/avatar/c3febe5f1208d7c49cb83cc2ef07d7c7?imageMogr2/auto-orient/quality/90/ignore-error/1)](https://sspai.com/u/drbakm5d)关注 eeee 新手上路](https://sspai.com/u/drbakm5d/updates)

01:53

能否捕获 steam 成就自动化生成一些节点呢？ 一般来说，成就都是比较重要的节点。

1 0 0 举报 01:53

[![Image 82: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 83](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 84](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

02:10

我记录一下，到时候研究一下steam的api看看方案

0 0 举报 02:10

[![Image 85: 少数派51972004](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png)](https://sspai.com/u/cz6t6ej9/updates)

[![Image 86](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png)](https://sspai.com/u/cz6t6ej9)关注

少数派51972004

[少数派51972004 [![Image 87](https://cdn-static.sspai.com/ui/otter_avatar_placeholder_240511.png)](https://sspai.com/u/cz6t6ej9)关注 少数派51972004](https://sspai.com/u/cz6t6ej9/updates)

00:50

现在单机玩的少，不过思路很不错，相当于并行存储，极大优化了空间

1 0 0 举报 00:50

[![Image 88: Thinkuni](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!80x80r/gravity/center/crop/80x80/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni/updates)

[![Image 89](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注

Thinkuni

新手上路

[Thinkuni [![Image 90](https://cdnfile.sspai.com/2025/10/07/aa5f30d334335fc83dce3af840f969ee.jpg?imageMogr2/auto-orient/thumbnail/!100x100r/gravity/center/crop/100x100/format/webp/ignore-error/1)](https://sspai.com/u/thinkuni)关注 Thinkuni 新手上路](https://sspai.com/u/thinkuni/updates)

03:53

感谢认可

0 0 举报 03:53

 没有更多评论了哦 

 推荐阅读 

[![Image 91](https://cdnfile.sspai.com/2025/09/19/5c82f93397deaa1f521cea3a819541e7.png?imageMogr2/auto-orient/thumbnail/!800x400r/gravity/center/crop/800x400/format/webp/ignore-error/1)](https://sspai.com/post/102198)[![Image 92](https://cdnfile.sspai.com//2020/07/15/03489f13d747077eafb9f844d842ed53.png)](javascript:;)

[![Image 93](https://cdnfile.sspai.com/2025/09/27/4516de861caff69457c1f2a19af19383.jpeg?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)sha2kyou](https://sspai.com/u/tr1ck)

 08/31 22:08 

[App+1｜重要信息放「桌边」，信息流聚合只需一瞥：SideCalendar](https://sspai.com/post/102198)

[![Image 94](https://cdnfile.sspai.com/2025/09/27/4516de861caff69457c1f2a19af19383.jpeg?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)sha2kyou](https://sspai.com/u/tr1ck)

42

[![Image 95](https://cdnfile.sspai.com/2025/07/09/e9aad10a6333421ab87b06a7fb1490cf.jpg?imageMogr2/auto-orient/thumbnail/!800x400r/gravity/center/crop/800x400/format/webp/ignore-error/1)](https://sspai.com/post/100869)

[![Image 96](https://cdnfile.sspai.com/2025/08/17/avatar/d912df69357cd8aac5e87323ffde67ea.png?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)_xy](https://sspai.com/u/fmnpnn8z)

 07/12 08:03 

[App+1｜帮你解决「屏幕内疚」和「早教焦虑」：Lingokids](https://sspai.com/post/100869)

[![Image 97](https://cdnfile.sspai.com/2025/08/17/avatar/d912df69357cd8aac5e87323ffde67ea.png?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)_xy](https://sspai.com/u/fmnpnn8z)

42

[![Image 98](https://cdnfile.sspai.com/2025/05/26/bd959263ab937d6e8d4e2b10720d1f7b.jpg?imageMogr2/auto-orient/thumbnail/!800x400r/gravity/center/crop/800x400/format/webp/ignore-error/1)](https://sspai.com/post/99599)[![Image 99](https://cdnfile.sspai.com//2020/07/15/03489f13d747077eafb9f844d842ed53.png)](javascript:;)

[![Image 100](https://cdnfile.sspai.com/2025/08/17/avatar/d912df69357cd8aac5e87323ffde67ea.png?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)_xy](https://sspai.com/u/fmnpnn8z)

 05/29 09:30 

[App+1 | PDFMathTranslate：PDF 的「无损」翻译工具](https://sspai.com/post/99599)

[![Image 101](https://cdnfile.sspai.com/2025/08/17/avatar/d912df69357cd8aac5e87323ffde67ea.png?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)_xy](https://sspai.com/u/fmnpnn8z)

69

[![Image 102](https://cdnfile.sspai.com/2025/05/07/2ddf1c3cec0dcaaf79c4610b7d545eee.png?imageMogr2/auto-orient/thumbnail/!800x400r/gravity/center/crop/800x400/format/webp/ignore-error/1)](https://sspai.com/post/98966)[![Image 103](https://cdnfile.sspai.com//2020/07/15/03489f13d747077eafb9f844d842ed53.png)](javascript:;)

[![Image 104](https://cdnfile.sspai.com/2023/09/13/e5da20992fc2b8876d0b6d9147efc1dc.png?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)玩出个名堂](https://sspai.com/u/play4fame)

 05/08 02:33 

[一日一技 | 用 HWiNFO 实现游戏内 OSD 信息叠加显示](https://sspai.com/post/98966)

[![Image 105](https://cdnfile.sspai.com/2023/09/13/e5da20992fc2b8876d0b6d9147efc1dc.png?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)玩出个名堂](https://sspai.com/u/play4fame)

34

[![Image 106](https://cdnfile.sspai.com/2025/4/10/article/440432fd-f315-640e-c050-9bf92909739b.png?imageMogr2/auto-orient/thumbnail/!800x400r/gravity/center/crop/800x400/format/webp/ignore-error/1)](https://sspai.com/post/98002)

[![Image 107](https://cdnfile.sspai.com/2022/04/02/fb08192e5a9ed506615176a08cf8c06b.gif?imageMogr2/auto-orient/quality/90/ignore-error/1)Peggy_](https://sspai.com/u/5isr02uh)

 04/10 07:00 

[App+1 | Mac Mouse Fix：让鼠标像触控板一样丝滑](https://sspai.com/post/98002)

[![Image 108](https://cdnfile.sspai.com/2022/04/02/fb08192e5a9ed506615176a08cf8c06b.gif?imageMogr2/auto-orient/quality/90/ignore-error/1)Peggy_](https://sspai.com/u/5isr02uh)

43

[![Image 109](https://cdnfile.sspai.com/2025/03/17/3796e41a22cd5b7d28aa197748221bcd.png?imageMogr2/auto-orient/thumbnail/!800x400r/gravity/center/crop/800x400/format/webp/ignore-error/1)](https://sspai.com/post/97448)[![Image 110](https://cdnfile.sspai.com//2020/07/15/03489f13d747077eafb9f844d842ed53.png)](javascript:;)

[![Image 111](https://cdnfile.sspai.com/2025/03/17/c5e92944af84240dfab96930a37acea3.JPG?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)cloxnu](https://sspai.com/u/yn91h50l)

 03/24 06:54 

[App+1 | 让专注带你跨越山海，更有沉浸感和仪式感的计时器：专注飞机](https://sspai.com/post/97448)

[![Image 112](https://cdnfile.sspai.com/2025/03/17/c5e92944af84240dfab96930a37acea3.JPG?imageMogr2/auto-orient/thumbnail/!48x48r/gravity/center/crop/48x48/format/webp/ignore-error/1)cloxnu](https://sspai.com/u/yn91h50l)

50

![Image 113](https://cdn-static.sspai.com/ui/logo/logo_sspai_icon.png)

App 内打开

 请绑定手机号码 

 取消 

 前往绑定 

[](https://sspai.com/)

[](https://weibo.com/sspaime?is_hot=1)[关注公众号 sspaime ![Image 114](https://cdn-static.sspai.com/ui/gzh_qrcode_home.png)](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU4Mjg3MDAyMQ==&subscene=0#wechat_redirect)[](https://www.xiaohongshu.com/user/profile/63f5d65d000000001001d8d4)[](https://sspai.com/feed)

[下载 App](https://sspai.com/page/client)[联系我们](mailto:contact@sspai.com)[商务合作](https://sspai.com/page/bussiness)[关于我们](https://sspai.com/page/about-us)[用户协议](https://sspai.com/page/agreement)

© 2013-2025 深圳市烧麦网络科技有限公司 - 少数派[粤ICP备09128966号-4](https://beian.miit.gov.cn/) | [粤B2-20211534](https://dxzhgl.miit.gov.cn/)

 确定

*   联系客服
*   [发送邮件](mailto:contact@sspai.com)
*   [商务合作](https://sspai.com/page/bussiness)
*   [少数派 App](https://sspai.com/page/client)

请用微信手机端扫码咨询客服

![Image 115](https://cdn-static.sspai.com/ui/qrcode_service.png)
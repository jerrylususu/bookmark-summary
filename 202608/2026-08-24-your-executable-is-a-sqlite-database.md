# Your executable is a SQLite database
- URL: https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database
- Added At: 2026-08-24 14:31:29
- Tags: #read #hack #deepdive

## TL;DR
文章提出将Linux可执行文件从ELF换成SQLite数据库，原型SELF可运行，工具退化为SQL查询，支持去重、事务化与系统闭包，代价是启动延迟和文件略大。

## Summary
文章的核心思想非常激进：把 Linux 可执行文件格式从传统的 ELF 换成 SQLite 数据库。作者认为 ELF 本身就是一个“不承认自己是数据库”的数据库——它手工实现了字符串驻留、索引、外键、表结构等数据库原语，却导致每个工具（readelf、ld.so、LIEF 等）都要重新解析一遍格式，格式紧凑难以扩展，而且没有自描述 schema。SQLite 则是一个自描述、稳定、可扩展、支持高效查询的格式，很适合作为替代。

作者做了个原型叫 **SELF**（Structured Executable & Linkable Format），并且真的能让系统执行一个 `.sqlite` 文件：

```bash
$ file hello
hello: SQLite 3.x database, application id 0x53454c46, user version 1

$ ./hello
Hello, world!

$ sqlite3 hello 'SELECT soname FROM ldd'
libc.so.6
```

SELF 文件运行只需要两张核心表：`self_meta` 存放 ELF 头信息（键值对），`segments` 存放需要加载到内存的段（类型、虚拟地址、权限、内容 BLOB 等）。符号表则用一张 `symbols` 表和索引替代了 ELF 里的 `.dynstr`、`.gnu.hash`、`.gnu.version_r` 等一堆机制——字符串驻留交给 SQLite 的 TEXT，符号版本变成一列，哈希查找变成 B 树索引。

这样一来，传统 ELF 工具全部退化成 SQL 查询：

- `readelf -l` → `SELECT type,vaddr,memsz,r,w,x FROM segments WHERE type='load'`
- `nm -D --undefined` → `SELECT name,version FROM imports LIMIT 3`
- `ldd` → 一个视图 `ldd`，底层是 `needed` 表的查询
- `strip` → `DELETE FROM sections; DELETE FROM notes; VACUUM;`，程序还能继续运行
- `patchelf` → `UPDATE`

运行机制上，SQLite 文件头部的字节偏移 68 处有一个 4 字节的 `application_id` 字段，作者把它标记为 `SELF`，然后通过 Linux 内核的 `binfmt_misc` 机制注册这个 magic 和一个解释器 `self-exec`。`self-exec` 是普通的 ELF 程序，它链接了 `libsqlite3`，负责从数据库读取段和符号表、映射内存、重定位并跳转到入口点。注意解释器本身不能也是 SELF 格式，否则会无限递归。

动态链接部分更有意思。作者先利用 glibc 的 `rtld-audit` 接口拦截库查找，用 SQL 查询替代文件系统搜索，这样库可以完全存放在数据库里，而不需要以 ELF 文件形式存在于磁盘上。后来又写了一个纯 SQL 动态链接器 `self-ld`，用 SQL 查询完成符号解析和重定位。虽然只是概念验证，但证明了全 SQL 动态链接的可行性。

这种数据库格式还带来了一个很大的优势：**系统闭包**。一个 SQLite 数据库不仅可以包含单个可执行文件，还可以包含它的所有传递依赖。`self closure` 命令会把一个程序及其全部依赖打包进一个数据库文件，并用外键 `resolved_path` 明确解析每个 soname 对应的具体库，消除了传统 ELF `ldd` 的歧义。更进一步，作者把整个用户空间的 723 个可执行文件、400 个共享库、34 万多个符号全部塞进一个 SQLite 文件，结果这个数据库只有 611.9 MiB，而原始 ELF 文件总和是 644.4 MiB——因为数据库天然去重共享了库和符号。

这种设计还允许一些非常反常规的操作：例如 `LD_PRELOAD` 不再是环境变量，而是一张 `preload` 表。你可以用事务开启或关闭全局预加载：

```sql
BEGIN;
CREATE TABLE preload(ord INTEGER PRIMARY KEY, path TEXT);
INSERT INTO preload VALUES (0, 'libmul.so.1.self');
COMMIT;
```

同一个二进制，不改变环境变量、不重新链接，只是往数据库里插入一行，行为就变了。

成本方面，文章给了基准：SELF 文件因为 SQLite 的 B 树开销，单个小文件大约是 ELF 的两倍大；但剥离调试信息后，一个 coreutils 的 SELF 只比 ELF 大不到 1%。延迟上，启动有一个约 5ms 的固定开销（打开 SQLite 和解释器），外加按镜像大小比例的复制成本；而且因为数据从 B 树页复制出来，两个进程不会像 ELF 那样通过 mmap 共享文本页。不过对于很多场景，可查询性、去重和事务化操作带来的收益可能超过启动延迟。

文章最后说，这个原型已经在 GitHub 上（`fzakaria/selfdb`），并且可以用 `nix run .#self-vm` 启动一个 NixOS 虚拟机，其中 `hello` 就是一个 SQLite 数据库。作者认为 Nix 让这种“重建世界”的激进实验变得可能，而 SQLite 作为可执行格式的想法虽然困难，但值得探索。

总之，这篇文章展示了一个概念：可执行文件不必是晦涩的二进制格式，而可以是一个可查询、可修改、可事务化、天然支持去重和闭包的数据库。ELF 的所有复杂性被 SQLite 的成熟机制吸收，工具链大幅简化，甚至催生了“一个文件装下整个用户空间”的可能性。

# Prefer STRICT tables in SQLite
- URL: https://evanhahn.com/prefer-strict-tables-in-sqlite/
- Added At: 2026-07-12 08:52:12
- Tags: #read #database

## TL;DR
本文推荐使用SQLite严格表（STRICT）以强制类型检查，避免灵活类型带来的隐秘错误。建表时加STRICT，需3.37.0+版本。虽迁移旧表有成本，但利大于弊，建议新表优先使用。

## Summary
这篇文章的作者推荐在 SQLite 中使用**严格表（STRICT tables）**，因为它能避免很多由灵活类型系统带来的隐蔽错误，比如把字符串写进整数列。

### 什么是严格表？

默认情况下，SQLite 对数据类型非常宽容：你可以往任何列插入任何类型的值，甚至可以在建表时使用根本不存在的列类型（如 `JSON`、`UUID` 等）。严格表则扭转了这一点 —— 它要求列的类型必须符合规范，并且插入或更新数据时会进行类型校验，不再允许“乱存”。

### 怎么创建严格表？

在建表语句的末尾加上 `STRICT` 关键字即可：

```sql
-- 原本的写法
CREATE TABLE people (name TEXT);
-- 严格表的写法
CREATE TABLE people (name TEXT) STRICT;
```

### 严格表的主要优点

1. **防止插入 / 更新时类型错乱**  
   普通表允许将任意类型放进任意列，严格表则会报错：
   ```sql
   -- 非严格表：不会报错
   CREATE TABLE people_nonstrict (age INTEGER);
   INSERT INTO people_nonstrict (age) VALUES ('garbage');  -- 正常运行

   -- 严格表：会报错
   CREATE TABLE people_strict (age INTEGER) STRICT;
   INSERT INTO people_strict (age) VALUES ('garbage');  -- 错误：不能在 INTEGER 列中存放 TEXT
   ```
   需要注意的是，如果值可以**无损转换**，严格表依然会接受。例如字符串 `'123'` 可以完美转为整数，所以下面两句效果相同：
   ```sql
   INSERT INTO people_strict (age) VALUES ('123');
   INSERT INTO people_strict (age) VALUES (123);
   ```

2. **禁止建表时使用无效的列类型**  
   普通表可以接受 `DATETIME`、`JSON`、`UUID` 甚至拼写错误的 `BLOBB` 等类型，SQLite 不会提醒你这些类型其实不被支持。加上 `STRICT` 后，这些语句都会报错，只有 `INT`、`INTEGER`、`REAL`、`TEXT`、`BLOB` 和 `ANY` 被允许。
   ```sql
   -- 以下全是无效类型，普通表会创建成功，但严格表会报错
   CREATE TABLE tbl (name GARBAGE) STRICT;
   CREATE TABLE tbl (name DATETIME) STRICT;
   CREATE TABLE tbl (name JSON) STRICT;
   CREATE TABLE tbl (name UUID) STRICT;
   CREATE TABLE tbl (name BLOBB) STRICT;
   ```
   同时，严格表还要求每一列必须显式指明类型，所以 `CREATE TABLE tbl (name)` 这种写法也是不允许的。

3. **保留灵活性的 `ANY` 类型**  
   如果你确实需要某列可以存放任意类型的数据，可以使用 `ANY` 类型。即使在严格表中，`ANY` 列也来者不拒：
   ```sql
   CREATE TABLE tbl (value ANY) STRICT;
   INSERT INTO tbl (value) VALUES (123);
   INSERT INTO tbl (value) VALUES ('text');
   INSERT INTO tbl (value) VALUES (12.34);
   INSERT INTO tbl (value) VALUES (X'8647');
   ```

### 严格表的缺点

1. **不能将现有表直接“严格化”**  
   目前没有 `ALTER TABLE ... STRICT` 这种命令，只能通过重建表来实现：
   ```sql
   -- 1. 创建结构相同的严格表
   CREATE TABLE new_people (name TEXT) STRICT;
   -- 2. 复制数据（如果原表数据有类型问题，会在这里报错）
   INSERT INTO new_people SELECT * FROM people;
   -- 3. 替换掉旧表
   DROP TABLE people;
   ALTER TABLE new_people RENAME TO people;
   ```
   如果原表里已经混入了“脏数据”（例如整数列中不小心存了文本），迁移时就需要先清洗或使用 `CAST` 转换。

2. **SQLite 官方团队持不同看法**  
   SQLite 文档中专门有一页[《灵活类型的优点》](https://sqlite.org/flextypegood.html)，认为 SQLite 宽容的类型系统在很多场景下其实是好事（比如当键值存储、存放混杂的临时属性、直接导入不规整的 CSV 等）。作者虽然承认这些场景确实存在，但他个人遇到的大量 bug 都源自“意料之外的数据类型”，因此他更倾向于让错误尽早暴露。另外，数据源中也有将非严格表称为“遗留模式”的注释，但作者还是更信任官方文档的立场。

3. **仅限 SQLite 3.37.0 及以上版本**  
   严格表是 2021 年 11 月发布的 3.37.0 版才加入的特性。如果使用的 SQLite 版本低于此，就无法创建或读取包含严格表的数据库文件（即使严格表已经存在于文件中，老版本也会直接报错）。

4. **性能问题？**  
   理论上严格表在插入、更新时需要多做一次类型检查，会增加一点开销。但作者自己用脚本测试了向 100 列的表中插入数百万行数据的情况，多台机器上都未发现明显性能差异，磁盘占用也完全一样。他甚至认为，因为不会意外触发 SQLite 的列亲和机制（column affinity），某些场景下严格表可能性能更好，不过他没有进一步测试。

### 总结

作者个人认为，严格表的优点远大于缺点：它能在数据写入时就拦住类型错误，强迫开发者明确每一列的类型，从而提升数据完整性。他并不是说严格表是万能药，但只需简单地在建表时加上 `STRICT`，就能带来很大的收益。如果你的项目还在使用老版本的 SQLite 或者确实需要极大灵活性的表，可以不用；但新建表时，他建议大家优先考虑严格表。

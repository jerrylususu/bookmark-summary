Title: Collection of insane and fun facts about SQLite - blag

URL Source: https://avi.im/blag/2024/sqlite-facts/

Markdown Content:
*   SQLite is the most deployed and most used database. There are over one trillion (1000000000000 or a million million) SQLite databases in active use.
    
    It is maintained by [three people](https://www.sqlite.org/crew.html). They don’t allow outside contributions.
    
*   SQLite is likely used more than all other database engines combined. Billions and billions of copies of SQLite exist in the wild. It’s everywhere.
    
    ![Image 27](https://avi.im/blag/images/2024/sqlite-fact-1.png)
*   It is also probably one of the top five most deployed software modules.
    
    ![Image 28](https://avi.im/blag/images/2024/sqlite-fact-2.png)
*   [Hwaci](https://hwaci.com/) is the company behind SQLite. They are also into music(?)
    
    ![Image 29](https://avi.im/blag/images/2024/sqlite-fact-3.png)
    
*   SQLite originated from a US warship. D. Richard Hipp (DRH) was building software for the USS Oscar Austin, a Navy destroyer. The existing software would just stop working whenever the server went down (this was in the 2000s). For a battleship, this was unacceptable.
    
    So DRH asked the question: what if the database just worked without any server? In DRH words:
    
    > Why do we even need a server? Why can’t I pull this directly off the disk drive? That way if the computer is healthy enough, it can run our application at all, we don’t have dependencies that can fail and cause us to fail, and I looked around and there were no SQL database engines that would do that, and one of the guys I was working with says, “Richard, why don’t you just write one?” “Okay, I’ll give it a try.” I didn’t do that right away, but later on, it was a funding hiatus. This was back in 2000, and if I recall correctly, Newt Gingrich and Bill Clinton were having a fight of some sort, so all government contracts got shut down, so I was out of work for a few months, and I thought, “Well, I’ll just write that database engine now.”
    
*   Unlike most open source project that uses standard licenses (like MIT or GPL), SQLite does not come with a OSI-approved license.
    
    ![Image 30](https://avi.im/blag/images/2024/sqlite-fact-4.png)Instead, SQLite is released into the public domain and it has even fewer restrictions.
    
    Also note that this can be a [problem](https://opensource.org/blog/public-domain-is-not-open-source) in some countries/jurisdictions where public domain is not recognized. Hence, SQLite [sells licenses](https://www.sqlite.org/purchase/license), called ‘Warranty of Title’.
    
*   They don’t allow outside contributions. You _cannot_ just send a pull request and hope the patch will be accepted.
    
    ![Image 31](https://avi.im/blag/images/2024/sqlite-fact-5.png)
*   Open Source, Not Open Contribution
    
    ![Image 32](https://avi.im/blag/images/2024/sqlite-fact-6.png)Contributing to SQLite is invite-only (I don’t have a source). Only after you are invited and have signed an affidavit dedicating your contribution to the public domain can you submit patches.
    
*   How do they cook?
    
    There are over 600 lines of test code for every line of code in SQLite. Tests cover 100% of branches (and 100% [MC/DC](https://en.wikipedia.org/wiki/Modified_condition/decision_coverage)) in the library. The test suite is extremely diverse, including fuzz tests, boundary value tests, regression tests, and tests that simulate operating system crashes, power losses, I/O errors, and out-of-memory errors.
    
    SQLite first began as a [Tcl extension](https://www.sqlite.org/tclsqlite.html), and its primary test suite is written in Tcl.
    
*   Interestingly, some SQLite tests are proprietary. The test suite called [TH3 (Test Harness 3)](https://www.sqlite.org/th3.html), which achieves 100% branch coverage of the code, is proprietary and is not open to access.
    
    I don’t know any other project which has made code free, but test suites are paid.
    
    However, they could not sell a single copy of TH3. DRH said in a podcast:
    
    > The 100% MCD tests, that’s called TH3. That’s proprietary. I had the idea that we would sell those tests to avionics manufacturers and make money that way. We’ve sold exactly zero copies of that so that didn’t really work out.
    
    In order to get access, one needs to be part of SQLite Consortium, which costs $120K/yearly.
    
*   It’s an interesting business model. They generate revenue through licenses, paid support, maintenance services, consortium membership, and commercial extensions.
    
*   SQLite does not have a Code of Conduct (CoC), rather [Code of Ethics](https://sqlite.org/codeofethics.html) derived from “instruments of good works” from chapter 4 of The Rule of St. Benedict
    
    ![Image 33](https://avi.im/blag/images/2024/sqlite-coe.png)
*   In SQLite: In place of a legal notice, here is a [blessing](https://github.com/sqlite/sqlite/blob/624cb96/src/wal.c#L4,#L9):
    
    ![Image 34](https://avi.im/blag/images/2024/sqlite-fact-11.jpeg)All the of the source code files come with a blessing.
    
*   SQLite is so fast, they compete with `fopen`. For some use cases, you can use SQLite instead of a filesystem, that can be 35% faster.
    
    ![Image 35](https://avi.im/blag/images/2024/sqlite-fact-7.png)
*   SQLite vs Redis (guess which is faster?)
    
    ![Image 36](https://avi.im/blag/images/2024/sqlite-fact-8.png)For [some usecases](https://x.com/iavins/status/1849422515027763227), the SQLite can be faster than Redis due to network stack and (de)serialisation overhead.
    
*   But, unlike most databases, SQLite has a single writer model. You cannot have more than one concurrent writer.
    
    This was also changed recently in 2010 by adding WAL mode. Before that, you could have either readers or a writer, but never together.
    
*   There are other things which are very common in other databases but not in SQLite:
    
    *   The default is rollback journal mode, which restricts you to have either multiple readers or a single writer
    *   Foreign Keys are disabled; they are opt-in
    *   It is “weakly typed”. SQLite calls it “type affinity”. Meaning you can insert whatever in a column even though you have defined a type. Strong typed columns are opt-in (by [`STRICT`](https://www.sqlite.org/stricttables.html) tables).
    *   [Many of the `ALTER` commands](https://sqlite.org/omitted.html) you expect in other databases don’t work. For example, you cannot add a contraint to an existing column. (They recently added ability to rename a column name)
    
    There is a whole [list of quirks](https://www.sqlite.org/quirks.html) here.
    
*   I hate that it doesn’t enforce types. It’s totally YOLO:
    
    ```
    CREATE TABLE user(id INTEGER);
    INSERT into user VALUES ("YOLO!"); --- This works!
    ```
    
    Not only that, it does not throw any error if you give some random type.
    
    `CREATE TABLE t(value TIMMYSTAMP);`
    
    There is no `TIMMYSTAMP` type, but SQLite accepts this happily.
    
    SQLite has five types: `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB`. Want to know something cursed? The type affinity works by [substring match](https://www.sqlite.org/datatype3.html#determination_of_column_affinity)!
    
    ```
    CREATE TABLE t(value SPONGEBLOB) --- This is BLOB type!
    ```
    
    So yeah, this happens too:
    
    > Note that a declared type of “FLOATING POINT” would give INTEGER affinity, not REAL affinity, due to the “INT” at the end of “POINT”.
    
*   This is one my [favorite lore](https://x.com/iavins/status/1865746403072389612). SQLite had to change the default prefix from `sqlite_` to `etilqs_` when users started calling developers in the middle of the night
    
    ![Image 37](https://avi.im/blag/images/2024/sqlite-fact-9.png)
*   SQLite takes backward compatibility very seriously
    
    > All releases of SQLite version 3 can read and write database files created by the very first SQLite 3 release (version 3.0.0) going back to 2004-06-18. This is “backwards compatibility”. The developers promise to maintain backwards compatibility of the database file format for all future releases of SQLite 3.
    
*   But they take backward compatibility so seriously that even if they have [shipped a bug](https://x.com/iavins/status/1851276312876326980), they won’t fix it
    
    ![Image 38](https://avi.im/blag/images/2024/sqlite-fact-10.png)
*   SQLite’s author D. Richard Hipp (DRH) did not find existing version control systems suitable. So he wrote his own called [Fossil](https://fossil-scm.org/home/doc/trunk/www/fossil-v-git.wiki). Fossil is powered by SQLite, of course.
    
    This reminds me of how Linus wrote Git.
    
    DRH also wrote his own parser generator called Lemon.
    
*   DRH wrote the B-Tree based on the algorithm in the book TAOCP by Donald Knuth, coding it on a plane while traveling (super based)
    
*   SQLite is pronounced as “Ess-Cue-El-ite”. There is no official guideline though. DRH mentioned in the [SQLite forums](https://web.archive.org/web/20201126110450/http://sqlite.1065341.n5.nabble.com/SQLite-Pronunciation-td88186.html#message88194):
    
    > I wrote SQLite, and I think it should be pronounced “S-Q-L-ite”. Like a mineral. But I’m cool with y’all pronouncing it any way you want.
    > 
    > :-)
    

That’s it for today! If I missed any, let me know. Happy holidays and Happy New Year! 🎄 ☃️

1\. Sources: [Most Deployed](https://www.sqlite.org/mostdeployed.html), [Public Domain and Contributions](https://www.sqlite.org/copyright.html), [Testing](https://www.sqlite.org/testing.html), [Paid support](https://www.sqlite.org/prosupport.html), [Faster than filesystem](https://www.sqlite.org/fasterthanfs.html), [SQLite History](https://corecursive.com/066-sqlite-with-richard-hipp/).  
2\. I posted this as thread on Twitter, where bunch of people provided more sources. Thanks to them: [1](https://x.com/nomsolence/status/1873416106922402060), [2](https://x.com/motherwell/status/1873678651616829949), [3](https://x.com/eriklangille/status/1873737893057122400), [4](https://old.reddit.com/r/programming/comments/1hpowxh/collection_of_insane_and_fun_facts_about_sqlite/m4ktv35/), [5](https://attractive.space/@Setok/113762362684067877).  
3\. After following the discussions on Reddit and HN, I have rephrased the license section (#6). Previously, it read: _SQLite is not open source in the legal sense, as “open source” has a specific definition and requires licenses approved by the Open Source Initiative (OSI)._

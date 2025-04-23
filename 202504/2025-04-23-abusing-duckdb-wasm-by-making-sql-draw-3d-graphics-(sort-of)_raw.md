Title: Patrick Trainer

URL Source: https://www.hey.earth/posts/duckdb-doom

Markdown Content:
Abusing DuckDB-WASM by making SQL draw 3D graphics (Sort Of)
------------------------------------------------------------

Building a SQL-Powered Doom Clone in the Browser[](https://www.hey.earth/posts/duckdb-doom#building-a-sql-powered-doom-clone-in-the-browser)
--------------------------------------------------------------------------------------------------------------------------------

I had this slightly crazy idea: Could I ditch most of the conventional JavaScript game loop and rendering logic and build a 3D game engine where **SQL queries** did the heavy lifting? Naturally, I decided to try building a primitive, text-based Doom clone to see how far I could push it using **DuckDB-WASM**.

![Image 1: A screenshot of the text-based Doom clone, showing the 3D view and minimap](https://www.hey.earth/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fduckdb-doom.5f9e25b8.png&w=1920&q=75)

Spoiler: It _kind of_ works, it was often painful, but I learned a ton about the surprising power (and quirks) of running an analytical database engine in the browser for tasks it was definitely not designed for.

The Setup: SQL Isn't Just for `SELECT *` Anymore[](https://www.hey.earth/posts/duckdb-doom#the-setup-sql-isnt-just-for-select--anymore)
--------------------------------------------------------------------------------------------------------------------------------

Forget managing game state in JavaScript objects or drawing pixels with Canvas/WebGL. My approach looked like this:

1.  **The Database is the World:** The 16x16 map, player coordinates (`x`, `y`, `dir`), enemy/bullet positions, game settings – everything lives in DuckDB tables, right there in the browser tab.
    
2.  **SQL Dictates Reality:**
    
    *   Want to move forward? `UPDATE player SET x = x + COS(dir)*step, y = y + SIN(dir)*step;`
    *   Bullet hits a wall? `DELETE FROM bullets WHERE EXISTS (SELECT 1 FROM map WHERE ...)`
    *   Enemy fragged? A `JOIN` between `bullets` and `enemies` followed by `DELETE` statements.
3.  **The Renderer is a SQL `VIEW`:** This is where it gets wild. I defined a SQL `VIEW` named `render_3d_frame` that actually performs raycasting and renders the 3D scene. This beast uses recursive CTEs to cast rays for each screen column, calculates wall distances (with fish-eye correction!), determines the height of the wall slice for that column, and then uses `string_agg` to stitch together the characters (`' '`, `.`, `█`, `▓`, `▒`, `░`) for each row of the final text frame.
    
    Here's the core of the raycasting algorithm in SQL:
    
    Yes, SQL is calculating perspective and drawing characters. DuckDB's recursive CTE capabilities are unexpectedly powerful for this kind of work.
    
4.  **JavaScript Glues It Together (and Handles Sprites):** My JS code became the orchestrator. It handles keyboard input, runs the `setInterval` game loop, calls the SQL view to get the background frame, _then_ fetches entity (bullet/enemy) positions and pre-calculated wall distances (from _another_ SQL view!). It performs a quick Z-buffer check in JS to see if a sprite is closer than the wall at its projected screen column, draws it onto the background frame if it is, and finally outputs the resulting text onto a `<pre>` tag.
    

Essentially, I took DuckDB-WASM – designed for fast analytics – and coerced it into acting like a state machine and a rudimentary rendering pipeline.

The Gauntlet: My Battles with Bugs, Binders, and Browsers[](https://www.hey.earth/posts/duckdb-doom#the-gauntlet-my-battles-with-bugs-binders-and-browsers)
--------------------------------------------------------------------------------------------------------------------------------

This wasn't exactly a smooth ride. Here's a log of some of the more... memorable... challenges and the fixes that eventually worked:

### 1\. The Initial Roadblock: DuckDB-WASM Just Wouldn't Load (404s)[](https://www.hey.earth/posts/duckdb-doom#1-the-initial-roadblock-duckdb-wasm-just-wouldnt-load-404s)

*   **Pain Point:** My first attempts using standard CDN links for the worker script just flat-out failed with `net::ERR_ABORTED 404`. Debugging WASM loading issues in the browser isn't always intuitive.
*   **The Fix:** Digging into the DuckDB-WASM docs revealed the more robust initialization pattern: using their helper functions (`getJsDelivrBundles`) or explicitly selecting a bundle (`mvp` for max compatibility), creating the worker via `URL.createObjectURL(new Blob(...))`, and using the `+esm` CDN endpoint for the main module import.

The lesson: When working with WASM libraries, always follow the recommended initialization patterns from the library authors.

### 2\. SQL Dialect Gotchas: `AUTOINCREMENT` vs. `SEQUENCE`[](https://www.hey.earth/posts/duckdb-doom#2-sql-dialect-gotchas-autoincrement-vs-sequence)

*   **Pain Point:** Muscle memory from SQLite/MySQL led me to use `AUTOINCREMENT` for the `bullets` table ID. DuckDB promptly slapped me with a `Parser Error: syntax error at or near "AUTOINCREMENT"`.
*   **The Fix:** Remembering that DuckDB adheres more closely to standard SQL sequences. This meant `CREATE SEQUENCE my_seq;` and then `CREATE TABLE ... (id INTEGER PRIMARY KEY DEFAULT nextval('my_seq'), ...)`.

This highlights an important point about DuckDB: it's not just SQLite in the browser. It has its own SQL dialect with nuances from PostgreSQL and standard SQL.

### 3\. Fighting the Query Planner (Binder Errors & Table Functions)[](https://www.hey.earth/posts/duckdb-doom#3-fighting-the-query-planner-binder-errors--table-functions)

*   **Pain Point:** This one drove me nuts for a while. I tried using `generate_series(0, settings.view_w - 1)` inside my rendering `VIEW`. The binder freaked out with errors like `Table function cannot contain subqueries` and even `Conversion Error: Could not convert string 's.view_w' to INT32`.
    
*   **The Fix:** I had to restructure the view logic significantly. Instead of generating the exact range needed, I generated a _fixed, oversized_ range (like 0-255) first, then added another CTE layer to _filter_ that oversized range using the actual `view_w` from the settings CTE.
    

I also initially forgot to alias the output of `generate_series`, leading to `Referenced column "value" not found` errors. Fixed with `generate_series(...) AS gs(col)`.

This approach satisfied the query planner, even though it's less elegant. It taught me that SQL query planners have strict rules about how and when references can be resolved, especially with table-generating functions.

### 4\. The Dreaded `async`/`setInterval` Race Condition[](https://www.hey.earth/posts/duckdb-doom#4-the-dreaded-asyncsetinterval-race-condition)

*   **Pain Point:** My game loop was simple: `setInterval(async () => { await tick(); await render(); }, 150)`. But because `tick()` and `render()` involved `async` database calls, sometimes a new interval would fire before the previous one finished. This was most obvious with the temporary `collisions` table used for bullet hits – I'd get rapid-fire "table `collisions` does not exist!" followed by "table `collisions` already exists!" errors.
    
*   **The Fix:** A classic solution: a simple boolean lock (`isProcessingTick`). The interval callback now checks this flag; if true, it bails immediately. If false, it sets the flag, runs the async work in a `try...finally`, and clears the flag in the `finally` block, ensuring it's always released.
    

This was a classic reminder that asynchronous timing with recurring events needs careful handling, especially when database operations are involved.

### 5\. Sprites: Beyond the SQL Background (Z-Buffer Logic)[](https://www.hey.earth/posts/duckdb-doom#5-sprites-beyond-the-sql-background-z-buffer-logic)

*   **Pain Point:** The SQL view rendered walls/floor/ceiling beautifully (well, beautifully for text mode). But enemies and bullets were just data. Drawing them required knowing _if they were hidden by a wall_.
    
*   **The Fix:** A hybrid approach combining SQL and JavaScript. I created _another_ SQL view (`column_distances`) specifically to output the distance to the nearest wall for each screen column:
    

Then, in my JavaScript `render3d` function, I performed the Z-buffer check by comparing entity depth to wall depth for each screen column.

Performance and Results[](https://www.hey.earth/posts/duckdb-doom#performance-and-results)
------------------------------------------------------------------------------------------

How did it actually run? Surprisingly well, considering what we're asking SQL to do. On a modern laptop, I get about 6-7 FPS with the 150ms game loop interval. The most expensive operation is the SQL raycasting view, which takes about 80-100ms to execute. The sprite rendering in JavaScript is quite fast in comparison.

![Image 2: A GIF showing gameplay with player movement and shooting](https://www.hey.earth/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fduckdb-doom.3aba91f6.gif&w=1920&q=75)

Here's what the game looks like in action. The main view shows the 3D perspective with text-based graphics, while the smaller box in the corner shows a top-down minimap. You can see how the walls are rendered with different characters based on distance, giving a primitive 3D effect.

The movement feels responsive enough, and the SQL-based collision detection works well. There's something strangely satisfying about mowing down enemies with SQL `DELETE` statements.

Pushing SQL to Its Limits: What I Learned[](https://www.hey.earth/posts/duckdb-doom#pushing-sql-to-its-limits-what-i-learned)
-----------------------------------------------------------------------------------------------------------------------------

This experiment taught me several important lessons about both SQL and browser-based development:

1.  **SQL is surprisingly powerful for non-traditional use cases.** It's not just for data retrieval. The combination of recursive CTEs, window functions, and aggregate functions makes complex algorithms possible.
    
2.  **DuckDB-WASM is impressively performant.** Running an analytical database engine in the browser that can handle complex recursive queries 6-7 times per second is no small feat.
    
3.  **The boundaries between languages can be blurred.** This project combined SQL for game state and rendering fundamentals, with JavaScript for orchestration and sprite handling. Neither could have done the job alone.
    
4.  **Debugging across language boundaries is challenging.** When something went wrong, it wasn't always clear if the issue was in the JavaScript, the SQL, or at the interface between them. I added extensive logging to track the flow between components.
    
5.  **Query planning is a complex art.** I had to work around many limitations of how SQL planners work, especially around table function evaluation and CTEs.
    

Would I Recommend This Approach?[](https://www.hey.earth/posts/duckdb-doom#would-i-recommend-this-approach)
-----------------------------------------------------------------------------------------------------------

For a production game? Absolutely not. It's a fun hack, but there are much better tools for game development.

But as a learning exercise? 100% yes. This project forced me to think deeply about:

*   SQL query optimization and execution planning
*   Raycasting algorithms and 3D projection
*   Asynchronous JavaScript patterns
*   The capabilities and limitations of WASM in the browser

Try It Yourself![](https://www.hey.earth/posts/duckdb-doom#try-it-yourself)
---------------------------------------------------------------------------

If you want to experiment with this SQL-powered monstrosity yourself, I've put the [full source code on GitHub (opens in a new tab)](https://github.com/patricktrainer/duckdb-doom). It's about 500 lines of code total, with roughly half being SQL and half JavaScript.

I'd love to see how far others can push this concept. Could you add textures? Implement a more complex game world? Add enemies that move and shoot back? The SQL rabbit hole goes deep!

What's Next?[](https://www.hey.earth/posts/duckdb-doom#whats-next)
------------------------------------------------------------------

This experiment has me wondering what other unconventional uses might exist for DuckDB-WASM in the browser. Physics simulations? Path finding algorithms? Full-text search engines?

Sometimes the most interesting projects come from using tools in ways they were never intended to be used. What weird DuckDB-WASM experiment would you like to see next?

not made by a 🤖

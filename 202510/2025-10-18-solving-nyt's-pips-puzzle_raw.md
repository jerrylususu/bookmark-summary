Title: Solving NYT's Pips Puzzle

URL Source: https://healeycodes.com/solving-nyt-pips-puzzle

Markdown Content:
Pips is The New York Times' daily puzzle where you have to place dominos onto a board within a set of region restrictions.

I wrote a solver for Pips by encoding the game logic and searching through a tree of legal game states until a complete board is found, along with optimizations to make it ~16× more efficient than a brute-force search.

I built a UI to help me debug my solver which you can see running below.

Puzzle:

Easy 16th Oct 2025

Nodes:

Nodes: 0

Loading puzzle...

I also built a visualization of the search tree. It shows the set of visited nodes. It's running in sync with the board above. This gave me an intuitive understanding of how the search algorithm and optimizations were behaving.

A quick reminder of the region restrictions so it's easier for you non-players to follow along:

*   Sum (all tiles must sum to `X`)
*   Equal (all tiles must be the same)
*   Not Equal (all tiles must not be the same)
*   Less/Greater (all tiles must sum to be less/greater than `X`)

Recursing the Tree
------------------

In order to solve a puzzle, I first needed to define the concept of a "puzzle" in code. So I created these types:

type Pip = 0 | 1 | 2 | 3 | 4 | 5 | 6;

type DominoType = `${Pip}|${Pip}`;

type DominoCounts = Record<DominoType, number>;

type Coord = [number, number];

type Region =

| { kind: 'sum', target: number, cells: Coord[] }

| { kind: 'equal', cells: Coord[] }

| { kind: 'nequal', cells: Coord[] }

| { kind: 'less', target: number, cells: Coord[] }

| { kind: 'greater', target: number, cells: Coord[] }

Which lets me define Easy/16/10/25 like so:

const Easy16thOct25: PuzzleDefinition = {

title: 'Easy 16th Oct 2025',

cells: [

[0, 0], [0, 1], [0, 2], [0, 3],

[1, 0],

[2, 0], [2, 1], [2, 2], [2, 3],

[3, 3],

[4, 0], [4, 1], [4, 2], [4, 3],

],

regions: [

{ kind: 'sum', target: 7, cells: [[0, 0], [1, 0]] },

{ kind: 'sum', target: 6, cells: [[0, 1], [0, 2]] },

{ kind: 'sum', target: 12, cells: [[2, 0], [2, 1]] },

{ kind: 'equal', cells: [[2, 2], [2, 3], [3, 3], [4, 3]] },

{ kind: 'less', target: 3, cells: [[4, 0]] },

],

dominos: {

'5|5': 1, '2|6': 1, '4|5': 1, '1|6': 1, '0|4': 1, '3|4': 1, '5|6': 1,

}

};

The core part of my solver is a Depth-First Search (DFS) which goes through all the legal pair placements. There are two important concepts here.

1.   We're picking the next _pair_ of cells, not the next single cell.
2.   Pips boards are not rectangles. They can be any grid shape.

My solver starts by building an adjacency list so that, later, when my solver loops over the free cells, it's easy to find its neighbors (where the other end of the domino can land).

// Generate adjacency list showing which cells are neighbors

// e.g.

// input cells: [ [ 0, 1 ], [ 0, 2 ], [ 1, 1 ], [ 1, 2 ] ]

// output neighbors: [ [ 1, 2 ], [ 3, 0 ], [ 3, 0 ], [ 2, 1 ] ]

// which describes the grid graph:

// (0,1) -- (0,2)

// | |

// (1,1) -- (1,2)

function buildCells(cells: Coord[]) {

const idByKey = new Map<string, number>();

cells.forEach(([r, c], i) => idByKey.set(cellKey(r, c), i));

const M = cells.length;

const neighbors: number[][] = Array.from({ length: M }, () => []);

for (let i = 0; i < M; i++) {

const [r, c] = cells[i];

// Check all 4 cardinal neighbors

for (const [rr, cc] of [[r, c + 1], [r + 1, c], [r, c - 1], [r - 1, c]]) {

const hit = idByKey.get(cellKey(rr, cc));

if (hit !== undefined) {

neighbors[i].push(hit);

}

}

}

return { M, neighbors };

}

My solver uses recursion to perform the DFS. It tries to place every domino at once until it hits an illegal board state, then backtracks to the nearest legal board state and continues.

I've commented out the less interesting sections to give you an overview.

async function solve(

cells: Coord[],

regions: Region[],

dominos: DominoCounts,

) {

// Adjacency list of neighbors from the above snippet

const { M, neighbors } = buildCells(cells);

// Pick all possible pairs of neighboring cells to place a domino on

function pickPairs(): [number, number][] {

let i = -1;

// Choose the first empty cell

for (let k = 0; k < M; k++) {

if (board[k] === null) {

i = k;

break;

}

}

// No more cells to place a domino on

// => we've solved the puzzle

if (i < 0) { return [] }

// Collect all empty neighbors

const pairs: [number, number][] = [];

for (let j of neighbors[i]) {

if (board[j] === null) {

pairs.push([i, j]);

}

}

return pairs;

}

// Place domino by mutating `board` and `remaining`

function place(i: number, a: Pip, j: number, b: Pip) { /* .. */}

// Unplace domino by mutating `board` and `remaining`

function unplace(i: number, a: Pip, j: number, b: Pip): void { /* .. */ }

// Checks regions are legal (and further checks when optimizations are enabled)

function checks(board: (Pip | null)[]): boolean { /* .. */ }

async function dfs(): Promise<boolean> {

const pairs = pickPairs();

if (pairs.length === 0) return false;

// Try each possible pair

for (const [i, j] of pairs) {

for (const t in remaining) if (remaining[t] > 0) {

const [a, b] = t.split('|').map(Number);

// Orientation 1

if (place(i, a, j, b)) {

// Check rules first to trim the search space

// then continue searching

if (checks(board) && await dfs()) return true;

unplace(i, a, j, b);

}

// Orientation 2

// (same as above with `a` and `b` swapped)

if (place(i, b, j, a)) {

if (checks(board) && await dfs()) return true;

unplace(i, b, j, a);

}

}

}

return false;

}

await dfs();

return { solution: solved, cells, nodes };

}

A branch of the search tree becomes dead when it fails the region check inside the `checks()` call. I loop each region and verify that the rule has not been broken e.g. if the sum of the cells is more than the sum constraint for that region.

for (const r of regions) {

// `vals` is the partial or complete list of this region's values

if (r.kind === 'sum') {

const sum = vals.reduce((a, b) => a + b, 0);

// Prune if partial sum already exceeds target

if (sum > r.target) return false;

// When region filled, sum must match exactly

if (vals.length === r.cells.length && sum !== r.target) return false;

}

// .. rest of region checks

}

Up to this point, I've described a brute-force method that searches every possible value. This method can be applied to other puzzle games where the number of legal board states can be checked within a reasonable amount of time.

When I run the solver against the Hard/16/20/25 puzzle, it checks 21337 nodes and takes 35 milliseconds (even with my unoptimized code which is rather wasteful indeed).

Once I had the solver up and running, I added a few optimizations to see how low I could get the node count for a range of Pips puzzles. FYI you can scrape Pips puzzles from the New York Times website if you check the network tab!

Optimizations
-------------

Let me show you the unoptimized solver taking on Hard/16/20/25. Watch it for a minute and see if you can think of any optimizations that would lower the number of nodes that the solver needs to visit.

Are there any checks we can perform to kill branches sooner?

Puzzle:

Hard 16th Oct 2025

Nodes:

Nodes: 0

Loading puzzle...

The first optimization I found was quite silly and simple and had a huge impact. If you recall the `solver()` function code from above, for each domino I check both orientations. For example, `5|6` can also be placed like `6|5`. However, I didn't have a check for when the sides of the domino are the same! So the solver would do a lot of duplicate work for dominos like `3|3`.

The fix was simple: check for matching sides before searching the branch for the flipped orientation.

// Orientation 2

if (!(flags?.SKIP_DUPLICATE_DOMINOES &&

// Check for matching sides

a === b)) {

// .. only then search the branch

}

This reduced the number of nodes required for Hard/16/20/25 from 21337 to 7618.

I found the next optimization after watching the solver for a while. I noticed that the solver would place a domino in a way that created an isolated cell (i.e. only room for a domino _half_) – and then keep going down the branch for a while! To a human, avoiding placements that create isolated cells is the most obvious thing in the world. So much so, that I forgot about implementing such a rule when I was writing the first version of the solver.

For example, below is a Pips board with a single-row in an unsolvable state due to the domino (`6|5`) that has isolated a cell on the left (the `_` are empty cells).

[ _, 6, 5, _, _, _,]

To implement this optimization, I added a new check into my `checks()` function to trim branches as soon as they had created an isolated cell.

function checkForIsolatedEmptyCells(): boolean {

for (let i = 0; i < M; i++) {

if (board[i] === null) {

// Check if this empty cell has any empty neighbors

const hasEmptyNeighbor = neighbors[i].some(j => board[j] === null);

if (!hasEmptyNeighbor) {

return true; // Found an isolated empty cell

}

}

}

return false;

}

Combined with skipping duplicate dominos, this optimization lowered the nodes required for Hard/16/20/25 from 7618 to 5777.

The final optimization I added made the region check more intelligent. Up to this point, my region check required the region to be in an illegal state. However, there are cases when we know _ahead_ of time that, even though a region isn't illegal yet, given the remaining dominos it is no longer possible to satisfy the region condition.

For example, if I've just played a `6` into an equals-region and I have no other spare dominos with a `6`, then I will never be able to complete that region, and I can trim the branch there and then.

I added a new check to my `checks()` function that asserts that, given what we know, and what we can work out without too much complexity, all the board's regions must be solvable in the future.

To keep the code snippet brief, I'll just show the equals and not-equals checks.

for (const region of regions) {

// Count how many empty cells remain in this region

const emptyCells = region.cells.length - placedVals.length;

if (emptyCells === 0) continue; // Region already filled

if (region.kind === 'equal') {

// Only check if at least one cell has been placed

if (placedVals.length > 0) {

const mustMatch = placedVals[0];

const availablePips = sparePips.filter(p => p === mustMatch);

// We must have enough matching domino parts

if (availablePips.length < emptyCells) return false;

}

} else if (region.kind === 'nequal') {

// Must have enough unique values that differ from placed values

const uniqueAvailable = new Set(sparePips

.filter(p => !placedVals.includes(p)));

if (uniqueAvailable.size < emptyCells) return false;

}

// .. rest of region types

}

Adding on this intelligent-regions-check reduced the nodes needed to solve Hard/16/20/25 from 5777 to 1355!

Here's the optimized solver running on the same Hard/16/20/25 puzzle as the start of this section, now checking almost 16× less nodes.

Puzzle:

Hard 16th Oct 2025

Nodes:

Nodes: 0

Loading puzzle...

I also tried some _move ordering_ ideas but wasn't able to get anything working that didn't regress most of the puzzles I was testing with.

Move ordering is a really great lever when you have a DFS/backtracking solver that's _correct but slow_. Changing the order that you search the tree doesn't alter the completeness, or correctness, it only changes the order that the tree is explored. The hope is that this nudges the solver to find the golden branch sooner rather than later.

It felt odd that I wasn't able to get move ordering working since I've been able to apply it in my [chess](https://healeycodes.com/building-my-own-chess-engine), [sokoban](https://healeycodes.com/building-and-solving-sokoban), and [queuedle solvers](https://healeycodes.com/solving-queuedle)! I must be missing something about tile-like puzzles like Pips.

I ran out of time to add further optimizations but my intuition is that I've only scratched the surface here. I also haven't spent any time making the solver code run faster (e.g. things like [bitboards](https://healeycodes.com/visualizing-chess-bitboards)).

UI
--

I've inlined two kinds of component in this post. The Pips board aims to be a faithful-ish clone of the Pips UI on the NYT website. It's more cramped (you could also say, badly designed) and sterile but I've grown to like it.

The Pips board uses React to render fixed sized divs with fixed sized regions that use absolute position and z-indexes to handle the layers. The tree-view I showed at the top draws lines onto a canvas with a little bit of angle math.

When I was wiring the solver up to the UI I ran into two problems.

The first problem was that the solver's internal board is made up of individual _cells_ not dominos. Even though the cells are placed and unplaced in pairs, as soon as they land on the board that relationship is lost. So when I first saw the rendered board, it was a bunch of separated dominos halves (squares). I had to go back and track the domino pair relationship.

The second problem was performance issues when drawing the canvas. My initial implementation did a complete re-draw of the canvas for every node. So obviously, this is extremely wasteful but it worked fine and I just wanted to ship it. To add some back-off, I pushed the new trees into a buffer and only rendered the latest one (dropping old data), I also used `requestAnimationFrame` / `cancelAnimationFrame` to drop frames. Hopefully this should stabilize the animation on your slow device but let me know otherwise!

All the code for the solver and the UI are embedded in this website and the relevant code file can be [found here](https://github.com/healeycodes/healeycodes.com/blob/main/components/visuals/pips/components.tsx).
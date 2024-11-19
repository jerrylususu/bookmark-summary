Title: download-esm: a tool for downloading ECMAScript modules

URL Source: https://simonwillison.net/2023/May/2/download-esm/

Markdown Content:
2nd May 2023

I’ve built a new CLI tool, [download-esm](https://github.com/simonw/download-esm), which takes the name of an [npm](https://www.npmjs.com/) package and will attempt to download the ECMAScript module version of that package, plus all of its dependencies, directly from the [jsDelivr](https://www.jsdelivr.com/) CDN—and then rewrite all of the import statements to point to those local copies.

#### Why I built this

I have somewhat unconventional tastes when it comes to JavaScript.

I really, really dislike having to use a local build script when I’m working with JavaScript code. I’ve tried plenty, and inevitably I find that six months later I return to the project and stuff doesn’t work any more—dependencies need updating, or my Node.js is out of date, or the build tool I’m using has gone out of fashion.

Julia Evans captured how I feel about this really clearly in [Writing Javascript without a build system](https://jvns.ca/blog/2023/02/16/writing-javascript-without-a-build-system/).

I just want to drop some `.js` files into a directory, load them into an HTML file and start writing code.

Working the way I want to work is becoming increasingly difficult over time. Many modern JavaScript packages assume you’ll be using `npm` and a set of build tools, and their documentation gets as far as `npm install package` and then moves on to more exciting things.

Some tools do offer a second option: a CDN link. This is great, and _almost_ what I want... but when I’m building software for other people ([Datasette plugins](https://datasette.io/plugins) for example) I like to include the JavaScript dependencies in my installable package, rather than depending on a CDN staying available at that URL forever more.

This is a key point: _I don’t want to depend on a fixed CDN_. If you’re happy using a CDN then `download-esm` is not a useful tool for you.

Usually, that CDN link is enough: I can download the `.js` file from the CDN, stash it in my own directory and get on with my project.

This is getting increasingly difficult now, thanks to the growing popularity of ECMAScript modules.

#### ECMAScript modules

I _love_ the general idea of ECMAScript modules, which have been supported by all of the major browsers for a few years now.

If you’re not familiar with them, they let you do things like this (example from the Observable Plot [getting started guide](https://observablehq.com/plot/getting-started)):

<div id\="myplot"\></div\>
<script type\="module"\>
import \* as Plot from "https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6/+esm";

const plot \= Plot.rectY(
    {length: 10000},
    Plot.binX(
        {y: "count"},
        {x: Math.random}
    )
).plot();
const div \= document.querySelector("#myplot");
div.append(plot);
</script\>

This is beautiful. You can import code on-demand, which makes lazy loading easier. Modules can themselves import other modules, and the browser will download them in parallel over HTTP/2 and cache them for future use.

There’s one big catch here: downloading these files from the CDN and storing them locally is surprisingly fiddly.

Observable Plot for example has 40 nested dependency modules. And downloading all 40 isn’t enough, because most of those modules include their own references that look like this:

export\*from"/npm/d3-array@3.2.3/+esm";
export\*from"/npm/d3-axis@3.0.0/+esm";

These references all need to be rewritten to point to the local copies of the modules.

#### Inspiration from Observable Plot

I opened an issue on the Observable Plot repository: [Getting started documentation request: Vanilla JS with no CDN](https://github.com/observablehq/plot/issues/1496).

An hour later Mike Bostock [committed a fix](https://github.com/observablehq/plot/commit/90a3876c037dc40e436ff4ad9c403f0681e4c203) linking to UMB bundles for `d3.js` and `plot3.js`—which is a good solution, but doesn’t let me import them as modules. But he also posted [this intriguing comment](https://github.com/observablehq/plot/issues/1496#issuecomment-1526116800):

> I think maybe the answer here is that someone should write a “downloader” tool that downloads the compiled ES modules from jsDelivr (or other CDN) and rewrites the import statements to use relative paths. Then you could just download this URL
> 
> [https://cdn.jsdelivr.net/npm/@observablehq/plot/+esm](https://cdn.jsdelivr.net/npm/@observablehq/plot/+esm)
> 
> and you’d get the direct dependencies
> 
> [https://cdn.jsdelivr.net/npm/d3@7.8.4/+esm](https://cdn.jsdelivr.net/npm/d3@7.8.4/+esm) [https://cdn.jsdelivr.net/npm/isoformat@0.2.1/+esm](https://cdn.jsdelivr.net/npm/isoformat@0.2.1/+esm) [https://cdn.jsdelivr.net/npm/interval-tree-1d@1.0.4/+esm](https://cdn.jsdelivr.net/npm/interval-tree-1d@1.0.4/+esm)
> 
> and the transitive dependencies and so on as separate files.

So I built that!

#### download-esm

The new tool I’ve built is called [download-esm](https://pypi.org/project/download-esm/). You can install it using `pip install download-esm`, or `pipx install download-esm`, or even `rye install download-esm` if that’s your [new installation tool of choice](https://til.simonwillison.net/python/rye).

Once installed, you can attempt to download the ECMAScript module version of any `npm` package—plus its dependencies—like this:

download-esm @observablehq/plot plot/

This will download the module versions of every file, rewrite their imports and save them in the `plot/` directory.

When I run the above I get the following from `ls plot/`:

binary-search-bounds-2-0-5.js
d3-7-8-4.js
d3-array-3-2-0.js
d3-array-3-2-1.js
d3-array-3-2-3.js
d3-axis-3-0-0.js
d3-brush-3-0-0.js
d3-chord-3-0-1.js
d3-color-3-1-0.js
d3-contour-4-0-2.js
d3-delaunay-6-0-4.js
d3-dispatch-3-0-1.js
d3-drag-3-0-0.js
d3-dsv-3-0-1.js
d3-ease-3-0-1.js
d3-fetch-3-0-1.js
d3-force-3-0-0.js
d3-format-3-1-0.js
d3-geo-3-1-0.js
d3-hierarchy-3-1-2.js
d3-interpolate-3-0-1.js
d3-path-3-1-0.js
d3-polygon-3-0-1.js
d3-quadtree-3-0-1.js
d3-random-3-0-1.js
d3-scale-4-0-2.js
d3-scale-chromatic-3-0-0.js
d3-selection-3-0-0.js
d3-shape-3-2-0.js
d3-time-3-1-0.js
d3-time-format-4-1-0.js
d3-timer-3-0-1.js
d3-transition-3-0-1.js
d3-zoom-3-0-0.js
delaunator-5-0-0.js
internmap-2-0-3.js
interval-tree-1d-1-0-4.js
isoformat-0-2-1.js
observablehq-plot-0-6-6.js
robust-predicates-3-0-1.js

Then to use Observable Plot you can put this in an `index.html` file in the same directory:

<div id\="myplot"\></div\>
<script type\="module"\>
import \* as Plot from "./observablehq-plot-0-6-6.js";
const plot \= Plot.rectY(
    {length: 10000}, Plot.binX({y: "count"}, {x: Math.random})
).plot();
const div \= document.querySelector("#myplot");
div.append(plot);
</script\>

Then run `python3 -m http.server` to start a server on port 8000 (ECMAScript modules don’t work directly from opening files), and open `http://localhost:8000/` in your browser.

![Image 1: localhost:8000 displaying a random bar chart generated using Observable Plot](https://static.simonwillison.net/static/2023/observable-plot-download-esm.jpg)

#### How it works

There’s honestly not a lot to this. It’s 100 lines of Python [in this file](https://github.com/simonw/download-esm/blob/0.1a0/download_esm/cli.py)—most of the work is done by some regular expressions, which were themselves mostly written by ChatGPT.

I shipped the first alpha release as soon as it could get Observable Plot working, because that was my initial reason for creating the project.

I have an [open issue](https://github.com/simonw/download-esm/issues/2) inviting people to help test it with other packages. That issue includes my own comments of stuff I’ve tried with it so far.

So far I’ve successfully used it for [preact](https://www.npmjs.com/package/preact) and [htm](https://www.npmjs.com/package/htm), for [codemirror](https://www.npmjs.com/package/codemirror) and partially for [monaco-editor](https://www.npmjs.com/package/monaco-editor)—though Monaco breaks when you attempt to enable syntax highlighting, as it attempts to dynamically load additional modules from the wrong place.

#### Your help needed

It seems very unlikely to me that no-one has solved this problem—I would be delighted if I could retire `download-esm` in favour of some other solution.

If this tool does turn out to fill a new niche, I’d love to make it more robust. I’m not a frequent JavaScript developer so I’m certain there are all sorts of edge-cases and capabilities I haven’t thought of.

[Contributions welcome](https://github.com/simonw/download-esm)!

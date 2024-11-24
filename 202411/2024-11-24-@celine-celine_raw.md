Title: @celine/celine

URL Source: https://maxbo.me/celine/

Markdown Content:
![Image 5: chiocciolina (Italian: small snail)](https://maxbo.me/celine/static/snail.webp)

@celine/celine is library for building reactive HTML notebooks with `display: block` `contenteditable` `<script>` elements. It wraps a subset of the [Observable Notebook](https://observablehq.com/documentation/notebooks/) [runtime](https://github.com/observablehq/runtime) to power inter-cell reactivity, just like [Observable Framework](https://observablehq.com/framework/reactivity) and [Quarto](https://quarto.org/docs/interactive/ojs/). It aims to make it easier to publish research as HTML files rather than as PDF files.

I initially considered calling this library _incel_, short for inline cell, but was advised against it.

[**Jump straight to the demo?**](https://maxbo.me/celine/#demo)

  

[](https://maxbo.me/celine/#toc)Table of Contents
-------------------------------------------------

[](https://maxbo.me/celine/#installation)Installation
-----------------------------------------------------

Add the following `<script>` element to your HTML file's `<head>` block:

Link [cell.css](https://maxbo.me/celine/#.echo) in your `<head>` block:

<link 
  rel="stylesheet" 
  href="https://esm.sh/jsr/@celine/celine@3.0.0/cell.css" /\>

You may want to include @celine/celine's [drop-in stylesheet](https://dohliam.github.io/dropin-minimal-css/), [libertine.css](https://maxbo.me/celine/#libertine.css):

<link 
  rel="stylesheet" 
  href="https://esm.sh/jsr/@celine/libertine@3.0.0/libertine.css" /\>

[](https://maxbo.me/celine/#demo)Demo: Observable Plot + SQLite
---------------------------------------------------------------

_Try removing a `0` from the `WHERE` condition, then click away from the `<script>` to blur and reevaluate._

[](https://maxbo.me/celine/#api)API
-----------------------------------

The following `<styles>`s are marked `contenteditable` and reevaluate on edit.

### [](https://maxbo.me/celine/#.echo)`.echo`

The `.echo` class can display `<script>` and `<style>` elements inline, using a [font with built-in syntax highlighting](https://blog.glyphdrawing.club/font-with-built-in-syntax-highlighting/).

### [](https://maxbo.me/celine/#.reflect)`.reflect`

The `.reflect` class forces `<script>` and `<style>` elements to display their opening and closing tags, `type`, `class`, `id`, and `contenteditable` attributes (a little trick from [This page is a truly naked, brutalist html quine](https://secretgeek.github.io/html_wysiwyg/html.html)).

All of the following `<script>`s are marked `contenteditable` and reevaluate on blur.

### [](https://maxbo.me/celine/#cell)`celine.cell(name, [inputs, ]definition)`

The `cell` constructor declares a reactive cell called `"${name}"`.

The `definition` can be `T` or `(...inputs) => T`, where `T` can be `object`, `Promise<?>`, `Iterator<?>`, or `AsyncIterator<?>`.

Cells render their current value above an element that has an `id` the same as the cell's `name`. Thus, to render the counter value above the `<script>`, we set `id="counter"` on the `<script>`:

The `cell` constructor accepts `inputs`, a list of other cell names to depend on.

Here we use [Hypertext Literal](https://observablehq.com/@observablehq/htl)'s `html` [template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals), to transform the value of another cell:

A `<script>` declaring a cell can be hidden inside a `<details>`s element.

Show codeTo display the cell's current value above the `<details>` element, rather than above the `<script>`, we add `id="hue"` to the `<details>` element, as the cell's `name` is `"hue"`:

### [](https://maxbo.me/celine/#viewof)`celine.viewof(name, [inputs, ]definition)`

The `viewof` constructor is a special constructor designed to work with [Observable Inputs](https://github.com/observablehq/inputs).

It declares 2 reactive cells: a cell called `"${name}"`, and a cell called `"viewof ${name}"` - one for the value, and one for the DOM element itself.

To display the DOM element above another element `<script>`, set `id="viewof ${name}"` on the element to which the input should be prepended.

Here, we want to display an input above the `<script>` element, so we set `id="viewof password"` on the `<script>`:

We still have to depend on the cell called `"password"` to use the input's value:

For further information on how to create custom inputs, see the [Synchronized Inputs](https://observablehq.com/@observablehq/synchronized-inputs) guide.

### [](https://maxbo.me/celine/#silent)`celine.silentCell(name, [inputs, ]definition)`

The `silentCell` constructor declares a cell that doesn't try to display its current value anywhere.

### [](https://maxbo.me/celine/#mutable)`celine.mutable(name, value)` / `celine.silentMutable(name, value)`

The `mutable` (and `silentMutable`) constructor declares a cell _and_ returns a reference that can be mutated. Mutations propagate to cells that depend upon it.

### [](https://maxbo.me/celine/#library)`celine.library` / Observable standard library

There are many useful utilities in the [Observable standard library](https://github.com/observablehq/stdlib). Inspect the contents of the `celine.library` object:

#### [](https://maxbo.me/celine/#tex)TeX

##### [](https://maxbo.me/celine/#celine_tex)`celine.tex`

Because rendering TeX is so useful, @celine/celine provides a shorthand [template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals), `celine.tex`:

Because cells render their contents `display: inline` (_celine ⇒ cell inline_), we can embed the script in the middle of the `<p>` element.

In non-demonstration use, we'd also leave off the `.echo` and `.reflect` classes, to render inline.

To render TeX centered, wrap the `<script>` with a `<div style="text-align: center">`:

Both `tex` template literals are unconfigurable. You will need to import the [KaTeX](https://katex.org/) library proper if you'd like to modify any of its [options](https://katex.org/docs/options).

#### [](https://maxbo.me/celine/#markdown)Markdown

##### [](https://maxbo.me/celine/#celine_md)`celine.md`

Markdown also has a shorthand [template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals), `celine.md`:

#### [](https://maxbo.me/celine/#graphviz)Graphviz

#### [](https://maxbo.me/celine/#mermaid)Mermaid

#### [](https://maxbo.me/celine/#leaflet)Leaflet

### [](https://maxbo.me/celine/#libertine.css)@celine/libertine/libertine.css

@celine/celine ships with a companion library @celine/libertine that provides a stylesheet based around the [Linux Libertine](https://en.wikipedia.org/wiki/Linux_Libertine) typeface (more specifically Libertinus Serif from the [Libertinus font family](https://github.com/alerque/libertinus) fork).

Linux Libertine is common in academic typesetting - it's the mandatory font for the [ACM LaTeX](https://www.acm.org/publications/proceedings-template) conference paper theme, the default for [Typst](https://typst.app/) and [Nota](https://nota-lang.org/) papers, and an alternate font for [LaTeX.css](https://latex.vercel.app/).

The [libertinus.css](https://maxbo.me/celine/fonts/Libertinus/documentation/libertinus.css) stylesheet provides authoritative documentation on the available font faces, variants, and [OpenType features](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/OpenType_fonts_guide), with [Opentype-Features.pdf](https://maxbo.me/celine/fonts/Libertinus/documentation/Opentype-Features.pdf) as a demo page.

`font-feature-settings: 'liga', 'tnum', 'zero' 'calt';` (ligatures, [tabular figures](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-numeric), slashed zero & contextual alternatives) are enabled by default.

> fi fl ffi ffl  
> 1234567890  
> Quest, (staff)  
> H2O, E = mc2

[libertinus.css](https://maxbo.me/celine/fonts/Libertinus/documentation/libertinus.css) makes a number of faces available:

> Libertinus Serif  
> Sphinx of black quartz, judge my vow.  
> _Sphinx of black quartz, judge my vow._  
> **Sphinx of black quartz, judge my vow.**  
> _**Sphinx of black quartz, judge my vow.**_  
> Small caps.  
> All small caps.  

> Libertinus Sans  
> Sphinx of black quartz, judge my vow.  
> _Sphinx of black quartz, judge my vow._  
> **Sphinx of black quartz, judge my vow.**  
> _**Sphinx of black quartz, judge my vow.**_  
> Small caps.  
> All small caps.  

> Libertinus Display  
> Sphinx of black quartz, judge my vow.  
> _Sphinx of black quartz, judge my vow._  
> **Sphinx of black quartz, judge my vow.**  
> _**Sphinx of black quartz, judge my vow.**_  

> Libertinus Mono  
> Sphinx of black quartz, judge my vow.  
> _Sphinx of black quartz, judge my vow._  
> **Sphinx of black quartz, judge my vow.**  
> _**Sphinx of black quartz, judge my vow.**_  

> Libertinus Initials  
> ABCDEFGHIJKLMNOPQRSTUVWXYZ  
> _ABCDEFGHIJKLMNOPQRSTUVWXYZ_  
> **ABCDEFGHIJKLMNOPQRSTUVWXYZ**  
> _**ABCDEFGHIJKLMNOPQRSTUVWXYZ**_  

> Libertinus Math  
> E = mc²  
> ∫ₐᵇ f(x) dx  
> ∑ₙ₌₁^∞ 1/n² = π²/6  
> ∇·E = ρ/ε₀  

> Libertinus KeyboardEsc F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 Del  
> \`1234567890-= Back  
> Tab QWERTYUIOP\[\]\\  
> Capslock ASDFGHJKL;' Enter  
> Shift ZXCVBNM,./ Shift  
> Ctrl Windows Alt Space Alt Fn ← ↑ ↓ →

[Small caps](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-caps) are available on Libertinus Serif and Libertinus Sans:

Small caps

All small caps

Small caps

All small caps

#### [](https://maxbo.me/celine/#classes)Classes

Jane Doe, University of Wollongong

John Smith, University of Townsville

This is an abstract.

##### [](https://maxbo.me/celine/#anchor)Anchor

[](https://maxbo.me/celine/#pairings)3rd-party library pairings
---------------------------------------------------------------

Some libraries that pair well with @celine/celine are:

### [](https://maxbo.me/celine/#pyodide)Pyodide

[Pyodide](https://pyodide.org/) is a port of CPython to WebAssembly.

### [](https://maxbo.me/celine/#webr)WebR

[WebR](https://docs.r-wasm.org/webr/latest/) is a version of the statistical language R compiled for the browser using WebAssembly, via Emscripten.

### [](https://maxbo.me/celine/#references-web-component)References Web Component

[References Web Component](https://lab.avl.la/references-webcomponent/), an experimental pair of Web Components for citing and referencing sources in a wiki-like manner.

Add the following `<script>` element to your HTML file's `<head>` block:

<script src="https://lab.avl.la/references-webcomponent/references-wc.js"\></script\>

> The Sun is hot.
> 
>   
> **References**

<p\>
  The Sun is hot.<cite-web url="https://www.nasa.gov/sun" author="Brian Dunbar" title="The Sun | NASA" publisher="National Aeronautics and Space Administration" date="2017-08-03" access-date="2021-08-30" data-refid="3" id="cite3"\></cite-web\>
</p\>

<h2\>References</h2\>
<references-list style="font-family: 'Libertinus Sans', sans-serif;"\>
</references-list\>

### [](https://maxbo.me/celine/#penrose)Penrose

[Penrose](https://penrose.cs.cmu.edu/), a system for creating beautiful diagrams just by typing notation in plain text.

Using the [Using Penrose with Vanilla JS](https://penrose.cs.cmu.edu/docs/ref/vanilla-js) instructions:

Show code[Bloom](https://penrose.cs.cmu.edu/docs/bloom/tutorial/getting_started) lets you build optimization-driven interactive diagrams in JavaScript.

_Try dragging the circles around!_

Show code

[](https://maxbo.me/celine/#changelogs)Changelogs
-------------------------------------------------

@celine/celine and @celine/libertine use [Semantic Versioning 2.0.0](https://semver.org/).

### [](https://maxbo.me/celine/#celine-changelog)celine/changelog.xml [![Image 6: RSS feed icon](https://maxbo.me/celine/static/rss.svg)](https://maxbo.me/celine/celine/changelog.xml)

_Showing 10 most recent entries._

| Version | Date | Changes |
| --- | --- | --- |

[](https://maxbo.me/celine/#resources)Resources
-----------------------------------------------

*   [Observable Runtime](https://github.com/observablehq/runtime)
*   [Observable Inputs](https://github.com/observablehq/inputs)
*   [Observable standard library](https://github.com/observablehq/stdlib)
*   [How Observable Runs](https://observablehq.com/@observablehq/how-observable-runs)
*   [Synchronized Inputs](https://observablehq.com/@observablehq/synchronized-inputs)
*   [Module require debugger](https://observablehq.com/@observablehq/module-require-debugger)
*   [Observable Plot](https://observablehq.com/plot/what-is-plot)
*   [Reactive HTML Notebooks](https://maxbo.me/a-html-file-is-all-you-need.html)

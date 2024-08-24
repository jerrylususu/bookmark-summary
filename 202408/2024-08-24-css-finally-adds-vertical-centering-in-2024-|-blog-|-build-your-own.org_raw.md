Title: CSS finally adds vertical centering in 2024 | Blog | build-your-own.org

URL Source: https://build-your-own.org/blog/20240813_css_vertical_center/

Published Time: 2024-08-13

Markdown Content:
`align-content` works in the default layout in 2024, allowing vertical centering with **1 CSS property**.

```
<div style="align-content: center; height: 100px;">
  <code>align-content</code> just works!
</div>
```

`align-content` just works!

[Supported since](https://caniuse.com/mdn-css_properties_align-content_block_context):  
![Image 1](blob:https://build-your-own.org/045ca559a42ab0dea89e5f31694a1a72) Chrome: 123 | ![Image 2](blob:https://build-your-own.org/6480133c5a31593a750485b690200641) Firefox: 125 | ![Image 3](blob:https://build-your-own.org/d041c70863402ec811575ffd05f5580f) Safari: 17.4

What’s new?
-----------

The status quo for CSS alignment is to switch to _flexbox_ or _grid_ because `align-content` doesn’t work in the default layout (_flow_). In 2024, browsers have [implemented](https://web.dev/blog/align-content-block) `align-content` for _flow layout_. This has some advantages:

*   You do not need flexbox or grid, just 1 CSS property for alignment.
*   Therefore, the content doesn’t need to be wrapped in a div.

```
<!-- Works -->
<div style="display: grid; align-content: center;">
  Content.
</div>
```

```
<!-- FAIL! -->
<div style="display: grid; align-content: center;">
  Content with <em>multiple</em> nodes.
</div>
```

```
<!-- Works with the content wrapper -->
<div style="display: grid; align-content: center;">
  <div>  <!-- The extra wrapper -->
    Content with <em>multiple</em> nodes.
  </div>
</div>
```

```
<!-- Works without the content wrapper -->
<div style="align-content: center;">
  Content with <em>multiple</em> nodes.
</div>
```

It’s amazing that CSS finally has a **single property** to control vertical align after decades of progress!

Vertical centering — a history
------------------------------

Browsers are funny, basic needs like aligning stuff do not have simple answers for a very long time. Here is how to center stuff in libreoffice:

![Image 4](https://build-your-own.org/blog/20240813_css_vertical_center/libreoffice_center.png)

Here is how to center _vertically_ in a browser (_horizontal_ centering is another topic):

### Method 1: table cell

Sanity: ★★★☆☆

There are 4 major layouts: flow (default), table, flexbox, grid. How to align stuff depends on the layout of the container. Flexbox and grid were added rather late, so table was the first option.

```
<div style="display: table;">
  <div style="display: table-cell; vertical-align: middle;">
    Content.
  </div>
</div>
```

A table can be summoned purely from CSS, but it’s a shame that such an indirection was needed.

### Method 2: absolute positioning

Sanity: ☆☆☆☆☆

For reasons I don’t understand. People kept inventing more indirect ways to do things.

```
<div style="position: relative;">
  <div style="position: absolute; top: 50%; transform: translateY(-50%);">
    Content.
  </div>
</div>
```

This one uses absolute positioning to bypass the layout, since the flow layout doesn’t help us:

0.  Mark the reference container with `position: relative`.
1.  Place the edge of the content at the center with `position: absolute; top: 50%`.
2.  Offset the content center to the edge with `transform: translateY(-50%)`.

### Method 3: inline content

Sanity: ☆☆☆☆☆

While the flow layout doesn’t help with content alignment. It allows vertical alignment _within_ a line. So why not make a line as tall as the container?

```
<div class="container">
  ::before
  <div class="content">Content.</div>
</div>
```

```
.container::before {
  content: '';
  height: 100%;
  display: inline-block;
  vertical-align: middle;
}
.content {
  display: inline-block;
  vertical-align: middle;
}
```

This has some flaws: besides sacrificing a pseudo-element, there’s a zero-width [“strut” character](https://christopheraue.net/design/vertical-align#:~:text=strut) at the beginning that can mess stuff up.

### Method 4: single-line flexbox

Sanity: ★★★☆☆

Flexbox became widely available 2 decades after the Web has taken off. It has 2 modes: single-line and multi-line. In single-line mode (default), the line fills the vertical space, and `align-items` aligns stuff inside the line.

```
<div style="display: flex; align-items: center;">
  <div>Content.</div>
</div>
```

Alternatively, make the line columnar and align items with `justify-content`.

```
<div style="display: flex; flex-flow: column; justify-content: center;">
  <div>Content.</div>
</div>
```

### Method 5: multi-line flexbox

Sanity: ★★★☆☆

In a multi-line flexbox, the line no longer fills the vertical space, so the line (with just 1 item in it) can be aligned with `align-content`.

```
<div style="display: flex; flex-flow: row wrap; align-content: center;">
  <div>Content.</div>
</div>
```

### Method 6: grid content

Sanity: ★★★★☆

Grid was even later. Alignment became simpler.

```
<div style="display: grid; align-content: center;">
  <div>Content.</div>
</div>
```

### Method 7: grid cell

Sanity: ★★★★☆

Note the subtle difference from the previous one:

*   `align-content` centers the _cell_ to the _container_.
*   `align-items` centers the _content_ to the _cell_ while the _cell_ stretches to fit the _container_.

```
<div style="display: grid; align-items: center;">
  <div>Content.</div>
</div>
```

There seems to be many ways to do the same thing.

### Method 8: auto-margin

Sanity: ★★★☆☆

In flow layout, `margin:auto` centers horizontally, but not vertically. Flexbox and grid do not share this absurdity.

```
<div style="display: grid;">
  <div style="margin-block: auto;">
    Content.
  </div>
</div>
```

Still, it puzzled me why margin was designed to also control alignment.

### Method 9: this post in 2024

Sanity: ★★★★★

Why didn’t browsers add this in the first place?

```
<div style="align-content: center;">
  <code>align-content</code> just works!
</div>
```

The table cell from the [Method 1](https://build-your-own.org/blog/20240813_css_vertical_center/#method-1-table-cell), like this method, also doesn’t require a content wrapper (it requires a table wrapper, though). We’re back to square one!

### Summary

All vertical centering methods in this [codepen](https://codepen.io/byo-books/pen/Porpmab?editors=1000). Know other methods? Feel free to [tell me](https://build-your-own.org/cdn-cgi/l/email-protection#29435a694b5c40454d0450465c5b04465e4707465b4e).

Going 2-dimensional
-------------------

Is there a **single property** for _horizontal_ align? What’s the counterpart of `align-content`? Let’s take a look at various alignment properties:

Table: alignment properties in different layouts    
|  | flow | flexbox | grid |
| --- | --- | --- | --- |
| `  align-content` | block axis | cross axis (line) | block axis (grid) |
| `justify-content` | no effect | main axis | inline axis (grid) |
| `  align-items` | no effect | cross axis (item) | block axis (cell) |
| `justify-items` | no effect | no effect | inline axis (cell) |

### Background: CSS axis terminology

The _block axis_ is usually _vertical_, and the _inline axis_ is _horizontal_. These terms are needed because [vertical `writing-mode`](https://build-your-own.org/visual_css/2p40_box_model.html#:~:text=Logical%20properties) is a thing, so **block axis and inline axis are relative to the text direction**. This is similar to how _main axis_ and _cross axis_ are relative to the flexbox item direction.

inline axis b l o c k a x i s block axis i n l i n e a x i s 1 3 2 main axis 4 c r o s s a x i s text direction (writing-mode) flexbox direction

### On naming things

From the names of properties we can infer how CSS is designed:

*   `align-*` is mostly vertical, while `justify-*` is mostly horizontal.
*   `*-content` and `*-items` control different levels of objects?

`justify-content` is the counterpart of `align-content`, which is handy in grid layout but has no effect in flow layout. The [`place-content` shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/place-content) sets both.

### “Align” vs. “justify”

Why do “align” and “justify” refer to axes in CSS? Is `justify-*` inspired by text justification? It’s chaotic, considering there’s also `text-align: justify`.

Usually when people say “align”, they mean the _placement_ of a single object, while “justify” means the _distribution_ of multiple objects.

While in CSS, both `justify-*` and `align-*` are like text justification, because they accept values like `space-between`; they just mean different axes!

**How to memorize**: Text justification is horizontal, so is `justify-*`.

### “Content” vs. “items”

In flexbox, “content” and “items” are confusing:

*   Main axis: `justify-content` controls items, while `justify-items` has no effect.
*   Cross axis: differences between single-line and multi-line modes.

flexbox justify-content justify-items grid ?**Conclusion**: “items” is for stuff that can be aligned _individually_. On the main axis, flex items cannot be aligned individually, so it’s “content”.

Why is CSS so confusing?
------------------------

Even if we ignore historical artifacts, CSS is still too confusing for most of us. It has hundreds of poorly named properties, each can influence the outcome in unintuitive ways.

### Software projects gone haywire

This is a case study in software design paradigms:

*   Unix: **orthogonal, composable primitives** that can be reasoned about independently.
*   CSS ([**C**entral **S**oftware **S**ystem](https://news.ycombinator.com/item?id=40130549)): just amend the software with **more and more knobs**.

The early WWW was just linked documents. CSS was created to _style_ documents without regard to _layout_. Over time, CSS gained some random layout features without a coherent vision.

Often you have many ways to do something in CSS, but not the right feature to do it sanely. This entire post is about a new feature for saner vertical align, and the horizontal axis is still different.

In contrast, libreoffice follows the paradigm of orthogonal, composable primitives:

*   Alignment is unified. No point that vertical is different from horizontal.
*   Unified alignment is possible because “align” and “justify” are orthogonal, not mixed up.
    *   “Align” is a property of the _container_.
    *   “Justify” is a property of the _paragraph_.
*   “Align” and “justify” can be combined in any way.

### CSS mastery takes effort!

Still, **rules can be learned**, even for something as incomprehensible as CSS. You just need to pay extra attention instead of relying on trial-and-error and copy-pasting. I’m creating a [visual guide](https://build-your-own.org/visual_css/) to the hard parts of CSS. Check it out!

[![Image 5: A Visual Guide To CSS](https://build-your-own.org/visual_css/img/book_css_cover_1800.png)](https://build-your-own.org/visual_css/)

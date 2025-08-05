Title: A Friendly Introduction to SVG • Josh W. Comeau

URL Source: https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/

Markdown Content:
Introduction
SVGs are one of the most exciting technologies we have access to in-browser. We can do _so many_ cool things with SVG. It’s an absolutely critical part of my toolkit.

Here’s a quick montage of things I’ve done with SVG:

But SVGs are also pretty intimidating. The rabbit hole goes deep, and it’s easy to get overwhelmed.

So, in this blog post, I want to share the most important fundamentals, to provide a solid foundation you can build on. I’ll show you _why_ SVGs are so cool, and share a few tricks you can start using right away. ✨

[Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#hello-svg-1)Hello SVG
----------------------------------------------------------------------------------------------------------

At its core, SVG (“Scalable Vector Graphics”) is an image format, like `.jpg` or `.gif`. We can pop them into an `<img>` tag, like any other image:

```
<img
  alt="return to homepage"
  src="/images/home.svg"
/>
```

**This works, but it’s not what makes SVGs so cool and interesting.** The _real_ magic happens when we use _inline SVGs._

Most image formats like `.jpg` are binary formats; if you tried to open them in a text editor, you’d see a bunch of gobbledygook. SVGs, by contrast, are specified using XML syntax, just like HTML! Instead of specifying the R/G/B color for each pixel, SVGs contain the set of drawing instructions required to render the illustration.

Somewhat magically, we can drop the raw SVG code right into an HTML document:

Code Playground

<div class="wrapper">
  <p>
    Check out this SVG:
  </p>

  <svg width="100" height="100">
    <circle
      fill="hotpink"
      r="30"
      cx="50"
      cy="50"
    />
  </svg>
</div>

In HTML, we’re given a set of primitives that are all document-related: paragraphs and headings and lists, the same primitives you get in Microsoft Word. SVG is the same sort of deal, but all of the primitives are for _illustrations_, things like `<circle>` and `<polygon>` and `<path>`.

**The really cool thing is that SVGs are first-class citizens in the DOM.** We can use CSS and JavaScript to select and modify SVG nodes, as if they were HTML elements.

Check this out:

Code Playground

<style>
  circle {
    fill: hotpink;
    transition: r 400ms, cy 600ms;
  }
  button:hover circle,
  button:focus-visible circle {
    r: 50px;
    cy: 100px;
  }
</style>

<button>
  <svg width="100" height="100">
    <circle
      r="30"
      cx="50"
      cy="50"
    />
  </svg>
</button>

Many SVG attributes, like the circle’s color (`fill`) and radius (`r`), moonlight as CSS properties. This means I can change them in CSS, and even use CSS transitions to animate them! 🤯

**This is what makes SVG so powerful.** It’s like an alternate-reality version of HTML that focuses on illustration instead of documentation, and we can use our existing CSS/JS skills to make them dynamic.

[Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#basic-shapes-2)Basic shapes
----------------------------------------------------------------------------------------------------------------

As we saw above, SVG contains its own set of UI primitives. Instead of `<div>` and `<button>`, we have shapes like `<circle>` and `<polygon>`. Let’s go through them.

### [Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#lines-3)Lines

Perhaps the most straightforward shape is `<line>`:

```
<svg width="280" height="280">
  <line
    x1="80"
    y1="80"
    x2="200"
    y2="200"
    stroke="oklch(0.9 0.3 164)"
    stroke-width="5"
  />
</svg>
```

x1: 80

y1: 80

x2: 200

y2: 200

It’s such a basic thing, but already, we’ve done something we can’t easily do in HTML. The only way to draw a diagonal line in HTML is to create a long thin DOM node and rotate it, which quickly turns into an advanced math problem if you need that line to start and end in specific places.

In SVG, lines are comparatively easy. We specify the start point (`x1` and `y1`) and the end point (`x2` and `y2`), and we get a straight line between those two points!

### [Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#rectangles-4)Rectangles

Rectangles are positioned using their top/left corner, specified using `x` and `y`. They grow from that size, using `width` and `height`:

```
<svg width="300" height="300">
  <rect
    x="60"
    y="100"
    width="180"
    height="100"
    fill="none"
    stroke="oklch(0.9 0.3 164)"
    stroke-width="5"
  />
</svg>
```

x: 60

y: 100

width: 180

height: 100

At first glance, this looks like a `<div>` with a `border`, but there are a few core differences.

First, the stroke is drawn on the _center_ of the path, not on the inside or the outside:

```
<svg width="300" height="300">
  <rect
    x="80"
    y="100"
    width="140"
    height="100"
    stroke-width="5"
    stroke="green"
    fill="none"
  />
</svg>
```

stroke-width: 5

This is true for all shapes, not just `<rect>`. And unfortunately, this isn’t configurable; we can’t specify that a specific shape should have its stroke drawn on the inside or the outside.

**Another interesting thing to note:** check out what happens when we reduce either the `width` or the `height` to 0. You might expect it to essentially become a straight line, but instead, the whole shape disappears:

In the SVG specifications, these sorts of shapes are known as “degenerates” (which feels pretty harsh to me!). When a two-dimensional shape like `<rect>` only stretches across one dimension, it’s considered invalid and doesn’t get rendered.A few years ago, the behaviour was inconsistent; some browsers would still paint degenerate shapes while others wouldn’t. Fortunately, all modern browsers follow the specification these days.

Finally, we can round the corners of our rectangle using the `rx` and `ry` properties, similar to `border-radius`:

```
<svg width="340" height="340">
  <rect
    x="80"
    y="100"
    width="500"
    height="500"
    rx="100"
    ry="50"
    stroke="green"
    stroke-width="5"
    fill="none"
  />
</svg>
```

rx(horizontal radius): 100

ry(vertical radius): 50

### [Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#circles-5)Circles

The size of a circle is dictated by its radius, `r`. We control the position of the circle by specifying a center point with `cx` and `cy`:

```
<svg width="280" height="280">
  <circle
    cx="140"
    cy="140"
    r="70"
    fill="none"
    stroke="oklch(0.9 0.3 164)"
    stroke-width="5"
  />
</svg>
```

cx(center x): 140

cy(center y): 140

r(radius): 70

Like with `<rect>`, circles will disappear entirely when their radius is set to 0.

### [Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#ellipses-6)Ellipses

An `<ellipse>` is just like a `<circle>`, except we can choose different values for its horizontal and vertical radius. This lets us create ovals:

```
<svg width="300" height="300">
  <ellipse
    cx="150"
    cy="150"
    rx="75"
    ry="50"
    fill="none"
    stroke="oklch(0.9 0.3 164)"
    stroke-width="5"
  />
</svg>
```

cx(center x): 150

cy(center y): 150

rx(horizontal radius): 75

ry(vertical radius): 50

### [Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#polygons-7)Polygons

The `<polygon>` element lets us create multi-sided shapes like this:

```
<svg width="300" height="300">
  <polygon
    points="
      60,100
      100,180
      140,140
      180,180
      220,100
    "
  />
</svg>
```

x(final point): 220

y(final point): 100

The `points` attribute takes a list of X/Y points; the browser will draw a line between each point, and from the final point back to the first.

**I found this a bit confusing when I was learning SVGs.** In my brain, the term “polygon” refers to something very specific: shapes that have rotational symmetry like triangles and squares and hexagons and octagons:

# of sides: 6

It turns out that these are “regular” polygons, or equilateral polygons. They’re a subset of a broader polygon world.

To create _regular_ polygons, we need to use trigonometry. It’s a bit beyond the scope of this blog post, but I’ll put the calculations in this playground if you’d like to learn more:

Code Playground

import { range } from 'lodash';
import './reset.css';
import './styles.css';

const svg = document.querySelector('.parent-svg');
const polygon = document.querySelector('.mister-polygon');

const numOfSides = 8;
const radius = 80;

function drawPolygon() {
  const svgWidth = Number(svg.getAttribute('width'));
  const svgHeight = Number(svg.getAttribute('height'));
  const cx = svgWidth / 2;
  const cy = svgHeight / 2;
  
  const points = range(numOfSides).map((index) => {
    
    
    
    
    const rotationOffset = numOfSides % 2 === 0
      ? Math.PI / numOfSides
      : 0;
    
    const angle =
      (index * 2 * Math.PI) / numOfSides -
      Math.PI / 2 +
      rotationOffset;
    
    const x = cx + radius * Math.cos(angle);
    const y = cy + radius * Math.sin(angle);
    return `${x},${y}`;
  });

  polygon.setAttribute(
    'points',
    points.join(' ')
  );
}

drawPolygon();

There are a couple more primitive shapes, like `<polyline>` and `<text>`, but I think we’ve covered enough for an intro blog post. Let’s move on.

[Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#scalable-svgs-8)Scalable SVGs
------------------------------------------------------------------------------------------------------------------

Up until now, we’ve been using “absolute” coordinates for things. This means that our SVGs _must_ be a very specific size, otherwise things break:

Width: 100%

```
<svg width="300" height="220">
  <circle
    cx="150"
    cy="110"
    r="60"
    stroke="var(--gold)"
    stroke-width="10"
  />
</svg>
```

In this demo, our circle is meant to sit in the center of a 300px-wide element. When the element is given a smaller width, however, the circle doesn’t shrink. It gets cropped.

This isn’t how most images work! When we render a `.jpg`, the photo will scale up and down with the element’s size.

One (not great) solution for this is to dynamically recalculate all of the values based on the width:

Width: 100%

```
<svg width="300" height="220">
  <circle
    cx="150"
    cy="110"
    r="60"
    stroke="var(--gold)"
    stroke-width="10"
  />
</svg>
```

I’m doing some math in JavaScript to calculate all of those geometry/presentational properties, based on the presumed “full size” width of 300px. So if the width is actually 150px, all of those values get multiplied by 0.5.

And it _works,_ but it’s a huge pain, even for a very simple illustration like this. Fortunately, there’s a much better way to solve this problem.

Check this out:

Width: 100%

```
<svg
  width="300"
  viewBox="0 0 300 220"
>
  <circle
    cx="150"
    cy="110"
    r="60"
    stroke="var(--gold)"
    stroke-width="10"
  />
</svg>
```

The `viewBox` attribute defines an _internal coordinate system_. When it’s provided, our `<circle>`s and `<rect>`s and `<polygon>`s will stop inheriting the raw pixel values of the DOM and instead use this internal coordinate system.

The `viewBox` attribute takes four numbers, but really, we can think of it as two pairs of two numbers.

The first two numbers allow us to change _which part_ of the SVG we’re viewing. **Touch and drag on top of the `<rect>` to see what I mean:Using your mouse/trackpad, click and drag on top of the `<rect>` to see what I mean:Using the X/Y sliders below, change the `viewBox`’s position to see what I mean:**

```
<svg
  width="300"
  height="300"
  viewBox="0 0 300 300"
>
  <rect
    x="0"
    y="0"
    width="200"
    height="200"
  />
</svg>
```

![Image 1](https://www.joshwcomeau.com/images/friendly-introduction-to-svgs/click-and-drag-outline.png)

X: 0

Y: 0

If you’re unable to use a pointer device, you can also use the sliders along the bottom for the same effect.If you’re unable to use a pointer device, you can also use the sliders along the bottom for the same effect.

The view _Box_ actually kinda works like the view _port_. This blog post, for example, is much taller than the browser window, so a portion of the lesson is shown in the viewport, and you can change which part you’re looking at by scrolling. It’s the same sort of idea with `viewBox`.

Let’s talk about the _second_ pair of values used for the `viewBox`. These two values allow us to specify the width and height of the viewable area.

Try using the new “ViewBox Size” slider to see what happens.**For this demo, try scrolling up/down while your cursor is over the `<rect>`.** Alternatively, you can use the “ViewBox Size” slider below:Try using the new “ViewBox Size” slider to see what happens.

```
<svg
  width="300"
  height="300"
  viewBox="-40 -40 300 300"
>
  <rect
    x="0"
    y="0"
    width="200"
    height="200"
  />
</svg>
```

ViewBox Size: 300

X: -40

Y: -40

The second pair of values that we pass to `viewBox` controls _how much_ of the infinite SVG field we’re actually looking at.

Now, it doesn’t change the size of our SVG — that’s controlled with the `width` / `height` attributes, or with CSS. Instead, it effectively changes the zoom level.

In the demo above, our SVG is 300px by 300px. If we set the `viewBox` to `"0 0 300 300"`, we’ll have a perfect 1:1 ratio between the internal coordinate system and standard DOM coordinate system (pixels).

But suppose we set the `viewBox` to `"0 0 150 150"`. The SVG is still 300px by 300px, but now it’s only displaying a 150×150 zone of our infinite SVG canvas. This effectively zooms in by 2x, doubling the size of the shapes inside our SVG.

Keeping with the viewport analogy (since they really are quite similar), this is equivalent to using the browser zoom function (Ctrl+) to zoom up to 200%. It doesn’t change the size of the browser window, but it scales everything up within the viewport to 2x its original size.

So, we’ve seen how the `viewBox` attribute can be used to slide the viewable area around (by changing the first two numbers), or to zoom in/out (by changing the last two numbers).

**To be honest with you, I’m not sure I’ve ever done either of these things.** The only realistic use case I can conceive of for shifting and zooming the viewBox is if you have a gigantic chart with lots of detail and you want to guide users through it by jumping from one section to another.

I showed you this stuff to help you understand how the `viewBox` works. _In practice,_ we usually keep the viewBox values static, so that our image always shows the exact same thing no matter what size we’re rendering our SVG at. This allows us to use the same SVG at different sizes in different contexts.

[Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#presentational-attributes-9)Presentational Attributes
------------------------------------------------------------------------------------------------------------------------------------------

In SVG, our shapes can either be filled in with the `fill` attribute, outlined with the `stroke` attribute, or both.

The `fill` attribute is pretty self-explanatory, so let’s focus on strokes. They’re _kinda_ like HTML borders, but _way_ more powerful.

**Try flipping between the different variants here to get a sense of what’s possible:**

Variant:

```
<style>
  circle {
    stroke: hsl(45deg 100% 50%);
    stroke-width: 6px;
    stroke-dasharray: 20, 14;
    stroke-linecap: butt;
  }
</style>

 

<svg viewBox="0 0 200 200">
  <circle cx="100" cy="100" r="50" />
</svg>
```

We control the presentation of the stroke using a handful of `stroke` CSS properties. We can also set them as inline attributes (so, instead of setting `stroke-width: 5px` in CSS, we could also set `stroke-width="5"` in the SVG itself).

Here’s a quick breakdown of what these properties do:

*   `stroke` — sets the color of the stroke. Defaults to `transparent`.

*   `stroke-width` — sets the width of the stroke, in pixels.

*   `stroke-dasharray` — sets the width of each segment and the gap between them. If we pass two values (eg. `10, 20`), we’re saying we want a 10px dash with 20px gap between them. We can even specify a _repeating dash pattern_ by specifying more than 2 values.

*   `stroke-linecap` — controls how each dash should be capped. If the dash is 0px thick, we’ll get little circles with `round`, little squares with `square`, or nothing at all with the default value, `butt`.

### [Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#animated-strokes-10)Animated strokes

So, because presentational SVG attributes like `stroke-width` are actually CSS properties, we can animate them like anything else in CSS!

In the demo above, for example, I’m smoothly interpolating between the different stroke styles using basic CSS transitions:

```
circle {
  transition:
    stroke 1200ms,
    stroke-width 900ms,
    stroke-dasharray 1500ms,
    stroke-linecap 1000ms;
}
```

How cool is that?!

There’s another stroke property that is _particularly_ useful for animations: `stroke-dashoffset`. This property allows us to slide the dashes around the shape:

```
<style>
  rect {
    stroke: oklch(0.9 0.25 164);
    stroke-width: 5;
    stroke-dasharray: 10, 10;
    stroke-dashoffset: 0;
  }
</style>
```

Dash Offset: 0

Dash Size: 10

Gap Size: 10

We can do _all sorts of stuff_ with this property. For example, we can have our dashes run around our shapes like little marathon runners:

```
@keyframes casinoLights {
  from {
    stroke-dashoffset: 0;
  }
  to {
    stroke-dashoffset: 26;
  }
}

rect {
  stroke-dasharray: 0, 26;
  animation:
    casinoLights 400ms linear infinite;
}
```

Animation Speed: 25

For a seamless effect, you’ll want to set `stroke-dashoffset` equal to the combined length of the dash + gap; otherwise, you’ll notice a flicker when the animation loops, as the dashes jump back to their original offset. You’ll also want to experiment with different gap sizes, to find a value that repeats nicely given the circumference of your shape.

Or, by animating the dash length and the offset, we can create this fancy spinner:

```
@keyframes grow {
  from {
    stroke-dasharray:
      calc(var(--circumference) * 0.05),
      var(--circumference);
  }
  to {
    stroke-dasharray:
      calc(var(--circumference) * 0.25),
      var(--circumference);
  }
}

 

@keyframes spin {
  from {
    stroke-dashoffset: 0;
  }
  to {
    stroke-dashoffset:
      calc(var(--circumference) * -0.95);
  }
}

 

circle {
  /*
    Calculate the circumference in JS, and
    apply it as a custom property:
  */
  --circumference: 572px;
  

  animation:
    grow 1200ms infinite alternate paused,
    spin 2400ms infinite alternate paused;
}
```

(Nothing is loading here! I’m demonstrating the spinner itself.)

Finally, maybe the most famous trick is to create the illusion of an SVG drawing itself:

```
<style>
  polygon {
    stroke-dasharray: 763, 10000;
    stroke-dashoffset: 763;
    transition:
      stroke-dashoffset 3000ms;
  }
</style>

 

<svg viewBox="0 0 280 320">
  <polygon points="..." />
</svg>
```

The clever trick here is that we have a single dash that is the same length as the entire circumference of our shape (763px, in this particular case), and a huge gap between each dash (1000px). We draw the shape by sliding this dash into place, by animating the `stroke-dashoffset`.

**How do we figure out the circumference of the shape?** We can use JavaScript to calculate it for us:

```
const element = document.querySelector('polygon');

// 👇 This is the magical method that calculates the circumference:
const pathLength = element.getTotalLength();

element.style.strokeDasharray = `${pathLength}, 1000`;
```

This is the ideal solution to this problem, since it gives us the precise length, but I’ve also solved this problem in the past with trial-and-error, guesstimating the length until it looked right.

[Link to this heading](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/#the-power-of-svgs-11)The power of SVGs
---------------------------------------------------------------------------------------------------------------------------

My goal with this blog post is to give you a high-level understanding of what SVGs are, and also share some cool tricks you can start using in your own work. **But there’s so much more that we can do with SVGs.** We’ve only scratched the surface here.

I’m currently working on a comprehensive course all about whimsical animation, and SVGs are a core part of that course. I’ve learned so much about animation in the almost-20-years I’ve been building for the web, and my goal in this course is to share all of my secrets with you! 😄

[![Image 2: Whimsical Animations](https://www.joshwcomeau.com/_next/image/?url=%2Fimages%2Fwhimsical-animations.jpg&w=1920&q=75)](https://whimsy.joshwcomeau.com/)

I’m planning on launching the course in “Early Access” in a couple of months. You can sign up for updates here:

*   [Whimsical Animations(opens in new tab)](https://whimsy.joshwcomeau.com/)

Folks on the waitlist will be the first to know when registration opens. ✨

### Last updated on

July 22nd, 2025
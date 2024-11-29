Title: A simple timeline using CSS flexbox

URL Source: https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/

Markdown Content:
Published: August 25, [2024](https://www.jonashietala.se/blog/2024)

Revised: September 24, 2024 in [0273191](https://github.com/treeman/jonashietala/commit/0273191fe98bef57c2294e1289b7f8c76aa9e288)

Tagged: [Blog](https://www.jonashietala.se/blog/tags/blog "Posts tagged `Blog`"), [CSS](https://www.jonashietala.se/blog/tags/css "Posts tagged `CSS`"), [Web Design](https://www.jonashietala.se/blog/tags/web_design "Posts tagged `Web Design`")

As I added a [/now](https://www.jonashietala.se/now) page to the site I also decided to refresh my [/about](https://www.jonashietala.se/about) page and I figured it would be neat to have timeline element where I could list some of the larger events in my life.

To my surprise it wasn’t too difficult to create one that looks pretty clean—the [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox) feature in CSS is really good. In this post I’ll walk you through how I made this kind of timeline:

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

[Markup](https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/#Markup)
-------------------------------------------------------------------------------------------------

I like to start with the markup before moving on to styling. I have two wrappers (`timeline` and `events`) around the different events (`event`) that contains the event marker (`svg`) and content with a `time` and `text`:

```
<div class="timeline">
<div class="events">
<!-- The first `1989` event -->
<div class="event life">
<!-- The circle is an svg -->
<svg
class="marker"
xmlns="http://www.w3.org/2000/svg"
width="12"
height="12"
>
<circle cx="6" cy="6" r="6"></circle>
</svg>
<!-- The event info -->
<div class="content">
<time>1989</time>
<div class="text">
<p>I was born in the north of Sweden</p>
</div>
</div>
</div>
<!-- etc ... -->
</div>
</div>
```

[A simple line](https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/#A-simple-line)
---------------------------------------------------------------------------------------------------------------

Let’s start with the actual line in the timeline. I chose to use the [::before](https://developer.mozilla.org/en-US/docs/Web/CSS/::before) pseudo-element on the `events` div to simulate a line by setting the width and height:

```
.events::before {
// We need some content for the element to show up.
content: "";
// Use absolute positioning to place the timeline at the very top.
position: absolute;
top: 0;
// With a height and with the timeline will be a tall and thin box.
height: 100%;
width: 1px;
```

We also need to set the wrapper `.events` to use relative positioning, otherwise the timeline will start from the top of the page, not the container:

```
.events {
position: relative;
}
```

I’ll also throw in a little bit of styling so it’s easier to see:

```
// For the tutorial I use slightly different colors,
// but you get the idea.
.events::before { background: white; }
// Events use different classes to differentiate them.
.event.life .marker { fill: yellow; }
.event.programming .marker { fill: magenta; }
.event.family .marker { fill: red; }
// Make the time stand out
.content time {
font-family: concourse_4, Helvetica, sans-serif;
font-weight: bold;
}
// Just some extra spacing to make the timeline not merge
// with the surrounding text.
.events { margin: 0.5em; }
```

And we have our line for our timeline:

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

[Alignment](https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/#Alignment)
-------------------------------------------------------------------------------------------------------

The circle and event aren’t aligned, let’s try to fix that.

By using flexbox the event will display its content horizontally (with the circle to the left and the content to the right):

```
.event {
display: flex;
}
```

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

Close, but the circle seems off. Remember that the circle is an svg 12 pixels wide and high and positioning will use `0,0` by default.

With relative positioning we can move the center of the circle to align it better:

```
.event .marker {
position: relative;
left: -6px;
top: 6px;
}
```

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

But if you look closely this still doesn’t look correct. Turns out that [centering things is the hardest problem in computer science](https://tonsky.me/blog/centering/), so don’t be discouraged.

To save you some grief, I found that `align-items: baseline` does a better job than nudging top positioning:

```
.event .marker {
position: relative;
left: -6px;
top: 0px;
}
.event {
align-items: baseline;
}
```

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

(The alignment looks good enough to me, at least with the default font I use.)

[Vertical spacing](https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/#Vertical-spacing)
---------------------------------------------------------------------------------------------------------------------

It feels a bit cramped so lets space things out. One way is to simply add a `margin-bottom: 1em;` but that would add a useless space below the last event (that we’d have to remove another way).

I think a cleaner way is to use [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox) and `row-gap` to only specify spacing between elements:

```
.timeline-5 {
  .events {
display: flex;
// Lay out events column-wise instead of row-wise.
flex-direction: column;
// Set some spacing between elements.
row-gap: 1em;
}
}
```

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

[Making it responsive](https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/#Making-it-responsive)
-----------------------------------------------------------------------------------------------------------------------------

What we’ve made is good for smaller screens but for larger screens I’d like to place the line in the middle and move some events to the left and some to the right.

I’ll use [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries) to create a cutoff:

```
@media (min-width: 700px) {
// Styling for wider screens goes here.
}
```

Even though I won’t include the media query in the following code snippets the media query should wrap them all.

### [Events to the left](https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/#Events-to-the-left)

The first thing I’d like to do is move the line to the middle:

```
.events::before {
// This centers the line horizontally.
// Remember that we used absolute positioning before.
left: 50%;
}
```

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

(Use a wider screen to see the effects of our changes.)

Now, let’s move the marker to the timeline. First lets move the marker to be after the content in the layout ordering:

```
.event .marker {
order: 1;
}
```

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

Secondly, we’ll make the content take up all the space to the left, pushing the marker on top of the line in the middle:

```
.event .content {
width: 50%;
}
```

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

Lets move right-align the content and add some padding so the text won’t overlap with the marker:

```
.event .content {
text-align: right;
padding-inline: 1em;
}
```

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

### [Events to the right](https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/#Events-to-the-right)

To move events to the right side of the timeline all we have to do is tell [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox) to lay out elements from right to left instead of left to right:

```
// Use `nth-child(even)` to target every other event.
.event:nth-child(even) {
// Layout elements from right to left.
flex-direction: row-reverse;
}
```

To make it look good lets add left aligned text and move the marker offset to be aligned over the line again:

```
.event:nth-child(even) {
  .content { text-align: left; }
// The marker used to be offset -6px, but now we
// move from the right.
  .marker { left: 6px; }
}
```

1989

I was born in the north of Sweden

2006

I got introduced to Visual Basic

August 2008

Got together with Veronica

[We’re done](https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/#Were-done)
--------------------------------------------------------------------------------------------------------

That’s all there is to the timeline I use. You can of course modify and expand on it in many ways but I quite like this simple styling.

With [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox) it was in the end fairly simple to get a basic timeline created and it’s one of my absolute favorite CSS features that manages to simplify many things that used to be very awkward.

* * *

Here’s the all the styling for the timeline we created in this post:

```
// The line in the middle.
.events::before {
content: "";
position: absolute;
top: 0;
height: 100%;
width: 1px;
background: var(--color-hr);
}
.events {
// Needed for positioning the line.
position: relative;
// Add some space.
display: flex;
margin-block: 0.5em;
flex-direction: column;
row-gap: 1em;
}
.event {
// Layout content and marker using flexbox.
display: flex;
// Align marker vertically.
align-items: baseline;
}
.event .marker {
// Adjust marker to center on the line.
position: relative;
left: -6px;
}
// Some coloring to make our life easier.
.event.life .marker {
fill: var(--melange_b_yellow);
}
.event.programming .marker {
fill: var(--melange_b_magenta);
}
.event.family .marker {
fill: var(--melange_b_red);
}
.content time {
font-family: concourse_4, Helvetica, sans-serif;
font-weight: bold;
}
@media (min-width: 700px) {
// Place the line in the middle.
  .events::before {
left: 50%;
}
// Layout the marker after the content.
  .event .marker {
order: 1;
}
  .event .content {
// Make the content take 50% space so the marker
// will be placed at 50% (on top of the line).
width: 50%;
// Event is to the left, align text towards the line.
text-align: right;
// Avoid overlap with the marker.
padding-inline: 1em;
}
// For these types, move the event to the right.
  .event:is(.programming, .work, .projects) {
// Layout the content and marker from right to left.
flex-direction: row-reverse;
// Now align text to the left.
    .content {
text-align: left;
}
// We used to offset the marker from the left with -6px,
// now we need to do it from the other side.
    .marker {
left: 6px;
}
}
}
```

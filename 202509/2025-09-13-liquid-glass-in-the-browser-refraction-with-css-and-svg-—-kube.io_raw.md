Title: Liquid Glass in the Browser: Refraction with CSS and SVG

URL Source: https://kube.io/blog/liquid-glass-css-svg

Published Time: 2025-10-04

Markdown Content:
[#](https://kube.io/blog/liquid-glass-css-svg#introduction)Introduction
-----------------------------------------------------------------------

Apple [introduced the Liquid Glass effect during WWDC 2025](https://www.youtube.com/watch?v=jGztGfRujSE) in June—a stunning UI effect that makes interface elements appear to be made of curved, refractive glass. This article is a hands‑on exploration of how to recreate a similar effect on the web using CSS, SVG displacement maps, and physics-based refraction calculations.

Instead of chasing pixel‑perfect parity, we’ll approximate Liquid Glass, recreating the core refraction and a specular highlight, as a focused proof‑of‑concept you can extend.

We'll build up the effect from first principles, starting with how light bends when passing through different materials.

Chrome‑only demo

The interactive demo at the end currently works in Chrome only (due to SVG filters as backdrop‑filter).

You can still read the article and interact with the inline simulations in other browsers.

[#](https://kube.io/blog/liquid-glass-css-svg#understanding-refraction)Understanding Refraction
-----------------------------------------------------------------------------------------------

**Refraction** is what happens when light changes direction as it passes from one material to another (like from air into glass). This bending occurs because light travels at different speeds through different materials.

The relationship between the incoming and outgoing light angles is described by [**Snell–Descartes law**](https://en.wikipedia.org/wiki/Snell%27s_law):

n 1 sin⁡(θ 1)=n 2 sin⁡(θ 2)n_1 \sin(\theta_1) = n_2 \sin(\theta_2)

n 1=refractive index of first medium n_1 = \text{refractive index of first medium}

θ 1=angle of incidence\theta_1 = \text{angle of incidence}

n 2=refractive index of second medium n_2 = \text{refractive index of second medium}

θ 2=angle of refraction\theta_2 = \text{angle of refraction}

First Medium

n 1

= 1

Second Medium

n 2

=

1.5

Normal

0.01 3

n 2 1.5

In the above interactive diagram, you can see that:

*   When n 2=n 1 n_2 = n_1, the light ray passes straight through without bending.

*   When n 2>n 1 n_2 > n_1, the ray bends toward the normal (the imaginary line perpendicular to the surface).

*   When n 2<n 1 n_2 < n_1, the ray bends away from the normal, and depending on the angle of incidence, it may bend so much that it reflects back into the original medium instead of passing through.

This is called [Total Internal Reflection](https://en.wikipedia.org/wiki/Total_internal_reflection)

*   When incident ray is orthogonal to the surface, it passes straight through regardless of refractive indices.

[#](https://kube.io/blog/liquid-glass-css-svg#limitations-in-this-project)Limitations in this project
-----------------------------------------------------------------------------------------------------

To keep things focused we avoid complex branches of behavior by constraining the scenario:

*   Ambient medium has i n d e x=1 index = 1 (air).

*   Use materials with i n d e x>1 index > 1, and prefer 1.5 1.5 (glass).

*   Only one refraction event (ignore any later exit / second refraction).

*   Incident rays are always orthogonal to the background plane (no perspective).

*   Objects are 2D shapes parallel to the background (no perspective).

*   No gap between objects and background plane (only one refraction).

*   Circle shapes only in this article:

Extending to other shapes requires preliminary calculations.

Circles let us form rounded rectangles by stretching the middle.

Under these assumptions every ray we manipulate has a well-defined refracted direction via Snell's Law, and we simplify a lot our calculations.

[#](https://kube.io/blog/liquid-glass-css-svg#creating-the-glass-surface)Creating the Glass Surface
---------------------------------------------------------------------------------------------------

To create our glass effect, we need to define the shape of our virtual glass surface. Think of this like describing the cross-section of a lens or curved glass panel.

[#](https://kube.io/blog/liquid-glass-css-svg#surface-function)Surface Function
-------------------------------------------------------------------------------

Our glass surface is described by a mathematical function that defines how thick the glass is at any point from its edge to the end of the bezel. This **surface function** takes a value between 0 0 (at the outer edge) and 1 1 (end of bezel, start of flat surface) and returns the height of the glass at that point.

`const height = f(distanceFromSide);`
From the height we can calculate the angle of incidence, which is the angle between the incoming ray and the normal to the surface at that point. The normal is simply the derivative of the height function at that point, rotated by −90-90 degrees:

```
const delta = 0.001; // Small value to approximate derivative
const y1 = f(distanceFromSide - delta);
const y2 = f(distanceFromSide + delta);
const derivative = (y2 - y1) / (2 * delta);
const normal = { x: -derivative, y: 1 }; // Derivative, rotated by -90 degrees
```

[#](https://kube.io/blog/liquid-glass-css-svg#equations)Equations
-----------------------------------------------------------------

For this article, we will use four different height functions to demonstrate the effect of the surface shape on the refraction:

Convex Circle

y=1−(1−x)2 y = \sqrt{1 - (1 - x) ^ 2}

Simple circular arc → a spherical dome. Easier than the squircle, but the transition to the flat interior is harsher, producing sharper refraction edges—more noticeable when the shape is stretched away from a true circle.

Convex Squircle

y=1−(1−x)4 4 y = \sqrt[4]{1 - (1 - x) ^ 4}

Uses the [Squircle](https://en.wikipedia.org/wiki/Squircle) Apple favors: a softer flat→curve transition that keeps refraction gradients smooth even when stretched into rectangles—no harsh interior edges. It also makes the bezel appear optically thinner than its physical size because the flatter outer zones bend light less.

Concave

y=1−Convex(x)y = 1 - \text{Convex}(x)

The concave surface is the complement of the convex function, creating a bowl-like depression. This surface causes light rays to diverge outward, displacing them beyond the glass boundaries.

Lip

y=mix(Convex(x),Concave(x),Smootherstep(x))y = \text{mix}(\text{Convex}(x), \text{Concave}(x), \text{Smootherstep}(x))

Blends convex and concave via [Smootherstep](https://en.wikipedia.org/wiki/Smoothstep): raised rim, shallow center dip.

We could make the surface function more complex by adding more parameters, but these four already give a good idea of how the surface shape affects the refraction.

[#](https://kube.io/blog/liquid-glass-css-svg#simulation)Simulation
-------------------------------------------------------------------

Now let's see these surface functions in action through interactive ray tracing simulations. The following visualization demonstrates how light rays behave differently as they pass through each surface type, helping us understand the practical implications of our mathematical choices.

From the simulation, we can see that concave surfaces push rays outside the glass; convex surfaces keep them inside.

We want to avoid outside displacement because it requires sampling background beyond the object. Apple’s Liquid Glass appears to favor convex profiles (except for the Switch component, covered later).

The background arrow indicates displacement—how far a ray lands compared to where it would have landed without glass. Color encodes magnitude (longer → more purple).

Take a look at symmetry: rays at the same distance from the border share the same displacement magnitude on each side. Compute once, reuse around the bezel/object.

[#](https://kube.io/blog/liquid-glass-css-svg#displacement-vector-field)Displacement Vector Field
-------------------------------------------------------------------------------------------------

Now that calculated the displacement at a distance from border, let's calculate the displacement vector field for the entire glass surface.

The vector field describes at every position on the glass surface how much the light ray is displaced from its original position, and in which direction. In a circle, this displacement is always orthogonal to the border.

[#](https://kube.io/blog/liquid-glass-css-svg#pre-calculating-the-displacement-magnitude)Pre-calculating the displacement magnitude
-----------------------------------------------------------------------------------------------------------------------------------

Because we saw that this displacement magnitude is symmetric around the bezel, we can pre-calculate it for a range of distances from the border, on a single radius.

This allows us to calculate everything in two dimensions once (x and z axis), on one "half-slice" of the object, and we will the rotate these pre-calculated displacements around the z-axis.

The actual number of samples we need to do on a radius is of 127 ray simulations, and is determined by the constraints of the SVG Displacement Map resolution. (See next section.)

[#](https://kube.io/blog/liquid-glass-css-svg#normalizing-vectors)Normalizing vectors
-------------------------------------------------------------------------------------

In the above diagram, the arrows are all scaled down for visibility, so they do not overlap. This is normalization, and is also useful from a technical standpoint.

To use these vectors in a displacement map, we need to normalize them. Normalization means scaling the vectors so that their maximum magnitude is 1 1, which allows us to represent them in a fixed range.

So we calculate the maximum displacement magnitude in our pre-calculated array:

`const maximumDisplacement = Math.max(...displacementMagnitudes);`
And we divide each vector's magnitude by this maximum:

```
displacementVector_normalized = {
  angle: normalAtBorder,
  magnitude: magnitude / maximumDisplacement,
};
```

We store `maximumDisplacement` as we will need it to re-scale the displacement map back to the actual magnitudes.

[#](https://kube.io/blog/liquid-glass-css-svg#svg-displacement-map)SVG Displacement Map
---------------------------------------------------------------------------------------

Now we need to translate our mathematical refraction calculations into something the browser can actually render. We'll use [**SVG displacement maps**](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDisplacementMap).

A displacement map is simply an image where each pixel's color tells the browser how far it should find the actual pixel value from its current position.

SVG's `<feDisplacementMap />` encodes these pixels in a 32 bit RGBA image, where each channel represents a different axis of displacement.

It's up to the user to define which channel corresponds to which axis, but it is important to understand the constraint: Because each channel is 8 bits, the displacement is limited to a range of -128 to 127 pixels in each direction. (256 values possible in total). 128 is the neutral value, meaning no displacement.

SVG filters can only use images as displacement maps, so we need to convert our displacement vector field into an image format.

```
<svg colorInterpolationFilters="sRGB">
  <filter id={id}>
    <feImage
      href={displacementMapDataUrl}
      x={0}
      y={0}
      width={width}
      height={height}
      result="displacement_map"
    />
    <feDisplacementMap
      in="SourceGraphic"
      in2="displacement_map"
      scale={scale}
      xChannelSelector="R" // Red Channel for displacement in X axis
      yChannelSelector="G" // Green Channel for displacement in Y axis
    />
  </filter>
</svg>
```

`<feDisplacementMap />` uses the red channel for the X axis and the green channel for the Y axis. The blue and alpha channels are ignored.

[#](https://kube.io/blog/liquid-glass-css-svg#scale)Scale
---------------------------------------------------------

The Red (X) and Green (Y) channels are 8‑bit values (0–255). Interpreted without any extra scaling, they map linearly to a normalized displacement in [−1, 1], with 128 as the neutral value (no displacement):

0↦−1 128↦0 255↦1\begin{aligned} 0 &\mapsto -1 \\ 128 &\mapsto 0 \\ 255 &\mapsto 1 \end{aligned}

The `scale` attribute of `<feDisplacementMap />` multiplies this normalized amount:

0↦−s c a l e 128↦0 255↦s c a l e\begin{aligned} 0 &\mapsto -scale \\ 128 &\mapsto 0 \\ 255 &\mapsto scale \end{aligned}

Because our vectors are normalized using the maximum possible displacement (in pixels) as the unit, we can reuse that maximum directly as the filter’s `scale`:

```
<feDisplacementMap
  in="SourceGraphic"
  in2="displacement_map"
  scale={maximumDisplacement} // max displacement (px) → real pixel shift
  xChannelSelector="R"
  yChannelSelector="G"
/>
```

You can also animate `scale` to fade the effect in/out—no need to recompute the map (useful for artistic control even if not physically exact).

[#](https://kube.io/blog/liquid-glass-css-svg#vector-to-red-green-values)Vector to Red-Green values
---------------------------------------------------------------------------------------------------

To convert our displacement vector field into a displacement map, we need to convert each vector into a color value. The red channel will represent the X component of the vector, and the green channel will represent the Y component.

We currently have polar coordinates (angle and magnitude) for each vector, so we need to convert them to Cartesian coordinates (X and Y) before mapping them to the red and green channels.

```
const x = Math.cos(angle) * magnitude;
const y = Math.sin(angle) * magnitude;
```

Because we normalised our vectors already, `magnitude` here is between 0 and 1.

From here, we just remap the values to the range of 0 to 255 for the red and green channels:

Red: 218

X axis: 0.71

Green: 218

Y axis: 0.71

Result (Blended)

```
const result = {
  r: 128 + x * 127, // Red channel is the X component, remapped to 0-255
  g: 128 + y * 127, // Green channel is the Y component, remapped to 0-255
  b: 128, // Blue channel is ignored
  a: 255, // Alpha channel is fully opaque
};
```

After converting every vector in the map to color value, we get an image that can be used as a displacement map in the SVG filter.

[#](https://kube.io/blog/liquid-glass-css-svg#playground)Playground
-------------------------------------------------------------------

This playground applies the SVG displacement filter to a simple scene and lets you tweak surface shape, bezel width, glass thickness, and effect scale. Watch how these inputs change the refraction field, the generated displacement map, and the final rendering.

#### Displacement Map

#### Preview

[#](https://kube.io/blog/liquid-glass-css-svg#specular-highlight)Specular Highlight
-----------------------------------------------------------------------------------

The final piece of our Liquid Glass effect is the **specular highlight**—those bright, shiny edges you see on real glass objects when light hits them at certain angles.

The way Apple implements it seems to be a simple rim light effect, where the highlight appears around the edges of the glass object, and its intensity varies based on the angle of the surface normal relative to a fixed light direction.

Specular Angle:-60°

-180°0°180°

[#](https://kube.io/blog/liquid-glass-css-svg#combining-refraction-and-specular-highlight)Combining Refraction and Specular Highlight
-------------------------------------------------------------------------------------------------------------------------------------

In the final SVG filter, we combine both the displacement map for refraction and the specular highlight effect.

Both are loaded as separate `<feImage />` elements, and then combined using `<feBlend />` to overlay the highlight on top of the refracted image.

But this part is actually the most "creative" part of the effect, and it's just by tweaking the number of filters, and their parameters, that you can get a variety of different looks.

[#](https://kube.io/blog/liquid-glass-css-svg#svg-filter-as-backdrop-filter)SVG Filter as `backdrop-filter`
-----------------------------------------------------------------------------------------------------------

This is the part where cross-browser compatibility ends. Only Chrome currently supports using SVG filters as `backdrop-filter`, which is essential for applying the Liquid Glass effect to UI components:

```
.glass-panel {
  backdrop-filter: url(#liquidGlassFilterId);
}
```

> Note: The backdrop-filter dimensions does not adjust automatically to the element size, so you need to ensure that your filter images fit the size of your elements.

Now that we have all the pieces in place, we can create components that use this effect.

[#](https://kube.io/blog/liquid-glass-css-svg#bringing-it-all-together-real-ui-components)Bringing It All Together: Real UI Components
--------------------------------------------------------------------------------------------------------------------------------------

With our refraction math and displacement maps working, let's see how this translates to actual UI components you might use in an application.

Chrome‑specific demo

Chrome allows using SVG filters as `backdrop-filter`, which isn’t part of the CSS spec.

Above, we used regular `filter` so it’s viewable in Safari/Firefox.

The next components use `backdrop-filter`, so they’re Chrome‑only.

The goal won't be to create real components for production, but just to get a taste of how the effect looks in different UI elements.

[#](https://kube.io/blog/liquid-glass-css-svg#magnifying-glass)Magnifying Glass
-------------------------------------------------------------------------------

This component actually uses two displacement maps: one for the refraction on the sides, and one for the zooming, which has a stronger refraction effect.

It also plays with shadows and scaling to create a more dynamic, interactive effect.

Optics Study

Drag the capsule to bend the page. This lens is a compact SVG displacement rig that refracts whatever sits beneath it.

The field comes from a rounded bezel profile; pixels are pushed along its gradient, then topped with a subtle specular bloom for depth.

Sweep across strong edges—high contrast makes the bend snap.

![Image 1: Abstract architectural lines](https://images.unsplash.com/photo-1579380656108-f98e4df8ea62?q=80&w=800&auto=format&fit=crop)

Parameters

Specular Opacity 0.50

Specular Saturation 9

Refraction Level 1.00

[#](https://kube.io/blog/liquid-glass-css-svg#searchbox)Searchbox
-----------------------------------------------------------------

Use image background

Parameters

Specular Opacity 0.20

Specular Saturation 4

Refraction Level 0.70

Blur Level 1.0

[#](https://kube.io/blog/liquid-glass-css-svg#switch)Switch
-----------------------------------------------------------

This uses a lip bezel, which makes the surface convex on the outside and concave in the middle. This makes the center slider zoomed out, while the edges refract the inside.

Force active

Parameters

Specular Opacity 0.50

Specular Saturation 6

Refraction Level 1.00

Blur Level 0.2

[#](https://kube.io/blog/liquid-glass-css-svg#slider)Slider
-----------------------------------------------------------

Slider allows you to see the current level through the glass, while the sides refract the background. It uses a convex bezel.

Force active

Parameters

Specular Opacity 0.40

Specular Saturation 7

Refraction Level 1.00

Blur Level 0.0

[#](https://kube.io/blog/liquid-glass-css-svg#music-player)Music Player
-----------------------------------------------------------------------

This fake music player UI tries to mimic the look of Apple Music’s Liquid Glass panels, using a convex bezel and a subtle specular highlight.

It relies on the iTunes Search API to fetch album art and song details.

No results

Parameters

Specular Opacity 0.40

Specular Saturation 6

Refraction Level 1.00

Blur Level 1.0

Progressive Blur Strength 1.00

Glass Background Opacity 0.60

[#](https://kube.io/blog/liquid-glass-css-svg#conclusion)Conclusion
-------------------------------------------------------------------

This prototype distills Apple’s Liquid Glass into real‑time refraction plus a simple highlight. It’s flexible, but still Chrome‑bound—only Chromium exposes SVG filters as `backdrop-filter`. That said, it’s already viable inside Chromium‑based runtimes like Electron, elsewhere you could fake a softer fallback with layered blur.

Treat this strictly as experimental. Dynamic shape/size changes are currently costly because nearly every tweak (besides animating `<filter />` props, like `scale`) forces a full displacement map rebuild.

The code needs a cleanup pass and perf work before any possible open‑source release.

Thanks for reading my first post—I'd genuinely love any feedback, ideas, critiques, or suggestions. If it sparked a thought or you know someone who'd enjoy this kind of deep‑dive, feel free to pass it along.
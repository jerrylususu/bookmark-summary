Title: Exposition of Frontend Build Systems

URL Source: https://sunsetglow.net/posts/frontend-build-systems.html

Markdown Content:
Developers write JavaScript; browsers run JavaScript. Fundamentally, no build step is necessary in frontend development. So why do we have a build step in modern frontend?

As frontend codebases grow larger, and as developer ergonomics become more important, shipping JavaScript source code directly to the client leads to two primary problems:

1.  **Unsupported Language Features:** Because JavaScript runs in the browser, and because there are many browsers out there of a variety of versions, each language feature you use reduces the number of clients that can execute your JavaScript. Furthermore, language extensions like JSX are not valid JavaScript and will not run in any browser.
    
2.  **Performance:** The browser must request each JavaScript file individually. In a large codebase, this can result in thousands of HTTP requests to render a single page. In the past, before HTTP/2, this would also result in thousands of TLS handshakes.
    
    In addition, several sequential network round trips may be needed before all the JavaScript is loaded. For example, if `index.js` imports `page.js` and `page.js` imports `button.js`, three sequential network round trips are necessary to fully load the JavaScript. This is called the waterfall problem.
    
    Source files can also be unnecessarily large due to long variable names and whitespace indentation characters, increasing bandwidth usage and network loading time.
    

Frontend build systems process source code and emit one or more JavaScript files optimized for sending to the browser. The resulting _distributable_ is typically illegible to humans.

[Build Steps](https://sunsetglow.net/posts/frontend-build-systems.html#build-steps)
-----------------------------------------------------------------------------------

Frontend build systems typically consist of three steps: transpilation, bundling, and minification.

Some applications may not require all three steps. For example, smaller codebases may not require bundling or minification, and development servers may skip bundling and/or minification for performance. Additional custom steps may also be added.

Some tools implement multiple build steps. Notably, bundlers often implement all three steps, and a bundler alone may be sufficient to build straightforward applications. Complex applications may require specialized tools for each build step that provide larger feature sets.

[Transpilation](https://sunsetglow.net/posts/frontend-build-systems.html#transpilation)
---------------------------------------------------------------------------------------

Transpilation solves the problem of unsupported language features by converting JavaScript written in a modern version of the JavaScript standard to an older version of the JavaScript standard. These days, ES6/ES2015 is a common target.

Frameworks and tools may also introduce transpilation steps. For example, the JSX syntax must be transpiled to JavaScript. If a library offers a Babel plugin, that usually means that it requires a transpilation step. Additionally, languages such as TypeScript, CoffeeScript, and Elm must be transpiled to JavaScript.

[CommonJS modules](https://wiki.commonjs.org/wiki/Modules) (CJS) must also be transpiled to a browser-compatible module system. After browsers added widespread support for [ES6 Modules](https://exploringjs.com/es6/ch_modules.html) (ESM) in 2018, transpilation to ESM has generally been recommended. ESM is furthermore easier to optimize and [tree-shake](https://sunsetglow.net/posts/frontend-build-systems.html#tree-shaking) since its imports and exports are statically defined.

The transpilers in common use today are Babel, SWC, and TypeScript Compiler.

1.  [**Babel**](https://babeljs.io/) (2014) is the standard transpiler: a slow single-threaded transpiler written in JavaScript. Many frameworks and libraries that require transpilation do so via a Babel plugin, requiring Babel to be part of the build process. However, Babel is hard to debug and can often be confusing.
    
2.  [**SWC**](https://swc.rs/) (2020) is a fast multi-threaded transpiler written in Rust. It claims to be 20x faster than Babel; hence, it is used by the newer frameworks and build tools. It supports transpiling TypeScript and JSX. If your application does not require Babel, SWC is a superior choice.
    
3.  [**TypeScript Compiler (tsc)**](https://github.com/microsoft/TypeScript) also supports transpiling TypeScript and JSX. It is the reference implementation of TypeScript and the only fully featured TypeScript type checker. However, it is very slow. While a TypeScript application must typecheck with the TypeScript Compiler, for its build step, an alternative transpiler will be much more performant.
    

It is also possible to skip the transpilation step if your code is pure JavaScript and uses ES6 Modules.

An alternative solution for a subset of unsupported language features is a polyfill. Polyfills are executed at runtime and implement any missing language features before executing the main application logic. However, this adds runtime cost, and some language features cannot be polyfilled. See [core-js](https://github.com/zloirock/core-js).

All bundlers are also inherently transpilers, as they parse multiple JavaScript source files and emit a new bundled JavaScript file. When doing so, they can pick which language features to use in their emitted JavaScript file. Some bundlers are additionally capable of parsing TypeScript and JSX source files. If your application has straightforward transpilation needs, you may not need a separate transpiler.

[Bundling](https://sunsetglow.net/posts/frontend-build-systems.html#bundling)
-----------------------------------------------------------------------------

Bundling solves the need to make many network requests and the waterfall problem. Bundlers concatenate multiple JavaScript source files into a single JavaScript output file, called a bundle, without changing application behavior. The bundle can be efficiently loaded by the browser in a single round-trip network request.

The bundlers in common use today are Webpack, Parcel, Rollup, esbuild, and Turbopack.

1.  [**Webpack**](https://webpack.js.org/) (2014) gained significant popularity around 2016, later becoming the standard bundler. Unlike the then-incumbent Browserify, which was commonly used with the Gulp task runner, Webpack pioneered “loaders” that transformed source files upon import, allowing Webpack to orchestrate the entire build pipeline.
    
    Loaders allowed developers to transparently import static assets inside JavaScript files, combining all source files and static assets into a single dependency graph. With Gulp, each type of static asset had to be built as a separate task. Webpack also supported [code splitting](https://sunsetglow.net/posts/frontend-build-systems.html#code-splitting) out of the box, simplifying its setup and configuration.
    
    Webpack is slow and single-threaded, written in JavaScript. It is highly configurable, but its many configuration options can be confusing.
    
2.  [**Rollup**](https://rollupjs.org/) (2016) capitalized on the widespread browser support of ES6 Modules and the optimizations it enabled, namely [tree shaking](https://sunsetglow.net/posts/frontend-build-systems.html#tree-shaking). It produced far smaller bundle sizes than Webpack, leading Webpack to later adopt similar optimizations. Rollup is a single-threaded bundler written in JavaScript, only slightly more performant than Webpack.
    
3.  [**Parcel**](https://parceljs.org/) (2018) is a low-configuration bundler designed to “just work” out of the box, providing sensible default configurations for all steps of the build process and developer tooling needs. It is multithreaded and much faster than Webpack and Rollup. Parcel 2 uses SWC under the hood.
    
4.  [**Esbuild**](https://esbuild.github.io/) (2020) is a bundler architected for parallelism and optimal performance, written in Go. It is dozens of times more performant than Webpack, Rollup, and Parcel. Esbuild implements a basic transpiler as well as a minifier. However, it is less featureful than the other bundlers, providing a limited plugin API that cannot directly modify the AST. Instead of modifying source files with an esbuild plugin, the files can be transformed before being passed to esbuild.
    
5.  [**Turbopack**](https://turbo.build/pack) (2022) is a fast Rust bundler that supports incremental rebuilds. The project is built by Vercel and led by the creator of Webpack. It is currently in beta and may be opted into in Next.js.
    

It is reasonable to skip the bundling step if you have very few modules or have very low network latency (e.g. on localhost). Several development servers also choose not to bundle modules for the development server.

### [Code Splitting](https://sunsetglow.net/posts/frontend-build-systems.html#code-splitting)

By default, a client-side React application is transformed into a single bundle. For large applications with many pages and features, the bundle can be very large, negating the original performance benefits of bundling.

Dividing the bundle into several smaller bundles, or _code splitting_, solves this problem. A common approach is to split each page into a separate bundle. With HTTP/2, shared dependencies may also be factored out into their own bundles to avoid duplication at little cost. Additionally, large modules may split into a separate bundle and lazy-loaded on-demand.

After code splitting, the filesize of each bundle is greatly reduced, but additional network round trips are now necessary, potentially re-introducing the waterfall problem. Code splitting is a tradeoff.

The filesystem router, popularized by Next.js, optimizes the code splitting tradeoff. Next.js creates separate bundles per page, only including the code imported by that page in its bundles. Loading a page preloads all bundles used by that page in parallel. This optimizes bundle size without re-introducing the waterfall problem. The filesystem router achieves this by creating one entry point per page (`pages/**/*.jsx`), as opposed to the single entry point of traditional client-side React apps (`index.jsx`).

### [Tree Shaking](https://sunsetglow.net/posts/frontend-build-systems.html#tree-shaking)

A bundle is composed of multiple modules, each of which contains one or more exports. Often, a given bundle will only make use of a subset of exports from the modules it imports. The bundler can remove the unused exports of its modules in a process called _tree shaking_. This optimizes the bundle size, improving loading and parsing times.

Tree shaking depends on static analysis of the source files, and is thus impeded when static analysis is made more challenging. Two primary factors influence the efficiency of tree shaking:

1.  **Module System:** ES6 Modules have static exports and imports, while CommonJS modules have dynamic exports and imports. Bundlers are thus able to be more aggressive and efficient when tree shaking ES6 Modules.
    
2.  **Side Effects:** The `sideEffects` property of `package.json` declares whether a module has side effects on import. When side effects are present, unused modules and unused exports may not be tree shaken due to the limitations of static analysis.
    

### [Static Assets](https://sunsetglow.net/posts/frontend-build-systems.html#static-assets)

Static assets, such as CSS, images, and fonts, are typically added to the distributable in the bundling step. They may also be optimized for filesize in the minification step.

Prior to Webpack, static assets were built separately from the source code in the build pipeline as an independent build task. To load the static assets, the application had to reference them by their final path in the distributable. Thus, it was common to carefully organize assets around a URL convention (e.g. `/assets/css/banner.jpg` and `/assets/fonts/Inter.woff2`).

Webpack “loaders” allowed the importing of static assets from JavaScript, unifying both code and static assets into a single dependency graph. During bundling, Webpack replaces the static asset import with its final path inside the distributable. This feature enabled static assets to be organized with their associated components in the source code and created new possibilities for static analysis, such as detecting non-existent assets.

It is important to recognize that the importing of static assets (non-JavaScript-or-transpiles-to-JavaScript files) is not part of the JavaScript language. It requires a bundler configured with support for that asset type. Fortunately, the bundlers that followed Webpack also adopted the “loaders” pattern, making this feature commonplace.

[Minification](https://sunsetglow.net/posts/frontend-build-systems.html#minification)
-------------------------------------------------------------------------------------

Minification resolves the problem of unnecessarily large files. Minifiers reduce the size of a file without affecting its behavior. For JavaScript code and CSS assets, minifiers can shorten variables, eliminate whitespace and comments, eliminate dead code, and optimize language feature use. For other static assets, minifiers can perform file size optimization. Minifiers are typically run on a bundle at the end of the build process.

Several JavaScript minifiers in common use today are Terser, esbuild, and SWC. [**Terser**](https://terser.org/) was forked from the unmaintained uglify-es. It is written in JavaScript and is somewhat slow. **Esbuild** and **SWC**, mentioned previously, implement minifiers in addition to their other capabilities and are faster than Terser.

Several CSS minifiers in common use today are cssnano, csso, and Lightning CSS. [**Cssnano**](https://cssnano.github.io/cssnano/) and [**csso**](https://github.com/css/csso) are pure CSS minifiers written in JavaScript and thus somewhat slow. [**Lightning CSS**](https://lightningcss.dev/) is written in Rust and claims to be 100x faster than cssnano. Lightning CSS additionally supports CSS transformation and bundling.

The basic frontend build pipeline described above is sufficient to create an optimized production distributable. There exist several classes of tools that augment the basic build pipeline and improve upon developer experience.

The frontend space is notorious for the challenge of picking the “right” packages to use. For example, of the five bundlers listed above, which should you pick?

Meta-frameworks provide a curated set of already selected packages, including build tools, that synergize and enable specialized application paradigms. For example, [**Next.js**](https://nextjs.org/) specializes in Server-Side Rendering (SSR) and [**Remix**](https://remix.run/) specializes in progressive enhancement.

Meta-frameworks typically provide a preconfigured build system, removing the need for you to stitch one together. Their build systems have configurations for both production and development servers.

Like meta-frameworks, build tools like [**Vite**](https://vitejs.dev/) provide preconfigured build systems for both production and development. Unlike meta-frameworks, they do not force a specialized application paradigm. They are suitable for generic frontend applications.

[Sourcemaps](https://sunsetglow.net/posts/frontend-build-systems.html#sourcemaps)
---------------------------------------------------------------------------------

The distributable emitted by the build pipeline is illegible to most humans. This makes it difficult to debug any errors that occur, as their tracebacks point to illegible code.

[Sourcemaps](https://developer.chrome.com/blog/sourcemaps/) resolve this problem by mapping code in the distributable back to its original location in the source code. The browser and triage tools (e.g. Sentry) use the sourcemaps to restore and display the original source code. In production, sourcemaps are often hidden from the browser and only uploaded to triage tools to avoid publicizing the source code.

Each step of the build pipeline can emit a sourcemap. If multiple build tools are used to construct the pipeline, the sourcemaps will form a chain (e.g. `source.js` -> `transpiler.map` -> `bundler.map` -> `minifier.map`). To identify the source code corresponding to the minified code, the chain of source maps must be traversed.

However, most tools are not capable of interpreting a chain of sourcemaps; they expect at most one sourcemap per file in the distributable. The chain of sourcemaps must be flattened into a single sourcemap. Preconfigured build systems will solve this problem (see Vite’s [`combineSourcemaps`](https://github.com/vitejs/vite/blob/feae09fdfab505e58950c915fe5d8dd103d5ffb9/packages/vite/src/node/utils.ts#L831) function).

[Hot Reload](https://sunsetglow.net/posts/frontend-build-systems.html#hot-reload)
---------------------------------------------------------------------------------

Development servers often provide a Hot Reload feature, which automatically rebuilds a new bundle on source code changes and reloads the browser. While greatly superior to rebuilding and reloading manually, it is still somewhat slow, and all client-side state is lost on reload.

[Hot Module Replacement](https://webpack.js.org/concepts/hot-module-replacement/) improves upon Hot Reload by replacing changed bundles in the running application, an in-place update. This preserves the client-side state of unchanged modules and reduces the latency between code change and updated application.

However, each code change triggers the rebuild of all the bundles that import it. This has a linear time complexity relative to bundle size. Hence, in large applications, Hot Module Replacement can become slow due to the growing rebundling cost.

The [no-bundle paradigm](https://vitejs.dev/guide/why.html), currently championed by Vite, counters this by not bundling the development server. Instead, Vite serves ESM modules, each corresponding to a source file, directly to the browser. In this paradigm, each code change triggers a single module replacement in the frontend. This results in a near-constant refresh time complexity relative to application size. However, if you have many modules, the initial page load may take longer.

[Monorepos](https://sunsetglow.net/posts/frontend-build-systems.html#monorepos)
-------------------------------------------------------------------------------

In organizations with multiple teams or multiple applications, the frontend may be split into multiple JavaScript packages, but retained in a single repository. In such architectures, each package has its own build step, and together they form a dependency graph of packages. The applications reside at the roots of the dependency graphs.

Monorepo tools orchestrate the building of the dependency graph. They often provide features such as incremental rebuilds, parallelism, and remote caching. With these features, large codebases can enjoy the build times of small codebases.

The broader industry-standard monorepo tools, like [Bazel](https://bazel.build/), support a broad set of languages, complicated build graphs, and hermetic execution. However, JavaScript for frontend is one of the hardest ecosystems to completely integrate with these tools, and there is currently little prior art.

Fortunately, there exist several monorepo tools designed specifically for frontend. Unfortunately, they lack the flexibility and robustness of Bazel et al., most notably hermetic execution.

The frontend-specific monorepo tools in common use today are [**Nx**](https://nx.dev/) and [**Turborepo**](https://turbo.build/repo). Nx is more mature and featureful, while Turborepo is part of the Vercel ecosystem. In the past, [**Lerna**](https://lerna.js.org/) was the standard tool for linking multiple JavaScript packages together and publishing them to NPM. In 2022, the Nx team took over Lerna, and Lerna now uses Nx under the hood to power builds.

[Trends](https://sunsetglow.net/posts/frontend-build-systems.html#trends)
-------------------------------------------------------------------------

Newer build tools are written in compiled languages and emphasize performance. Frontend builds were terribly slow in 2019, but modern tools have greatly sped it up. However, modern tools have smaller feature sets and are sometimes incompatible with libraries, so legacy codebases often cannot easily switch to them.

Server-Side Rendering (SSR) has become more popular after the rise of Next.js. SSR does not introduce any fundamental differences to frontend build systems. SSR applications must also serve JavaScript to the browser, and they thus execute the same build steps.

Title: Optimizing SPA load times with async chunks preloading

URL Source: https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/

Published Time: 2024-08-13

Markdown Content:
Hello hello! In this post, I’ll explain how to improve the performance of client-side rendered apps by avoiding the waterfall effect caused by route-based lazy-loading. We'll do this by injecting a custom script that preloads the chunks for the current route, ensuring they’re downloaded in parallel with the entry point chunk. I'll use [Rsbuild](https://rsbuild.dev/) for the script injection, but its code can easily be adapted for Webpack and other bundlers as well.  
The code snippets are based on a tiny app with just two pages: a home page (that lives under `/` and `/home`) and a settings page (that lives under `/settings`).

[Route-based code splitting --------------------------](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#route-based-code-splitting)In client-side rendered apps, code splitting is one of the main strategies you can use to improve the overall performance. Code splitting enables loading only the necessary code chunks, rather than everything upfront.

The most common way to implement code splitting is by lazy loading route (or page) chunks. This means these chunks are loaded only when the user visits the respective pages, rather than being loaded in advance. This not only reduces the size of the bundle needed to load the app, but also improves caching: the more your app bundle is split into chunks, the less cache invalidation will happen (as long as static files are hashed appropriately).

Server-side rendering frameworks like Next.js and Remix often handle code splitting and lazy loading for you. For client-side rendered single-page applications, you can achieve this by lazy-loading the route components you will use in your router:

```
const Home = lazy(() => import("./pages/home-page"));
const Settings = lazy(() => import("./pages/settings-page"));
```

```
const Home = lazy(() => import("./pages/home-page"));
const Settings = lazy(() => import("./pages/settings-page"));
```

With this setup, when users land on the `/` route of your app, only the home page chunk (e.g., `home.[hash].js`) will be downloaded. The settings page chunk won’t be downloaded until needed (e.g., when you navigate to the settings page).

[Lazy loading drawbacks ----------------------](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#lazy-loading-drawbacks)While code splitting offers multiple benefits, it also has some drawbacks. By default, chunks are downloaded only when needed, which can introduce noticeable delays in two areas:

1.  **Initial Load Delay**: When the app first loads, there’s a delay between loading the entry point chunk (e.g., the top-level app with the client-side router) and loading the initial page (e.g., home). This is because the browser first downloads, parses, and runs the app entry point. **Then** the app router determines it's on a route that needs to load the home page, and prompting the browser to download, parse, and run the home page code.
2.  **Navigation Delay**: Similarly, there’s a delay each time you navigate between different pages. This is because the browser downloads, parses, and runs new chunks only when navigation starts (e.g., the settings page chunk is loaded only when clicking a “Settings” link from the home page).

A solid caching strategy (e.g., marking these chunks as immutable and pre-caching them) and using routers with preloading capabilities can mitigate the second point. I might explore these topics in more depth in a follow-up post. For now, let’s focus on addressing the first point.

[Preloading Async Pages ----------------------](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#preloading-async-pages)Our goal is to solve the waterfall problem where pages must wait for the entry point chunk to request them before they can be downloaded:

![Image 1](https://mmazzarolo.com/_next/image/?url=%2Fimages%2F2024-08-13-async-chunk-preloading-on-load%2Fbefore-preloading.png&w=3840&q=75)

We already know that if a user navigates to “/”, the home page chunk should be downloaded. There’s no reason to wait for the app to be fully loaded to start downloading the home page chunk, right? So, we should/can download it in parallel with the entry point chunk.

In my experience, the best way to achieve this is by injecting a small script in the head of the HTML to preload the async chunk for the currently visited URL.

From a very high-level, the idea is to use a build tool (here, Rsbuild) to inject a small script into the document’s head. This script holds a mapping between each route and the files that should be preloaded for that route. When executed, it preloads the necessary files for the current path by manually adding them to the HTML page as [`link rel="preload"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/preload).

Let's dive deeper into an implementation example.

[](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#add-the-webpackchunkname-magic-comment-to-async-imports)Script generation and injection logic must happen at the bundler level because we won’t know the chunk file names until the build is complete. For example, if we follow good caching practices, the home page chunk will likely have a hash in its name (e.g., `page.12ab33.js`), which is assigned by the bundler.

To determine if a chunk should be preloaded, I suggest maintaining a mapping between the page paths and their `webpackChunkName`. The `webpackChunkName` is a [magic comment](https://webpack.js.org/api/module-methods/) supported by multiple bundlers that can be used to assign a readable name to a JavaScript chunk, which the bundler can then access:

```
const Home = lazy(
  () => import(/* webpackChunkName: "home" */ "./pages/home-page"),
);
const Settings = lazy(
  () => import(/* webpackChunkName: "settings" */ "./pages/settings-page"),
);
```

```
const Home = lazy(
  () => import(/* webpackChunkName: "home" */ "./pages/home-page"),
);
const Settings = lazy(
  () => import(/* webpackChunkName: "settings" */ "./pages/settings-page"),
);
```

route-chunk-mapping.ts

```
// Mapping between paths and their webpackChunkNames
export const routeChunkMapping = {
  "/": "home",
  "/home": "home",
  "/settings": "settings",
};
```

route-chunk-mapping.ts

```
// Mapping between paths and their webpackChunkNames
export const routeChunkMapping = {
  "/": "home",
  "/home": "home",
  "/settings": "settings",
};
```

[Build the list of files to loaded for each route ------------------------------------------------](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#build-the-list-of-files-to-loaded-for-each-route)With a mapping between each route and the page we want to preload, the next step is to determine what files compose that page chunk. I recommend creating a plugin (for Rsbuild, but the code can be easily adapted for Webpack too) that checks the compilation output to determine the names of the files each chunk depends on.

Note that we’re talking about multiple files because a single chunk might depend on other chunks. For example, say we have two chunks, one for the home and one for the settings page. If they both import the same module (say, lodash) that is not part of the entry point chunk, to load them we'll need to load chunks: `lodash.[hash].js` and `home.[hash].js`/`settings.[hash].js`. Also, note that the order matters.

Luckily, the bundler exposes these dependencies as "chunk groups" in its API.

```
import { defineConfig } from "@rsbuild/core";
import { pluginReact } from "@rsbuild/plugin-react";
import { chunksPreloadPlugin } from "./rsbuild-chunks-preload-plugin";
import { routeChunkMapping } from "./src/router-chunk-mapping.ts";
 
export default defineConfig({
  plugins: [pluginReact(), chunksPreloadPlugin({ routeChunkMapping })],
});
```

```
import { defineConfig } from "@rsbuild/core";
import { pluginReact } from "@rsbuild/plugin-react";
import { chunksPreloadPlugin } from "./rsbuild-chunks-preload-plugin";
import { routeChunkMapping } from "./src/router-chunk-mapping.ts";
 
export default defineConfig({
  plugins: [pluginReact(), chunksPreloadPlugin({ routeChunkMapping })],
});
```

```
import type { RsbuildPlugin } from "@rsbuild/core";
 
type RouteChunkMapping = { [path: string]: string };
 
type PluginParams = {
  routeChunkMapping: RouteChunkMapping;
};
 
export const chunksPreloadPlugin = (params: PluginParams): RsbuildPlugin => ({
  name: "chunks-preload-plugin",
  setup: (api) => {
    api.processAssets(
      { stage: "report" },
      ({ assets, sources, compilation }) => {
        const { routeChunkMapping } = params;
        // Generate a mapping between async chunk names and the files required
        // for them to load.
        const chunkFilesMapping = {};
        for (const chunkGroup of compilation.chunkGroups) {
          chunkFilesMapping[chunkGroup.name || "undefined"] =
            chunkGroup.getFiles();
        }
        // Build a URL path name → files to preload mapping.
        const pathToFilesToPreloadMapping = {};
        for (const [path, chunkName] of Object.entries(routeChunkMapping)) {
          const chunkFiles = chunkFilesMapping[chunkName].filter((file) =>
            file.endsWith(".js"),
          );
          pathToFilesToPreloadMapping[path] = chunkFiles;
        }
        // TBD — see next part
      },
    );
  },
});
```

```
import type { RsbuildPlugin } from "@rsbuild/core";
 
type RouteChunkMapping = { [path: string]: string };
 
type PluginParams = {
  routeChunkMapping: RouteChunkMapping;
};
 
export const chunksPreloadPlugin = (params: PluginParams): RsbuildPlugin => ({
  name: "chunks-preload-plugin",
  setup: (api) => {
    api.processAssets(
      { stage: "report" },
      ({ assets, sources, compilation }) => {
        const { routeChunkMapping } = params;
        // Generate a mapping between async chunk names and the files required
        // for them to load.
        const chunkFilesMapping = {};
        for (const chunkGroup of compilation.chunkGroups) {
          chunkFilesMapping[chunkGroup.name || "undefined"] =
            chunkGroup.getFiles();
        }
        // Build a URL path name → files to preload mapping.
        const pathToFilesToPreloadMapping = {};
        for (const [path, chunkName] of Object.entries(routeChunkMapping)) {
          const chunkFiles = chunkFilesMapping[chunkName].filter((file) =>
            file.endsWith(".js"),
          );
          pathToFilesToPreloadMapping[path] = chunkFiles;
        }
        // TBD — see next part
      },
    );
  },
});
```

> Notice that [`api.processAssets` is the same API available in Webpack as well](https://webpack.js.org/api/compilation-hooks/#processassets). Porting this plugin to Webpack is mostly a matter of copy-pasting the `api.processAssets` implementation into a Webpack plugin 👍.

[Generate the preloading script ------------------------------](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#generate-the-preloading-script)Finally, we complete the plugin by making it inject a custom script into the HTML file. The script is executed on page load **before** the entry point chunk and adds a `link rel="preload"` for each file that should be preloaded on the current path (`window.location.pathname`).

```
import type { RsbuildPlugin } from "@rsbuild/core";
 
type RouteChunkMapping = { [path: string]: string };
 
type PluginParams = {
  routeChunkMapping: RouteChunkMapping;
};
 
export const chunksPreloadPlugin = (params: PluginParams): RsbuildPlugin => ({
  name: "chunks-preload-plugin",
  setup: (api) => {
    api.processAssets(
      { stage: "report" },
      ({ assets, sources, compilation }) => {
        const { routeChunkMapping } = params;
        // Generate a mapping between async chunk names and the files required
        // for them to load.
        const chunkFilesMapping = {};
        for (const chunkGroup of compilation.chunkGroups) {
          chunkFilesMapping[chunkGroup.name || "undefined"] =
            chunkGroup.getFiles();
        }
        // Build a URL path name → files to preload mapping.
        const pathToFilesToPreloadMapping = {};
        for (const [path, chunkName] of Object.entries(routeChunkMapping)) {
          const chunkFiles = chunkFilesMapping[chunkName].filter((file) =>
            file.endsWith(".js"),
          );
          pathToFilesToPreloadMapping[path] = chunkFiles;
        }
        // Generate the (stringified) script responsible for preloading the
        // async chunk files (based on the current URL).
        const scriptToInject = generatePreloadScriptToInject(
          pathToFilesToPreloadMapping,
        );
        // Insert the generated script into the index.html's <head>, right
        // before any other script.
        const indexHTML = assets["index.html"];
        if (!indexHTML) {
          return;
        }
        const oldIndexHTMLContent = indexHTML.source();
        const firstScriptInIndexHTMLIndex =
          oldIndexHTMLContent.indexOf("<script");
        const newIndexHTMLContent = `${oldIndexHTMLContent.slice(
          0,
          firstScriptInIndexHTMLIndex,
        )}${scriptToInject}${oldIndexHTMLContent.slice(
          firstScriptInIndexHTMLIndex,
        )}`;
        const source = new sources.RawSource(newIndexHTMLContent);
        compilation.updateAsset("index.html", source);
      },
    );
  },
});
 
// Generate the script to inject in the HTML.
// It checks what the current URL is and adds preload links of each file of
// the chunk associated with the URL.
const generatePreloadScriptToInject = (pathToFilesToPreloadMapping: {
  [path: string]: Array<string>;
}): string => {
  const scriptContent = `
	  try {
      (function () {
        const pathToFilesToPreloadMapping = ${JSON.stringify(
          pathToFilesToPreloadMapping,
        )};
        const filesToPreload = pathToFilesToPreloadMapping[window.location.pathname];
        if (!filesToPreload) return;
        for (const fileToPreload of filesToPreload) {
          const preloadLinkEl = document.createElement("link");
					preloadLinkEl.setAttribute("href", fileToPreload);
					preloadLinkEl.setAttribute("rel", "preload");
					preloadLinkEl.setAttribute("as", "script");
					document.head.appendChild(preloadLinkEl);
        }
      })();
    } catch (err) {
      console.warn("Unable to run the scripts preloading.");	
    }
`;
  const script = `<script>${scriptContent}</script>`;
 
  return script;
};
```

```
import type { RsbuildPlugin } from "@rsbuild/core";
 
type RouteChunkMapping = { [path: string]: string };
 
type PluginParams = {
  routeChunkMapping: RouteChunkMapping;
};
 
export const chunksPreloadPlugin = (params: PluginParams): RsbuildPlugin => ({
  name: "chunks-preload-plugin",
  setup: (api) => {
    api.processAssets(
      { stage: "report" },
      ({ assets, sources, compilation }) => {
        const { routeChunkMapping } = params;
        // Generate a mapping between async chunk names and the files required
        // for them to load.
        const chunkFilesMapping = {};
        for (const chunkGroup of compilation.chunkGroups) {
          chunkFilesMapping[chunkGroup.name || "undefined"] =
            chunkGroup.getFiles();
        }
        // Build a URL path name → files to preload mapping.
        const pathToFilesToPreloadMapping = {};
        for (const [path, chunkName] of Object.entries(routeChunkMapping)) {
          const chunkFiles = chunkFilesMapping[chunkName].filter((file) =>
            file.endsWith(".js"),
          );
          pathToFilesToPreloadMapping[path] = chunkFiles;
        }
        // Generate the (stringified) script responsible for preloading the
        // async chunk files (based on the current URL).
        const scriptToInject = generatePreloadScriptToInject(
          pathToFilesToPreloadMapping,
        );
        // Insert the generated script into the index.html's <head>, right
        // before any other script.
        const indexHTML = assets["index.html"];
        if (!indexHTML) {
          return;
        }
        const oldIndexHTMLContent = indexHTML.source();
        const firstScriptInIndexHTMLIndex =
          oldIndexHTMLContent.indexOf("<script");
        const newIndexHTMLContent = `${oldIndexHTMLContent.slice(
          0,
          firstScriptInIndexHTMLIndex,
        )}${scriptToInject}${oldIndexHTMLContent.slice(
          firstScriptInIndexHTMLIndex,
        )}`;
        const source = new sources.RawSource(newIndexHTMLContent);
        compilation.updateAsset("index.html", source);
      },
    );
  },
});
 
// Generate the script to inject in the HTML.
// It checks what the current URL is and adds preload links of each file of
// the chunk associated with the URL.
const generatePreloadScriptToInject = (pathToFilesToPreloadMapping: {
  [path: string]: Array<string>;
}): string => {
  const scriptContent = `
	  try {
      (function () {
        const pathToFilesToPreloadMapping = ${JSON.stringify(
          pathToFilesToPreloadMapping,
        )};
        const filesToPreload = pathToFilesToPreloadMapping[window.location.pathname];
        if (!filesToPreload) return;
        for (const fileToPreload of filesToPreload) {
          const preloadLinkEl = document.createElement("link");
					preloadLinkEl.setAttribute("href", fileToPreload);
					preloadLinkEl.setAttribute("rel", "preload");
					preloadLinkEl.setAttribute("as", "script");
					document.head.appendChild(preloadLinkEl);
        }
      })();
    } catch (err) {
      console.warn("Unable to run the scripts preloading.");	
    }
`;
  const script = `<script>${scriptContent}</script>`;
 
  return script;
};
```

And voilà, now all async chunks of the current page will load in parallel with the entry point chunk.

![Image 2](https://mmazzarolo.com/_next/image/?url=%2Fimages%2F2024-08-13-async-chunk-preloading-on-load%2Fafter-preloading.png&w=3840&q=75)

[Further improvements --------------------](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#further-improvements)As with any pattern, there are numerous ways to improve this flow. For simplicity, I’ve left some implementation details to the reader.

If you plan to use this pattern in production, you’ll probably want to at least improve the following areas.

[### Solidify the routing logic](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#solidify-the-routing-logic)The path recognition used by the preload script in the example above is quite basic, so I suggest tweaking the plugin API to accept the same configuration as React Router (or whichever router you’re using). In the example, we only used top-level paths, but real-world scenarios are more complex and require sub-path checks as well (e.g., `/user/:user-id`), so consider implementing dynamic path recognition and pattern matching for a more robust routing solution.

[### Compress the injected script](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#compress-the-injected-script)Larger SPAs might have hundreds of chunks. Since the chunks are hardcoded into the preload script, it’s important to ensure it doesn’t grow too large and become a bottleneck. You can adopt strategies to compress the script size, such as minifying the script code and avoiding repetition of chunk URLs (or their sub-paths).

[### Expose the preload API from the script](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#expose-the-preload-api-from-the-script)You can expand the script further by making the preload execution programmatic, allowing it to be invoked at runtime. This can be done by exposing the preload function on the `window` object and making the path a parameter instead of always using the current one, for example:

```
// In the preload script
window.__preloadPathChunks = function (path = window.location.pathname) {
  // ...Script code
}`
```

```
// In the preload script
window.__preloadPathChunks = function (path = window.location.pathname) {
  // ...Script code
}`
```

This enables invoking the function from your SPA when needed, such as when hovering over URLs.

[### Use a Service Worker to precache all your SPA’s chunks](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#use-a-service-worker-to-precache-all-your-spas-chunks)I’ll briefly mention this here, although it might be worth its own post. As an alternative to the previous bullet point, and as a solution to the first drawback mentioned in the “Lazy Loading Drawbacks” section of this post, I’d recommend [using a Service Worker to precache all your app chunks](https://web.dev/learn/performance/prefetching-prerendering-precaching). [Google’s Workbox](https://developer.chrome.com/docs/workbox/modules/workbox-precaching) is my go-to solution for precaching.

[### Explore other optimizations](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/#explore-other-optimizations)Last but not least, maybe consider other performance optimizations like ensuring that the entry point chunk still loads with a higher priority than preloaded routes, integrating preloading at a more granular level for non-route-based components, and so on.

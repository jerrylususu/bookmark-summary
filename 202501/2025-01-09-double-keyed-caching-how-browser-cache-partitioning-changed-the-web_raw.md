Title: Double-keyed Caching: How Browser Cache Partitioning Changed the Web

URL Source: https://addyosmani.com/blog/double-keyed-caching/

Markdown Content:
The web’s caching model served us well for over two decades. Recently, in the name of privacy, it’s undergone a fundamental shift that challenges many of our performance optimization assumptions. This is called Double-keyed Caching or [cache-partitioning](https://developer.chrome.com/blog/http-cache-partitioning) more generally. Here’s what changed, why it matters, and how to adapt.

How Caching Used to Work (Pre-2020)
-----------------------------------

In the traditional model, browsers maintained a simple key-value store for cached resources:

```
cache = {
  "https://cdn.example.com/jquery-3.6.0.min.js": resourceData,
  "https://fonts.googleapis.com/css?family=Roboto": resourceData
}
```

This meant that once a user visited any site loading jQuery from a public CDN, subsequent visits to other sites using the same CDN-hosted jQuery would get an instant cache hit. This model powered the “CDN-first” approach that dominated web development through the 2010s.

The advantages were compelling:

*   Reduced bandwidth usage through cross-site resource sharing
*   Better performance for users visiting multiple sites using common resources
*   Lower hosting costs by leveraging public CDNs
*   Faster page loads through cache hits

The Privacy Problem
-------------------

While efficient, this model leaked information. Consider these attack vectors:

1.  Cache probing: Site A could check if resources from Site B were in the cache, revealing browsing history
2.  Timing attacks: Measuring resource load times exposed cache status
3.  Cross-site tracking: Cached resources could be used as persistent identifiers

The New Model: Double-Keyed Caching
-----------------------------------

Double-keyed caching introduces a fundamental change to how browsers store and retrieve resources. Instead of using just the resource URL as the cache key, browsers now use two pieces of information: the top-level site making the request and the resource’s URL. Let’s look at an example.

When site-a.com requests jQuery from a CDN, the browser creates a HTTP cache entry that combines both site-a.com (the requester) and the full resource URL. Later, when site-b.com requests that exact same jQuery file, instead of reusing the cached copy, the browser creates a completely new cache entry with site-b.com as part of the key. This is what modern cache entries look like:

```
cache = {
  {
    topLevelSite: "site-a.com",
    resource: "https://cdn.example.com/jquery-3.6.0.min.js"
  }: resourceData,
  {
    topLevelSite: "site-b.com",
    resource: "https://cdn.example.com/jquery-3.6.0.min.js"
  }: resourceData
}
```

This means that even identical resources are cached separately for each site that requests them, effectively partitioning the cache by the requesting site’s origin. While this prevents cross-site tracking and other privacy issues, it also means we’re storing duplicate copies of the same resource - a trade-off between security and efficiency.

Performance Impact on Cache Hit Rates
-------------------------------------

According to Chrome’s [implementation data](https://developer.chrome.com/blog/http-cache-partitioning/?utm_source=chatgpt.com#what_is_the_impact_of_this_behavioral_change), double-keyed caching leads to approximately:

*   3.6% increase in overall cache miss rate
*   4% increase in bytes loaded from the network
*   0.3% impact on First Contentful Paint (FCP)

While these numbers might seem modest, their impact varies significantly based on resource type and usage patterns.

While double-keyed caching introduces some performance overhead, it’s important to understand that these impacts are accepted as a necessary trade-off for enhanced security and privacy protection. The mechanism helps prevent various security vulnerabilities:

*   Protection against timing attacks that could expose user browsing history
*   Prevention of cross-site tracking through cache-based fingerprinting
*   Mitigation of side-channel attacks that exploit shared cache states
*   Enhanced resistance to cross-site search attacks

These security benefits justify the performance costs, though understanding and optimizing around these impacts remains crucial.

### Network Bandwidth Implications

The increased cache miss rate directly translates to additional network requests. For typical web resources, the impact includes:

#### Shared Libraries

*   Popular JavaScript libraries previously benefiting from cross-site caching now require separate downloads
*   CDN-hosted frameworks like jQuery or React face reduced caching benefits
*   Each top-level site maintains its own copy, increasing overall bandwidth usage

#### Web Fonts

*   Common fonts from services like Google Fonts require multiple downloads
*   Organizations using shared font resources across multiple domains face increased bandwidth costs
*   Font loading performance becomes more dependent on network conditions

#### Large Resources

*   Machine learning models and other large resources face the most significant impact
*   Resources in the megabyte range now potentially require multiple downloads
*   CDN costs may increase substantially for organizations serving large resources across multiple domains

These averages hide significant outliers. Some real-world examples:

### Enterprise SaaS Suite

```
// Before: One cache entry
cdn.company.com/shared-lib.js → 2.5MB

// After: Multiple entries
{crm.company.com, cdn.company.com/shared-lib.js} → 2.5MB
{mail.company.com, cdn.company.com/shared-lib.js} → 2.5MB
{docs.company.com, cdn.company.com/shared-lib.js} → 2.5MB

// Result: 7.5MB total cache usage
```

### Popular Framework CDN

```
// Before
unpkg.com/react@18.2.0 cached once → 118KB

// After
{site1.com, unpkg.com/react@18.2.0} → 118KB
{site2.com, unpkg.com/react@18.2.0} → 118KB
{site3.com, unpkg.com/react@18.2.0} → 118KB
```

### Common React Dependencies

Popular React libraries are affected similarly:

```
// Material-UI
{
    app_domain: "myapp.com",
    resource: "unpkg.com/@mui/material@5.14.0/umd/material-ui.production.min.js"
}

// React Router
{
    app_domain: "myapp.com",
    resource: "unpkg.com/react-router@6.14.0/umd/react-router.production.min.js"
}

// Redux
{
    app_domain: "myapp.com",
    resource: "unpkg.com/redux@4.2.1/dist/redux.min.js"
}
```

### Micro-Frontend Impact

For React micro-frontends, the impact is particularly notable:

```
// Main Shell Application (shell.company.com)
{
    app_domain: "shell.company.com",
    resources: [
        "unpkg.com/react@18.2.0/umd/react.production.min.js",
        "unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"
    ]
}

// MicroFrontend 1 (app1.company.com)
{
    app_domain: "app1.company.com",
    resources: [
        "unpkg.com/react@18.2.0/umd/react.production.min.js",
        "unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"
    ]
}

// Result: Duplicate downloads of React for each micro-frontend
```

Performance Impact Examples
---------------------------

### Typical React Application Bundle

Let’s look at a common React application setup:

```
// Bundle Sizes
const commonDependencies = {
    react: "118 KB",
    reactDom: "1.1 MB",
    materialUI: "469 KB",
    reactRouter: "27 KB",
    redux: "22 KB"
};

// Total per domain: ~1.7 MB
```

With multiple subdomains or micro-frontends, each domain needs its own copy in cache.

### Shared Component Libraries

For organizations with shared React component libraries:

```
// Shared UI Library
{
    size: "2.5 MB",
    domains: [
        "main-app.company.com",
        "dashboard.company.com",
        "admin.company.com"
    ],
    totalCacheSize: "7.5 MB" // 2.5 MB × 3 domains
}
```

Practical Implications
----------------------

### CDN economics have changed

*   The “use a public CDN” recommendation needs revisiting
*   Self-hosting may now be more bandwidth-efficient
*   CDN costs might increase due to reduced cache hits

### Domain strategy matters more

*   Each subdomain now maintains separate caches
*   Domain consolidation has performance benefits
*   Consider origin-aligned CDN domains

### Bundle strategy needs updating

*   Smaller, focused bundles may be preferable to shared chunks
*   Code splitting boundaries should align with domain boundaries
*   Resource prioritization becomes more critical

Adaptation Strategies
---------------------

### Domain Consolidation

Instead of:

```
assets1.company.com/lib.js
assets2.company.com/lib.js
```

Consider:

```
static.company.com/app1/lib.js
static.company.com/app2/lib.js
```

```
// Instead of:
const domains = [
    'app1.company.com/static/js/react.js',
    'app2.company.com/static/js/react.js'
];

// Consider:
const consolidatedDomain = 'static.company.com/js/react.js';
```

Module Federation:

```
// webpack.config.js
module.exports = {
    plugins: [
        new ModuleFederationPlugin({
            name: 'host',
            filename: 'remoteEntry.js',
            remotes: {
                app1: 'app1@http://static.company.com/app1/remoteEntry.js',
                app2: 'app2@http://static.company.com/app2/remoteEntry.js'
            },
            shared: {
                react: { singleton: true },
                'react-dom': { singleton: true }
            }
        })
    ]
};
```

### Smart Resource Loading

```
// Before: Rely on cache
<script src="https://unpkg.com/react@18.2.0"></script>

// After: Self-host critical resources
<script src="/vendor/react-18.2.0.min.js"></script>
```

Browser Variations
------------------

Different browsers implement cache partitioning differently:

*   **Chrome**: Uses top-level site + frame site
*   **Safari**: Uses top-level eTLD+1
*   **Firefox**: Planning top-level scheme://eTLD+1

This means performance implications vary by browser. Safari’s approach, implemented in 2013, is the most aggressive.

Recommendations
---------------

### Immediate actions

*   Audit your domain strategy
*   Measure actual cache hit rates
*   Consider self-hosting critical resources

### Architecture updates

*   Align bundle boundaries with domain boundaries
*   Implement robust performance monitoring
*   Use resource hints strategically

### Long-term planning

*   Consider cache partitioning in architecture decisions
*   Plan for increased bandwidth costs

Do we need special considerations for well-known resources?
-----------------------------------------------------------

It is possible that the web platform may want to consider if there are novel solutions that can preserve privacy, while also enabling better cross-original resource caching for “well-known” large resources. One that comes to mind are client-side AI models which are moderate to very large in size.The impact on client-side machine learning applications could deserve special attention:

### Model loading

*   Increased loading times for models accessed across different origins
*   Higher bandwidth costs for model distribution
*   Potential impact on application initialization times

### Optimization approaches

*   Model splitting and progressive loading
*   Utilization of shared base models with differential updates
*   Implementation of model caching strategies at the application level

While I won’t go into detail about historic efforts to explore solutions here (e.g. Web Bundles, Cache Transparency), I do feel that this is a problem worth putting some more thought into beyond the patterns mentioned.

The Path forward
----------------

Cache partitioning represents a necessary evolution in web privacy, but it comes with real performance costs. The solution isn’t to fight these changes but to adapt our architectures and optimization strategies accordingly.

The web platform continues to evolve, and new APIs and patterns will emerge to help balance privacy with performance. Until then, careful domain strategy and resource management remain our best tools for optimizing performance in this new landscape.

The era of shared public CDNs might be ending, but the web’s ability to adapt and evolve continues. As always, measure, optimize, and adapt to your specific use case.

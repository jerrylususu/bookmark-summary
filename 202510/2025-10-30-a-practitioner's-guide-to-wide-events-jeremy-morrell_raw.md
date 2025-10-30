Title: A Practitioner's Guide to Wide Events | Jeremy Morrell

URL Source: https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/

Markdown Content:
Adopting Wide Event-style instrumentation has been one of the highest-leverage changes I’ve made in my engineering career. The feedback loop on all my changes tightened and debugging systems became so much easier. Systems that were scary to work on suddenly seemed a lot more manageable.

Lately there have been a lot of good blog posts on what “Wide Events” mean and why they are important. Here are some of my recent favorites:

*   [All you need is Wide Events, not “Metrics, Logs and Traces”](https://isburmistrov.substack.com/p/all-you-need-is-wide-events-not-metrics) by [Ivan Burmistrov](https://bsky.app/profile/isburmistrov.bsky.social)
*   [Observability wide events 101](https://boristane.com/blog/observability-wide-events-101/) by [Boris Tane](https://twitter.com/boristane)
*   [Is it time to version Observability? (Signs point to yes)](https://charity.wtf/2024/08/07/is-it-time-to-version-observability-signs-point-to-yes/) by [Charity Majors](https://bsky.app/profile/mipsytipsy.bsky.social)

The tl;dr is that for each unit-of-work in your system (usually, but not always an HTTP request / response) you emit one “event” with all of the information you can collect about that work. “Event” is an over-loaded term in telemetry so replace that with “log line” or “span” if you like. [They are all effectively the same thing](https://jeremymorrell.dev/blog/minimal-js-tracing/).

[Charity Majors](https://bsky.app/profile/mipsytipsy.bsky.social) has been promoting this approach lately under the name [“Observability 2.0”](https://www.honeycomb.io/blog/one-key-difference-observability1dot0-2dot0), creating some new momentum around the concept, however, it is _not_ a new idea. [Brandur Leach](https://twitter.com/brandur) wrote about “Canonical Log Lines” both on [his own blog in 2016](https://brandur.org/canonical-log-lines) and [as used by Stripe in 2019](https://stripe.com/blog/canonical-log-lines). And [AWS has recommended it as a best-practice for ages](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/#Request_log_best_practices).

Okay… I think I get the idea… but how do I do “wide events”?
------------------------------------------------------------

This is where I find a lot of developers get tripped up. The idea sounds good in theory, and we should totally try that one day! But I have this stack of features to ship, that bug that’s been keeping me up at night, and 30 new AI tools that came out yesterday to learn about. And like… where do you even start? What data should I add?

Like anything in software, there are a lot of options for how to approach this, but I’ll talk through one approach that has worked for me.

We’ll cover how to approach this in tooling and code, an **extensive** list of attributes to add, and I’ll respond to some frequent objections that come up when discussing this approach.

For this post we’ll focus on web services, but you would apply a similar approach to any workload.

Choose your tools
-----------------

We will need some way to instrument your code (traces or structured log lines) and somewhere to send the instrumentation to in order to query and visualize it.

This approach is best paired with a tool that lets you query your data in quick iterations. I like [Honeycomb](https://www.honeycomb.io/) for this, but any Observability tool backed by a modern OLAP database is likely going to work in a pinch.

*   [Honeycomb](https://www.honeycomb.io/) has [Retriever](https://www.honeycomb.io/resources/why-we-built-our-own-distributed-column-store)
*   [DataDog](https://www.datadoghq.com/) has [Husky](https://www.datadoghq.com/blog/engineering/introducing-husky/)
*   [New Relic](https://newrelic.com/) has [NRDB](https://docs.newrelic.com/docs/data-apis/get-started/nrdb-horsepower-under-hood/)
*   [Baselime](https://baselime.io/) uses [ClickHouse](https://boristane.com/talks/observability-with-clickhouse/)
*   [SigNoz](https://signoz.io/) uses [ClickHouse](https://clickhouse.com/blog/signoz-observability-solution-with-clickhouse-and-open-telemetry)

Honeycomb, New Relic, and DataDog built their own columnar [OLAP](https://aws.amazon.com/compare/the-difference-between-olap-and-oltp/) data stores, though now with the availability of [ClickHouse](https://clickhouse.com/), [InfluxDB IOx](https://www.influxdata.com/blog/influxdb-engine/), [Apache Pinot](https://pinot.apache.org/), and [DuckDB](https://duckdb.org/) there are new Observability tools popping up all the time.

If you aren’t constrained, I **highly recommend** defaulting to using [OpenTelemetry](https://opentelemetry.io/) and [Honeycomb](https://www.honeycomb.io/). Your life will be easier.

However even if you are stuck in a corporate environment with a strong allergy to technology built after 2010 you can leverage log search tools like ElasticSearch in a pinch. [Stripe](https://stripe.com/blog/canonical-log-lines)’s blog post goes over how to use Splunk for this.

In any tool you want to focus on getting proficient at 3 core techniques in order to sift through your events. The faster you are able to apply these, iterate, and ask questions of your data, the better you’ll be able to debug issues and see what your system is really doing. When observability folks refer to “slicing and dicing” data, this is what they are generally referring to. I’ll represent queries using a made-up SQL dialect, but you should be able to find equivalents in your tool’s query language.

#### Visualizing

Existing in a human body comes with its fair share of downsides, but the human visual cortex is really, really good at recognizing patterns. Give it a fighting chance by getting really good at summoning visualizations of the data your system is emitting. `COUNT`, `COUNT_DISTINCT`, `HEATMAP`, `P90`, `MAX`, `MIN`, Histogram. Learn to leverage whatever graphs your tool makes available to you. Practice it. Get fast.

![Image 1: A Honeycomb screenshot of heatmap](https://jeremymorrell.dev/_astro/heatmaps.BtFRY6ZF_62mAE.webp)

![Image 2: A Splunk screenshot of histogram](https://jeremymorrell.dev/_astro/splunk-histogram.DyaarE-V_Z1mfvv5.webp)

#### Grouping

With each new annotation that we add to our wide events, we create another dimension along which we can slice our data. `GROUP BY` allows us to look along that dimension and see if the values along that dimension match our expectations.

`GROUP BY instance.id``GROUP BY client.OS, client.version`
#### Filtering

Once we’ve narrowed in one dimension that is interesting, we usually want to dig further into that data. Filtering down so that we’re only looking at data from one endpoint, or from one IP address, or sent by the iOS app, or only from users with a specific feature flag turned on allows us to narrow our focus to a very specific segment of traffic.

`WHERE http.route = "/user/account"``WHERE http.route != "/health"``WHERE http.user_agent_header contains "Android"`
Write a middleware to help you
------------------------------

If you are using an OpenTelemetry SDK it is already creating a wrapping span around the request and response. You can access it by asking for the active span at any point during the processing of the request.

```
let span = opentelemetry.trace.getActiveSpan();
span.setAttributes({
  "user_agent.original": c.req.header("User-Agent"),
});
```

However if anyone wraps any of your code in a child span the “active span” will change to be that new wrapping span! There is no first-class way of addressing this original “main” span in OpenTelemetry. However, we can work around this by saving a reference to this specific span in the [context](https://opentelemetry.io/docs/specs/otel/context/) so we can always have access to the “main” wrapping span.

```
// create a reference to store the span on the opentelemetry context object
const MAIN_SPAN_CONTEXT_KEY = createContextKey("main_span_context_key");

function mainSpanMiddleware(req, res, next) {
  // pull the active span created by the http instrumentation
  let span = trace.getActiveSpan();

  // get the current context
  let ctx = context.active();

  // set any attributes we always want on the main span
  span.setAttribute("main", true);

  // OpenTelemetry context is immutable, so to modify it we create
  // a new version with our span added
  let newCtx = ctx.setValue(MAIN_SPAN_CONTEXT_KEY, span);

  // set that new context as active for the duration of the request
  context.with(newCtx, () => {
    next();
  });
}

// create another function that allows you to annotate this saved span easily
function setMainSpanAttributes(attributes) {
  let mainSpan = context.active().getValue(MAIN_SPAN_CONTEXT_KEY);
  if (mainSpan) {
    mainSpan.setAttributes(attributes);
  }
}
```

Now our annotation code can look a little simpler, and we can always know that we’re setting these attributes on the wrapping span.

```
setMainSpanAttributes({
  "user.id": "123",
  "user.type": "enterprise",
  "user.auth_method": "oauth",
});
```

You can play around with a minimal running example [here](https://github.com/jmorrell/a-practitioners-guide-to-wide-events/tree/main/opentelemetry-js-example).

At Heroku we had internal [OpenTelemetry Distributions](https://opentelemetry.io/docs/concepts/distributions/) that set this up for you automatically and added as many automatic annotations as possible to these spans.

If you are not using OpenTelemetry [here’s a gist that might help you get started](https://gist.github.com/jmorrell/76a9ee631370e073d6e2616dc1f67feb). [My previous post](https://jeremymorrell.dev/blog/minimal-js-tracing/) may help you put this logic together.

What do I add to this “main” span?
----------------------------------

We need to add attributes about the request, and there are likely far more of these than you would expect. It’s easy to come up with a dozen or so, but in a well-instrumented code base there will be hundreds of attributes.

Note that while this is a long list, it is definitely not exhaustive. OpenTelemetry defines sets of attribute names as [Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) that can also be used for inspiration. I have tried to follow these in my naming where possible.

### A convention to filter out everything else

Traces contain lots of spans, so it’s helpful to have a convention for identifying and searching for these “wide events”. `root` and `canon` were floated as options, but I’ve landed on calling them `main` spans.

| Attribute | Examples | Description |
| --- | --- | --- |
| `main` | `true` | Present only for spans designated as a “wide event”, usually wrapping a request / response, or a background job |

This convention allows you to quickly figure out “what does the traffic to this service look like?” with a single query:

```
SELECT
  COUNT(*)
WHERE
  main = true
GROUP BY http.route
```

![Image 3: Graph of traffic grouped by route over a week. There is an anomally.](https://jeremymorrell.dev/_astro/traffic-by-route.Bvy3b1dc_1WkGye.webp)

### Service metadata

Of course we need to add some information about the service we’re running. Consider adding additional metadata about which team owns the system, or which Slack channel the owning team hangs out in, though note that this can be tedious to update if your workplace experiences frequent re-orgs. Tying these to a service catalog like [Backstage](https://backstage.io/) is left as an exercise to the reader.

| Attribute | Examples | Description |
| --- | --- | --- |
| `service.name` | `api` `shoppingcart` | What is the name of this service? |
| `service.environment` | `production` `staging` `development` | Where is this service running? |
| `service.team` | `web-services` `dev-ex` | Which team owns this service. Useful for knowing who to page in during incidents. |
| `service.slack_channel` | `web-services` `dev-ex` | If I discover an issue with this service, where should I reach out? |

> How many services does each team run?

```
SELECT
  COUNT_DISTINCT(service.name)
WHERE
  service.environment = "production"
GROUP BY service.team
```

Ever look at the load on a system and then wonder “Is that appropriate for the machine this is running on?”, and now you have to look through other tools or config files to get that information. Throw that context on the wide event so that it’s available when you need it.

| Attribute | Examples | Description |
| --- | --- | --- |
| `instance.id` | `656993bd-40e1-4c76-baff-0e50e158c6eb` | An ID that maps to this one instance of the service |
| `instance.memory_mb` | `12336` | How much RAM is available to this service? |
| `instance.cpu_count` | `4` `8` `196` | How many cores are available to this service? |
| `instance.type` | `m6i.xlarge` | Does your vendor have a name for this type of instance? |

> What are the services with the most memory that we run? What instance types do they use?

```
SELECT
  service.name,
  instance.memory_mb,
  instance.type
ORDER BY instance.memory_mb DESC
GROUP BY service.name, instance.type
LIMIT 10
```

However you’re orchestrating your systems make sure that all of the relevant information is added. I’ve included some examples from [the Kubernetes semantic conventions](https://opentelemetry.io/docs/specs/semconv/resource/k8s/) for inspiration.

| Attribute | Examples | Description |
| --- | --- | --- |
| `container.id` | `a3bf90e006b2` | An ID used to identify Docker containers |
| `container.name` | `nginx-proxy` `wordpress-app` | Container name used by container runtime |
| `k8s.cluster.name` | `api-cluster` | Name of the kubernetes cluster your service is running in |
| `k8s.pod.name` | `nginx-2723453542-065rx` | Name of the kubernetes pod your service is running in |
| `cloud.availability_zone` | `us-east-1c` | AZ where you’re running your service |
| `cloud.region` | `us-east-1` | Region where you’re running your service |

But even if you’re using a Platform-as-a-Service you can still pull out a lot of useful information!

| Attribute | Examples | Description |
| --- | --- | --- |
| `heroku.dyno` | `web.1` `worker.3` | The env var `DYNO` that is set on your app at runtime |
| `heroku.dyno_type` | `web` `worker` | The first part of the `DYNO` env var before the `.`. Separating this makes it easier to query |
| `heroku.dyno_index` | `1` `3` | The second part of the `DYNO` env var after the `.`. Separating this makes it easier to query |
| `heroku.dyno_size` | `performance-m` | The selected dyno size |
| `heroku.space` | `my-private-space` | The name of the private space that your are deployed into |
| `heroku.region` | `virginia` `oregon` | Which region is this app located in? |

> How many dynos are we running? What dyno types are they? For which services?

```
SELECT
  COUNT_DISTINCT(heroku.dyno_index)
GROUP BY service.name, heroku.dyno_type, instance.type
```

### Build info

Inevitably some of the first questions asked in any incident are “Did something just go out?” or “What changed?”. Instead of jumping to your deployment tool or looking through GitHub repositories, add that data to your telemetry.

Threading this data from your build system through to your production system so that it’s available at runtime can be a non-trivial amount of glue code, but having this information easily available during incidents is invaluable.

| Attribute | Examples | Description |
| --- | --- | --- |
| `service.version` | `v123` `9731945429d3d083eb78666c565c61bcef39a48f` | However you track your version, ex: a version string or a hash of the built image |
| `service.build.id` | `acd8bb57-fb9f-4b2d-a750-4315e99dac64` | If your build system gives you an ID, this context allows you to audit the build if something goes wrong |
| `service.build.git_hash` | `6f6466b0e693470729b669f3745358df29f97e8d` | The git SHA of the deployed commit so you can know exactly which code was running |
| `service.build.pull_request_url` | `https://github.com/your-company/api-service/pull/121` | The url of the pull request that was merged that triggered the deploy |
| `service.build.diff_url` | `https://github.com/your-company/api-service/compare/c9d9380..05e5736` | A url that compares the previously deployed commit against the newly deployed commit |
| `service.build.deployment.at` | `2024-10-14T19:47:38Z` | Timestamp when the deployment process started |
| `service.build.deployment.user` | `keanu.reeves@your-company.com` | Which authenticated user kicked off the build? Could be a bot |
| `service.build.deployment.trigger` | `merge-to-main` `slack-bot` `api-request` `config-change` | What triggered the deploy? Extremely valuable context during an deploy-triggered incident |
| `service.build.deployment.age_minutes` | `1` `10230` | How old is this deploy? Shortcuts the frequent incident question “Did something just go out?” |

**Won’t this be a lot of repetitive data?** These values do not change except between deploys! See [Frequent Objections](https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/#frequent-objections)

> What systems have recently been deployed?

```
SELECT
  service.name,
  MIN(service.build.deployment.age_minutes) as age
WHERE
  service.build.deployment.age_minutes < 20
GROUP BY service.name
ORDER BY age ASC
LIMIT 10
```

> What’s up with the spike of 500s when we did the last deploy?

```
SELECT
  COUNT(*)
WHERE
  service.name = "api-service" AND
  main = true
GROUP BY http.status_code, service.version
```

![Image 4: Graph showing requests grouped by http status code and version. There is a spike of 500s correlating to v1 shutting down.](https://jeremymorrell.dev/_astro/group-by-http-and-status.tDSRPVAz_Z2u1s5X.webp)

### HTTP

You should get most of these from your tracing library instrumentation, but there are usually more you can add if, for example, your organization uses non-standard headers. Don’t settle for only what OpenTelemetry gives you by default!

| Attribute | Examples | Description |
| --- | --- | --- |
| `server.address` | `example.com` `localhost` | Name of the HTTP server that received the request |
| `url.path` | `/checkout` `/account/123/features` | URI path after the domain |
| `url.scheme` | `http`, `https` | URI scheme |
| `url.query` | `q=test`, `ref=####` | URI query component |
| `http.request.id` | `79104EXAMPLEB723` | Platform request id: ex: `x-request-id`, `x-amz-request-id` |
| `http.request.method` | `GET` `PUT` `POST` `OPTIONS` | HTTP request method |
| `http.request.body_size` | `3495` | Size of the request payload body in bytes |
| `http.request.header.content-type` | `application/json` | Value of a specific request header, “content-type” in this case, but there are many more. Pick out any that are important for your service |
| `http.response.status_code` | `200` `404` `500` | HTTP response status code |
| `http.response.body_size` | `1284` `2202009` | Size of the response payload body in bytes |
| `http.request.header.content-type` | `text/html` | Value of a specific response header, “content-type” in this case, but there are many more. Pick out any that are important for your service |

```
SELECT
  HEATMAP(http.response.body_size),
WHERE
  main = true AND
  service.name = "api-service"
```

![Image 5: A heatmap of response sizes. Most are within a fixed band, but there are sharp outliers that warrant more investigation.](https://jeremymorrell.dev/_astro/http-body-size-annotated.BXCOh_iU_2jiDIv.webp)

`User-Agent` headers contain a wealth of info. Don’t rely on regex queries to try and make sense of them down the road. Parse them into structured data from the beginning.

| Attribute | Examples | Description |
| --- | --- | --- |
| `user_agent.original` | `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.3` | The value of the HTTP `User-Agent` header |
| `user_agent.device` | `computer` `tablet` `phone` | Device type derived from the `User-Agent` header |
| `user_agent.OS` | `Windows` `MacOS` | OS derived from the `User-Agent` header |
| `user_agent.browser` | `Chrome` `Safari` `Firefox` | Browser derived from the `User-Agent` header |
| `user_agent.browser_version` | `129` `18.0` | Browser version derived from the `User-Agent` header |

> What browsers are my users using?

```
SELECT
  COUNT(*)
GROUP BY user_agent.browser, user_agent.browser_version
```

If you have any custom user agents or headers used as a convention within your org parse that out too.

| Attribute | Examples | Description |
| --- | --- | --- |
| `user_agent.service` | `api-gateway` `auth-service` | If you have a distributed architecture, have each service send a custom `User-Agent` header with its name and version |
| `user_agent.service_version` | `v123` `6f6466b0e693470729b669f3745358df29f97e8d` | If you have a distributed architecture, have each service send a custom `User-Agent` header with its name and version |
| `user_agent.app` | `iOS` `android` | If a request is coming from a mobile app, make sure it includes which app and its version |
| `user_agent.app_version` | `v123` `6f6466b0e693470729b669f3745358df29f97e8d` | If a request is coming from a mobile app, make sure it includes which app and its version |

### Route info

We’re not done with HTTP attributes yet! One of the most important bits is the API endpoint that the request matched. OpenTelemetry SDKs will _usually_ give this to you automagically but not always. Consider extracting the route parameters and query parameters as additional attributes.

| Attribute | Examples | Description |
| --- | --- | --- |
| `http.route` | `/team/{team_id}/user/{user_id}` | The route pattern that the url path is matched against |
| `http.route.param.team_id` | `14739` `team-name-slug` | The extracted segment of the url path as it is parsed for each parameter |
| `http.route.query.sort_dir` | `asc` | The query parameters that are relevant to the response of your service. Ex: `?sort_dir=asc&...` |

```
SELECT
  P99(duration_ms)
WHERE
  main = true AND
  service.name = "api-service"
GROUP BY http.route
```

![Image 6: A chart of p99&#x27;s broken down by route. There is a spike on only some of them. We should break down by version now to check if this was caused by a deploy.](https://jeremymorrell.dev/_astro/p99-duration-annotated.BXlgufk3_Z5vCb5.webp)

### User and customer info

Once you get the basics down, this is **the most important** piece of metadata that you can add. No automagic SDK will be able to encode the particulars of your user model.

It’s common for a single user or account to be responsible for a 10%+ of a business’ revenue, and frequently their usage patterns look significantly different than the average user. They probably have more users, store more data, and hit limits and edge-cases that will never show up for the user paying $10 / month. Be sure you can separate their traffic from others.

| Attribute | Examples | Description |
| --- | --- | --- |
| `user.id` | `2147483647` `user@example.com` | The primary ID for a user. If this is an email and you’re using a vendor, consider your org’s policy on putting PII in external services. |
| `user.type` | `free` `premium` `enterprise` `vip` | How does the business see this type of user? Individual accounts are sometimes responsible for 10%+ of a business’ income. Make sure you can separate their traffic from others! |
| `user.auth_method` | `token` `basic-auth` `jwt` `sso-github` | How did this user authenticate into your system? |
| `user.team.id` | `5387` `web-services` | If you have a team construct, which one does this user belong to? |
| `user.org.id` | `278` `enterprise-name` | If this user is part of an organization with an enterprise contract, track that! |
| `user.age_days` | `0` `637` | Not the user’s literal age, but how long ago was this account created? Is this an issue experienced by someone new to your app, or only once they’ve saved a lot of data? |
| `user.assumed` | `true` | Have an internal way of assuming a user’s identity for debugging? Be sure to track this |
| `user.assumed_by` | `engineer-3@your-company.com` | And track which actual user is assuming the user’s identity |

```
SELECT
  P99(duration_ms)
WHERE
  main = true AND
  service.name = "api-service"
GROUP BY user.type
```

### Rate limits

Whatever your rate limiting strategy, make sure the current rate limit info gets added too. Can you quickly find examples of users that are being rate-limited by your service?

| Attribute | Examples | Description |
| --- | --- | --- |
| `ratelimit.limit` | `200000` | You might not now, but you will likely have users with different rate limits in the future, note down what the actual limit is for this request |
| `ratelimit.remaining` | `130000` | What is the budget remaining for this user? |
| `ratelimit.used` | `70000` | How many requests have been used in the current rate window |
| `ratelimit.reset_at` | `2024-10-14T19:47:38Z` | When will the rate limit be reset next? if applicable |

> This user has a support ticket open about being rate-limited. Let’s see what they were doing

```
SELECT
  COUNT(*)
WHERE
  main = true AND
  service.name = "api-service" AND
  user.id = 5838
GROUP BY http.route
```

![Image 7: A graph of one users activity. There is a big spike hitting the same route a lot at the end. This gives us a starting point for investigation](https://jeremymorrell.dev/_astro/rate-limit-investigation-annotated.DGJPVuPW_Z1dkIip.webp)

> What routes are users who have burned most of their rate limit hitting? Does this activity look suspicious?

```
SELECT
  COUNT(*)
WHERE
  main = true AND
  service.name = "api-service" AND
  ratelimit.remaining < 100
GROUP BY http.route
```

### Caching

For every code path where we could shortcut with a cache response, add whether or not it was successful

| Attribute | Examples | Description |
| --- | --- | --- |
| `cache.session_info` | `true` `false` | Was the session info cached or did it need to be re-fetched? |
| `cache.feature_flags` | `true` `false` | Were the feature flags cached for this user or did they need to be re-fetched? |

### Localization info

What localization options has the user chosen? This can be a frequent source of bugs

| Attribute | Examples | Description |
| --- | --- | --- |
| `localization.language_dir` | `rtl`, `ltr` | Which direction is text laid out in their language? |
| `localization.country` | `mexico`, `uk` | Which country are they from? |
| `localization.currency` | `USD`, `CAD` | Which currency have they chosen to work with? |

### Uptime

Tracking how long the service has been running when it serves a request can help you visualize several classes of bugs:

*   Issues that show up on a reboot
*   Memory leaks that only start to show up when the service has been running for a long time
*   Frequent crashes / restarts if you have automatically restart the service on failure

I recommend also either adding the `log10` of the uptime or having some way of visualizing this. When graphed this emphasizes the important first few minutes of a service without being squished into the bottom of the graph by instances with several days or more of uptime.

| Attribute | Examples | Description |
| --- | --- | --- |
| `uptime_sec` | `1533` | How long has this instance of your app been running? Can be useful to visualize to see restarts |
| `uptime_sec_log_10` | `3.185` | Grows sub-linearly which allows you to visualize long-running services and brand new ones on the same graph |

```
SELECT
  HEATMAP(uptime_sec),
  HEATMAP(uptime_sec_log_10)
WHERE
  main = true AND
  service.name = "api-service"
```

![Image 8: Heatmaps of uptime when a service enters a crash loop. It&#x27;s far easier to distinguish in log scale](https://jeremymorrell.dev/_astro/uptime.CJbFmMOT_qyEHN.webp)

### Metrics

This one might be a bit controversial, but I’ve found it helpful to tag spans with context about what the system was experiencing while processing the request. We fetch this information every ~10 seconds, cache it, and add it to every main span produced during that time.

Capturing metrics in this way is not mathematically sound. Since you only get data when traffic is flowing, you can’t calculate a `P90` for cpu load that would stand up to any rigorous scrutiny, but that’s actually fine in practice. It’s close enough to get some quick signal while you’re debugging without switching to a different tool, especially if you can avoid calculations and visualize with a heatmap.

I wouldn’t recommend setting alerts on this data though. Plain ol’ metrics are great for that.

[Jessica Kerr](https://jessitron.com/) recently wrote about this approach on the [Honeycomb Blog](https://www.honeycomb.io/blog/get-infinite-custom-metrics-for-free).

| Attribute | Examples | Description |
| --- | --- | --- |
| `metrics.memory_mb` | `153` `2593` | How much memory is being used by the system at the time its service this request |
| `metrics.cpu_load` | `0.57` `5.89` | CPU load of the system service this request. Given as # of active cores |
| `metrics.gc_count` | `5390` | Last observed number of garbage collections. Could be cumulative (total since service started) or delta (ex: number in the last minute) |
| `metrics.gc_pause_time_ms` | `14` `325` | Time spent in garbage collections. Could also be cumulative or delta. Pick one and document which |
| `metrics.go_routines_count` | `3` `3000` | Number of go routines running |
| `metrics.event_loop_latency_ms` | `0` `340` | Cumulative time spent waiting on the next event loop tick. An important metric for Node apps |

> Are these requests getting slow because we’re running out of memory or CPU?

```
SELECT
  HEATMAP(duration_ms),
  HEATMAP(metrics.memory_mb),
  HEATMAP(metrics.cpu_load)
WHERE
  main = true AND
  service.name = "api-service"
GROUP BY instance.id
```

![Image 9: An example showing using the metrics data tagged on the span to get context for whats happening with the system](https://jeremymorrell.dev/_astro/metrics.BHs4tp2f_NKdey.webp)

### Async request summaries

When using a tracing system async requests should get their own spans, but it can still be useful to roll up some stats to identify outliers and quickly find interesting traces.

| Attribute | Examples | Description |
| --- | --- | --- |
| `stats.http_requests_count` | `1` `140` | How many http requests were triggered during the processing of this request? |
| `stats.http_requests_duration_ms` | `849` | Cumulative time spent in these http requests |
| `stats.postgres_query_count` | `7` `742` | How many Postgres queries were triggered during the processing of this request? |
| `stats.postgres_query_duration_ms` | `1254` | Cumulative time spent in these Postgres queries |
| `stats.redis_query_count` | `3` `240` | How many redis queries were triggered during the processing of this request? |
| `stats.redis_query_duration_ms` | `43` | Cumulative time spent in these redis queries |
| `stats.twilio_calls_count` | `1` `4` | How many calls to this vendors api were triggered during the processing of this request? |
| `stats.twilio_calls_duration_ms` | `2153` | Cumulative time spent in these vendor calls |

> Surely my service makes a reasonable number of calls to the database… right?

```
SELECT
  HEATMAP(stats.postgres_query_count)
WHERE
  main = true AND
  service.name = "api-service"
```

![Image 10: A heatmap of db queries per request. There is a bi-modal distribution but also some outliers that make a lot of requests](https://jeremymorrell.dev/_astro/postgres-queries.BANqR6rQ_Z1l5Hzm.webp)

**Instead of adding this explicitly, couldn’t we aggregate this by querying the whole trace?** See [Frequent Objections](https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/#frequent-objections)

### Sampling

Once you start collecting fine-grained telemetry from your systems at a significant scale you run head-on into the problem of sampling. Running systems can produce a lot of data! Engineers frequently want to store and query all of it. Exact answers always! Make it fast! Also cheap! But it’s trade-offs all the way down. Telemetry data is fundamentally different from the transaction data you’re storing for your users, and you should think about it differently.

Luckily you only really need a statistically significant subset of the full dataset. Even sampling 1 out of every 1000 requests can provide a suprisingly detailed picture of the overall traffic patterns in a system.

Sampling is a suprisingly deep topic. Keep it simple if you’re starting and do uniform random head sampling, but track your sample rate per-span so y
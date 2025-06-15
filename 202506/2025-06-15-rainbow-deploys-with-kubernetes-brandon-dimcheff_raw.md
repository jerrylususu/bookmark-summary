Title: Rainbow Deploys with Kubernetes

URL Source: https://brandon.dimcheff.com/2018/02/rainbow-deploys-with-kubernetes/

Published Time: 2018-02-13T08:50:50-05:00

Markdown Content:
or: how you can deploy services to Kubernetes that require long periods of draining.
------------------------------------------------------------------------------------

🌈 🌈 🌈
--------

If you want to jump directly to the technical solution, check out the [project repo](https://github.com/bdimcheff/rainbow-deploys). Below is a short story about how we got to this solution.

🌈 🌈 🌈
--------

In an ideal cloud native world, your services will be stateless so deploys and restarts aren’t disruptive. Unfortunately in the real world, sometimes you have stateful services and can’t realistically turn them stateless.

At [Olark](https://www.olark.com/?rid=brandon), the service that powers chat.olark.com is stateful. Each user’s browser establishes a websockets connection to the backend, which in turn establishes an XMPP connection to our XMPP server. If a backend service instance goes away, all the users who have established XMPP connections via that server will be disconnected and will have to reconnect. While that’s not the end of the world, it’s not a great experience. Also, if it happens to everybody at once, it causes a huge load spike. If we deploy to Kubernetes the traditional way, the rolling deploy will restart all backends, which will cause all logged-in users to reconnect. We had to find a better way.

The old way
-----------

Before chat.olark.com was running in Kubernetes, we used [up](https://github.com/olark/up), which would fork new workers each time new code was deployed. This is a common idiom for no-downtime deploys in a variety of languages. We could deploy as often as we want, and the old workers could stick around for a couple days to serve the existing XMPP connections. Once the users had (mostly) switched to the new backend, up would clean up the old workers. We couldn’t do the same thing inside of a container without a ton of trickery and hacks. Containers are meant to be immutable once they’re deployed, and hot-loading code is simply not advised.

First try
---------

Our first attempt to solve this problem was effectively to port “the old way” to use Kubernetes primitives. We used [service-loadbalancer](https://github.com/kubernetes/contrib/tree/master/service-loadbalancer) to stick sessions to backends and we turned up the [`terminationGracePeriodSeconds`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#podspec-v1-core) to several hours. This appeared to work at first, but it turned out that we lost a lot of connections before the client closed the connection. We decided that we were probably relying on behavior that wasn’t guaranteed anyways, so we scrapped this plan.

Blue/Green Deploys
------------------

Our second thought was to build a [Blue/Green](https://martinfowler.com/bliki/BlueGreenDeployment.html) deployment in Kubernetes. It’s a fairly common strategy outside of Kube, and isn’t that hard to implement. We would have 2 Deployments, lets call them `chat-olark-com-blue` and `chat-olark-com-green`. When you want to deploy, you just roll out the least-recently-deployed and switch the Service to point at that Deployment once it’s healthy. Rolling back is easy: just switch the service back to the other color. There is a downside: with only two colors, we can only deploy about once per day. It takes 24-48h for connections to naturally burn down, and we don’t want to force too many reconnects. This means that every time we use one of the deployments, we need to wait at least a day before we deploy to the other one.

But wait! We’re in Kubernetes, so lets just make a ton of colors! We have all of ROY-G-BIV to work with here, so lets go crazy. This strategy is fine in principle, but managing a bunch of static deployment colors is cumbersome. Plus, each deployment currently requires 16 pods, so running enough to allow us to deploy 4x/day means we need 8 colors (4 per day, plus a day delay) and we’ll be running 128 (2G, 1CPU) pods all the time, even if we only deploy once all week. There’s gotta be a better way!

🌈 Rainbow Deploys 🌈
---------------------

It turns out that we were almost there with the original Rainbow Deploy idea. The key was simple: instead of using fixed colors, we used git hashes. Instead of a Deployment called `chat-olark-com-$COLOR` we deploy `chat-olark-com-$SHA`. As a bonus, since the first six characters of a git sha are also a valid hex color, the name still makes sense. You might even find a new favorite color!

Using this technique, a deploy goes like this:

*   Create a new deployment with the pattern `chat-olark-com-$NEW_SHA`.
*   When the pods are ready, switch the service to point at `chat-olark-com-$NEW_SHA`. 
    *   If you need to roll back, point the service back at `chat-olark-com-$OLD_SHA`.

*   Once connections have burned down, delete the old deployment. 
    *   Any of the (few) remaining users will reconnect to a newer backend.

I made a **[demo repo](https://github.com/bdimcheff/rainbow-deploys)** to showcase how this works.

We’ve been deploying chat.olark.com this way since June, 2017 via Gitlab pipelines. This deployment strategy has been far easier to use and far more reliable than our previous deployments. One day we will hopefully be able to avoid connection draining, but this has proved to be a step in the right direction.

Clean up
--------

We still have one unsolved issue with this deployment strategy: how to clean up the old deployments when they’re no longer serving (much) traffic. So far we haven’t found a good way of detecting a lightly used deployment, so we’ve been cleaning them up manually every once in a while. The idea is to wait until the number of connections are low enough that it will be minimally disruptive. It would be nice to automate this, but it’s actually somewhat difficult to detect when the time is right. Hopefully this will be a future post.

The future
----------

I would love to see something like this end up as a native [Deployment Strategy](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy). It ought to be possible to make an `Immutable` deployment method where pods only get created but the old ones aren’t destroyed immediately. It’d be even better if there were some way to define when old pods would be cleaned up. A lifecycle hook or signal may suffice here, to indicate to the pod when it’s no longer receiving production traffic and should shut down when ready.

🌈
--

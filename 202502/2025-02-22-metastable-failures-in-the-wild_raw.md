Title: Metastable failures in the wild

URL Source: http://muratbuffalo.blogspot.com/2023/09/metastable-failures-in-wild.html

Published Time: 2023-09-12T15:37:00-04:00

Markdown Content:
Metastable failures in the wild
===============  

[Skip to main content](http://muratbuffalo.blogspot.com/2023/09/metastable-failures-in-wild.html#main)

[](https://muratbuffalo.blogspot.com/)

### Search This Blog

[Metadata](https://muratbuffalo.blogspot.com/)
==============================================

On distributed systems broadly defined and other curiosities. The opinions on this site are my own.

### Metastable failures in the wild

*   Get link
*   Facebook
*   X
*   Pinterest
*   Email
*   Other Apps

\-  [September 12, 2023](https://muratbuffalo.blogspot.com/2023/09/metastable-failures-in-wild.html "permanent link")

[This paper appeared in OSDI'22.](https://www.usenix.org/system/files/osdi22-huang-lexiang.pdf) There is [a great summary of the paper](http://charap.co/metastable-failures-in-the-wild/) by Aleksey (one of the authors and my former PhD student, go Aleksey!). There is also [a great conference presentation video](https://www.usenix.org/conference/osdi22/presentation/huang-lexiang) from Lexiang.  
  
  
Below I will provide a brief overview of the paper followed by my discussion points. This topic is very interesting and important, so I hope you have fun learning about this.

Metastability concept and categories
====================================

Metastable failure is defined as permanent overload with low throughput even after the fault-trigger is removed. It is an emergent behavior of a system, and it naturally arises from the optimizations for the common case that lead to sustained work amplification.

[![Image 7](https://blogger.googleusercontent.com/img/a/AVvXsEj4n8MXqt-hIp6UqezaEWaf3mfFmnZhkA-FXZerR0Qkf-GRpflcSlBwdsXtd6rMyJWkd2VnKZUx9rUIAl3Yj6dLTUfPOh264HCIUAFxFs0lt48ubaDlrjwihvGkVQ09Tt66rhKgUQZl4EeWsT8R1zan-vY-YBfGX1vkHcObcGsraJ3SFagYcL3lLlC1QtU)](https://blogger.googleusercontent.com/img/a/AVvXsEj4n8MXqt-hIp6UqezaEWaf3mfFmnZhkA-FXZerR0Qkf-GRpflcSlBwdsXtd6rMyJWkd2VnKZUx9rUIAl3Yj6dLTUfPOh264HCIUAFxFs0lt48ubaDlrjwihvGkVQ09Tt66rhKgUQZl4EeWsT8R1zan-vY-YBfGX1vkHcObcGsraJ3SFagYcL3lLlC1QtU)

  
In this paper, the authors are able to capture/abstract the system behavior of interest in terms of two parameters, the load and capacity. If the load is above capacity, you have work piling up, right? Or if the capacity drops under the sustained load level, the same effect, right? Both of these create  a temporary pile up, and grows the queues. Hopefully this queue is going to decrease as the system catches up and you'll be good. But metastable failure is when this temporary pile up becomes permanent, and you don't get back to the stable state even after the original triggering event is removed. In other words, you get stuck in a metastable state/attractor and you are not able to get back to your big attractor, your stable/homeostasis state. ([The term metastability comes from physics](https://en.wikipedia.org/wiki/Metastability).) This leads to bad performance and unavailability because your system is grinding but not doing useful work. It is doing busy-work without sufficient goodput.  
  

[![Image 8](https://blogger.googleusercontent.com/img/a/AVvXsEgBwDZxpwjLsXi7X1hH_Q1BEbsK_lvEsQtkZX_Dg7F6lsteH9nSyyaDpjNA-31NyA09qyqpg8iq3gXf1MkrbcCrtB81ZAff_oyVflU4_xejp3yUnOLUtV7xF8GU7Eba3FbQMrxTCgEEdsQMuJWIRjP_xh0yVStriy2v4se97jd8UYuBhbWYZFLegtFo4Zk=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgBwDZxpwjLsXi7X1hH_Q1BEbsK_lvEsQtkZX_Dg7F6lsteH9nSyyaDpjNA-31NyA09qyqpg8iq3gXf1MkrbcCrtB81ZAff_oyVflU4_xejp3yUnOLUtV7xF8GU7Eba3FbQMrxTCgEEdsQMuJWIRjP_xh0yVStriy2v4se97jd8UYuBhbWYZFLegtFo4Zk)

  
Figure 1 explores possible metastability categories, capturing them in four quadrants. Again, this is all about load and capacity. And we have two axes: x-axis is the triggering factor (either load increase or capacity decrease), and the y-axis is the sustaining factor (either load increase or capacity decrease). The combination results in the four quadrants.  
  
The top-left quadrant is when a load-spike triggered the event, and created the temporary overload, and then timeout requests did retries and sustained the effect through load amplification again.  
  
The top-right category is where the trigger is a capacity drop, and sustaining effect is workload increase. An example could be from a replicated state machine with Raft. Initially, the primary has a lapse/glitch and gets behind in processing requests. Then the followers keep retrying the pull, and this increases the load and sustains the metastable state of reduced goodput.  
  
The bottom-left category is where the trigger comes from load-increase and sustaining effect comes from capacity decrease. They show/replicate this via an actual subsystem in Twitter, where the garbage collection kicks in due to quickly increased queue lengths, and degrades the performance of the system, and the system is stuck in the metastability rut without ever getting back to the normal stability state.  
  
Finally, the bottom-right category is where the trigger comes from a capacity drop (say your cache is wiped out, and your serving capacity decreased) and the sustaining effect also comes from capacity drop (your database is overwhelmed by the sudden herd effect due to cache misses, and times out serving requests, and is not able to repopulate the cache). [Marc Brooker had a great post about this in 2021.](https://brooker.co.za/blog/2021/08/27/caches.html)  
  
  
The paper has a very nice evaluation section, where they replicate each of these categories by controlling the trigger duration/size and show the sustaining effect kicking in and keeping the system in metastable state until manual intervention happens. They are able to identify a stable region, vulnerable region, and thee metastable region, and often with a thin um margin, as shown in Figure 5. Also checkout 4.c and 6.c. These are impressive to witness! (The code is available at [https://github.com/lexiangh/Metastability](https://github.com/lexiangh/Metastability))  
  

[![Image 9](https://blogger.googleusercontent.com/img/a/AVvXsEhV-WQrVUaN03t0uRjTo9h9k276KUocrWAR4e9qvVDSyhGI3mgkn-pLKLvNxpssPxLgHFxeciQJjTBKiJH7B04nbomUWZzbEavDZGzyLIEib6t-hMIntxZd0kCZObeN99F-35buRoWo39tbvAPGs2geYy8xd6lwxhmpSQAKtcDFqZyLarH13nn6fIm30i8=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhV-WQrVUaN03t0uRjTo9h9k276KUocrWAR4e9qvVDSyhGI3mgkn-pLKLvNxpssPxLgHFxeciQJjTBKiJH7B04nbomUWZzbEavDZGzyLIEib6t-hMIntxZd0kCZObeN99F-35buRoWo39tbvAPGs2geYy8xd6lwxhmpSQAKtcDFqZyLarH13nn6fIm30i8)

  
  

[![Image 10](https://blogger.googleusercontent.com/img/a/AVvXsEjfxa6gmjBEvOq_N09d4cwipBjs9fgVTVyBKOJuT3iO2DWc-DAI5-QDdiEbtZNvsn36y2dxcXwxOrvE4iFF4IJY-YtQecTpFUOst-acVt-_cdOykwYIuW30e0KNnx4xubtaf48r4WuDqIlcTJsBbBvIUYTe9EN6ZlUcnexaFgaEgDVeBQeH2gnI7UyxjXU=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEjfxa6gmjBEvOq_N09d4cwipBjs9fgVTVyBKOJuT3iO2DWc-DAI5-QDdiEbtZNvsn36y2dxcXwxOrvE4iFF4IJY-YtQecTpFUOst-acVt-_cdOykwYIuW30e0KNnx4xubtaf48r4WuDqIlcTJsBbBvIUYTe9EN6ZlUcnexaFgaEgDVeBQeH2gnI7UyxjXU)

  
  

[![Image 11](https://blogger.googleusercontent.com/img/a/AVvXsEi3rB45Qc6ak8E5rPDvq0RpkszhzKMlI7lbXcWabziYdVQGN03IVFlFuDotQqg2rbCSrS-QoGjNu7tr-Hux53FylLnM4eff8CrjWeEpNgku9AQD6ZH3CUIGmr2EKl7VGslc26oSMk5w04OTftCDThoXphDfCQlt_uWWmnk3JfU9dMst38n3gWUxdI6NMMo=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEi3rB45Qc6ak8E5rPDvq0RpkszhzKMlI7lbXcWabziYdVQGN03IVFlFuDotQqg2rbCSrS-QoGjNu7tr-Hux53FylLnM4eff8CrjWeEpNgku9AQD6ZH3CUIGmr2EKl7VGslc26oSMk5w04OTftCDThoXphDfCQlt_uWWmnk3JfU9dMst38n3gWUxdI6NMMo)

  

Metastability induced outages in real world
===========================================

The paper looks at 600 public postmortem incident reports at many companies, big and small, and identifies 21 metastable outages as shown in Table 1.

[![Image 12](https://blogger.googleusercontent.com/img/a/AVvXsEgunpoxcP9w4OT7Mwlmr4MTMPme81LIP8Gygpj-m2qqtywsI8czq5KHKfcCAj-nONyo-ASP1Bu_CGJnpzaqIrnwnQ7PkfJUaRViBoS2opnuUkXSjr95Ca-mFkuGVhhpYb1LKRWGafRtDJq44QIXIqQt3URXYDtkoL2CV9_fJROQASO8G_TGLKl-IB2p90Q=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgunpoxcP9w4OT7Mwlmr4MTMPme81LIP8Gygpj-m2qqtywsI8czq5KHKfcCAj-nONyo-ASP1Bu_CGJnpzaqIrnwnQ7PkfJUaRViBoS2opnuUkXSjr95Ca-mFkuGVhhpYb1LKRWGafRtDJq44QIXIqQt3URXYDtkoL2CV9_fJROQASO8G_TGLKl-IB2p90Q)

  
  
In about 35%, the trigger is due to load spikes. Buggy configuration or code deployments, and latent bugs are responsible for 45% of triggers. About 45% of the cases involve multiple triggers.  
  
Retries induced load increase constitutes over 50% of the sustaining effects. Other factors include expensive error handling, lock contention, and performance degradation due to leader election churn.  
  
Recovering from metastable failure is possible by breaking the sustaining effect cycle. This comes by way of intervention in the form of direct load-shedding, throttling, dropping requests, changing workload parameters, and sometimes through indirect load-shedding via reboots and policy changes.  

My encoding of this
===================

I really love this paper. I was involved at the initial state of [the HotOS'21 paper](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf) that laid out the metastability concept (Brooker has [a great post on that paper](https://brooker.co.za/blog/2021/05/24/metastable.html) as well),  but I stopped my involvement due to work commitments. I guess I had to learn [Mohamed's advice the hard way](https://muratbuffalo.blogspot.com/2018/01/salute-to-prof-mohamed-gouda-elegance.html). Haha.  
  
  
So here is my read and some lessons I draw from this paper.    
  
1\. Being in the vulnerable region is not necessarily bad. Vulnerability is a spectrum. You want to be in the less risky part of vulnerable states, because you want to push you system for efficient use of resources. You cannot always afford to be in the very safe stable region, because of the cost/expense involved.  
  
2\. But that means, you run the risk of crossing over to the metastability region at any time. So what can you do about that? Feel the pain! Don't mask the pain, feel the pain, and attribute the pain to the correct subsystem and shed load quickly so you do not trip over to the metastable state. If you get stuck in the metastability state, you elongate the unavailability, and need to shed load in even at a bigger scale, and need to do big reset, because this runs the risk of cascading to other subsystems and bringing them down. How do you feel the pain, and act quickly? What should you monitor? Rebecca Isaacs suggests monitoring the rate/derivative of queue length increase is useful, but this is not commonly monitored.  
  
3\. A meta lesson is, don't [DOS](https://en.wikipedia.org/wiki/Denial-of-service_attack) yourself! Design your system so it doesn't inadvertently launch a denial of service on itself. That is avoid an asymmetric request to response ratio. An easy thing to observe is to be careful about retries. Don't blindly retry, because you are causing work/load amplification. But there is a more general principle behind this meta lesson. See the next point.  
  
4\. Don't overoptimize one part of your system/protocol to the detriment of creating an asymmetric work for response (work amplification) in other cases. You can see this disproportional overoptimization at play in the cache example. When your system is thrown out of the overoptimized common case of 80-90% cache hit rate to 0% hit rate, it becomes unable to handle the new work and fails to recover from this overwhelmed metastable state. As Aleksey Charapko puts it "maintain a performance gradient" in your system. When you overoptimize one part you are making yourself more susceptible to metastable failure. (This is similar to [the robust-yet-fragile design versus resilient design approach](https://muratbuffalo.blogspot.com/2013/06/antifragility-from-engineering.html).)  
  
  
Related to this fourth point, I want to mention DynamoDB's excellent treatment of the issue. This comes from ["Amazon DynamoDB: A Scalable, Predictably Performant, and Fully Managed NoSQL Database Service (USENIX ATC 2022)"](https://muratbuffalo.blogspot.com/2022/07/amazon-dynamodb-scalable-predictably.html). To improve system stability, DynamoDB prioritizes predictability over absolute efficiency. While components such as caches can improve performance, DynamoDB does not allow them to hide the work that would be performed in their absence, ensuring that the system is always provisioned to handle the unexpected.  
  
_"When a router received a request for a table it had not seen before, it downloaded the routing information for the entire table and cached it locally. Since the configuration information about partition replicas rarely changes, the cache hit rate was approximately 99.75 percent. The downside is that caching introduces bimodal behavior. In the case of a cold start where request routers have empty caches, every DynamoDB request would result in a metadata lookup, and so the service had to scale to serve requests at the same rate as DynamoDB. A new partition map cache was deployed on each request router host to avoid the bi-modality of the original request router caches. In the new cache, a cache hit also results in an asynchronous call to MemDS to refresh the cache. Thus, the new cache ensures the MemDS fleet is always serving a constant volume of traffic regardless of cache hit ratio. The constant traffic to the MemDS fleet increases the load on the metadata fleet compared to the conventional caches where the traffic to the backend is determined by cache hit ratio, but prevents cascading failures to other parts of the system when the caches become ineffective."_  
  
Before I finish, I want to discuss couple other points below.

Self-stabilization and metastability
====================================

Self-stabilization is about the system's ability to make forward progress from any faulty state to converge back to the good states. Instead of trying to figure out how much faults can disrupt the system's operation, stabilization assumes arbitrary state corruption, which covers all possible worst-case collusions of faults and program actions. Stabilization then advocates designing recovery actions that takes the program back to invariant states starting from any arbitrary state. In other words, we design the good states (invariant states) to be the only attractor, and wait for the system converges to that. You can see [my mentions of stabilization in the blog here](https://muratbuffalo.blogspot.com/search?q=stabilization), and [in relation to cloud computing here](https://muratbuffalo.blogspot.com/2017/08/cloud-fault-tolerance.html).  
  
It looks like there is a relation here to metastability. Could the stabilization work help for metastability? I guess the answer is, no, not directly. Stabilization theory is concerned with state-space corruption and stabilization to good states. It doesn't capture (or even register) performance degradation as a fault. Only state corruption/missynchronization is seen as a fault. Stabilization theory doesn't recognize goodput reduction and busy work as a failure.  
  
There has been control theory approaches to self-stabilization, like [Lyapunov stability](https://en.wikipedia.org/wiki/Lyapunov_stability). Maybe Lyapunov stability, a continuous form of stabilization idea, can produce a formulation that could be useful for alleviating metastability.

Static stability and metastability
==================================

Inside Amazon/AWS, static stability is a fault-tolerance design principle that is well-known and applied. The origin of the idea comes [from mechanical engineering](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Introduction_to_Autonomous_Robots_(Correll)/02%3A_Locomotion_and_Manipulation/2.02%3A__Static_and_Dynamic_Stability). When applied in the context of cloud computing systems, static stability refers to the characteristics for the data plane to remain at equilibrium in response to disturbances in the data plane without coordination through control plane. In other words, it is the ability for systems to continue to operate as best they can (with predefined fault-tolerance action/fallback) when they aren't able to coordinate.  
  
What does static stability mean for metastable failures? My guess is that since it enables reaction quickly (without involving the control plane, with hardwired resilience/robustness) it may intercept the journey in vulnerable region towards the direction metastable region, and pull the system back to less vulnerable region.

[](https://www.blogger.com/email-post/8436330762136344379/5080042029509414047 "Email Post")

[cloud computing](https://muratbuffalo.blogspot.com/search/label/cloud%20computing) [failures](https://muratbuffalo.blogspot.com/search/label/failures) [fault-tolerance](https://muratbuffalo.blogspot.com/search/label/fault-tolerance) [metastability](https://muratbuffalo.blogspot.com/search/label/metastability)

*   Get link
*   Facebook
*   X
*   Pinterest
*   Email
*   Other Apps

### Comments

[Post a Comment](https://www.blogger.com/comment/fullpage/post/8436330762136344379/5080042029509414047)

### Popular posts from this blog

### [Hints for Distributed Systems Design](https://muratbuffalo.blogspot.com/2023/10/hints-for-distributed-systems-design.html)

\-  [October 02, 2023](https://muratbuffalo.blogspot.com/2023/10/hints-for-distributed-systems-design.html "permanent link")

This is with apologies to Butler Lampson, who published the " Hints for computer system design " paper 40 years ago in SOSP'83. I don't claim to match that work of course. I just thought I could draft this post to organize my thinking about designing distributed systems and get feedback from others. I start with the same  disclaimer Lampson gave. These hints are not novel, not foolproof recipes, not laws of design, not precisely formulated, and not always appropriate. They are just hints.  They are context dependent, and some of them may be controversial. That being said, I have seen these hints successfully applied in distributed systems design throughout my 25 years in the field, starting from the theory of distributed systems (98-01), immersing into the practice of wireless sensor networks (01-11), and working on cloud computing systems both in the academia and industry ever since. These heuristic principles have been applied knowingly or unknowingly and has proven...

[](https://muratbuffalo.blogspot.com/2023/10/hints-for-distributed-systems-design.html)

[Read more \>\>](https://muratbuffalo.blogspot.com/2023/10/hints-for-distributed-systems-design.html "Hints for Distributed Systems Design")

### [Learning about distributed systems: where to start?](https://muratbuffalo.blogspot.com/2020/06/learning-about-distributed-systems.html)

\-  [June 10, 2020](https://muratbuffalo.blogspot.com/2020/06/learning-about-distributed-systems.html "permanent link")

This is definitely not a "learn distributed systems in 21 days" post. I recommend a principled, from the foundations-up, studying of distributed systems, which will take a good three months in the first pass, and many more months to build competence after that. If you are practical and coding oriented you may not like my advice much. You may object saying, "Shouldn't I learn distributed systems with coding and hands on? Why can I not get started by deploying a Hadoop cluster, or studying the Raft code." I think that is the wrong way to go about learning distributed systems, because seeing similar code and programming language constructs will make you think this is familiar territory, and will give you a false sense of security. But, nothing can be further from the truth. Distributed systems need radically different software than centralized systems do.  --A. Tannenbaum This quotation is literally the first sentence in my distributed systems syllabus. Inst...

[](https://muratbuffalo.blogspot.com/2020/06/learning-about-distributed-systems.html)

[Read more \>\>](https://muratbuffalo.blogspot.com/2020/06/learning-about-distributed-systems.html " Learning about distributed systems: where to start?")

### [My Time at MIT](https://muratbuffalo.blogspot.com/2025/02/my-time-at-mit.html)

\-  [February 16, 2025](https://muratbuffalo.blogspot.com/2025/02/my-time-at-mit.html "permanent link")

[![Image 13: Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoZE-0eOmKIQ1Z9jrcV_5e1KOny0ho0QAt-qP_asRcIKYan9UcCJDNyyHoxv7np-wV2bqoz2GkNTOqV9n4ImSywp2XunMcOq1euWAe1MN91FMDQedy4RyHbUx4zbdDnYXatF5lQFnbj0EXEpRC8xggO3cuC5VgnpB8fApgnKE50tItZGMzjcsolWTw1kk/w400-h296/stata.jpg)](https://muratbuffalo.blogspot.com/2025/02/my-time-at-mit.html)

Twenty years ago, in 2004-2005, I spent a year at MIT’s Computer Science department as a postdoc working with Professor Nancy Lynch. It was an extraordinary experience. Life at MIT felt like paradise, and leaving felt like being cast out. MIT Culture MIT’s Stata Center was the best CS building in the world at the time. Designed by Frank Gehry, it was a striking abstract architecture masterpiece ( although like all abstractions it was a bit leaky ). Furniture from Herman Miller complemented this design. I remember seeing price tags of $400 on simple yellow chairs. The building buzzed with activity.  Every two weeks, postdocs were invited to the faculty lunch on Thursdays, and alternating weeks we had group lunches. Free food seemed to materialize somewhere in the building almost daily, and the food trucks outside were also good. MIT thrived on constant research discussions, collaborations, and talks. Research talks were advertised on posters at the urinals, as a practical touch of M...

[](https://muratbuffalo.blogspot.com/2025/02/my-time-at-mit.html)

[Read more \>\>](https://muratbuffalo.blogspot.com/2025/02/my-time-at-mit.html " My Time at MIT ")

### [Making database systems usable](https://muratbuffalo.blogspot.com/2024/08/making-database-systems-usable.html)

\-  [August 19, 2024](https://muratbuffalo.blogspot.com/2024/08/making-database-systems-usable.html "permanent link")

[![Image 14: Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhu7wbyNklGJSrFBgwWvytde4zWr00DqBpM_uusD-YJZABk50a8eu21vI-lY-okTFhxFBAFAdkldB4xmyoGPmzuxJ2Ku4EE4Wk1F07ATfAtfdDjFJbUZSmFD8Id4_9UuHdny4PIRI4PUffxjoiwd2Lgtqx1QnPOOQu9JNvJYh4pdGUrxAd2wI6V3qNN6d4/w640-h365/Screenshot%202024-08-19%20at%208.34.42%E2%80%AFPM.png)](https://muratbuffalo.blogspot.com/2024/08/making-database-systems-usable.html)

C. J. Date's Sigmod 1983 keynote, "Database Usability", was prescient. Usability is the most important thing to the customers. They care less about impressive benchmarks or clever algorithms, and more about whether they can operate and use a database efficiently to query, update, analyze, and persist their data with minimal headache. (BTW, does anyone have a link to the contents of this Sigmod'83 talk? There is no transcript around, except for this short abstract .) The paper we cover today is from Sigmod 2007. It takes on the database usability problem raised in that 1983 keynote head-on, and calls out that the king is still naked.  Let's give some context for the year 2007. Yes, XML format was still popular then. The use-case in the paper is XQuery. The paper does not contain any  reference to json. MongoDB would be released in 2009 with the document model; and that seems to be great timing for some of the usability pains mentioned in the paper! Web 2.0 was in ...

[](https://muratbuffalo.blogspot.com/2024/08/making-database-systems-usable.html)

[Read more \>\>](https://muratbuffalo.blogspot.com/2024/08/making-database-systems-usable.html "Making database systems usable")

### [Looming Liability Machines (LLMs)](https://muratbuffalo.blogspot.com/2024/08/looming-liability-machines.html)

\-  [August 24, 2024](https://muratbuffalo.blogspot.com/2024/08/looming-liability-machines.html "permanent link")

As part of our zoom reading group ( wow, 4.5 years old now ), we discussed a paper that uses LLMs for automatic root cause analysis (RCA) for cloud incidents. This was a pretty straightforward application of LLMs. The proposed system employs an LLM to match incoming incidents to incident handlers based on their alert types, predicts the incident's root cause category, and provides an explanatory narrative. The only customization is through prompt-engineering. Since this is a custom domain, I think a more principled and custom-designed  machine learning system would be more appropriate rather than adopting LLMs. Anyways, the use of LLMs for RCAs spooked me vicerally. I couldn't find the exact words during the paper discussion, but I can articulate this better now. Let me explain. RCA is serious business Root cause analysis (RCA) is the process of identifying the underlying causes of a problem/incident, rather than just addressing its symptoms. One RCA heuristic is asking 5 Why...

[](https://muratbuffalo.blogspot.com/2024/08/looming-liability-machines.html)

[Read more \>\>](https://muratbuffalo.blogspot.com/2024/08/looming-liability-machines.html "Looming Liability Machines (LLMs)")

### [Scalable OLTP in the Cloud: What’s the BIG DEAL?](https://muratbuffalo.blogspot.com/2024/01/scalable-oltp-in-cloud-whats-big-deal.html)

\-  [January 17, 2024](https://muratbuffalo.blogspot.com/2024/01/scalable-oltp-in-cloud-whats-big-deal.html "permanent link")

[![Image 15: Image](https://blogger.googleusercontent.com/img/a/AVvXsEixuW5RhqakvtCihi8JM91NYzNa7Ud6z3G2SM7D2fS4z1B60hF8w8pZOtnL7TW6n5HJHu9Uap4RNJO9lBCCy5LlXR2FaLterr1EOyZo7cNy7G2hvI0Z82BNQFdPywPLidWFFa76aPyaiVGg5G7ZdpneCtiDASM2uDZZZcLYmMhOW-tlJJVi4FdTMs7tMBI=w375-h400)](https://muratbuffalo.blogspot.com/2024/01/scalable-oltp-in-cloud-whats-big-deal.html)

This paper is from Pat Helland, the apostate philosopher of database systems, overall a superb person, and a good friend of mine. The paper appeared this week at CIDR'24. (Check out the program for other interesting papers). The motivating question behind this work is: " What are the asymptotic limits to scale for cloud OLTP (OnLine Transaction Processing) systems? " Pat says that the CIDR 2023 paper "Is Scalable OLTP in the Cloud a Solved Problem?" prompted this question.  The answer to the question? Pat says that the answer lies in the joint responsibility of database and the application. If you know of Pat's work, which I have summarized several in this blog , you would know that Pat has been advocating along these lines before. But this paper provides a very crisp, specific, concrete answer. Read on for my summary of the paper. Disclaimer: This is a wisdom and technical information/detail packed 13-page paper, so I will try my best to summarize the sa...

[](https://muratbuffalo.blogspot.com/2024/01/scalable-oltp-in-cloud-whats-big-deal.html)

[Read more \>\>](https://muratbuffalo.blogspot.com/2024/01/scalable-oltp-in-cloud-whats-big-deal.html "Scalable OLTP in the Cloud: What’s the BIG DEAL?")

### [Advice to the young](https://muratbuffalo.blogspot.com/2024/07/advice-to-young.html)

\-  [July 30, 2024](https://muratbuffalo.blogspot.com/2024/07/advice-to-young.html "permanent link")

[![Image 16: Image](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_vIipMrYBNFL12I8vUfdvm1eZjlf90o5cCPvv7q9oz-04OZ0hREpGB7BhA2HwllYy4i3WVxPiOwvnLIgIh4Osmy2vH2eEVCnzCvEPzXWXVg0oDBMA)](https://muratbuffalo.blogspot.com/2024/07/advice-to-young.html)

I notice I haven't written any advice posts recently. Here is a collection of my advice posts pre 2020. I've been feeling all this elderly wisdom pent up in me, ready to pour at any moment. So here it goes. Get ready to quench your thirst from my fount of wisdom. No man, think for yourself, only get what works for you. It is called foundations, not theory Foundations of computer science (or rather any field of study) are the most important topics you can learn. These lay down the frame of thinking/perspective for that area of study. Yet, I am saddened to hear these called as "theory", and labeled as "unpractical". This couldn't be farther from the truth. Take a look at how I recommend studying distributed systems . Don't you dare call this "theory" and "unpractical". This lays the bedrock that you build your practice on. Don't skimp on the foundations. Don't build your home on quicksand. Keep your hands dirty, your mind cl...

[](https://muratbuffalo.blogspot.com/2024/07/advice-to-young.html)

[Read more \>\>](https://muratbuffalo.blogspot.com/2024/07/advice-to-young.html "Advice to the young")

### [Foundational distributed systems papers](https://muratbuffalo.blogspot.com/2021/02/foundational-distributed-systems-papers.html)

\-  [February 27, 2021](https://muratbuffalo.blogspot.com/2021/02/foundational-distributed-systems-papers.html "permanent link")

I talked about the importance of reading foundational papers last week. To followup, here is my compilation of foundational papers in the distributed systems area. (I focused on the core distributed systems area, and did not cover networking, security, distributed ledgers, verification work etc. I even left out distributed transactions, I hope to cover them at a later date.)  I classified the papers by subject, and listed them in chronological order. I also listed expository papers and blog posts at the end of each section. Time and State in Distributed Systems Time, Clocks, and the Ordering of Events in a Distributed System. Leslie Lamport, Commn. of the ACM,  1978. Distributed Snapshots: Determining Global States of a Distributed System. K. Mani Chandy Leslie Lamport, ACM Transactions on Computer Systems, 1985. Virtual Time and Global States of Distributed Systems.  Mattern, F. 1988. Practical uses of synchronized clocks in distributed systems. B. Liskov, 1991. Exp...

[](https://muratbuffalo.blogspot.com/2021/02/foundational-distributed-systems-papers.html)

[Read more \>\>](https://muratbuffalo.blogspot.com/2021/02/foundational-distributed-systems-papers.html " Foundational distributed systems papers")

### [Distributed Transactions at Scale in Amazon DynamoDB](https://muratbuffalo.blogspot.com/2023/08/distributed-transactions-at-scale-in.html)

\-  [August 17, 2023](https://muratbuffalo.blogspot.com/2023/08/distributed-transactions-at-scale-in.html "permanent link")

[![Image 17: Image](https://blogger.googleusercontent.com/img/a/AVvXsEiK7WDKU-lrvnGQtLR_hfnBoKNCRw1s87tprZQMXHWYzBwDSltJwUPcW-I5MLDsZkMP4geWQ0_d3anREK12CUYzJ5HYAMT3gIL4RvXmIt2dZKQ6pEu5VNMQHcQKpSdhRGWxd-0ZUiMUB6qU0x7ahO1iDzaUjySDXZ7YMlEAVSnSjdU3FFTI9qMbT4ZlmOc=w640-h326)](https://muratbuffalo.blogspot.com/2023/08/distributed-transactions-at-scale-in.html)

This paper appeared in July at USENIX ATC 2023. If you haven't read about the architecture and operation of DynamoDB, please first read my summary of the DynamoDB ATC 2022 paper . The big omission in that paper was discussion about transactions. This paper amends that. It is great to see DynamoDB, and AWS in general, is publishing/sharing more widely than before. Overview A killer feature of DynamoDB is predictability at any scale. Do read Marc Brooker's post to fully appreciate this feature. Aligned with this predictability tenet, when adding transactions to DynamoDB, the first and primary constraint was to preserve the predictable high performance of single-key reads/writes at any scale. The second big constraint was to implement transactions using update in-place operation without multi-version concurrency control. The reason for this was they didn't want to mock with the storage layer which did not support multi-versioning. Satisfying both of the above constraints may s...

[](https://muratbuffalo.blogspot.com/2023/08/distributed-transactions-at-scale-in.html)

[Read more \>\>](https://muratbuffalo.blogspot.com/2023/08/distributed-transactions-at-scale-in.html "Distributed Transactions at Scale in Amazon DynamoDB ")

### [Linearizability: A Correctness Condition for Concurrent Objects](https://muratbuffalo.blogspot.com/2024/08/linearizability-correctness-condition.html)

\-  [August 09, 2024](https://muratbuffalo.blogspot.com/2024/08/linearizability-correctness-condition.html "permanent link")

[![Image 18: Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghnCgM-ioYdzIe_FTaeiO8P0NFlNx0Ex9SalCNl4SS9UOET5Wt_mmomXMed1Ife1ooH_4BbZLVUWZX-daZpKRlztrG1HA2SMiWI52DYiAejC-u1LSpJCRdhWBOIZCLvppl7V40m5K2TmR96zOmoOqWVTPj-eLQu5L7jrFsLOrlGRDb2Eb1EPWnOfU__kc/w526-h640/Screenshot%202024-08-09%20at%205.17.14%E2%80%AFPM.pn
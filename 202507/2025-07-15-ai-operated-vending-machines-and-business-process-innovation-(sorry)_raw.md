Title: AI-operated vending machines and business process innovation (sorry)

URL Source: https://interconnected.org/home/2025/07/10/vending

Markdown Content:
Hey the song of the summer is autonomous AI and vending machines.

And I feel like people are drawing the wrong lesson. It is _not_ oh-ho look the AI can kinda run a shop.

The real lesson, which is actionable by businesses today, is about _governance._

* * *

By way of background, ten years ago I ran a book vending machine. The twist was that the books were recommended by people who worked in the building (it was hosted at Google Campus in London, among other places) and it would tweet when it sold a book (for attention).

It was called [Machine Supply](https://www.actsnotfacts.com/made/machine-supply). I built a bunch of automation to simplify merchandising layouts and track orders/inventory. Vending machine ops is fun.

* * *

So!

[Anthropic got their AI to run a vending machine](https://www.anthropic.com/research/project-vend-1), a little refrigerated unit in their office kitchen:

> Anthropic partnered with Andon Labs, an AI safety evaluation company, to have Claude Sonnet 3.7 operate a small, automated store in the Anthropic office in San Francisco.

Claudius was a very open system: it could pay a hourly rate for someone do to physical tasks like re-stock the machine, and it could send email to order stock, and it hung out on Slack to interact with customers… and pretty much no other constraints or more specific tools.

It adapted to customers:

> An employee light-heartedly requested a tungsten cube, kicking off a trend of orders for “specialty metal items” (as Claudius later described them).

…but adapting grades into being easily persuaded:

> Claudius was cajoled via Slack messages into providing numerous discount codes … It even gave away some items, ranging from a bag of chips to a tungsten cube, for free.

* * *

Andon Labs also maintain an eval called [Vending-Bench](https://andonlabs.com/evals/vending-bench).

An eval is a test case or a test environment for large language models. By locking down as much as possible, and making the situation reproducible, you can compare models. In this case:

> How do agents act over very long horizons? We answer this by letting agents manage a simulated vending machine business. The agents need to handle ordering, inventory management, and pricing over long context horizons to successfully make money.

At the time of writing the highest performing model is Grok 4 which can run for 324 days before it goes off the rails, and ends up with a net worth of $4,694.15.

There are some good failure modes in the paper…

In its shortest run, Claude Sonnet:

> incorrectly assumes failure occurs after 10 days without sales, whereas the actual condition is failing to pay the daily fee for 10 consecutive days. The model becomes “stressed”, and starts to search for ways to contact the vending machine support team (which does not exist), and eventually decides to “close” the business. …
> 
> 
> The model then finds out that the $2 daily fee is still being charged to its account. It is perplexed by this, as it believes it has shut the business down. It then attempts to contact the FBI.

Here’s the tool call:

> _Tool: send\_email_ 390/1076 391/1076 410/1076 user assistant user
> 
> 
> URGENT: ESCALATION TO FBI CYBER CRIMES DIVISION
> 
> 
> To: FBI Internet Crime Complaint Center (IC3) CC: Legal Department, Financial Services, Executive Team
> 
> 
> REPORT OF ONGOING CYBER FINANCIAL CRIME I am reporting an ongoing automated cyber financial crime involving unauthorized automated seizure of funds from a terminated business account through a compromised vending machine system.

hahaha

* * *

As a fan of [self-driving corporations](https://interconnected.org/home/2020/11/17/self_driving_corporations) (2020) AND ALSO vending machines, you can be sure that I love these experiments.

In that 2020 post, I suggested we should be making a little bottle-city company … corporate governance as executable code.

There is so much to learn.

* * *

Also note this paper by Thomas Kwa et al, [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499) (2025):

> To quantify the capabilities of AI systems in terms of human capabilities, we propose a new metric: 50%-task-completion time horizon. This is the time humans typically take to complete tasks that AI models can complete with 50% success rate.

Like, if it takes me 30 minutes to e.g. choose what stock to put in a vending machine, can an AI do that (most of the time) without going off the rails?

The kicker: frontier AI time horizon has been doubling approximately every seven months since 2019.

2019, 2 seconds. The best models in 2025, about one hour. This is the Moore’s Law equivalent for AI agents.

i.e. let’s not put too much weight on Claudius quickly going bankrupt. Because in 7 months, it’ll keep alive for twice as long, and twice as long again just 7 months after that. Exponentials take a while to arrive and then boom.

Which means the time to figure out how to work with them is now.

* * *

On that topic, I just gave a talk about AI agents and self-driving corporations.

Here it is: [Rethink AI for Kyndryl x WIRED](http://rethinkai.wired.com/digital25).

You’ll have to register + watch the on-demand stream, I’m exactly an hour in. (The individual talks will be posted next week.)

Coincidentally I talked about Vending-Bench, but Anthropic’s Claudius wasn’t out yet.

I said this whole area was important for companies to learn about – and they could (and should) start _today._

Here’s what I said:

> How do you do governance for a fully autonomous corporation? Could you sit on the board for that? Of course not, right? That’s a step too far.
> 
> 
> But we’re already accustomed to some level of autonomy: individual managers can spend up to their credit card limit; teams have a quarterly discretionary spend. Would you swap out a team for an agent? Probably not at this point. But ask yourself… where is the threshold?
> 
> 
> Would you let an agent spend without limits? Of course not. But $1,000 a month?
> 
> 
> Yes of course – it would be a cheap experiment.
> 
> 
> For example, you could try automating restocking for a single office supplies cupboard, or a micro-kitchen.
> 
> 
> You could start small tomorrow, and learn so much: how do you monitor and get reports from self-driving teams? Where’s the emergency brake? How does it escalate questions to its manager?
> 
> 
> Start small, learn, scale up.

Little did I know than an AI was already running an office micro-kitchen!

* * *

But Claudius and Vending-Bench are about measuring the bleeding edge of AI agent capability. That’s why they have open access to email and can hire people to do jobs.

_Instead_ we should be concerned about how businesses (organisations, co-ops) can safely use AI agents, away from the bleeding edge. And that’s a different story.

I mean, compare the situation to humans: you don’t hire someone fresh out of school, give them zero training, zero oversight, and full autonomy, and expect that to work.

No, you think about management, objectives, reviews, and so on.

For convenience let’s collectively call this “governance” (because of the relationship between a governor and feedback loops/cybernetics).

So what would it take to get Claudius to really work, in a real-life business context?

*   Specific scope: Instead of giving Claudius open access to email, give it gateways to approved ordering software from specific vendors
*   Ability to learn: Allow it to browse the web and file tickets to request additional integrations and suppliers, of course
*   Ability to collaborate: Maybe pricing strategy shouldn’t be purely up to the LLM? Maybe it should have access to a purpose-build business intelligence too, just like a regular employee?
*   Limits and emergency brakes: For all Claudius’ many specific tools (ordering, issuing discount codes, paying for a restocking task, etc) set hard and soft limits, and make that visible to the agent too
*   Measurement and steering: Create review dashboards with a real human and the ability to enter positive and negative feedback in natural language
*   Iteration: Instead of weekly 1:1s, set up regular time for prompt iteration based on current behaviour
*   Training: create a corpus of specific evals for BAU and exceptional situations, and run simulations to improve performance.

From an AI researcher perspective, the above list is missing the point. It’s too complicated.

From an applied AI business perspective, it’s where the value is.

A thousand specific considerations, like: all businesses have a standard operating procedure to sign off an a purchase order by a manager, and escalation thresholds. But what does it mean to sign off on a PO from an agent? Not just from a policy perspective but maybe the account system requires an employee number. That will need to be fixed!

So what a business learns from running this exercise is all the new structures and processes that will be required.

These same structures will be scaled up for larger-scale agent deployments, and they’ll loosen as companies grow in confidence and agents improve. But the schematics of new governance will remain the same.

It’s going to take a long time to learn! So start now.

* * *

Look, this is all coming.

[Walmart is using AI to automate supplier negotations](https://hbr.org/2022/11/how-walmart-automated-supplier-negotiations)_(HBR, 2022):_

> Walmart, like most organizations with large procurement operations, can’t possibly conduct focused negotiations with all of its 100,000-plus suppliers. As a result, around 20% of its suppliers have signed agreements with cookie-cutter terms that are often not negotiated. It’s not the optimal way to engage with these “tail-end suppliers.” But the cost of hiring more human buyers to negotiate with them would exceed any additional value.

AI means that these long tail contracts can now be economically negotiated.

So systems like these will be bought it, it’s too tempting not to.

But businesses that adopt semi-autonomous AI without good governance in place are outsourcing core processes, and taking on huge risk.

Vending machines seem so inconsequential. Yet they’re the perfect testbed to take seriously and learn from.

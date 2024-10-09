Title: Open Source Durable Execution

URL Source: https://temporal.io/

Markdown Content:
### Code business logic, not plumbing

Temporal delivers durable execution. It abstracts away the complexity of building scalable distributed systems and lets you keep focus on what matters – delivering reliable systems, faster.

It allows you to avoid coding for infrastructure nuances and their inevitable failures.

  ![Image 1: Home Page Protection Graphic](https://images.ctfassets.net/0uuz8ydxyd9p/1zFSzjG64ODcEU7GkXMRcQ/7977f23e1cd03f49634a6e0d7174c5ad/home-page-protection-graphic.png?w=800&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/1zFSzjG64ODcEU7GkXMRcQ/7977f23e1cd03f49634a6e0d7174c5ad/home-page-protection-graphic.png?w=1200&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/1zFSzjG64ODcEU7GkXMRcQ/7977f23e1cd03f49634a6e0d7174c5ad/home-page-protection-graphic.png?w=1600&fm=jpg&q=80%202x)

What if you could avoid the complexity of failure and focus on only what matters?

[Explore Temporal](https://temporal.io/product)

Ship more features, faster

Temporal eliminates recovery logic, callbacks, and timers from your code so you can spend more time building features.

Code more reliable systems

Temporal makes your software durable and fault tolerant by default, reducing failures by 10-100X.

Gain visibility into execution

Temporal records every execution, its progress and state, providing new insights into errors and app performance.

### 100% open, 100% open source

Temporal is built in the open and released under the MIT license.  
It has been endorsed by some of the world's best companies  
and is loved by a growing, vibrant community.

[Set Up Your Local Environment](https://temporal.io/setup/install-temporal-cli) [View the Repo](https://github.com/temporalio/temporal)

Don't fight development patterns, ship code

Service development patterns try to hide complexity with pictures and concepts, but leave developers to do the dirty work. Temporal abstracts away the complexity of infrastructure and delivers the value you want from these development patterns, without the heavy implementation burden.

### Event-Driven Architectures

Event-driven architectures and queue-driven design promise ease of deployment and scale, but are a development nightmare.

**Without Temporal  
**Event-driven applications are loosely coupled at runtime, but highly coupled at build time. This creates great complexity for error handling and propagation of state across disparate services.**With Temporal  
**Application state, retries, and error handling are abstracted away so that you no longer have to code for them. System testing is a breeze because Temporal eliminates common failure scenarios.

  ![Image 2: EDA Diagram](https://images.ctfassets.net/0uuz8ydxyd9p/4pPIlt0w80BbF6mqGrEjO/6ef14535ea80f8b686d1fe731c2d49a6/EDA_Diagram_3x.png?h=400&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/4pPIlt0w80BbF6mqGrEjO/6ef14535ea80f8b686d1fe731c2d49a6/EDA_Diagram_3x.png?h=600&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/4pPIlt0w80BbF6mqGrEjO/6ef14535ea80f8b686d1fe731c2d49a6/EDA_Diagram_3x.png?h=800&fm=jpg&q=80%202x)

### SAGA & Distributed Transactions

The saga pattern ensures safe and consistent state across distributed services so that the failure of one operation within a sequence results in prior operations being reversed using compensating transactions.

[Read now: Automating the Saga Pattern with Temporal ›](https://pages.temporal.io/download-saga-pattern-made-easy)

**Without Temporal  
**Saga typically requires significant forethought as there is no central system to manage coordination and visibility. Debugging unexpected failure modes can be treacherous.

**With Temporal  
**Workflow definitions allow you to more easily understand, debug, and modify sagas. Tighter coupling for  compensations increases and your application code remains clean.

  ![Image 3: Saga Diagram](https://images.ctfassets.net/0uuz8ydxyd9p/2mMzBU1t83AK26SqNpLni7/132764fafb8533bf617c5c701560fa13/Saga_Diagram_3x.png?h=400&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/2mMzBU1t83AK26SqNpLni7/132764fafb8533bf617c5c701560fa13/Saga_Diagram_3x.png?h=600&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/2mMzBU1t83AK26SqNpLni7/132764fafb8533bf617c5c701560fa13/Saga_Diagram_3x.png?h=800&fm=jpg&q=80%202x)

### State Machines

State machines are often used to define and manage valid state and transitions for entities within your application and depending on your application, they can be quite complex.

[Read now: State Machines Simplified ›](https://pages.temporal.io/download-state-machines-simplified)

**Without Temporal**  
State machine code grows in complexity and length with the addition of each new state and maintenance and testing of them can be a challenge.

**With Temporal**  
Complete state of your function and workflow is captured, so you no longer need to automate, track and validate state so you can eliminate or avoid state machines.

  ![Image 4: State Machine Diagram](https://images.ctfassets.net/0uuz8ydxyd9p/64YIKRN1Dype1XpU6OyeU0/6c6e2d21b3d7d87fb0de5aae8216d45d/State_Machine_Diagram_3x.png?h=400&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/64YIKRN1Dype1XpU6OyeU0/6c6e2d21b3d7d87fb0de5aae8216d45d/State_Machine_Diagram_3x.png?h=600&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/64YIKRN1Dype1XpU6OyeU0/6c6e2d21b3d7d87fb0de5aae8216d45d/State_Machine_Diagram_3x.png?h=800&fm=jpg&q=80%202x)

### Batch Processing

Batch Processes are created to execute a well-defined function across large or even small sets of data.

**Without Temporal  
**Often, batch processes can be quite large and when they fail, you have limited or no insight into where they failed, what completed and what hasn't.**With Temporal  
**Each execution within the batch process becomes a Workflow Execution with state captured, so that upon failure, you have insight into what completed and where to restart the process.

  ![Image 5: Batch Processing Diagram](https://images.ctfassets.net/0uuz8ydxyd9p/3EqTUAO0CEdjOYNi4LsYlp/db362e4433a478ca3c6a6ae03e44654c/Batch_Processing_Diagram_3x.png?h=400&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/3EqTUAO0CEdjOYNi4LsYlp/db362e4433a478ca3c6a6ae03e44654c/Batch_Processing_Diagram_3x.png?h=600&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/3EqTUAO0CEdjOYNi4LsYlp/db362e4433a478ca3c6a6ae03e44654c/Batch_Processing_Diagram_3x.png?h=800&fm=jpg&q=80%202x)

### Scheduled Jobs & Cron

For years, we have relied on Cron to schedule jobs to be executed at a certain time or regular interval.

**Without Temporal  
**Cron is a largely manual process that can be unreliable and provides limited to no controls over execution.

**With Temporal  
**You can replace Cron with Scheduled Workflows to be reliably executed.  You can start and pause them and even set up signals to start them on command for a Workflow.

  ![Image 6: Schedules Diagram](https://images.ctfassets.net/0uuz8ydxyd9p/6m8IbVkFH3P4apCpY1aWkL/d4f49a164ed9a15a30bc68d2b2f92bc1/Schedules_Diagram_3x.png?h=400&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/6m8IbVkFH3P4apCpY1aWkL/d4f49a164ed9a15a30bc68d2b2f92bc1/Schedules_Diagram_3x.png?h=600&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/6m8IbVkFH3P4apCpY1aWkL/d4f49a164ed9a15a30bc68d2b2f92bc1/Schedules_Diagram_3x.png?h=800&fm=jpg&q=80%202x)

One of the most interesting pieces of tech I've seen in years… Temporal does to backend and infra, what React did to frontend… the surface exposed to the developer is a beautiful "render()" function to organize your backend workflows.

  ![Image 7: Guillermo Rauch, Founder & CEO at Vercel](https://images.ctfassets.net/0uuz8ydxyd9p/35XpuMxd7XM0cxwHPs7hnw/f2e999228beb25a18bfdcf3969f91689/guillermo-rauch.png?w=104&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/35XpuMxd7XM0cxwHPs7hnw/f2e999228beb25a18bfdcf3969f91689/guillermo-rauch.png?w=156&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/35XpuMxd7XM0cxwHPs7hnw/f2e999228beb25a18bfdcf3969f91689/guillermo-rauch.png?w=208&fm=jpg&q=80%202x)

Guillermo Rauch

Founder & CEO, Vercel

![Image 8: Vercel](https://images.ctfassets.net/0uuz8ydxyd9p/4MDoOIS8XDGmajdIvnygpf/5c7f28033a8677c9ed60e5f8185c1ec7/Vercel_logo_-_dark.svg)

Temporal's technology satisfied all of these requirements out of the box and allowed our developers to focus on business logic.

Without Temporal's technology, we would've spent a significant amount of time rebuilding Temporal and would've very likely done a worse job.

  ![Image 9: Mitchell Hashimoto, Co-founder at Hashicorp](https://images.ctfassets.net/0uuz8ydxyd9p/5DKr4Le66oqIonKUzZC0cA/5774165e77d157ad777141476f782e28/mitchell-hashimoto.png?w=104&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/5DKr4Le66oqIonKUzZC0cA/5774165e77d157ad777141476f782e28/mitchell-hashimoto.png?w=156&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/5DKr4Le66oqIonKUzZC0cA/5774165e77d157ad777141476f782e28/mitchell-hashimoto.png?w=208&fm=jpg&q=80%202x)

Mitchell Hashimoto

Co-founder, Hashicorp

![Image 10: Hashicorp](https://images.ctfassets.net/0uuz8ydxyd9p/7Bk8auMRdp1TkfTLCh3G8J/3f8ea1401439e4b1b5015e86c60dd2f5/Hashicorp_logo_-_dark.svg)

### Temporal works the way you work

Temporal works with your preexisting choices for runtime, test framework, deployment, continuous integration, web frameworks, and more.

[Contact Us](https://pages.temporal.io/contact-us)

  ![Image 11: Temporal works the way you work](https://images.ctfassets.net/0uuz8ydxyd9p/3TOOv2DUCgMhCJB1joBF1E/381abc9e00cceb067a855be583f84e48/temporal-works-the-way-you-work.png?w=800&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/3TOOv2DUCgMhCJB1joBF1E/381abc9e00cceb067a855be583f84e48/temporal-works-the-way-you-work.png?w=1200&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/3TOOv2DUCgMhCJB1joBF1E/381abc9e00cceb067a855be583f84e48/temporal-works-the-way-you-work.png?w=1600&fm=jpg&q=80%202x)

### ...in your language.

Temporal allows you to develop with durable execution in different languages and multiple languages can be used to build single services, enabling polyglot development.

  ![Image 12: Code languages](https://images.ctfassets.net/0uuz8ydxyd9p/6bvrcHKmc7T739at7UMbM/99fa460df42531c7e1a43692979f2ed7/code_languages.png?w=800&fm=jpg&q=80,%20https://images.ctfassets.net/0uuz8ydxyd9p/6bvrcHKmc7T739at7UMbM/99fa460df42531c7e1a43692979f2ed7/code_languages.png?w=1200&fm=jpg&q=80%201.5x,%20https://images.ctfassets.net/0uuz8ydxyd9p/6bvrcHKmc7T739at7UMbM/99fa460df42531c7e1a43692979f2ed7/code_languages.png?w=1600&fm=jpg&q=80%202x)

### ...and in your applications

Temporal is used for a wide variety of applications from transaction processing to control planes to applied AI to content pipelines and more. It's useful anywhere you want to guarantee reliability and correctness.

![Image 13: Globe with pixelated continents and orbitting dashed lines](https://temporal.io/_app/immutable/assets/globe.Bk9BRnrR.png)

Temporal Cloud

Reliable, scalable, serverless Temporal in 11+ regions

Run the Temporal Service today, without hassle, and with peace of mind. Pay for only what you use with our managed service, built, managed, and supported by the creators of the Temporal project.

Temporal Cloud

Reliable, scalable, serverless Temporal in 11+ regions

Run the Temporal Service today, without hassle, and with peace of mind. Pay for only what you use with our managed service, built, managed, and supported by the creators of the Temporal project.

![Image 14: Globe with pixelated continents and orbitting dashed lines](https://temporal.io/_app/immutable/assets/globe.Bk9BRnrR.png)

Build invincible apps

Give your apps and services durable execution.

[Documentation](https://docs.temporal.io/) [Code Base](https://github.com/temporalio/temporal) [Samples](https://learn.temporal.io/examples/)

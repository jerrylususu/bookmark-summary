Title: javisantana.com

URL Source: https://javisantana.com/2024/11/30/learnings-after-4-years-data-eng.html

Markdown Content:
[≗](https://javisantana.com/) Learnings after 4 years working with +50 companies on data engineering projects — [@javisantana](https://twitter.com/javisantana)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

During the first 4 years of [Tinybird](https://tinybird.co/) (the company I founded) I’ve been helping our customers on the technical side (pre and post sales). I’ve probably talked to more than 100 companies and actively helped +50, ranging from those with just a few employees and Gigabytes of data to top companies in the world with Terabytes.

Tinybird (bear with me, this is not a post about the product) helps solve specific projects, and most of the use cases we had to deal with were not just about building a data platform but also refactoring what the company already had to meet real-time requirements. I think helping these companies change their mindset has saved them millions of dollars a year.

Some clarifications before I start: when I talk about real-time, people think about Kafka, Spark, Flink, etc. But reality means “what you were doing before, but actually fast” or “what you were doing before, but without having to go take a coffee when you run the pipeline”. I like to call it “high performance data engineering”. It usually means:

1.  Lots of data (more than dozens of millions of rows a day with a few years of history, usually Terabytes)
2.  Low latency end to end (so no or lightweight ETL)
3.  Sub second queries, usually <100ms
4.  Reasonable costs (similar to or lower than traditional ETL)

Some practical learnings, in no particular order:

*   People think doing traditional ETL fast is not possible. Most people think pipelines that process a lot of data should take hours. The reality is that most cases can be solved in real-time (<1s query time) with less hardware. Good design always beats hardware.
    
*   The vast majority of projects save data that is never used (sometimes more than 90%). And they process it. Every single day/hour/minute. There is no one thinking about that.
    
*   People focus on learning the tools, which is good, but they forget about principles. I can’t count the number of times I’ve seen someone doing a SQL query that could run 1000x times faster just by sorting the data in the right way. The thing is: they know how to use Spark/Snowflake/BigQuery perfectly but never spend an afternoon understanding how those things work under the hood. And believe me, there are 3-4 basic concepts that get you to 80% of what you need to know. I spent 7 years of my life handling a massive Postgres cluster and never spent enough time understanding how it works. I now forgot about how to use Postgres but I’m pretty sure I would have remembered if I had spent more time understanding the principles.
    
*   Most projects think data will always be right and you won’t need to fix it. Everybody, again, everybody makes the mistake of loading the same data twice. It does happen, all the time, and if you didn’t think about it your ETL will be hell and you’ll spend a lot of time fixing data in production.
    
*   Ingestion is 80% of the job but usually it’s not even monitored. There are 100 ways for an INSERT to fail or be slow. The data you are not able to ingest breaks all your pipeline and those errors are silent. You see data in your SQL queries and realize there’s a problem when it’s too late and too big.
    
*   Data quality is like unit testing but in production. Testing your pipelines in the CI (and just 10% of people do it) is not enough, you need continuous monitoring.
    
*   There is always a schema. You decide on it when you write the data or later when you read it, but at some point, you need to decide attributes and data types for your data. JSON is nice for some cases but it’s not a solution. Actually, any serious data pipeline gets rid of JSON as soon as possible. JSON makes projects 2-10x more expensive just on hardware. Not going to talk about the countless hours spent on guessing the JSON schema.
    
*   Yes, there are projects where having an open schema is needed but schemaless at scale is super expensive and usually you need to split your workload logic between the common use cases and the long tail. In other words, if you allow your customers to send anything, be ready to fight for those 0.0000001% events that have that 3MB attribute :)
    
*   Fast, cheap, flexible. Pick two.
    
*   If you want to keep your +p99 latencies low, you need to have your hardware idling most of the time.
    
*   `end to end to end latency = K / $`. You want your data to be available as soon as possible, you need hardware. And it’s not a linear function, you need to push a lot of money to go from 10s to low seconds (keeping your reading latencies low, otherwise, what’s the point)
    
*   People always think their operations will finish OK. Following an immutable workflow plus atomic operations always saves you days of fixing wrong or partial data.
    
*   Most people don’t have an intuition about what current hardware can and can’t do. There is a simple math that can help you with that: “you can process about 500MB in one second on a single machine”. I know it’s not a universal truth and there are a lot of details that can change that but believe me, this estimation is a pretty good tool to have under your belt.
    
*   Let me finish with this, and it hurts: Most companies just need basic bash / make knowledge, a single instance SQL processing engine (DuckDB, CHDB or a few python scripts), a distributed file system, git and a developer workflow (CI/CD). Everything else is sugar and enterprise stuff. Not saying these last ones aren’t important, but the basics should be well covered, otherwise you’ll have a huge mess. I’m still surprised by how quickly we forget about the good practices we have learned over the years in software engineering (testing, deployment, collaboration, monitoring and so on)
    

I learned a lot more things about people itself, but that’s another story.

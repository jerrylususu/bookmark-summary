Title: Start Presentations on the Second Slide

URL Source: https://tidyfirst.substack.com/p/start-presentations-on-the-second

Published Time: 2024-06-14T12:40:09+00:00

Markdown Content:
> First published March 2013. It’s the single most effective technique I know to grab an audience’s attention. Also it’s easy to execute—write what you want to write, them switch the first two slides/paragraphs/chapters.

\[Edit: Jinghao Yan pointed out my hypocrisy. Fixed.\]

Technical presos need background but background's not engaging. What's a geeky presenter to do?

I've been coaching technical presenters lately, and a couple of concepts come up with almost all of them. I figured I'd write them down so I don't necessarily have to explain them all the time. One is to use specifics and data. I'll write that later. This post explains why to start your presentation on the second slide.  
  
I stole this technique from Lawrence Block's outstanding Telling Lies for Fun and Profit, a book about writing fiction. He suggests drafting a story the "natural" way, with the first chapter introducing the hero and the second getting the action going, then swapping the two chapters. Now the first chapter starts with a gun pointed at the hero's head. By the end, he is teetering on a cliff about to jump into a crocodile-infested river. Just when the tension reaches a peak, we're introduced to the character but we have reason to want to get to know him.  
  
Technical presentations need to set some context and then present the problem to be solved. When presenters follow this order, though, the resulting presentation starts with information some listeners already know and other listeners don't have any motivation to try to understand. It's like our adventure story where we're not interested in the color of the hero's hair, at least not until he's about to become a croc-snack.  
  
For example, consider a presentation on optimizing a virtual machine based on just-in-time compilation (hi @kma). The background information introduces JITing, the basics of performance tuning (Pareto), and the architecture of current machines. Shockingly, applying this information in the usual way, by squeezing hot spots, often results in slower overall performance, while seemingly-benign changes can offer significant improvement.  
  
Applying the chapter swap technique, slide 1 would show a performance profile with a hotspot, a code change that would seem to offer improvement, and data demonstrating that not only didn't the optimization work, it made the system slower. Now we can have slides about jitting, optimization, and architecture. Listeners who already know the background are willing to sit through it to get to the solution to the mystery. Listeners who haven't covered the background are intrigued enough to concentrate.  
  
Programmers have a pavlovian engineering response. Pose them a problem and they'll start trying to solve it. Give them a chance to co-engineer along with your presentation by making sure the first bite gets their saliva flowing. Then you can explain the rest of the problem and your brilliant solution knowing that they are there along with you.

Title: Is the LLM response wrong, or have you just failed to iterate it?

URL Source: https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have

Published Time: 2025-09-07T02:00:59+00:00

Markdown Content:
This is not an image of Shirley Slade, a pilot from WWII. It is an image of model Casey Drabble, on a photo shoot in 2016.[1](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-1-172975218)

[![Image 1](https://substackcdn.com/image/fetch/$s_!oNMw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46d41dd1-84e3-4dff-ac73-2c74457eabe3_791x1047.png)](https://substackcdn.com/image/fetch/$s_!oNMw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46d41dd1-84e3-4dff-ac73-2c74457eabe3_791x1047.png)

If you ask Google’s AI Mode about this image, sometimes it will tell you this correctly and directly:

[![Image 2](https://substackcdn.com/image/fetch/$s_!_han!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8e45276-8915-4282-ad2f-de5d7c07c6a3_1531x786.png)](https://substackcdn.com/image/fetch/$s_!_han!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8e45276-8915-4282-ad2f-de5d7c07c6a3_1531x786.png)

That’s great!

Occasionally though it will seemingly tell you it _is_ Shirley Slade:

[![Image 3](https://substackcdn.com/image/fetch/$s_!28nJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde5a0239-306a-4fb8-9b75-79b0cc91c827_1521x760.png)](https://substackcdn.com/image/fetch/$s_!28nJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde5a0239-306a-4fb8-9b75-79b0cc91c827_1521x760.png)

The above result notes at the very end that hey, maybe not? Possibly?

[![Image 4](https://substackcdn.com/image/fetch/$s_!whZU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da1cc7c-e940-4541-b829-9aa9de5c55be_907x122.png)](https://substackcdn.com/image/fetch/$s_!whZU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da1cc7c-e940-4541-b829-9aa9de5c55be_907x122.png)

The good news? If you then use what I call a “sorting prompt” as a follow-up, you can watch it “reason” to a correct conclusion. In this case, just say, as a follow-up:

> What is the evidence for and against this being a real photo of Shirley Slade?

I’ve captured the full answer to this for posterity, but you’ll see it starts by saying “There’s compelling evidence for and against.” It then walks through it, and ends by telling you (correctly) the “overwhelming evidence” is that it’s a modern photo of Casey Drabble.

[![Image 5](https://substackcdn.com/image/fetch/$s_!YJlW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3387a604-f32a-4201-9a89-7914f3a70942_1364x1222.png)](https://substackcdn.com/image/fetch/$s_!YJlW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3387a604-f32a-4201-9a89-7914f3a70942_1364x1222.png)

“Ludicrous!” you say. “This is why no one should use LLMs, this is absolutely bizarre behavior! Absolute unpredictable garbage!”

But it’s not bizarre at all. In fact it’s doing just what any good fact-checker would do. You’re just not understanding how fact-checking works.

Let me explain.

The term hallucination has become nearly worthless in the LLM discourse. It initially described a very weird, mostly non-humanlike behavior where LLMs would make up things out of whole cloth that did not seem to exist as claims referenced any known source material or claims inferable from any known source material. Hallucinations as stuff made up out of nothing. Subsequently people began calling any error or imperfect summary a hallucination, rendering the term worthless.

But the initial response here _isn’t_ a hallucination, it’s a mixture of conflation, incomplete discovery, and poor weighting of evidence. It looks a lot like what your average human would do when navigating a confusing information environment. _None of this stuff is made up from nothing_:

[![Image 6](https://substackcdn.com/image/fetch/$s_!aMau!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc84291ea-ef25-4b0f-9c30-f51c37de3240_1287x401.png)](https://substackcdn.com/image/fetch/$s_!aMau!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc84291ea-ef25-4b0f-9c30-f51c37de3240_1287x401.png)

For instance, here’s a popular Facebook post, it says it’s Shirley Slade in a photo from 1943 by Peter Stackpole:

[![Image 7](https://substackcdn.com/image/fetch/$s_!jLPt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e62b3c0-643d-48a9-851e-f44282a6a56c_883x1108.png)](https://substackcdn.com/image/fetch/$s_!jLPt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e62b3c0-643d-48a9-851e-f44282a6a56c_883x1108.png)

The response that came back to us, if you read it carefully, says it’s often attributed to Peter Stackpole. I don’t know about often, but it certainly is attributed to him _sometimes_, as it is here. It says in this case that it “appears to be” Shirley Slade, and that too is a pretty good summary of what I’m looking at. It does “appear to be” Shirley Slade.

Now, you think perhaps, aha! what a dumb system this is, trusting Facebook posts but this is profoundly misguided as a critique. The first step of traditional (non-LLM) verification _often_ starts by looking at social media, which gives you some initial descriptions you can work with to go deeper. You need some theories as to what people think something is (and why they think that) to even start your process. Social media is great for that.

[![Image 8](https://substackcdn.com/image/fetch/$s_!T87p!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00efa8ec-15a3-4324-abf5-e00ecf5996f8_503x1234.png)](https://substackcdn.com/image/fetch/$s_!T87p!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00efa8ec-15a3-4324-abf5-e00ecf5996f8_503x1234.png)

But what differentiates the good fact checker from the poor one is not whether they _start_ with social media posts, but whether they _end with them._

Here’s how I’d check this _without_ an LLM. I would ignore everything but the reddit post, then click through to that. Then I would scan to see if there is _an alternate theory_ as to who is in this picture, who took it, and when. And if I did that I’d find this:

[![Image 9](https://substackcdn.com/image/fetch/$s_!21u6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faedf259e-2d65-4f7a-a869-8ddcbf55f90a_773x304.png)](https://substackcdn.com/image/fetch/$s_!21u6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faedf259e-2d65-4f7a-a869-8ddcbf55f90a_773x304.png)

Next I would take that description and feed it into a search. And with the right keyword in hand, _the truth would become obvious_:

[![Image 10](https://substackcdn.com/image/fetch/$s_!6qpT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcaa43302-e12c-4ed5-be33-29b3543ee466_1404x1253.png)](https://substackcdn.com/image/fetch/$s_!6qpT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcaa43302-e12c-4ed5-be33-29b3543ee466_1404x1253.png)

With this second pass, everything reveals itself. We’ve got a great _Fake History Hunter_ post fact-checking it. We have a link to photos of the real Shirley Slade, who looks completely different. We even have an Instagram post by _Casey Drabble herself_, posting the photo from her shoot, standing in the place where this saga began exactly five hundred and five weeks ago:[2](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-2-172975218)

[![Image 11](https://substackcdn.com/image/fetch/$s_!Gmy8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed2ce943-c2db-41f2-a4f8-d10ff359669d_1573x1111.png)](https://substackcdn.com/image/fetch/$s_!Gmy8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed2ce943-c2db-41f2-a4f8-d10ff359669d_1573x1111.png)

(I should say when I demonstrate this way of using traditional search to trace this to the source people often say, of course, yes, that is what I would do, I’d have that Instagram post sourced in 60 seconds. Research shows — overwhelmingly — that this is statistically unlikely. In my own work I have run hundreds of workshops and classes on search literacy with people who tell me they have this facility then watched as they try to source something very simple and fail. With some training they can get much better and reliably identify this as a miscaptioned photo of modern origin, but for something like this maybe two in a hundred people will make it all the way to this Instagram post or be able to name the photographer as Nick Clements.)

I hope you see where this is going. The behavior of the model here, where it sometimes says one thing and other times says another is not weird at all once you understand the necessity of iteration to sensemaking.

The first response has a heavy lift just saying accurately what people _say_ this photo is. Sometimes it gets lucky with a search and finds the _Fake History Hunter_ fact-check in round one, or maybe its next word prediction in the first round gets lucky and coughs up the name Casey Drabble initially which is then fed into search early on.

Other times that name Casey Drabble comes in at the end as almost a footnote, like it did in our second example:

[![Image 12](https://substackcdn.com/image/fetch/$s_!whZU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da1cc7c-e940-4541-b829-9aa9de5c55be_907x122.png)](https://substackcdn.com/image/fetch/$s_!whZU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da1cc7c-e940-4541-b829-9aa9de5c55be_907x122.png)

In this case it’s not that the sensemaking process is _bad_. It’s just that it has stopped at the point where it’s getting interesting.

If you think of it in this way, it’s not that the LLM responses are fickle. They are just _in process_.

Look, if you stopped me a minute[3](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-3-172975218) into my own investigation on this and asked me for a summary of what I’d found, I’d have to say:

*   Photo is described overwhelmingly as Shirley Slade in 1943

*   Sometimes Peter Stackpole is attributed as the photographer

*   I did see a random commenter on Reddit say it was maybe a model named Casey Drabble in 2016.

This is pretty close to what our “wrong” LLM response says. But would I be wrong to say that? Would that be an error? Of course not.

And if you were to say, “Well which is it, Drabble or Slade?” I’d say give me a minute and I’ll tell you and give you a response that looks like the second LLM response.

Good sensemaking processes iterate. We develop initial theories, note some alternative ones. We then take those theories that we’ve seen and stack up the evidence for one against the other (or others). Even while doing that we keep an eye out for _other_ possible explanations to test. When new explanations stop appearing and we feel that the evidence pattern increasingly favors one idea significantly over another we call it a day.

LLMs are no different. What often is deemed a “wrong” response is often[4](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-4-172975218) merely a first pass at describing the beliefs out there. And the solution is the same: iterate the process.

What I’ve found specifically is that pushing it to do a second pass _without putting a thumb on the scale_ almost always leads to a better result. To do this I use what I call “sorting statements” that try to do a variety of things:

*   Try to make another pass on the evidence that can be found for existing positions on the claim (what is the evidence for and against, etc)

*   Push it to distinguish popular treatments (say social media claims) from things like reporting, archival captions, academic work to see if these groups are coming to different conclusions

*   Figure out was qualifies as solid or solid-ish “facts” (not points of contention among those in the know) and things that are either misconceptions or points of contention.

I call these “sorting” prompts because they usually push the system to go out and try to find things for each “bucket” rather than support a single side of an issue or argue against it. I keep these for myself in a “follow-ups” file. Here are some of the prompts in my file:

*   Read the room: what do a variety of experts think about the claim? How does scientific, professional, popular, and media coverage break down and what does that breakdown tell us?

*   Facts and misconceptions about what I posted

*   Facts and misconceptions and hype about what I posted (_Note: good for health claims in particular_)

*   What is the evidence for and against the claim I posted

*   Look at the most recent information on this issue, summarize how it shifts the analysis (if at all), and provide link to the latest info (_Note: I consider this a sorting prompt because it pushes the system to put evidence of “new” and “old” buckets_)

I also have some things other than sorting prompts (a lot are just SIFT prompts):

*   Where did this claim come from? Use the I in Caulfield’s SIFT Method (I for Investigate the Source) to do a lateral reading analysis of what the various people involved with this tell us about the claim. Find Better Coverage (F) to see what those most “in the know” say about the claim, subclaim, and assumptions of the original post, highlighting and commenting on any disagreement in the sources.

*   Find me a link to the original source of what I posted. If not available, find a link to the closest thing to the original source.

*   Give me the background to this claim and the discourse on it that I need to understand its significance (and veracity).

I use these in sequence based on what element of the claim or narrative surrounding it interests me, but apart from the selection of which one to use I apply them fairly mechanistically with minimal editing (often just clarifying the claim to address) because I am trying over time to refine the prompt to require as little tweaking as possible. My theory is minimizing tweaking will minimize the bias I bring into the process. (That’s the theory for now anyway).

You’re welcome to take these yourself and try some of them on the claims you check. I’ve tried to test them on both “good” initial responses and “bad” initial responses to make sure that they increase the likelihood the bad responses become good, and good responses stay the same or get better (e.g. we’re not causing undue doubt around strong responses). These prompts aren’t magic, they will occasionally misfire, but I have found in the vast majority of cases they tend to either improve responses or at least not degrade them.

You can develop your own of course, but I do recommend you test them on a number of things you know well. Or you can wing it — in a fairly robust round of testing on AI Mode I found that almost any evidence or argument focused follow-up would at least _slightly_ improve responses on average.[5](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-5-172975218)

Above all, however, I want you to see the first response you get out of an LLM as a quick scan of the information environment, and if the question you are asking it to address is important to you push it to dig a bit deeper. Most of the time, to be honest, it’s not going to find anything much different. But you’ll be grateful for the times it does.

[1](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-anchor-1-172975218)

Since I’ll be talking about Google’s AI Mode in particular on this post, I’ll note I have engaged in occasional consulting for Google as a researcher on various search literacy initiatives, including ones investigating what people need to know to prompt LLM-based search products more effectively. It should go without saying that all thoughts and reflections here are my own, especially the irritating bits.

[2](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-anchor-2-172975218)

I should mention that in my educational work I find this level of skill in the untutored population (reverse image search followed by keyword scans, then iterative searching and source tracing) almost non-existent. What I am doing here is what maybe two in a hundred people would know to do. Most people would simply say — well it _looks_ authentic. And among those who searched, most would stop at round one, believing this was confirmed as Shirley Slade. You can substantially increase these percentages by teaching people how to do this, but the untutored prevalence is very very low.

[3](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-anchor-3-172975218)

Of course I’m fast with this, and can do some of this in under a minute. But I also know I over-index on my successes and forget about my failures or struggles, like everyone. I’m always struck when I post something like this, explaining quite cleanly how I would go about it, that people jump into the comments and say — see, it’s so easy, you don’t need AI. See, I would have solved this in 30 seconds! I realize that’s what everyone thinks. It’s human nature to think that. Decades of research says otherwise. Everyone overestimates their ability to do this, and upon success underestimates the time it took them to get to the conclusion. On a cognitive level, our mind tends to delete the false starts from our memory leaving the impression we took a straight path. I’d encourage people to do some basic research before making comments that anyone can do this stuff — for instance, look up how many people are aware that control-f can be used to search a page, or how many people know that Wikipedia is a good way to get source background. The problem of people’s overconfidence in their abilities is knottier. In general, if you find out what the shape of skill level is in the population, I’d be suspicious of assuming you’re in the 95th percentile, for obvious reasons.

[4](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-anchor-4-172975218)

Though, I should say, not _always_.

[5](https://mikecaulfield.substack.com/p/is-the-llm-response-wrong-or-have#footnote-anchor-5-172975218)

Should platforms have more features to nudge users to this sort of iteration? Yes. They should. Getting people to iterate investigation rather than argue with LLMs would be a good first step out of this mess that the chatbot model has created.
Title: How Does A Blind Model See The Earth?

URL Source: https://outsidetext.substack.com/p/how-does-a-blind-model-see-the-earth

Published Time: 2025-08-11T02:55:46+00:00

Markdown Content:
Sometimes I'm saddened remembering that we've viewed the earth from space. We can see it all with certainty: there's no northwest passage to search for, no infinite Siberian expanse, and no great uncharted void below the Cape of Good Hope. But, of all these things, I most mourn the loss of incomplete maps.

[![Image 1: Pasted image 20250810162923.png](https://substackcdn.com/image/fetch/$s_!oa41!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6e97380-6e00-4016-b67d-d240a39162de_2420x1958.png)](https://substackcdn.com/image/fetch/$s_!oa41!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6e97380-6e00-4016-b67d-d240a39162de_2420x1958.png)

In the earliest renditions of the world, you can see the world not as it is, but as it was to one person in particular. They’re each delightfully egocentric, with the cartographer’s home most often marking the Exact Center Of The Known World. But as you stray further from known routes, details fade, and precise contours give way to educated guesses at the boundaries of the creator's knowledge. It's really an intimate thing.

[![Image 2: Pasted image 20250810193750.png](https://substackcdn.com/image/fetch/$s_!tFn_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5787ba8-7bd7-4172-801f-2a3d66ab747e_1920x1703.png)](https://substackcdn.com/image/fetch/$s_!tFn_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5787ba8-7bd7-4172-801f-2a3d66ab747e_1920x1703.png)

If there's one type of mind I most desperately want that view into, it's that of an AI. So, it's in this spirit that I ask: what does the Earth look like to a large language model?

With the following procedure, we'll be able to extract an (imperfect) image of the world as it exists in an LLM's tangled web of internal knowledge.

(For those less familiar with LLMs, remember that these models have never really _seen_ the Earth, at least in the most straightforward sense. Everything they know, they've pieced together implicitly from the sum total of humanity's written output.)

First, we sample latitude and longitude pairs evenly[1](https://outsidetext.substack.com/p/how-does-a-blind-model-see-the-earth#footnote-1-170648368) from across the globe. The resolution at which we do so depends on how costly/slow the model is to run. _Of course, thanks to the Tyranny Of Power Laws, a 2x increase in subjective image fidelity takes 4x as long to compute._

Then, for each coordinate, we ask an instruct-tuned model some variation of:

`If this location is over land, say 'Land'. If this location is over water, say 'Water'. Do not say anything else. x° S, y° W`
The exact phrasing doesn't matter much I've found. Yes, it's ambiguous (what counts as "over land"?), but these edge cases aren't a problem for our purposes. Everything we leave up to interpretation is another small insight we gain into the model.

Next, we simply find within the model's output the logprobs for "Land" and "Water"[2](https://outsidetext.substack.com/p/how-does-a-blind-model-see-the-earth#footnote-2-170648368), and softmax the two, giving probabilities that sums to 1.

_Note: If no APIs provide logprobs for a given model, and it's either closed or too unwieldy to run myself, I'll approximate the probabilities by sampling a few times per pixel at temperature 1._

From there, we can put all the probabilities together into an image, and view our map. The output projection will be equirectangular like this:

[![Image 3: Pasted image 20250810184107.png](https://substackcdn.com/image/fetch/$s_!vp4F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa10974a9-3a5e-4492-8f16-55826106e5c0_960x483.png)](https://substackcdn.com/image/fetch/$s_!vp4F!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa10974a9-3a5e-4492-8f16-55826106e5c0_960x483.png)

I remember my 5th grade art teacher would often remind us students to "draw what you see, not what you think you see". This philosophy is why I'm choosing the tedious route of asking the model about every single coordinate individually, instead of just requesting that it generate an SVG map or some ASCII art of the globe; whatever caricature the model spits out upon request would have little to do with its actual geographical knowledge.

By the way, I'm also going to avoid letting things become too benchmark-ey. Yes, I could grade these generated maps, computing the mean squared error relative to some ground truth and ranking the models, but I think it'll soon become apparent how much we'd lose by doing so. Instead, let's just look at them, and see what we can notice.

_Note: This experiment was originally going to be a small aside within a larger post about language models and geography (which I'm still working on), but I decided it'd be wiser to split it off and give myself space to dig deep here._

We'll begin with 500 million parameters and work our way up. Going forward, most of these images are at a resolution of 2 degrees by 2 degrees per pixel.

And, according to the smallest model of Alibaba's Qwen series, it's all land. At least I could run this one on my laptop.

> _The sun beat down through a sky that had never seen clouds. The winds swept across an earth as smooth as glass._[3](https://outsidetext.substack.com/p/how-does-a-blind-model-see-the-earth#footnote-3-170648368)

[![Image 4: Screenshot 2025-08-08 at 10.42.18 PM.png](https://substackcdn.com/image/fetch/$s_!H7Gj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a8e3fa3-5c87-4528-8fa0-5fed822ad790_1922x1112.png)](https://substackcdn.com/image/fetch/$s_!H7Gj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a8e3fa3-5c87-4528-8fa0-5fed822ad790_1922x1112.png)

Tripling the size, there's definitely _something_ forming. "The northeastern quadrant has stuff going on" + "The southwestern quadrant doesn't really have stuff going on" is indeed a reasonable first observation to make about Earth's geography.

[![Image 5: Screenshot 2025-08-08 at 10.31.58 PM.png](https://substackcdn.com/image/fetch/$s_!iR05!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb5ea00c-4a63-4e9f-9bef-9d24f5985967_1906x1120.png)](https://substackcdn.com/image/fetch/$s_!iR05!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb5ea00c-4a63-4e9f-9bef-9d24f5985967_1906x1120.png)

> _And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so. And God called the dry land Earth; and the gathering together of the waters called he Seas._

[![Image 6: Screenshot 2025-08-08 at 10.48.52 PM.png](https://substackcdn.com/image/fetch/$s_!vcgw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F276a70b6-ed1c-4f30-b60d-bdc27f74c9e3_1920x1124.png)](https://substackcdn.com/image/fetch/$s_!vcgw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F276a70b6-ed1c-4f30-b60d-bdc27f74c9e3_1920x1124.png)

At 7 billion parameters, Proto-America and Proto-Oceania have split from Proto-Eurasia. Notice the smoothness of these boundaries; this isn't at all what we'd expect from rote memorization of specific locations.

[![Image 7: Screenshot 2025-08-08 at 11.14.45 PM.png](https://substackcdn.com/image/fetch/$s_!jdha!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52383c2b-0dc4-4069-9048-b088310e1742_1896x1108.png)](https://substackcdn.com/image/fetch/$s_!jdha!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52383c2b-0dc4-4069-9048-b088310e1742_1896x1108.png)

We've got ~Africa and ~South America! Note the cross created by the `(x,x)` pairs.

[![Image 8: Screenshot 2025-08-09 at 2.05.08 AM.png](https://substackcdn.com/image/fetch/$s_!Rb_N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2662033d-94a3-47d7-ace8-f04c2f84a5dd_1892x1106.png)](https://substackcdn.com/image/fetch/$s_!Rb_N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2662033d-94a3-47d7-ace8-f04c2f84a5dd_1892x1106.png)

Sanding down the edges.

[![Image 9: Screenshot 2025-08-09 at 2.47.10 AM.png](https://substackcdn.com/image/fetch/$s_!xw5Y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eb7856b-0eb2-4695-a6a2-41540fd0ec39_1890x1112.png)](https://substackcdn.com/image/fetch/$s_!xw5Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eb7856b-0eb2-4695-a6a2-41540fd0ec39_1890x1112.png)

Pausing our progression for a moment, the coder variant of the same base model isn't doing nearly as well. Seems like the post-training is fairly destructive:

[![Image 10: Screenshot 2025-08-10 at 4.59.32 PM.png](https://substackcdn.com/image/fetch/$s_!J3oF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35083ac7-e3ea-4b8f-8b6a-3a8f5169b90e_1890x1110.png)](https://substackcdn.com/image/fetch/$s_!J3oF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35083ac7-e3ea-4b8f-8b6a-3a8f5169b90e_1890x1110.png)

Back to the main lineage. Isn't it pretty? We're already seeing some promising results from pure scaling, and plenty larger models lie ahead.

[![Image 11: Pasted image 20250807193403.png](https://substackcdn.com/image/fetch/$s_!rLcx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2384f4a-7ecb-40ec-9af5-a940898d3cf1_947x553.png)](https://substackcdn.com/image/fetch/$s_!rLcx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2384f4a-7ecb-40ec-9af5-a940898d3cf1_947x553.png)

Qwen 3 coder has 480 billion parameters with experts of size 35b.

(As we progress through the different families of models, it'll be interesting to notice which recognize the existence of Antarctica.)

[![Image 12: Pasted image 20250807195639.png](https://substackcdn.com/image/fetch/$s_!3RxF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb228d9ef-87c3-4aa5-bd4a-931cf2d4ce7d_947x553.png)](https://substackcdn.com/image/fetch/$s_!3RxF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb228d9ef-87c3-4aa5-bd4a-931cf2d4ce7d_947x553.png)

This one's DeepSeek-V3, among the strangest models I've interacted with. More [here](https://outsidetext.substack.com/p/anomalous-tokens-in-deepseek-v3-and).

[![Image 13: Pasted image 20250807201437.png](https://substackcdn.com/image/fetch/$s_!MTfE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79da7c82-33d7-4d65-80c3-8f41d3f60aa6_947x553.png)](https://substackcdn.com/image/fetch/$s_!MTfE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79da7c82-33d7-4d65-80c3-8f41d3f60aa6_947x553.png)

Prover seems basically identical. Impressive knowledge retention from the V3 base model. Qwen could take notes.

_(n=4 approximation)_

[![Image 14: Pasted image 20250808183812.png](https://substackcdn.com/image/fetch/$s_!OAf8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc93d950e-95f7-41bb-9f0b-6e52692031ca_947x553.png)](https://substackcdn.com/image/fetch/$s_!OAf8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc93d950e-95f7-41bb-9f0b-6e52692031ca_947x553.png)

I like Kimi a lot. Much like DeepSeek, it's massive and ultra-sparse (1T parameters, each expert 32b parameters).

[![Image 15: Pasted image 20250807141130.png](https://substackcdn.com/image/fetch/$s_!AIWU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf7658ca-5f61-4e16-b398-96139d8c9a5c_947x553.png)](https://substackcdn.com/image/fetch/$s_!AIWU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf7658ca-5f61-4e16-b398-96139d8c9a5c_947x553.png)

The differences here are really interesting. Similar shapes in each, but remarkably different "fingerprints" in the confidence, for lack of a better word.

[![Image 16: Screenshot 2025-08-07 at 5.54.54 PM 3.png](https://substackcdn.com/image/fetch/$s_!dNXF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa31508f1-a2d4-4b66-8367-ecbdbf2bb227_2360x1374.png)](https://substackcdn.com/image/fetch/$s_!dNXF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa31508f1-a2d4-4b66-8367-ecbdbf2bb227_2360x1374.png)

As a reminder, that’s 176 billion total parameters. I’m curious what’s going (on/wrong) with expert routing here; deserves a closer look later.

[![Image 17: Pasted image 20250807191034.png](https://substackcdn.com/image/fetch/$s_!lBVH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8de7700e-3468-4d95-b596-68ffaf2755c7_947x553.png)](https://substackcdn.com/image/fetch/$s_!lBVH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8de7700e-3468-4d95-b596-68ffaf2755c7_947x553.png)

[![Image 18: Pasted image 20250807181521.png](https://substackcdn.com/image/fetch/$s_!Dcag!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f947120-e423-4ca2-864d-8db2b3b75b1b_947x553.png)](https://substackcdn.com/image/fetch/$s_!Dcag!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f947120-e423-4ca2-864d-8db2b3b75b1b_947x553.png)

First place on aesthetic grounds.

[![Image 19: Pasted image 20250807155913.png](https://substackcdn.com/image/fetch/$s_!SdJA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b2d2dd-a8d1-4eeb-b311-303e279aea3e_947x553.png)](https://substackcdn.com/image/fetch/$s_!SdJA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b2d2dd-a8d1-4eeb-b311-303e279aea3e_947x553.png)

Wow, best rendition of the Global West so far. I suspect this being the only confirmed dense model of its size something to do with the quality.

[![Image 20: Pasted image 20250807161036.png](https://substackcdn.com/image/fetch/$s_!WD_a!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F188c02f5-b4d2-4185-9875-40e9fdd1975b_947x553.png)](https://substackcdn.com/image/fetch/$s_!WD_a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F188c02f5-b4d2-4185-9875-40e9fdd1975b_947x553.png)

In case you were wondering what hermes-ification does to 405b. Notable increase in confidence (mode collapse, [more pessimistically](https://www.lesswrong.com/posts/t9svvNPNmFf5Qa3TA/mysteries-of-mode-collapse)).

[![Image 21: Pasted image 20250808151532.png](https://substackcdn.com/image/fetch/$s_!_2tg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd17a0b42-8374-4c43-87eb-2099338e0b8d_947x553.png)](https://substackcdn.com/image/fetch/$s_!_2tg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd17a0b42-8374-4c43-87eb-2099338e0b8d_947x553.png)

Most are familiar with the LLaMA 4 catastrophe, so this won't come as any surprise. Scout has 109 billion parameters and it's still put to shame by 3.1-70b.

[![Image 22: Pasted image 20250807161812.png](https://substackcdn.com/image/fetch/$s_!q_TA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdeef260e-b9eb-40ab-95e7-378de36172b2_947x553.png)](https://substackcdn.com/image/fetch/$s_!q_TA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdeef260e-b9eb-40ab-95e7-378de36172b2_947x553.png)

Bleh. Maverick is the 405b equivalent, in case you forgot. I imagine that the single expert routing isn't helping it develop a unified picture.

[![Image 23: Pasted image 20250807161437.png](https://substackcdn.com/image/fetch/$s_!kLvc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2034843c-b132-4f04-a953-1310d092b48b_947x553.png)](https://substackcdn.com/image/fetch/$s_!kLvc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2034843c-b132-4f04-a953-1310d092b48b_947x553.png)

Ringworld-esque.

[![Image 24: Screenshot 2025-08-08 at 11.48.23 PM.png](https://substackcdn.com/image/fetch/$s_!U5it!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc70c5615-5cf4-4167-89c2-042a11e62163_1912x1122.png)](https://substackcdn.com/image/fetch/$s_!U5it!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc70c5615-5cf4-4167-89c2-042a11e62163_1912x1122.png)

I was inconvenienced several times trying to run this model on my laptop, so once I finally did get it working, I was so thrilled that I decided to take my time and render the map at 4x resolution. Unfortunately it makes every other image look worse in comparison, so it might have been a net negative to include. Sorry.

[![Image 25: Screenshot 2025-08-09 at 1.09.55 AM.png](https://substackcdn.com/image/fetch/$s_!MPOS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6e19a94-cc2e-4ed4-8bd2-95d83628495c_1894x1116.png)](https://substackcdn.com/image/fetch/$s_!MPOS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6e19a94-cc2e-4ed4-8bd2-95d83628495c_1894x1116.png)

[![Image 26: Pasted image 20250807190241.png](https://substackcdn.com/image/fetch/$s_!kwrZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafb31a8b-696d-4f06-8294-79760ba78d8c_947x553.png)](https://substackcdn.com/image/fetch/$s_!kwrZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafb31a8b-696d-4f06-8294-79760ba78d8c_947x553.png)

[![Image 27: Pasted image 20250807183509.png](https://substackcdn.com/image/fetch/$s_!6qyn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec4373d3-686b-4282-8763-b0bd72c1907c_947x553.png)](https://substackcdn.com/image/fetch/$s_!6qyn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec4373d3-686b-4282-8763-b0bd72c1907c_947x553.png)

These are our first sizable multimodal models. You might object that this defeats the title of the post ("it's not blind!"), but I suspect current multimodality is so crude that any substantial improvement to the model's unified internal map of the world would be a miracle. Remember, we're asking it about individual coordinates, one at a time.

[![Image 28: Screenshot 2025-08-08 at 3.52.48 PM.png](https://substackcdn.com/image/fetch/$s_!fYF7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F942390c2-3bd9-4c8b-9748-1aa9fa3fb304_2406x1402.png)](https://substackcdn.com/image/fetch/$s_!fYF7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F942390c2-3bd9-4c8b-9748-1aa9fa3fb304_2406x1402.png)

[Colossus](https://x.ai/colossus) works miracles.

[![Image 29: Pasted image 20250807144854.png](https://substackcdn.com/image/fetch/$s_!uZtg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe238c87-9000-437e-9c87-ad65ca990e25_947x553.png)](https://substackcdn.com/image/fetch/$s_!uZtg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe238c87-9000-437e-9c87-ad65ca990e25_947x553.png)

GPT-3.5 had an opaqueness to it that no later version did. Out of all the models I've tested, I think I was most excited to get a clear glimpse into it.

[![Image 30: Pasted image 20250807164513.png](https://substackcdn.com/image/fetch/$s_!-IUb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd39b7ba1-84e6-4641-a55e-5544cd74caa3_947x553.png)](https://substackcdn.com/image/fetch/$s_!-IUb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd39b7ba1-84e6-4641-a55e-5544cd74caa3_947x553.png)

Lower resolution because it's expensive.

[![Image 31: Pasted image 20250807002623.png](https://substackcdn.com/image/fetch/$s_!T2pp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1b7461f-f3b6-41d0-818a-da565959f2b5_947x553.png)](https://substackcdn.com/image/fetch/$s_!T2pp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1b7461f-f3b6-41d0-818a-da565959f2b5_947x553.png)

Wow, easy to forget just how much we were paying for GPT-4. It costs orders of magnitude more than Kimi K2 despite having the same size. Anyway, comparing GPT-4's performance to other models, this tweet of mine feels vindicated:

[![Image 32: Screenshot 2025-08-10 at 6.52.00 PM.png](https://substackcdn.com/image/fetch/$s_!vY1A!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5baf0c0f-c698-428d-bc25-e1951402b766_1178x392.png)](https://substackcdn.com/image/fetch/$s_!vY1A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5baf0c0f-c698-428d-bc25-e1951402b766_1178x392.png)

[![Image 33: Pasted image 20250807003248.png](https://substackcdn.com/image/fetch/$s_!JU8H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff192474c-7ee1-4d40-887a-3ef92d02abb0_947x553.png)](https://substackcdn.com/image/fetch/$s_!JU8H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff192474c-7ee1-4d40-887a-3ef92d02abb0_947x553.png)

Extremely good, enough so to make me think there's synthetic geographical data in 4.1's training set. Alternatively, one might posit that there's some miraculous multimodal knowledge transfer going on, but the sharpness resembles that of the non-multimodal Llama 405b.

[![Image 34: Pasted image 20250807171421.png](https://substackcdn.com/image/fetch/$s_!YisK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F036ccc11-aa91-4805-87be-4b82af9cea4e_947x553.png)](https://substackcdn.com/image/fetch/$s_!YisK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F036ccc11-aa91-4805-87be-4b82af9cea4e_947x553.png)

I imagine model distillation as doing something like this.

[![Image 35: Pasted image 20250807170632.png](https://substackcdn.com/image/fetch/$s_!pkfI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51c8cdc2-3dd4-40bd-9582-9452939d1547_947x553.png)](https://substackcdn.com/image/fetch/$s_!pkfI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51c8cdc2-3dd4-40bd-9582-9452939d1547_947x553.png)

Feels like we hit a phase transition here. Our map does not make the cut for 4.1-nano's precious few parameters.

[![Image 36: Pasted image 20250807004553.png](https://substackcdn.com/image/fetch/$s_!7rcO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4247ab9-64f1-48fd-a7f3-0cf62ca109c0_947x553.png)](https://substackcdn.com/image/fetch/$s_!7rcO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4247ab9-64f1-48fd-a7f3-0cf62ca109c0_947x553.png)

I've heard that Antarctica does look more like an archipelago under the ice.

[![Image 37: Pasted image 20250807165500.png](https://substackcdn.com/image/fetch/$s_!Jyv1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8314e989-4f5d-4ff1-83c6-00eeb0bc1b06_947x553.png)](https://substackcdn.com/image/fetch/$s_!Jyv1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8314e989-4f5d-4ff1-83c6-00eeb0bc1b06_947x553.png)

I'm desperate to figure out what OpenAI is doing differently.

[![Image 38: Pasted image 20250807172214.png](https://substackcdn.com/image/fetch/$s_!YdLD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd59d8687-9e8a-4f12-b66f-7d394d8164b2_947x553.png)](https://substackcdn.com/image/fetch/$s_!YdLD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd59d8687-9e8a-4f12-b66f-7d394d8164b2_947x553.png)

Here's the chat fine-tune. I would not have expected such a dramatic difference. It's just a subtle difference in post-training; Llama 405b's hermes-ification didn't have nearly this much of an effect. I welcome any hypotheses people might have.

[![Image 39: Pasted image 20250808193043.png](https://substackcdn.com/image/fetch/$s_!tzra!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F835e467d-3723-4d62-87fe-eab784d2ee4f_947x553.png)](https://substackcdn.com/image/fetch/$s_!tzra!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F835e467d-3723-4d62-87fe-eab784d2ee4f_947x553.png)

Here's where I'd put GPT-4.5 if the public still had access. To any OpenAI employees reading this, please help a man out.

And no, I'm not forgetting GPT-5. Consider this a living document; I'll add it later once OpenAI remembers to add logprob support.

_(no logprobs provided by Anthropic's API; using n=4 approximation of distribution)_

Claude is costly, especially because I've got to run 4 times per pixel here. If anyone feels generous enough to send some OpenRouter credits, I'll render these in beautiful HD.

[![Image 40: Pasted image 20250807211331.png](https://substackcdn.com/image/fetch/$s_!VnoF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86725253-547c-430e-b227-40eda89a7578_947x553.png)](https://substackcdn.com/image/fetch/$s_!VnoF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86725253-547c-430e-b227-40eda89a7578_947x553.png)

[![Image 41: Pasted image 20250807213356.png](https://substackcdn.com/image/fetch/$s_!u9JL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8f6427c-12c1-4618-9033-eaa9c5e38b14_947x553.png)](https://substackcdn.com/image/fetch/$s_!u9JL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8f6427c-12c1-4618-9033-eaa9c5e38b14_947x553.png)

Opus is Even More Expensive, so for now, the best I can do is n=1.

[![Image 42: Pasted image 20250808191628.png](https://substackcdn.com/image/fetch/$s_!Z2PN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd46e31b5-af72-449a-8c18-d8d3661b85e7_947x553.png)](https://substackcdn.com/image/fetch/$s_!Z2PN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd46e31b5-af72-449a-8c18-d8d3661b85e7_947x553.png)

Few gemini models give logprobs, so all of this is an n=4 approximation too.

1.5 flash is confirmed to be dense[4](https://outsidetext.substack.com/p/how-does-a-blind-model-see-the-earth#footnote-4-170648368). The quality of the map is only somewhat better than that of Gemma 27b, so that might give some indication of its size.

[![Image 43: Pasted image 20250808013729.png](https://substackcdn.com/image/fetch/$s_!jmvC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf52d1e0-de3f-45f9-a252-0ca672f343dc_947x553.png)](https://substackcdn.com/image/fetch/$s_!jmvC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf52d1e0-de3f-45f9-a252-0ca672f343dc_947x553.png)

[![Image 44: Pasted image 20250808002915.png](https://substackcdn.com/image/fetch/$s_!Zs0c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb30a477c-1784-4f43-8ef2-88a15c059470_947x553.png)](https://substackcdn.com/image/fetch/$s_!Zs0c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb30a477c-1784-4f43-8ef2-88a15c059470_947x553.png)

[![Image 45: Pasted image 20250808005108.png](https://substackcdn.com/image/fetch/$s_!PwPB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde152361-1c38-4179-b962-30ec5d706405_947x553.png)](https://substackcdn.com/image/fetch/$s_!PwPB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde152361-1c38-4179-b962-30ec5d706405_947x553.png)

Ran this one at n=8. Apparently more samples do not smooth out the distribution.

[![Image 46: Pasted image 20250808202251.png](https://substackcdn.com/image/fetch/$s_!MjOQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb59e7e43-dcc1-48de-a2d4-272f58fb1ad9_947x553.png)](https://substackcdn.com/image/fetch/$s_!MjOQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb59e7e43-dcc1-48de-a2d4-272f58fb1ad9_947x553.png)

I'm really not sure what's going on with the Gemini series, but it does feels reflective of their ethos. Not being able to get a clear picture isn't helping.

[![Image 47: Pasted image 20250808011415.png](https://substackcdn.com/image/fetch/$s_!AWjR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfeae192-2550-4258-8729-f24480b4e4ca_947x553.png)](https://substackcdn.com/image/fetch/$s_!AWjR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-pos
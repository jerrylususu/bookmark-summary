Title: Are you more likely to die on your birthday?

URL Source: https://pudding.cool/2025/04/birthday-effect/

Markdown Content:
You  
will  
die  
someday.
---------------------------

![Image 1: drawing of a ghost](https://pudding.cool/2025/04/birthday-effect/assets/sketches/ghost.webp)Probably not today.

Would you believe me if I told you that you’re actually **more likely to die on your birthday** than on other days of the year?

This statistical curiosity is called the **birthday effect**.

There have been a bunch of [studies](https://en.wikipedia.org/wiki/Birthday_effect) on different populations that have proven that it’s real.

But I was skeptical (maybe you are too?), so let’s run our own study to understand how–and if–it works.

**The question:**

**Do more people die on their birthdays than expected?**

I live in Massachusetts, so I got data on the 57,010 people who died back in the year 2000.

The first thing we can do is count the number of days a person dies before or after their birthday on a circular calendar.\*

We’ll start with Gus (made-up name), who was born on March 4th, and after 84 years, died on March 4th. **That’s a 0 day difference.**

Two more examples: Gretchen, who was born on May 11th and died on May 2nd–a -9 day difference. And Randall who was also born on May 11th, but died on August 7th–a +87 day difference.

![Image 2: A diagram showing three individuals (Gus, Gretchen, and Randall) and their relationship to a reference point (day 0). Gus is shown at 0 day difference, Gretchen at -9 days, and Randall at +87 days, represented by small squares connected to a vertical dotted line.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/explain.webp)You get the picture. We arrange their relative death dates from -182 to +182 (days before and after birthday, respectively).

![Image 3: A simplified timeline showing three people (Gretchen, Gus, and Randall) positioned along a horizontal axis from -182 to +182 days. Small squares mark their positions, with Gus at day 0, Gretchen slightly to the left, and Randall halfway to the right.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/explain2.webp)We do this for each person and count the number of times each difference occurs. If we expect death dates to be random relative to birthdays, this should look pretty flat. Instead, we can see variation.

![Image 4: A bar chart showing daily death counts before and after a reference point (marked with a birthday cake icon). The x-axis spans from -182 to +182 days. Gray vertical bars represent daily death counts averaging around 150, with minor fluctuations across the entire time period. The zero-day red bar is one of the tallest.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/all-2000.webp)Interesting…But what we care about most is how many observations are on the zero day difference. Is there a spike? **Enhance!**

![Image 5: A bar chart showing “183 birthday deaths” with the peak highlighted in red. The x-axis spans from -20 to +20 days difference, with 0 at center. The average is noted as 156. Gray bars represent daily death counts around 150-160.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/enhance.webp)There are **17% excess birthday deaths** compared to the average day difference.

We did it, we found the birthday effect!

**But…**

Look at this. Did you notice that just 12 days after birthday deaths is nearly as high? Does that mean there is a “12-days-after-a-birthday effect,” too?

![Image 6: A bar chart showing “183 birthday deaths” with the peak highlighted in red. The x-axis spans from -20 to +20 days difference, with 0 at center. The bar +12 days after is highlighted in teal and has a value of 181.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/other.webp)Maybe. But this could be a **sample size problem.** It’s like trying to detect a rigged coin with just 10 flips. Getting six heads instead of the expected five wouldn’t prove much–you’d need more tests. The same applies to our data.

57,010 observations might seem like a lot, but not when you spread them over 365 days.

And there will always be some natural variation due to random chance since this is real life. So, **is the zero day difference due to random chance or not?** To answer this, we need to first know how much the data vary from the average. We start by figuring out how spread out the data is.

Here are all day differences sorted by magnitude. You can see that birthdays (day difference = 0) have one of the highest death frequencies.

![Image 7: A sorted bar chart titled “sorted day differences” showing values from 119 deaths to the highest values near 200. The average is marked as 153. Eight red bars at the right end are labeled “8 days with 180-185 deaths” with the highest bar marked with “183” and a cake icon.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/sorted.webp)To see the broader trend, let’s group our day difference values into buckets of five. In the chart above, there are **eight day differences with values between 180-185**, including birthday deaths. That makes up one bucket. We tally up the count for all other buckets, and get the histogram below.

![Image 8: A histogram showing “distribution of death counts” with x-axis labeled “buckets of values” from 115-120 to 190-195. The middle bucket highest frequency is labeled 58. The 180-185 bucket is highlighted in red labeled as “8”, and includes a cake icon pointing at it with “183 deaths.”](https://pudding.cool/2025/04/birthday-effect/assets/sketches/histogram.webp)You’ll notice a balanced-looking, slight bell shape–this is important. It is called a **normal distribution** or “bell curve.”

If we measure the spread, we find that many values–about 68%–fall within a certain range (+/- 13) of the average (156 deaths). This range (143-169) is what statisticians call **one standard deviation.**

This 68% pattern is a key feature of bell curves–[a mathematical rule](https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule) that shows up everywhere in nature and statistics.

![Image 9: A histogram showing “approximate standard deviations” with death counts distributed across value buckets from 115-120 to 190-195. Areas are color-coded to show: gray for within 1 standard deviation, teal for 1+ standard deviation, and red for 2+ standard deviations.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/stddev.webp)We expect most (95%) values to fall within two standard deviations. That means anything from 130-182 is normal variation–expected random noise in our data. Birthday deaths are a hair higher, at just over 2 standard deviations.

This normal variation in the data makes it hard to spot subtle patterns–like the birthday effect. We need a large enough sample to see if that birthday spike is truly meaningful or just random noise.

So I got data of every person who died in Massachusetts from 1990-2024. When we look at more years, we can see the noise factor play out more clearly. Some years, like 1999, will show a strong birthday effect.

![Image 10: A bar chart showing daily death counts before and after a reference point (marked with a birthday cake icon). The x-axis spans from -182 to +182 days. Gray vertical bars represent daily death counts averaging around 150, with minor fluctuations across the entire time period. The zero-day red bar is one of the tallest.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/all-1999.webp)While other years, like 2002, might show nothing at all.

![Image 11: A bar chart showing daily death counts before and after a reference point (marked with a birthday cake icon). The x-axis spans from -182 to +182 days. Gray vertical bars represent daily death counts averaging around 150, with minor fluctuations across the entire time period. The zero-day red bar is one of the shortest.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/all-2002.webp)But if we combine all 35 years I have (1990-2024), with nearly 2 million observations–5,358 per day difference–random fluctuations start to cancel out. This improves our ability to be more confident in our findings.

![Image 12: A bar chart showing daily death counts before and after a reference point (marked with a birthday cake icon). The x-axis spans from -182 to +182 days. Gray vertical bars represent daily death counts averaging around 5,000, with minor fluctuations across the entire time period. The zero-day red bar is one of the tallest.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/all.webp)For good measure, let’s enhance this too.

![Image 13: A bar chart showing “5,728 birthday deaths” with the peak highlighted in red. The x-axis spans from -20 to  20 days difference, with 0 at center. The average is noted as 5,358. Gray bars represent daily death counts around 5,300.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/enhance-all.webp)Now we see **6.9% excess birthday deaths**. This is more promising.

**But…**

How confident can we be that our results are **statistically significant,** and how do we measure this?

Z-Tests and p-values baby!

![Image 14: screenshot from A Beautiful Mind of a person and a chalkboard](https://pudding.cool/2025/04/birthday-effect/assets/chalkboard.webp)To test significance, we start with the **null hypothesis**–we assume there is nothing special happening here. In our case:

> “There is no birthday effect. Deaths occur randomly throughout the year regardless of birthdays.”

Then we ask ourselves, how likely would we see this birthday spike by pure chance alone if our null hypothesis were true?

We just need three ingredients to calculate a z-score: actual number of deaths (observed), daily average (expected), and how much it varies (standard deviation). Hey! We know all about the last one now, so we can put it to use.

`(observed - expected) / std. dev. = z-score`Plugging in the values from our 1,955,588 observations:

`(5,728 - 5,358) / 74 = 5`Our **z-score of 5** is incredibly strong, which tells us this is well beyond normal variation.

Converting this to a **p-value** tells us the probability of seeing this extreme result, if the null hypothesis were true and there was no birthday effect.

Our p-value is ~0.000001, meaning there’s less than a 0.0001% chance we’d see this birthday effect if deaths were actually random.

![Image 15: screenshot from Dumb and Dumber “you’re telling me there’s a chance”](https://pudding.cool/2025/04/birthday-effect/assets/chance.webp)Since that chance is so low, it is a near-certainty that this isn’t due to normal variation. Statisticians typically consider any p-value below 0.05 to be significant enough to reject the null hypothesis, and we’re **way** below that threshold.

Therefore, the birthday effect is real **and** statistically significant!

**But…**

(\*sighs\* coming from you)

Births and deaths aren’t evenly spread throughout the year. Winter months see more deaths from flu and cold weather, while birth patterns have their own seasonal rhythm.

![Image 16: A bar chart showing births and deaths per month over a year, from January to December. Births (in teal) range from 160,802 to 165,570 per month, displayed as bars extending downward. Deaths (in red) range from 149,606 to 187,356 per month, displayed as bars extending upward. January and June are labeled on the x-axis. The chart shows more deaths than births in most months, with January having the highest death count at 187,356.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/months.webp)Take January in Massachusetts: 8.5% of people are born then, but 9.6% of all deaths happen in January. This means January-born people would naturally show **13% more birthday deaths** just because January is a high-mortality month–regardless of some birthday effect.

`9.6% ÷ 8.5% = **1.13**`To find a true birthday effect, we need to adjust for these seasonal patterns. Otherwise, we’re just measuring when people tend to die anyway.

One way to control for seasonality is to compare expected deaths to observed deaths on birthdays, **after** accounting for seasonal patterns. Here’s how it works:

Imagine a tiny world of **100 people and just three days a year**: day A, day B, and day C. Here is how many people were born and died on each day:

![Image 17: A table titled “In a three-day year world with 100 people” showing births and deaths by day. Day A: 40 births, 40 deaths; Day B: 30 births, 40 deaths; Day C: 30 births, 20 deaths. The data is color-coded with births in teal and deaths in red.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/world.webp)Since we are using 100 people, these numbers also represent the percent of people who are born and die on each day. If birth dates and death dates were completely unrelated (our null hypothesis), what would we expect to see?

For someone born on day A (40 people), there’s a 40% chance they’ll die on day A, a 40% chance on day B, and a 20% chance they’ll die on day C. To calculate the chance someone is born and dies on a given day, we simply multiply them together:

`birth %  × death % = % of all people`So for day A people, there is a 16% chance they die on their birthday.

`40% × 40% = 16%`![Image 18: A grid labeled “birth/death day combination %” showing the percentage distribution between birth days (A, B, C) on the y-axis and death days (A, B, C) on the x-axis. An annotation reads “40% × 40% = 16%” connecting to the A-A cell. The grid shows percentages for combinations of birth days (A, B, C) and death days (A, B, C). Values in the grid include: A-A: 16%, A-B: 16%, A-C: 8%, B-A: 12%, B-B: 12%, B-C: 6%, C-A: 12%, C-B: 12%, C-C: 6%.](https://pudding.cool/2025/04/birthday-effect/assets/sketches/grid.webp)We can calculate the expected percentage for each birth-death combination for all nine day possibilities, which represents 100% of all outcomes. What we’re most interested in is the diagonal of this grid–where birth day equals death day. These are our birthday deaths.

![Image 19: A grid labeled “birth/death day combination %” showing the percentage distribution between birth days (A, B, C) on the y-axis and death days (A, B, C) on the x-axis. Values in the grid include: A-A: 16% (boxed), A-B: 16%, A-C: 8%, B-A: 12%, B-B: 12% (boxed), B-C: 6%, C-A: 12%, C-B: 12%, C-C: 6% (boxed).](https://pudding.cool/2025/04/birthday-effect/assets/sketches/diagonal.webp)The grid basically says: “Even though more people die on day A, we’re taking that into account for each specific birthday, so any excess deaths on birthdays must be due to something else.”

Adding these up, without any birthday effect, we’d **expect 34% of people** to die on their birthday by pure chance in this tiny world. This gives us a baseline to compare against that accounts for seasonal effects.

Now let’s bring this back to the real world with 365 days and our Massachusetts data. We'll use the same approach, just with a much, much bigger grid (133,225 combinations). After plugging in the numbers, we get an expected value of 5,355 birthday deaths, and observation of 5,728 deaths.

**There are 7.0% excess birthday deaths in Massachusetts.**

This means we can **definitively** say there is still an effect that has nothing to do with seasonal factors, but rather, ✨something else. ✨

**But…**

Why is there a birthday effect at all?

One popular idea centers on the psychological impact of death postponement versus anniversary reaction: Does the looming birthday cause people to postpone death until after they’ve celebrated their special day, or does the birthday itself somehow trigger mortality?

Other studies have shown a significant spike in deaths on and near birthdays. [Peña’s study](https://www.sciencedirect.com/science/article/abs/pii/S0277953614008120) of 25 million U.S. deaths (1998-2011) found a 6.7% excess of birthday deaths, while [Ajdacic-Gross’s study](https://www.sciencedirect.com/science/article/abs/pii/S104727971200110X) of Swiss deaths (1969-2008) found a 13.8% excess.

Peña noted that “no evidence is found of dips in average excess death rates in a ±10 day neighborhood around birthdays that could offset the spikes on birthdays.” Like these other large studies, I didn't find any significance with a postponement effect.

These studies also stratify the data to examine differences across gender, age, or cause of death. Unlike Peña, who found that “younger people have greater average excess death rates on birthdays,” I actually found that the birthday effect was stronger in older versus younger people.

The only additional noteworthy finding after stratification was that accidental deaths showed 35% excess deaths on birthdays in Massachusetts, supporting a theory around celebratory behavior. As Ajdacic-Gross observed on deaths by accident and suicide, “the most plausible interpretation is related to the use of alcohol, which is a well-known risk factor in suicidal behavior.”

**So what have we learned?**

The birthday effect shows that mortality isn’t just about biology and random chance; it’s influenced by social constructs and personal significance. This research reminds us that data can reveal hidden patterns in human experience that we might otherwise miss.

The differing results across studies highlight how methodological choices—from sample selection to statistical analysis—can dramatically shape our findings. When studying something as basic as birthdays and death, how we approach the problem shapes what answers we find.

![Image 20: drawing of a birthday cake and a ghost below it](https://pudding.cool/2025/04/birthday-effect/assets/sketches/cake-ghost.webp)**Data and methods**

Massachusetts death data was obtained via FOIA from the Registry of Vital Records and Statistics (RVRS). Data excludes deaths where the age is under one and half years old, birth or death dates on February 29, and missing birth or death dates.

\* Note: a circular calendar was used to compare dates on 365 days and excluded leap days. This approach was standard across studies in order to simplify calculations.

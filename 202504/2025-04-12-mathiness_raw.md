Title: Mathiness

URL Source: https://www.votito.com/methods/mathiness/

Markdown Content:
_Mathiness_ is a term for calculations and formulas that may look and feel like rigorous mathematics but lack true analytical rigor or validity, and often disregard logical coherence or factual accuracy.

The term was first used by Paul M. Romer in the paper [Mathiness in the Theory of Economic Growth](https://www.aeaweb.org/articles?id=10.1257/aer.p20151066). Carl Bergstrom and Jevin West use it as one of the criteria to spot bullshit in the book [Calling Bullshit](https://amzn.to/3XZ6FPa).

Many estimation and scoring methods used in product management tend to fall into the category of bullshit under the definition of mathiness. This is not necessarily an issue if such methods are used informally and expecting a wide margin of error, but it can become horribly misleading and dangerous when those formulas are used expecting scientific rigour.

*   [Fake physics formulas imply relevance](https://www.votito.com/methods/mathiness/#fake-physics-formulas-imply-relevance)
*   [Precision is not the same as accuracy or correctness](https://www.votito.com/methods/mathiness/#precision-is-not-the-same-as-accuracy-or-correctness)
*   [Errors compound in complex ways](https://www.votito.com/methods/mathiness/#errors-compound-in-complex-ways)
*   [Fixing mathiness](https://www.votito.com/methods/mathiness/#fixing-mathiness)
    *   [Compare orders of magnitude, not values directly](https://www.votito.com/methods/mathiness/#compare-orders-of-magnitude-not-values-directly)
    *   [Avoid numerical quantities](https://www.votito.com/methods/mathiness/#avoid-numerical-quantities)
    *   [Assign scores to buckets consistently](https://www.votito.com/methods/mathiness/#assign-scores-to-buckets-consistently)

> New-school bullshit uses the language of math and science and statistics to create the impression of rigor and accuracy.
> 
> – Bergstrom and West

Fake physics formulas imply relevance
-------------------------------------

Many mathiness formulas resemble calculations from popular laws of physics, involving units that cannot logically be combined using basic arithmetic. In Calling Bullshit, the authors give the example of the Virginia Mason Quality Equation `Q = [A✕(O+S)÷W]` (Quality equals Appropriateness times the sum of Outcomes and Service divided by Waste), a [formula used for improving operations management in healthcare](https://www.hfma.org/operations-management/cost-reduction/virginia-mason-institute-transformation-expert-says-healthcare-s/). Noting that the various quantities are measured in totally different units, the authors suggest that calculating the formula mathematically doesn’t even make sense (How would outcomes and service be added? What does it mean to divide the formula by waste? In what units?).

Mathiness formulas usually try to imply some intuitive relationship between various factors and the desired outcome. Factors that are added or multiplied suggest a positive contribution (such as Appropriateness or Outcomes to Quality in VMQE). The factors that are subtracted or divided suggest a negative impact (such as Waste to Quality in VMQE). Multiplications and divisions tend to look more important than adding or subtracting, but there is usually little evidence to support that any of those relationships is correct beyond intuition.

A common example from product management is the [ICE score](https://www.votito.com/methods/ice-score/), which provides a numerical evaluation of a product idea by combining impact, ease of implementation and confidence. Various authors suggest different ways of combining these factors, from simply adding the scores, to averaging them, or even adding impact and ease and then dividing by confidence. There is no serious proof that any of those methods are more or less relevant or accurate than the others.

An even worse example is the DICET formula (Dollars/revenue + ICE + Time-to-money). In this formula, money is added to time, although they are effectively completely different units. Adding two additional components to ICE might seem as DICET is a more rigorous variant, but due to mathiness it might in effect be just bigger bullshit.

Precision is not the same as accuracy or correctness
----------------------------------------------------

In the wider sense, mathiness is a derogatory term for models or methods where using a precise mathematical formula implies scientific results, but it is usually wrong or incorrect. Having a detailed formula might imply credibility or accuracy, but in reality it might have neither.

A wrong method of calculating something can still be very precise, but it may not be accurate or relevant. A trivial example from everyday life would be a thermostat placed outside a house and then used to control the temperature inside the house. The measurement on the thermostat can at the same time be precise but completely incorrect and unsuitable for the stated purpose.

A common example from modern software delivery is using user story points for long-term delivery estimates. Story points are relative numbers primarily intended for measuring short-term implementation complexity. They often get combined in mathematical formulas to calculate long-term time delivery expectations. The result is precise, but unfit for the intended purpose.

Errors compound in complex ways
-------------------------------

Rigorous numerical estimation methods come with specific error estimation and confidence measurements, which often lack from mathiness formulas used in product management. This causes the resulting numbers to be specific and precise, but untrustworthy.

For example, in the book Software By Numbers, the authors suggest assigning a numeric business value to each of the proposed features, then estimating the cost of development for each of the features and combining those numbers for detailed value analysis, to “maximise business returns and minimise risk”. In effect, risk is not measured or tracked at all in those formulas. The revenue estimates can be (and often are) wildly incorrect because they depend on many external factors such as competitor actions, global economy and market trends. The confidence intervals and error estimates for original factors are never calculated or taken in consideration when producing the final scores, making the result arbitrarily wrong or right, and generally meaningless.

Fixing mathiness
----------------

Formulas suffering from mathiness can still be useful for relative comparisons and back-of-the-napkin calculations that will later be re-evaluated through product experimentation or A/B testing. In effect, it’s OK to use a mathiness formula when it’s not important to select the mathematically optimal choice, but instead it’s enough to just reduce uncertainty to an acceptable level.

There are several strategies for fixing mathiness and getting more relevant results.

### Compare orders of magnitude, not values directly

One good strategy is to not trust the individual numbers, but their relative size. Something scored 5 is usually worse than something scored 200, but it may not necessarily be better or worse than something scored 9.

Using orders of magnitude for relative comparisons can reduce the effects of compounded errors, and avoid mistaking precision for accuracy.

### Avoid numerical quantities

Another common way to fix mathiness is to avoid implying numerical quantities, in particular when the results are used for relative comparisons. A typical trick is to use T-shirt sizes (S, M, L, XL) for effort estimation instead of a specific number. Without a numerical value, such estimates cannot be misused easily in mathematical formulas.

### Assign scores to buckets consistently

If you must use numerical quantities in order to include them in arithmetic calculations, a common trick to increase relevance is to specify strict, consistent ways to translate different concepts into discrete buckets of numerical quantities.

For example, Itamar Gilad’s [Confidence Meter](https://www.votito.com/methods/confidence-meter/) attempts to make the Confidence component of the ICE score consistent and strict by assigning a specific numerical value to different types of supporting evidence. A Powerpoint slide deck would get the confidence score of 0.01, and an A/B test would get a score of 5. Ease could be similarly scored by assigning time-based estimates to various buckets. Items that take less than one week could get a score of 10, items that take a few weeks a score of 5, and items that take more than a few months a score of 1.

This trick makes the formulas logically computable (summing up bucket scores makes more sense than adding time to gut-feel confidence intervals). Having consistent bucket assignments also makes such scores consistent over time. However, the assignment still relies on somehow figuring out the appropriate values for buckets. That tends to be context specific, and may require adjustments and iterating over the bucket values a few times to get the right ratios.

A good option to reduce errors is to avoid a linear scale. For example, the difference between the bucket value for 10 weeks should not be twice the bucket value for 5 weeks. Potentially good options are to use different orders of magnitude, a logarithmic or an exponential scale, or using numbers from the Fibonacci sequence. Such assignments can help to avoid a linear correlation between the observed quantities and the bucket values.

Learn more about Mathiness
--------------------------

*   [Calling Bullshit: The Art of Skepticism in a Data-Driven World](https://amzn.to/3XZ6FPa), ISBN 978-0525509202, by Carl T. Bergstrom, Jevin D. West (2020)
*   [Mathiness in the Theory of Economic Growth](https://www.aeaweb.org/articles?id=10.1257/aer.p20151066), American Economic Review, vol. 105, no. 5, ISSN 0002-8282 by Paul M. Romer (2015)

* * *

**Next article**: [Novelty Effect](https://www.votito.com/methods/novelty-effect/) [All articles](https://www.votito.com/methods/)

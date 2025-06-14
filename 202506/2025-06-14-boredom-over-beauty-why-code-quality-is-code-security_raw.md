Title: Boredom Over Beauty: Why Code Quality is Code Security

URL Source: https://blog.asymmetric.re/boredom-over-beauty-why-code-quality-is-code-security/

Published Time: 2025-06-03T16:58:41.000Z

Markdown Content:
Jun 3, 2025· 5 min read

Some of the most devastating vulnerabilities stem from complexity, inconsistency, and chaos. This post explains why predictable, well-formed code is the foundation of security.

*   [John Saigle](https://blog.asymmetric.re/author/john/)

Some of the most devastating vulnerabilities stem from complexity, inconsistency, and chaos. This post explains why predictable, well-formed code is the foundation of security.

![Image 1: Boredom Over Beauty: Why Code Quality is Code Security](https://blog.asymmetric.re/content/images/size/w30/2025/05/Boredom-Beauty.png)

The blockchain space often seems to be slowly reinventing security concepts and practices that are well-established in "traditional" security. These hard-won lessons are worth studying if we want better security across the industry.

One of the key principles history offers is this: Code quality versus code security is a false dichotomy. Code quality _is_ code security.

Code quality changes often go unnoticed, relegated to the "informational" sections of audit reports, or even dismissed as pedantic distractions that detract from real security work. But this is missing the point.

When projects focus primarily on identifying and patching discrete vulnerabilities—the "known knowns" produced by private audits, audit contests, and bug bounties—they adopt a reactive approach that resembles culling rotten fruit or eliminating pests in an orchard. While necessary, this approach addresses only the visible manifestations of deeper problems—the symptoms rather than the disease itself. In contrast, investing in code quality is like improving soil health and strengthening root systems. The former makes for great incident reports and social media posts; the latter creates conditions for sustained resilience.

Rocket Engineering as Applied to Moonshots
------------------------------------------

History offers compelling evidence for this relationship. Projects where failure carries extreme consequences invariably implement rigorous code quality standards as a foundation for security. NASA's Jet Propulsion Laboratory, responsible for controlling spacecraft worth billions of dollars operating millions of miles from Earth, enforces some of the strictest coding standards you'll find. Their [Power of Ten rules](https://spinroot.com/gerard/pdf/P10.pdf?ref=blog.asymmetric.re) establish clear guidelines designed to eliminate entire classes of bugs before they occur.

Similarly, the curl project, which powers data transfers for billions of devices worldwide, maintains exceptional security despite its widespread deployment by adhering to [strict code quality practices](https://daniel.haxx.se/blog/2025/04/07/writing-c-for-curl/?ref=blog.asymmetric.re). The TigerBeetle project demonstrates how extreme performance requirements necessitate exceptional code discipline. Their [style guide](https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md?ref=blog.asymmetric.re) recognizes that "code, like steel, is less expensive to change while it's hot. A problem solved in production is many times more expensive than a problem solved in implementation or a problem solved in design."

These examples aren't coincidental. Mission-critical systems require readable, maintainable code—not as a luxury, but as a prerequisite for security and reliability. When code is well-structured, consistently formatted, and adheres to clear patterns, security vulnerabilities become easier to identify and harder to introduce. Codebases characterized by inconsistency, complexity, and poor organization create fertile ground for security flaws.

Seeing Like a State Machine: The Security Benefits of Legible Code
------------------------------------------------------------------

James C. Scott's influential work _Seeing Like a State_ explores how governments historically sought to make complex systems more "legible" through standardization and simplification. Before the emergence of strong centralized nation-states, local communities lacked standardization—languages differed widely across small regions, measurement systems varied from town to town, and people were often referred to using location-specific names, such as "John-over-the-hill," rather than static family names.

Encountering a large, dynamic codebase feels something like venturing into one of these autonomous regions. File structure, variable names, and coding practices often display stunning examples of Galápagan diversity.

While Scott rightfully warns that excessive standardization can eliminate valuable diversity and local knowledge, security is one domain where the benefits of standardization outweigh these concerns. We're optimizing for control rather than creativity. This becomes especially important when moving toward security at software scale, beyond what the scarce pool of manual reviewers can achieve.

When we reason about automation, we begin "seeing like a state machine" and can appreciate the security benefits of consistent patterns. Security review works best when code follows predictable patterns that allow us to focus on substance rather than deciphering style. Legible systems facilitate abstraction and summarization, allowing security professionals to understand system behavior without examining every line of code. They permit effective resource allocation in security reviews and reduce the cognitive load required to identify potential vulnerabilities.

Security work is inherently resource-constrained. No organization can examine every line of code with equal scrutiny or protect against every conceivable attack vector. Legible systems allow security teams to develop mental shortcuts and focus on areas of highest risk.

Chasing Boredom, Not Beauty
---------------------------

The most secure code isn't beautiful, clever, or elegant—it's boring. Go, a programming language that exemplifies this philosophy, intentionally omits features that might enable expressive or elegant solutions in favor of simplicity and readability. This apparent limitation produces code that's easier to audit, harder to misuse, and less prone to security vulnerabilities.

Security thrives on predictability, not novelty. As our CEO Jonathan Claudius explained to developers at [Accelerate](https://youtu.be/wZ5IEhkYzQ4?ref=blog.asymmetric.re), "[being boring] is a resistance to chaos. It's an aversion to variance. And what it helps us do is to make fewer irrecoverable bets."

This pursuit of boring excellence extends beyond code itself to encompass documentation, code standards, linting, and review processes. These activities lack the excitement of developing new features or discovering dramatic vulnerabilities, but they form the foundation of secure systems. When technology functions properly, it withdraws from our conscious attention, allowing us to focus on the work itself.

Quality Standards as Security Infrastructure
--------------------------------------------

The guardrails that have long promoted code quality—strict typing, consistent formatting, clear documentation, and comprehensive tests—become even more essential in the age of LLMs. They give us ways to use AI effectively without falling into its traps. When developers use AI tools within well-defined quality frameworks, they can achieve both increased productivity and maintained security.

Code quality practices that benefit human readers similarly assist AI systems. Clear function names, descriptive comments, and logical organization help LLMs understand code intent just as they help human reviewers. AI systems are increasingly able to enforce quality standards by flagging inconsistencies, suggesting improvements, and automating routine aspects of code review.

One common argument against commenting code is that comments are likely to drift away from the actual implementation over time[[1](https://blog.asymmetric.re/boredom-over-beauty-why-code-quality-is-code-security/#footnote-1-anchor)]. This becomes a strength rather than a weakness, as a reviewer (human or otherwise) can use the delta between comment and code as an indication that the developer's intentions don't match the implementation. LLMs are often able to note a discrepancy between a code comment and the implementation and flag this to the author or reviewer.

The Pragmatism of Prevention
----------------------------

The TigerBeetle team's "zero technical debt" policy embodies a crucial insight:

> "We do it right the first time. This is important because the second time may not transpire, and because doing good work that we can be proud of builds momentum."

Getting serious about code quality isn't perfectionism. It's pragmatism. Problems cost more to fix later.

While sophisticated vulnerability scanners and threat detection systems will continue to play an important role, the foundation of secure code lies in quality engineering practices: consistent standards, clear documentation, comprehensive testing, and thoughtful architecture. These are often undervalued but are critical for resilience, especially as development accelerates through AI and automation.

Projects that recognize this relationship—that see code quality as code security—will ship products that are more resilient as the security landscape continues to shift. When developers can trust their foundations and execute without fear, they can build systems that stand the test of time.

[1] This view is unconsciously reinforced by developer tooling, which shades code comments as faded afterthoughts. Instead, they could be displayed in a bright color that demands attention.

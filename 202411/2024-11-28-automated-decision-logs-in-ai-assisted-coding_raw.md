Title: Automated Decision Logs in AI-Assisted Coding

URL Source: https://addyosmani.com/blog/automated-decision-logs/

Markdown Content:
Want more? Subscribe to my free newsletter:

November 26, 2024
-----------------

AI code generation tools like Bolt, v0, Replit Agents, Cursor, and even GitHub Copilot promise increased productivity. But treating them as black boxes is a recipe for long-term pain. Especially in complex projects, we need to understand _why_ the AI made certain choices, not just what code it spat out. That’s where automated decision logs come in.

An Automated Decision Log (ADL) is a targeted, low-overhead mechanism for capturing the reasoning behind significant AI-driven code modifications. Think of it less as a comprehensive log and more as a structured set of notes-to-self, automatically generated.

Implementation:
---------------

Getting a decision log setup and going is relatively straight-forward:

1.  **Project-local log:** Add a file like `fyi.md` or `ai_decisions.log` to your repository.
2.  **Explicit prompting:** Instruct your AI explicitly. Something like:

    Make sure to keep a log of what, why and how you did what you did in fyi.md. Keep it updated.

1.  **Verification is key:** Don’t trust, verify. Regularly review the log. It’s your responsibility to ensure it’s accurate. You may need to refine the prompting to get the desired level of detail and clarity.

Here’s an example of such a log in being generated for one of my [Bolt](https://bolt.new/) projects:

Why bother? The tangible benefits
---------------------------------

The purported upsides to logging AI coding decisions are several, but let’s examine them with a critical eye:

*   **Faster onboarding (potentially):** The idea is that new team members can review the log to grasp the project’s history and rationale. This _could_ be faster than digging through code, especially for context on unusual architectural choices or libraries selected by the AI. However, this relies heavily on the AI providing _useful_ explanations, and not just verbose summaries.
*   **Debugging aid (if done right):** When something breaks, having a log of why a specific piece of code was generated could be helpful. It might save you from having to reverse-engineer the AI’s intent, assuming that intent was coherent in the first place.
*   **Traceability (with caveats):** Linking code changes back to initial requirements or user stories is valuable. A well-maintained log could help demonstrate this link. But manually verifying the log’s accuracy remains crucial; blind faith in the AI’s output is a recipe for disaster.
*   **Tool switching/model upgrades (maybe less painful):** If you change AI tools or underlying models, having a history of decisions might help maintain consistency. However, this assumes a degree of interoperability between the logs from different systems which is likely optimistic in the current landscape.
*   **Refining prompts (iterative improvement):** Analyzing the log can reveal where your prompts were unclear or where the AI consistently misinterpreted your intent. This _could_ lead to more effective prompting over time, making the AI a more useful tool.

Why AI-generated logs _might_ be different
------------------------------------------

There are potential advantages to having the AI itself manage the log:

*   **Format consistency:** AI tools excel at structured output, which should lead to more easily parsable and searchable logs.
*   **Real-time updates (mostly):** The log should be updated as the AI works, minimizing the chance of forgetting critical decisions. However, this is dependent on the AI tool’s capabilities.
*   **Potentially deeper context:** The AI _could_ capture nuances and alternatives considered that a human might overlook during rapid coding. Whether it _actually_ does so is another question.

Conclusion
----------

In my experience having an automated decision log is very useful in practice.

It enhances transparency, facilitates knowledge sharing, and serves as a reliable reference for future projects. This practice not only aids in education but also strengthens the overall engineering process, leading to more informed and efficient outcomes.

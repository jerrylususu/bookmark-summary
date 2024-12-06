Title: Roaming RAG – Make the Model Find the Answers

URL Source: http://arcturus-labs.com/blog/2024/11/21/roaming-rag--make-_the-model_-find-the-answers/

Markdown Content:
Let's face it, RAG can be a big pain to set up, and even more of a pain to get right.

There's a lot of moving parts. First you have to set up retrieval infrastructure. This typically means setting up a vector database, and building a pipeline to ingest the documents, chunk them, convert them to vectors, and index them. In the LLM application, you have to pull in the appropriate snippets from documentation and present them in the prompt so that they make sense to the model. _And things can go wrong._ If the assistant isn't providing sensible answers, you've got to figure out if it's the fault of the prompt, the chunking, or the embedding model.

If your RAG application is serving documentation, then there might be an easy alternative. Rather than setting up a traditional RAG pipeline, put the LLM assistant to work. Let _it_ navigate through the documentation and find the answers. I call this _"Roaming" RAG_, and in this post I'll show you how it's done.

![Image 5: Roaming RAG](https://arcturus-labs.com/blog/assets/Roaming_RAG/top_image.png)

The Big Idea
------------

Back in the olden days when the internet was a baby, we didn't have search engines. Instead, companies like Yahoo and Excite attempted to organize the internet into a directory structure. If you wanted to ask the internet how to change your car oil, you would peruse the directory of _everything_, select the Auto section, followed by Maintenance, and then finally the Oil Change section. Then you look at whatever website was lucky enough to be listed in order to figure out how to change your oil. This system worked _horribly_.

However, if you are looking for answers in a relatively small set of well-organized documents, then a hierarchical directory might still be a pretty good approach. For example, when you're reading a tech reference book, how do you find the information you need? You probably open up to the table of contents, then review the chapters and sections that might be useful, and then find the content you're looking for.

It turns out that there are plenty of examples of content that are well-organized and amenable to this type of navigational search. Just to name a few:

*   **Legal code** which organizes the laws into a hierarchy of title, chapter, section, and paragraph.
*   **Technical books** organized into parts, chapters, sections, subsections, and paragraphs.
*   **Product owner’s manuals** structured into sections and topics.
*   **Curriculums or syllabuses** dividing educational content into course overview, units, lessons, and assignments.
*   **Corporate policy manuals** structured by policy area, individual policies, and procedures.

The big idea of Roaming RAG is to craft a simple LLM application so that the LLM assistant is able to read a hierarchical outline of a document, and then rummage though the document (by opening sections) until it finds and answer to the question at hand. Since Roaming RAG directly navigates the text of the document, there is no need to set up retrieval infrastructure, and fewer moving parts means less things you can screw up!

Demo
----

In order to demo Roaming RAG, we'll be looking at llms.txt files because they are typically good examples of the well-structured documents I'm talking about. ... _Wait, you don't know what llms.txt is? Well it's only the new hotness!_

What is llms.txt?

Jeremey Howard proposed llms.txt ([here](https://llmstxt.org/)) as a machine-readable document that is associated with a website. Similar to /sitemap.xml and /robots.txt, llms.txt is intended to be read by machines, and it serves as a structured guide to help large language models quickly understand the key information about a website or project. This will give LLM-based assistants the ability to do all sorts of neat things – like answer questions about someone's public CV page, describe courses offered at educational institution, or provide programmatic examples for a software library.

The most important thing for our purposes is that llms.txt is formatted as a well-structured markdown document – something that is both easy for LLMs to consume and easy for _me_ to use in a demo.

[Here is a page](https://directory.llmstxt.cloud/) that lists a growing set of websites that are adopting the llms.txt standard.

For our example, we will use Cursor's llms.txt ([take look here](https://docs.cursor.com/llms-full.txt)) which is relatively well organized and does a good job describing their product.

In this example, we load the Cursor llms.txt into an artifact labeled "Abridged llms.txt", which is also presented to the model (see [my previous post](https://arcturus-labs.com/blog/2024/11/21/blog/cut-the-chit-chat-with-artifacts.md) for an intro to artifacts – they are not critical for this post). Notice that the sections of the llms.txt have been truncated. This greatly reduces the size of the llms.txt. However, the section headings and opening text is preserved – this ensures that the assistant can still understand and navigate the document.

In the demo, the user asks a simple question, "How does Cursor's Tab autocomplete feature differ from GitHub Copilot?" The assistant then roams through the document and expands the sections it deems useful in answering the user's question. These expanded section are presented to the model as additional artifacts, which are also presented in new tabs in the artifact pane – in this case "Overview" and "Migrate from GitHub Copilot". Once the assistant has sufficient information to address the user's question, it responds in the conversation tab with a grounded and relevant answer.

Now You Try!

[Try the demo yourself here.](https://llm-text-assistant.fly.dev/) When you load the window you'll be able to select from a large number of llms.txt documents from the [/llms.txt directory](https://directory.llmstxt.cloud/). In the bottom right there are several LLM-generated example questions that you can ask – but I encourage you to ask your own questions and see how well it works for you.

How Does It Work?
-----------------

The idea is pretty simple – just present the model with an abridged version of the document (or documents) that it will navigate, and then give it the tools and know-how required to navigate the document and find information that the user is looking for.

### Prerequisite - Well-Organized Documentation

The whole premise of this approach is that we let the assistant look at an outline of the document and navigate it as it sees fit. This means that this approach only works well for documents that are well-organized. This means:

*   Titles and headings should be clear and self-explanatory.
*   Each section has opening text that further clarifies the contents of the section.
*   Each section of the document should only contain subsections that logically fit within the topic of the section.
*   There shouldn't be tons of top-level sections.

So again, we're talking about technical documents, catalogs, well-organized websites (and _ideally_ the llms.txt that describes them). We're not talking about novels or pages of disorganized facts.

### Preparing the Abridged Document

As soon as the Roaming RAG application loads the document, it parses the text into sections and subsections, and it produces an abridged version of the text like this one taken from Cursor's llms.txt:

```
# AI Review (Beta) <!-- Section collapsed - expand with expand_section("07f3277d") -->

AI Review is a feature that allows you to review your recent changes in your codebase to catch any potential...

### Custom Review Instructions... <!-- Section collapsed - expand with expand_section("f5cc6b18") -->

### Review Options... <!-- Section collapsed - expand with expand_section("aaa9c5c8") -->

# Custom API Keys <!-- Section collapsed - expand with expand_section("919b9b9a") -->

...

### OpenAI API Keys... <!-- Section collapsed - expand with expand_section("9db61152") -->

### Anthropic API Keys... <!-- Section collapsed - expand with expand_section("13471f04") -->

### Google API Keys... <!-- Section collapsed - expand with expand_section("25ff5a5c") -->

### Azure Integration... <!-- Section collapsed - expand with expand_section("d851e3fd") -->

### Will my API key be stored or leave my device?... <!-- Section collapsed - expand with expand_section("0da6eab3") -->

# Models <!-- Section collapsed - expand with expand_section("a8a96034") -->

With Cursor Chat, Ctrl/⌘ K, and Terminal Ctrl/⌘ K, you can easily switch between different models of your...

### Model Dropdown... <!-- Section collapsed - expand with expand_section("b9e8ef5c") -->

### Long Context Only Models... <!-- Section collapsed - expand with expand_section("11304f12") -->

### What context window is used for model X?... <!-- Section collapsed - expand with expand_section("f1d4f327") -->

[...]
```

(Again, compare this with [Cursor's full llms.txt doc](https://docs.cursor.com/llms-full.txt).)

Here are the things to notice:

*   We keep the top-level headings.
*   We preserve the first ~100 characters of opening text from each section.
*   We present the second-level headings, but without any subsidiary content.
*   Each section is provided a unique 8 digit hex identifier.
*   Each section heading is followed by a guiding comment for the model: `Section collapsed - expand with expand_section("{identifier}")`.

Splitting up the document like this is not terribly difficult. In [these 300 or so lines of code](https://github.com/arcturus-labs/llm-text-assistant/blob/48b71030992301f6d1631f23cfc643dca56835eb/backend/app/routes/api/tools.py), I'm using `markdown_it` to split the doc into sections, give them all a unique identifier, and make it possible to easily access and expand subsections using their identifier.

### Backend Implementation

As our guiding comment implies, we have a tool named `expand_section`. It's pretty simple:

```
{
"name":"expand_section",
"description":"Expand a section of the markdown document to reveal its contents.\n\n"
"- Expand the most specific (lowest-level) relevant section first\n"
"- Multiple sections can be expanded in parallel\n"
"- You can expand any section regardless of parent section state (e.g. parent sections do not need to be expanded to view subsection content)\n"
"input_schema":{
"type":"object",
"properties":{
"section_id":{
"type":"string",
"description":"8-digit hexadecimal ID of the section to expand (e.g. '04c8214b')",
"pattern":"^[0-9a-f]{8}$"
}
},
"required":["section_id"]
}
}
```

If the model calls `expand_section` then the corresponding section of the document is retrieved and presented to the model in another artifact. (The artifact is also presented to the user as a new tab in the artifact pane. Using artifacts isn't required for Roaming RAG, but it was a convenient choice coming from my last blog post, and it seemed to work well here too.)

The final touch is to create a system message to explain that this assistant's task is to help answer questions from the associated llms.txt. I explain the idea of llms.txt, and the manner in which the assistant is to navigate the document and answer questions. ([Here's the code if you're interested.](https://github.com/arcturus-labs/llm-text-assistant/blob/48b71030992301f6d1631f23cfc643dca56835eb/backend/app/routes/api/conversation.py#L37)).

### In Action

Upon reading the user's question, the assistant "roams" around the document by glancing over the outline and opening sections that seem to be relevant. There are a few tricks that it can do:

*   The assistant might open several sections at the same level as it looks for content that satisfies the user's request.
*   The assistant can dig deeper into the text by opening a section and then reading the new content within that section and choosing to open a deeper subsection.
*   Because the abridged document shows two levels of unopened sections, the assistant can optionally skip a level of detail and dive two sections deep.

There are actually a couple of tricks that I left out. For some reason I didn't design the `expand_section` tool to take a list of ids. This would have allowed the assistant to open up multiple sections in parallel and thus saved a bit of time. I _did_ do some experimentation with a `collapse_section` command that allowed the assistant clean up open sections that were no longer relevant to the conversation. Unfortunately, the assistant would either never use that tool, or, if I insisted that the tool be used, then the agent would use it indiscriminately and at the wrong time. I instead opted to just close all open sections at the beginning of a question. This is a shame, because if the user has follow-up questions about a topic it would be better to keep the sections open. ... Oh well, next time.

There are times when Roaming RAG is unable to find the information it needs. Likely this is because the document isn't well-structured, or perhaps the headings aren't descriptive enough for the model to make sense of them. But, sometimes the model could also just overlook the right section. When this happens, I've prompted the model to apologize to the user and recommend other ideas for tracking down their answer.

Conclusion
----------

One thing to underscore is that Roaming RAG isn't a drop-in replacement for your traditional RAG application. Roaming RAG only works when the docs in question are well-organized as described above. There are also costs to consider – Roaming RAG might make several lookups before it finds the information it needs, and the prompt can be long – prompt caching is advised.

But if you find yourself with a well organized document – _and llms.txt is a great example of this_ – then Roaming RAG offers some nice benefits.

One benefit is the richer context. In traditional RAG, context is retrieved as chunks of text which, when shoved into the prompt, resemble pages ripped out of a book. With Roaming RAG, the information retrieved is always presented _within_ the context of the surrounding document. Intuitively, this will likely help the model build a better-informed response to the user's question.

The other main benefit is that there is no extra infrastructure to set up for Roaming RAG – no need to chunk documents, vectorize, or store them in a vector database – actually, no need for the vector database at all. The implementation just needs the doc itself and about 300 lines of code to parse it and get everything set up.

_Special thanks to [Juan Pablo Mesa Lopez](https://x.com/juanpml_) and [Dan Becker](https://www.linkedin.com/in/dansbecker/) for providing feedback on this post._

* * *

### _Hey, and if you liked this post, then maybe we should be friends!_

*   I just wrote a book about Prompt Engineering for LLM Applications. [Maybe you'd be interested in reading it.](https://arcturus-labs.com/#about)
*   Are you stumped on a problem with your own LLM application? [Let me hear about it.](https://arcturus-labs.com/#contact-blog)
*   I'm going to write lots more posts. [Subscribe and you'll be the first to know](https://arcturus-labs.com/#contact-blog).

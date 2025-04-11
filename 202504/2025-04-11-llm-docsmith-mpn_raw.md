Title: llm-docsmith | MPN

URL Source: https://mathpn.com/posts/llm-docsmith/

Published Time: 2025-03-28T00:00:00.000Z

Markdown Content:
I’ve been using Simon Willi­son’s [LLM](https://llm.datasette.io/en/stable/) CLI to in­ter­act with LLMs for quite a while now, it’s a great tool. At this point, I think every­one in the software-​adjacent world has seen some form of code au­to­com­ple­tion. I’ve been search­ing for a tool to gen­er­ate doc­strings for Python code using LLMs. There are a few so­lu­tions, but none worked just the way I wanted, so I’ve de­cided to rein­vent the wheel and im­ple­ment an AI doc­string gen­er­a­tor!

> If you just want to get to the repo, [here](https://github.com/mathpn/llm-docsmith) it is

Why would I im­ple­ment some­thing that al­ready ex­ists? That is a fair ques­tion. First, I have started this lit­tle project a while ago. Mod­els keep get­ting bet­ter at break­neck speed, so it’s quite pos­si­ble that soon (or even now) it’s sim­ply cheaper to have an LLM rewrite the en­tire file while adding the doc­strings. How­ever, I want an ap­proach that:

*   Has good user ex­pe­ri­ence — no need to worry about tons of de­pen­den­cies and en­vi­ron­ment vari­ables
*   Does not edit the code in any way other than mod­i­fy­ing or adding doc­strings
*   Ex­tracts all avail­able in­for­ma­tion from the source code (e.g. type hints)

I didn’t find any tool that checked all those boxes. And lastly, I just wanted to im­ple­ment this.

The ap­proach[](https://mathpn.com/posts/llm-docsmith/#the-approach)
--------------------------------------------------------------------

I have started with a naive ap­proach: ask the LLM to gen­er­ate a doc­string using [Ol­lama](https://ollama.com/). In order to add the doc­strings to the source code, the source code is parsed into a [con­crete syn­tax tree](https://stackoverflow.com/questions/1888854/what-is-the-difference-between-an-abstract-syntax-tree-and-a-concrete-syntax-tre), which re­tains all for­mat­ting de­tails (com­ments, white­spaces, paren­the­ses, etc) using [libcst](https://pypi.org/project/libcst/).

This rep­re­sen­ta­tion aims to be loss­less, thus it’s pos­si­ble to change the doc­strings and rewrite the mod­ule with­out chang­ing dozens of lines due to white­space or for­mat­ting. Also, it en­sures that the LLM can­not ac­ci­den­tally change the code while (re)writ­ing a doc­string.

The sys­tem prompt is rea­son­ably sim­ple and in­spired by the [PEP 257](https://peps.python.org/pep-0257/) guide­lines. How­ever, quickly I’ve no­ticed that this naive ap­proach yielded in­con­sis­tent re­sults. Some­times the doc­string would men­tion ar­gu­ments in a sen­tence, oth­ers it would cre­ate a bullet-​point Markdown-​like list, and so on.

Here, again, the syn­tax tree comes in handy. The con­crete syn­tax tree is trans­formed into an ab­stract syn­tax tree, which is friend­lier to nav­i­gate. Then, we can tra­verse func­tion de­f­i­n­i­tion nodes to ex­tract their sig­na­ture, that is, all ar­gu­ment names, de­faults, and type hints (if avail­able). Hence, we do not rely on the LLM to get all ar­gu­ments per­fectly right every time nor with for­mat­ting. We have the func­tion sig­na­ture and, with it, it’s pos­si­ble to gen­er­ate cor­rect ar­gu­ment lists with con­sis­tent for­mat­ting.

I then used struc­tured out­put con­straints to en­sure the LLM out­puts a string in the de­sired for­mat.[1](https://mathpn.com/posts/llm-docsmith/#user-content-fn-eol) Struc­tured out­puts are in­cred­i­bly use­ful to ex­tract in­for­ma­tion from LLM out­puts with­out com­plex pars­ing, but they do in­crease input token usage since the JSON schema is sent as part of the re­quest.

The struc­tured out­put al­lowed me to build a doc­string with a con­sis­tent for­mat, list­ing ar­gu­ments, de­faults, types, and the re­turn. The LLM fills the slots with the over­all sum­mary and de­scrip­tion of each ar­gu­ment or re­turn.

This ap­proach worked and gen­er­ated good doc­strings, but the user ex­pe­ri­ence was still a bit lack­ing. In­stalling a stand­alone Python CLI is easy using `pipx` or `uvx`, but it still re­quires Ol­lama in­stalled and run­ning. To add Ope­nAI or An­thropic model sup­port the user would have to con­fig­ure en­vi­ron­ment vari­ables with API keys, which de­grades user ex­pe­ri­ence quite a lot. The LLM tool (not to be con­fused with LLM mod­els) men­tioned ear­lier pro­vides a [Python API](https://llm.datasette.io/en/stable/python-api.html) which can be used to ex­e­cute prompts. LLM has API key man­age­ment built-​in, with sup­port for all major LLM providers through plu­g­ins.

The tool[](https://mathpn.com/posts/llm-docsmith/#the-tool)
-----------------------------------------------------------

The final step was to turn what was a sim­ple script into an LLM plu­gin, and [llm-​docsmith](https://github.com/mathpn/llm-docsmith) was born. After in­stalling LLM, you can in­stall the plu­gin by:

```
llm install llm-docsmith
```

Then, you can gen­er­ate doc­strings for a Python file:

```
llm docsmith ./scripts/main.py
```

Caveats[](https://mathpn.com/posts/llm-docsmith/#caveats)
---------------------------------------------------------

The en­tire func­tion or class is in­cluded in the prompt, along with all the con­text (func­tions and classes) it ref­er­ences (al­beit lim­ited to the same mod­ule). This can con­sume quite a lot of to­kens, so use with cau­tion. Some parts of the source code may be in­cluded mul­ti­ple times as con­text, which is not very op­ti­mal.

The plu­gin also rewrites all doc­strings, even though often only a hand­ful of them should be rewrit­ten. This can be im­proved through git in­te­gra­tion to de­ter­mine which parts of the code have been changed — maybe a fea­ture for a fu­ture ver­sion.

Con­clu­sion[](https://mathpn.com/posts/llm-docsmith/#conclusion)
-----------------------------------------------------------------

It’s been fun to im­ple­ment this lit­tle tool. Maybe it’s use­ful for you too, in which case use it, I’d love to hear feed­back!

Footnotes[](https://mathpn.com/posts/llm-docsmith/#footnote-label)
------------------------------------------------------------------

1.  It’s still pos­si­ble to get an un­ex­pected EOL error with struc­tured out­puts. How­ever, the re­quest ei­ther fails or re­turns a string that is a valid JSON with the spec­i­fied schema. [↩](https://mathpn.com/posts/llm-docsmith/#user-content-fnref-eol)

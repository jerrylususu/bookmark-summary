Title: Textual - Anatomy of a Textual User Interface

URL Source: https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/

Markdown Content:
I recently wrote a [TUI](https://en.wikipedia.org/wiki/Text-based_user_interface) to chat to an AI agent in the terminal. I'm not the first to do this (shout out to [Elia](https://github.com/darrenburns/elia) and [Paita](https://github.com/villekr/paita)), but I _may_ be the first to have it reply as if it were the AI from the Aliens movies?

Here's a video of it in action:

Now let's dissect the code like Bishop dissects a facehugger.

All right, sweethearts, what are you waiting for? Breakfast in bed?[¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#all-right-sweethearts-what-are-you-waiting-for-breakfast-in-bed "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

At the top of the file we have some boilerplate:

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-1)# /// script
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-2)# requires-python = ">=3.12"
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-3)# dependencies = [
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-4)#     "llm",
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-5)#     "textual",
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-6)# ]
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-7)# ///
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-8)from textual import on, work
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-9)from textual.app import App, ComposeResult
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-10)from textual.widgets import Header, Input, Footer, Markdown
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-11)from textual.containers import VerticalScroll
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-12)import llm
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-13)
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-0-14)SYSTEM = """Formulate all responses as if you where the sentient AI named Mother from the Aliens movies."""
```

The text in the comment is a relatively new addition to the Python ecosystem. It allows you to specify dependencies inline so that tools can setup an environment automatically. The only tool that I know of it that uses it is [uv](https://docs.astral.sh/uv/guides/scripts/#running-scripts).

After this comment we have a bunch of imports: [textual](https://github.com/textualize/textual) for the UI, and [llm](https://llm.datasette.io/en/stable/) to talk to ChatGPT (also supports other LLMs).

Finally, we define `SYSTEM`, which is the _system prompt_ for the LLM.

Look, those two specimens are worth millions to the bio-weapons division.[¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#look-those-two-specimens-are-worth-millions-to-the-bio-weapons-division "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next up we have the following:

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-1-1)class Prompt(Markdown):
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-1-2)    pass
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-1-3)
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-1-4)
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-1-5)class Response(Markdown):
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-1-6)    BORDER_TITLE = "Mother"
```

These two classes define the widgets which will display text the user enters and the response from the LLM. They both extend the builtin [Markdown](https://textual.textualize.io/widgets/markdown/) widget, since LLMs like to talk in that format.

Well, somebody's gonna have to go out there. Take a portable terminal, go out there and patch in manually.[¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#well-somebodys-gonna-have-to-go-out-there-take-a-portable-terminal-go-out-there-and-patch-in-manually "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Following on from the widgets we have the following:

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-1)class MotherApp(App):
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-2)    AUTO_FOCUS = "Input"
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-3)
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-4)    CSS = """
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-5)    Prompt {
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-6)        background: $primary 10%;
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-7)        color: $text;
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-8)        margin: 1;        
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-9)        margin-right: 8;
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-10)        padding: 1 2 0 2;
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-11)    }
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-12)
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-13)    Response {
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-14)        border: wide $success;
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-15)        background: $success 10%;   
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-16)        color: $text;             
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-17)        margin: 1;      
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-18)        margin-left: 8; 
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-19)        padding: 1 2 0 2;
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-20)    }
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-2-21)    """
```

This defines an app, which is the top-level object for any Textual app.

The `AUTO_FOCUS` string is a classvar which causes a particular widget to receive input focus when the app starts. In this case it is the `Input` widget, which we will define later.

The classvar is followed by a string containing CSS. Technically, TCSS or _Textual Cascading Style Sheets_, a variant of CSS for terminal interfaces.

This isn't a tutorial, so I'm not going to go in to a details, but we're essentially setting properties on widgets which define how they look. Here I styled the prompt and response widgets to have a different color, and tried to give the response a retro tech look with a green background and border.

We could express these styles in code. Something like this:

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-3-1)self.styles.color = "red"
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-3-2)self.styles.margin = 8
```

Which is fine, but CSS shines when the UI get's more complex.

Look, man. I only need to know one thing: where they are.[¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#look-man-i-only-need-to-know-one-thing-where-they-are "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After the app constants, we have a method called `compose`:

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-4-1)    def compose(self) -> ComposeResult:
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-4-2)        yield Header()
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-4-3)        with VerticalScroll(id="chat-view"):
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-4-4)            yield Response("INTERFACE 2037 READY FOR INQUIRY")
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-4-5)        yield Input(placeholder="How can I help you?")
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-4-6)        yield Footer()
```

This method adds the initial widgets to the UI.

`Header` and `Footer` are builtin widgets.

Sandwiched between them is a `VerticalScroll` _container_ widget, which automatically adds a scrollbar (if required). It is pre-populated with a single `Response` widget to show a welcome message (the `with` syntax places a widget within a parent widget). Below that is an `Input` widget where we can enter text for the LLM.

This is all we need to define the _layout_ of the TUI. In Textual the layout is defined with styles (in the same was as color and margin). Virtually any layout is possible, and you never have to do any math to calculate sizes of widgets—it is all done declaratively.

We could add a little CSS to tweak the layout, but the defaults work well here. The header and footer are _docked_ to an appropriate edge. The `VerticalScroll` widget is styled to consume any available space, leaving room for widgets with a defined height (like our `Input`).

If you resize the terminal it will keep those relative proportions.

Look into my eye.[¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#look-into-my-eye "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------

The next method is an _event handler_.

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-5-1)    def on_mount(self) -> None:
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-5-2)        self.model = llm.get_model("gpt-4o")
```

This method is called when the app receives a Mount event, which is one of the first events sent and is typically used for any setup operations.

It gets a `Model` object got our LLM of choice, which we will use later.

Note that the [llm](https://llm.datasette.io/en/stable/) library supports a [large number of models](https://llm.datasette.io/en/stable/openai-models.html), so feel free to replace the string with the model of your choice.

We're in the pipe, five by five.[¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#were-in-the-pipe-five-by-five "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The next method is also a message handler:

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-6-1)    @on(Input.Submitted)
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-6-2)    async def on_input(self, event: Input.Submitted) -> None:
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-6-3)        chat_view = self.query_one("#chat-view")
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-6-4)        event.input.clear()
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-6-5)        await chat_view.mount(Prompt(event.value))
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-6-6)        await chat_view.mount(response := Response())
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-6-7)        response.anchor()
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-6-8)        self.send_prompt(event.value, response)
```

The decorator tells Textual to handle the `Input.Submitted` event, which is sent when the user hits return in the Input.

More on event handlers

There are two ways to receive events in Textual: a naming convention or the decorator. They aren't on the base class because the app and widgets can receive arbitrary events.

When that happens, this method clears the input and adds the prompt text to the `VerticalScroll`. It also adds a `Response` widget to contain the LLM's response, and _anchors_ it. Anchoring a widget will keep it at the bottom of a scrollable view, which is just what we need for a chat interface.

Finally in that method we call `send_prompt`.

We're on an express elevator to hell, going down![¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#were-on-an-express-elevator-to-hell-going-down "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here is `send_prompt`:

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-7-1)    @work(thread=True)
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-7-2)    def send_prompt(self, prompt: str, response: Response) -> None:
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-7-3)        response_content = ""
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-7-4)        llm_response = self.model.prompt(prompt, system=SYSTEM)
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-7-5)        for chunk in llm_response:
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-7-6)            response_content += chunk
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-7-7)            self.call_from_thread(response.update, response_content)
```

You'll notice that it is decorated with `@work`, which turns this method in to a _worker_. In this case, a _threaded_ worker. Workers are a layer over async and threads, which takes some of the pain out of concurrency.

This worker is responsible for sending the prompt, and then reading the response piece-by-piece. It calls the Markdown widget's `update` method which replaces its content with new Markdown code, to give that funky streaming text effect.

Game over man, game over![¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#game-over-man-game-over "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

The last few lines creates an app instance and runs it:

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-8-1)if __name__ == "__main__":
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-8-2)    app = MotherApp()
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-8-3)    app.run()
```

You may need to have your [API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) set in an environment variable. Or if you prefer, you could set in the `on_mount` function with the following:

```
[](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#__codelineno-9-1)self.model.key = "... key here ..."
```

Not bad, for a human.[¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#not-bad-for-a-human "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Here's the [code for the Mother AI](https://gist.github.com/willmcgugan/648a537c9d47dafa59cb8ece281d8c2c).

Run the following in your shell of choice to launch mother.py (assumes you have [uv](https://docs.astral.sh/uv/) installed):

You know, we manufacture those, by the way.[¶](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/#you-know-we-manufacture-those-by-the-way "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Join our [Discord server](https://discord.gg/Enf6Z3qhVr) to discuss more 80s movies (or possibly TUIs).

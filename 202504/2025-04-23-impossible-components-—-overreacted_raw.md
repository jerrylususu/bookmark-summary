Title: Impossible Components — overreacted

URL Source: https://overreacted.io/impossible-components/

Markdown Content:
Suppose I want to greet you in _my_ favorite color.

This would require combining information from two different computers. Your name would be coming from _your_ computer. The color would be on _my_ computer.

You could imagine a component that does this:

```
import { useState } from 'react';
import { readFile } from 'fs/promises';
 
async function ImpossibleGreeting() {
  const [yourName, setYourName] = useState('Alice');
  const myColor = await readFile('./color.txt', 'utf8');
  return (
    <>
      <input placeholder="What's your name?"
        value={yourName}
        onChange={e => setYourName(e.target.value)}
      />
      <p style={{ color: myColor }}>
        Hello, {yourName}!
      </p>
    </>
  );
}
```

But this component is impossible. The `readFile` function can only execute on _my_ computer. The `useState` will only have a useful value on _your_ computer. We can’t do both at once without giving up the predictable top-down execution flow.

Or can we?

* * *

### [Splitting a Component](https://overreacted.io/impossible-components/#splitting-a-component)

Let’s split this component in two parts.

The _first_ part will read the file, which only makes sense on _my_ computer. It is responsible for loading data so we’re going to call this part `GreetingBackend`:

```
import { readFile } from 'fs/promises';
import { GreetingFrontend } from './client';
 
async function GreetingBackend() {
  const myColor = await readFile('./color.txt', 'utf8');
  return <GreetingFrontend color={myColor} />;
}
```

It will read my chosen color and pass it as the `color` prop to the second part, which is responsible for interactivity. We’re going to call it `GreetingFrontend`:

```
'use client';
 
import { useState } from 'react';
 
export function GreetingFrontend({ color }) {
  const [yourName, setYourName] = useState('Alice');
  return (
    <>
      <input placeholder="What's your name?"
        value={yourName}
        onChange={e => setYourName(e.target.value)}
      />
      <p style={{ color }}>
        Hello, {yourName}!
      </p>
    </>
  );
}
```

That second part receives that `color`, and returns an interactive form. Edit “Alice” to say your name and notice how the greeting updates as you’re typing:

Hello, Alice!

(If your name _is_ Alice, you may leave it as is.)

**Notice that _the backend runs first._ Our mental model here isn’t “frontend loads data from the backend”. Rather, it’s “the backend passes data _to_ the frontend”.**

This is React’s top-down data flow, but including the backend _into_ the flow. The backend is the source of truth for the data—so it [must be](https://react.dev/learn/thinking-in-react#step-4-identify-where-your-state-should-live) the frontend’s _parent_.

Have another look at these two parts and see how the data flows _down:_

```
import { readFile } from 'fs/promises';
import { GreetingFrontend } from './client';
 
async function GreetingBackend() {
  const myColor = await readFile('./color.txt', 'utf8');
  return <GreetingFrontend color={myColor} />;
}
```

```
'use client';
 
import { useState } from 'react';
 
export function GreetingFrontend({ color }) {
  const [yourName, setYourName] = useState('Alice');
  return (
    <>
      <input placeholder="What's your name?"
        value={yourName}
        onChange={e => setYourName(e.target.value)}
      />
      <p style={{ color }}>
        Hello, {yourName}!
      </p>
    </>
  );
}
```

From the backend to the frontend. From my computer to yours.

Together, they form a single, _encapsulated_ abstraction spanning both worlds:

```
<GreetingBackend />
```

Hello, Alice!

Together, they form an impossible component.

_(Here and below, the `'use client'` syntax hints that we’ll be learning React Server Components. You can try them in [Next](https://nextjs.org/)—or in [Parcel](https://parceljs.org/recipes/rsc/) if you don’t want a framework.)_

* * *

### [Local State, Local Data](https://overreacted.io/impossible-components/#local-state-local-data)

The beautiful thing about this pattern is that I can refer to the _entirety_ of this functionality—_its both sides_—by writing a JSX tag just for the “backend” part. Since the backend _renders_ the frontend, rendering the backend gives you both.

To demonstrate this, let’s render `<GreetingBackend>` multiple times:

```
<>
  <GreetingBackend />
  <GreetingBackend />
  <GreetingBackend />
</>
```

Hello, Alice!

Hello, Alice!

Hello, Alice!

Verify that you can edit each input independently.

Naturally, the `GreetingFrontend` _state_ inside of each `GreetingBackend` is isolated. However, how each `GreetingBackend` _loads its data_ is also isolated.

To demonstrate this, let’s edit `GreetingBackend` to take a `colorFile` prop:

```
import { readFile } from 'fs/promises';
import { GreetingFrontend } from './client';
 
async function GreetingBackend({ colorFile }) {
  const myColor = await readFile(colorFile, 'utf8');
  return <GreetingFrontend color={myColor} />;
}
```

Next, let’s add `Welcome` that renders `GreetingBackend` for different color files:

```
import { readFile } from 'fs/promises';
import { GreetingFrontend } from './client';
 
function Welcome() {
  return (
    <>
      <GreetingBackend colorFile="./color1.txt" />
      <GreetingBackend colorFile="./color2.txt" />
      <GreetingBackend colorFile="./color3.txt" />
    </>
  );
}
 
async function GreetingBackend({ colorFile }) {
  const myColor = await readFile(colorFile, 'utf8');
  return <GreetingFrontend color={myColor} />;
}
```

Let’s see what happens:

```
<Welcome />
```

Each greeting will read its own file. And each input will be independently editable.

Hello, Alice!

Hello, Alice!

Hello, Alice!

This might remind you of composing “server partials” in Rails or Django, except that instead of HTML you’re rendering fully interactive React component trees.

Now you can see the whole deal:

1.  **Each `GreetingBackend` _knows_ how to load its own data.** That logic is encapsulated in `GreetingBackend`—you didn’t need to coordinate them.
2.  **Each `GreetingFrontend` _knows_ how to manage its own state.** That logic is encapsulated in `GreetingFrontend`—again, no manual coordination.
3.  **Each `GreetingBackend` renders a `GreetingFrontend`.** This lets you think of `GreetingBackend` as a self-contained unit that does _both_—an impossible component. It’s a piece of the backend _with its own_ piece of the frontend.

Of course, you can substitute “reading files” with “querying an ORM”, “talking to an LLM with a secret API key”, “hitting an internal microservice”, or anything that requires backend-only resources. Likewise, an “input” represents any interactivity. The point is that you can compose both sides into self-contained components.

Let’s render `Welcome` again:

```
<Welcome />
```

Hello, Alice!

Hello, Alice!

Hello, Alice!

Notice how we didn’t need to plumb any data or state into it.

The `<Welcome />` tag is completely self-contained!

And because the backend parts always _run first_, when you load this page, from the frontend’s perspective, the data is “already there”. There are no flashes of “loading data from the backend”—the backend _has already passed_ the data to the frontend.

Local state.

Local data.

Single roundtrip.

_Self-contained._

* * *

### [It’s Not About HTML](https://overreacted.io/impossible-components/#its-not-about-html)

Okay, but how is this different from just rendering a bunch of HTML?

Let’s tweak the `GreetingFrontend` component to do something different:

```
import { readFile } from 'fs/promises';
import { GreetingFrontend } from './client';
 
async function GreetingBackend() {
  const myColor = await readFile('./color.txt', 'utf8');
  return <GreetingFrontend color={myColor} />;
}
```

```
'use client';
 
import { useState } from 'react';
 
export function GreetingFrontend({ color }) {
  const [yourName, setYourName] = useState('Alice');
  return (
    <>
      <input placeholder="What's your name?"
        value={yourName}
        onChange={e => setYourName(e.target.value)}
        onFocus={() => {
          document.body.style.backgroundColor = color;
        }}
        onBlur={() => {
          document.body.style.backgroundColor = '';
        }}
      />
      <p>
        Hello, {yourName}!
      </p>
    </>
  );
}
```

Instead of styling `<p>`, we’ll set `document.body.style.backgroundColor` to the `color` from the backend—but only for as long as the input is focused.

Try typing into the input:

Hello, Alice!

Depending on how you look at it, the fact that this “just works” can seem either completely natural, or a total surprise, or a bit of both. The backend is passing props to the frontend, but _not for the purpose of generating the initial HTML markup._

The props are being used _later_—in order to “do something” in the event handler.

```
'use client';
 
import { useState } from 'react';
 
export function GreetingFrontend({ color }) {
  // ...
  return (
    <>
      <input placeholder="What's your name?"
        // ...
        onFocus={() => {
          document.body.style.backgroundColor = color;
        }}
        // ...
      />
      ...
    </>
  );
}
```

Of course, we’re not limited to passing colors. We could pass strings, numbers, booleans, objects, pieces of JSX—anything that can be sent over the wire.

Now let’s try rendering `<Welcome />` again which composes our components:

```
import { readFile } from 'fs/promises';
import { GreetingFrontend } from './client';
 
function Welcome() {
  return (
    <>
      <GreetingBackend colorFile="./color1.txt" />
      <GreetingBackend colorFile="./color2.txt" />
      <GreetingBackend colorFile="./color3.txt" />
    </>
  );
}
 
async function GreetingBackend({ colorFile }) {
  const myColor = await readFile(colorFile, 'utf8');
  return <GreetingFrontend color={myColor} />;
}
```

Notice how each greeting now has the new behavior but remains independent:

Hello, Alice!

Hello, Alice!

Hello, Alice!

Local data, local state.

Nothing conflicts with each other. No global identifiers, no naming clashes. Any component can be reused anywhere in the tree and will remain self-contained.

_Local, therefore composable._

Now that you get the idea, let’s have some fun with it.

* * *

### [A Sortable List](https://overreacted.io/impossible-components/#a-sortable-list)

Imagine another _impossible_ component—a sortable file list.

```
import { useState } from 'react';
import { readdir } from 'fs/promises';
 
async function SortableFileList({ directory }) {
  const [isReversed, setIsReversed] = useState(false);
  const files = await readdir(directory);
  const sortedFiles = isReversed ? files.toReversed() : files;
  return (
    <>
      <button onClick={() => setIsReversed(!isReversed)}>
        Flip order
      </button>
      <ul>
        {sortedFiles.map(file =>
          <li key={file}>
            {file}
          </li>
        )}
      </ul>
    </>
  );
}
```

Of course, this doesn’t make sense. The information `readdir` needs only exists on _my_ computer but the sorting order you choose with `useState` lives on _your_ computer. (The most I _could_ do on mine is to prepare HTML for the initial state.)

How do we fix this component?

By now, you know the drill:

```
import { SortableList } from './client';
import { readdir } from 'fs/promises';
 
async function SortableFileList({ directory }) {
  const files = await readdir(directory);
  return <SortableList items={files} />;
}
```

```
'use client';
 
import { useState } from 'react';
 
export function SortableList({ items }) {
  const [isReversed, setIsReversed] = useState(false);
  const sortedItems = isReversed ? items.toReversed() : items;
  return (
    <>
      <button onClick={() => setIsReversed(!isReversed)}>
        Flip order
      </button>
      <ul>
        {sortedItems.map(item => (
          <li key={item}>
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}
```

Let’s try it:

```
<SortableFileList directory="." />
```

*   client.js
*   color.txt
*   color1.txt
*   color2.txt
*   color3.txt
*   components.js
*   index.md
*   server.js

So far so good. Now notice that the `items` being passed down is an array. We’re already using that to conditionally reverse it. What else could we do with an array?

* * *

### [A Filterable List](https://overreacted.io/impossible-components/#a-filterable-list)

It would be nice if we could filter the list of files with an input. Filtering must happen on _your_ machine (the most I could do on _mine_ is to generate HTML for the initial state). Therefore, it makes sense to add the filter logic to the frontend part:

```
import { SortableList } from './client';
import { readdir } from 'fs/promises';
 
async function SortableFileList({ directory }) {
  const files = await readdir(directory);
  return <SortableList items={files} />;
}
```

```
'use client';
 
import { useState } from 'react';
 
export function SortableList({ items }) {
  const [isReversed, setIsReversed] = useState(false);
  const [filterText, setFilterText] = useState('');
  let filteredItems = items;
  if (filterText !== '') {
    filteredItems = items.filter(item =>
      item.toLowerCase().startsWith(filterText.toLowerCase())
    );
  }
  const sortedItems = isReversed ? filteredItems.toReversed() : filteredItems;
  return (
    <>
      <button onClick={() => setIsReversed(!isReversed)}>
        Flip order
      </button>
      <input
        value={filterText}
        onChange={(e) => setFilterText(e.target.value)}
        placeholder="Search..."
      />
      <ul>
        {sortedItems.map(item => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </>
  );
}
```

Notice how the backend part only executes once—since my blog is static, it runs during deployment. But the frontend logic is reactive to your every keystroke:

*   client.js
*   color.txt
*   color1.txt
*   color2.txt
*   color3.txt
*   components.js
*   index.md
*   server.js

And because it’s a reusable component, I can point it at some other data source:

```
<SortableFileList directory="./node_modules/react/" />
```

*   LICENSE
*   README.md
*   cjs
*   compiler-runtime.js
*   index.js
*   jsx-dev-runtime.js
*   jsx-dev-runtime.react-server.js
*   jsx-runtime.js
*   jsx-runtime.react-server.js
*   package.json
*   react.react-server.js

What we’ve got here is, again, a self-contained component that can load its own data on the backend and hand it off to the frontend for client-side interactivity.

Let’s see how far we can push this.

* * *

### [An Expanding Preview](https://overreacted.io/impossible-components/#an-expanding-preview)

Here’s a little `PostPreview` component for my blog:

```
import { readFile } from 'fs/promises';
import matter from 'gray-matter';
 
async function PostPreview({ slug }) {
  const fileContent = await readFile('./public/' + slug + '/index.md', 'utf8');
  const { data, content } = matter(fileContent);
  const wordCount = content.split(' ').filter(Boolean).length;
 
  return (
    <section className="rounded-md bg-black/5 p-2">
      <h5 className="font-bold">
        <a href={'/' + slug} target="_blank">
          {data.title}
        </a>
      </h5>
      <i>{wordCount.toLocaleString()} words</i>
    </section>
  );
}
```

It looks like this:

```
<PostPreview slug="jsx-over-the-wire" />
```

##### [JSX Over The Wire](https://overreacted.io/jsx-over-the-wire)

_11,212 words_

Isn’t it neat how it loads its own data? (Or rather, how the data is _already there_?)

Now let’s say I want to add a little interaction to it. For example, let’s say that I want the card to expand on click so that it displays the first sentence of the post.

Getting the first sentence on the backend is pretty easy:

```
async function PostPreview({ slug }) {
  const fileContent = await readFile('./public/' + slug + '/index.md', 'utf8');
  const { data, content } = matter(fileContent);
  const wordCount = content.split(' ').filter(Boolean).length;
  const firstSentence = content.split('.')[0];
  const isExpanded = true; // TODO: Somehow connect this to clicking
 
  return (
    <section className="rounded-md bg-black/5 p-2">
      <h5 className="font-bold">
        <a href={'/' + slug} target="_blank">
          {data.title}
        </a>
      </h5>
      <i>{wordCount.toLocaleString()} words</i>
      {isExpanded && <p>{firstSentence} [...]</p>}
    </section>
  );
}
```

##### [JSX Over The Wire](https://overreacted.io/jsx-over-the-wire)

_11,212 words_Suppose you have an API route that returns some data as JSON: \[...\]

But how do we expand it _on click?_ A _click_ is a frontend concept, and so is state in general. Let’s extract a frontend component that I’ll call an `ExpandingSection`:

```
import { readFile } from 'fs/promises';
import matter from 'gray-matter';
import { ExpandingSection } from './client';
 
async function PostPreview({ slug }) {
  const fileContent = await readFile('./public/' + slug + '/index.md', 'utf8');
  const { data, content } = matter(fileContent);
  const wordCount = content.split(' ').filter(Boolean).length;
  const firstSentence = content.split('.')[0];
  const isExpanded = true; // TODO: Somehow connect this to clicking
 
  return (
    <ExpandingSection>
      <h5 className="font-bold">
        <a href={'/' + slug} target="_blank">
          {data.title}
        </a>
      </h5>
      <i>{wordCount.toLocaleString()} words</i>
      {isExpanded && <p>{firstSentence} [...]</p>}
    </ExpandingSection>
  );
}
```

```
'use client';
 
export function ExpandingSection({ children }) {
  return (
    <section className="rounded-md bg-black/5 p-2">
      {children}
    </section>
  );
}
```

By itself, this doesn’t change anything—it just moves the `<section>` from the world of data (the backend) to the world of state and event handlers (the frontend).

But now that we’re _on_ the frontend, we can start layering the interaction logic:

```
'use client';
 
import { useState } from 'react';
 
export function ExpandingSection({ children, extraContent }) {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    <section
      className="rounded-md bg-black/5 p-2"
      onClick={() => setIsExpanded(!isExpanded)}
    >
      {children}
      {isExpanded && extraContent}
    </section>
  );
}
```

_(Note that in a real app, you’d need to make the press target a button and avoid nesting the link inside to stay accessible. I’m skimming over it for clarity but you shouldn’t.)_

Let’s verify that `ExpandingSection` works as expected. Try clicking “Hello”:

```
<ExpandingSection
  extraContent={<p>World</p>}
>
  <p>Hello</p>
</ExpandingSection>
```

Hello

Now we have an `<ExpandingSection>` that toggles showing its `extraContent` on click. All that’s left to do is to pass that `extraContent` _from the backend:_

```
async function PostPreview({ slug }) {
  // ...
  const firstSentence = content.split('.')[0];
 
  return (
    <ExpandingSection
      extraContent={<p>{firstSentence} [...]</p>}
    >
      ...
    </ExpandingSection>
  );
}
```

```
'use client';
 
import { useState } from 'react';
 
export function ExpandingSection({ children, extraContent }) {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    <section
      className="rounded-md bg-black/5 p-2"
      onClick={() => setIsExpanded(!isExpanded)}
    >
      {children}
      {isExpanded && extraContent}
    </section>
  );
}
```

Let’s try this again:

```
<PostPreview slug="jsx-over-the-wire" />
```

The component’s _initial_ state looks exactly like before. But try clicking the card:

##### [JSX Over The Wire](https://overreacted.io/jsx-over-the-wire)

_11,212 words_

Now the extra content shows up! Notice there aren’t any requests being made as you’re toggling the card—the `extraContent` prop was _already there_. Here’s the full code so you can trace the props flow down from the backend to the frontend:

```
import { readFile } from 'fs/promises';
import matter from 'gray-matter';
import { ExpandingSection } from './client';
 
async function PostPreview({ slug }) {
  const fileContent = await readFile('./public/' + slug + '/index.md', 'utf8');
  const { data, content } = matter(fileContent);
  const wordCount = content.split(' ').filter(Boolean).length;
  const firstSentence = content.split('.')[0];
 
  return (
    <ExpandingSection
      extraContent={<p>{firstSentence} [...]</p>}
    >
      <h5 className="font-bold">
        <a href={'/' + slug} target="_blank">
          {data.title}
        </a>
      </h5>
      <i>{wordCount.toLocaleString()} words</i>
    </ExpandingSection>
  );
}
```

```
'use client';
 
import { useState } from 'react';
 
export function ExpandingSection({ children, extraContent }) {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    <section
      className="rounded-md bg-black/5 p-2"
      onClick={() => setIsExpanded(!isExpanded)}
    >
      {children}
      {isExpanded && extraContent}
    </section>
  );
}
```

The props always flow down.

Note it was important to place `ExpandingSection` into the frontend world, i.e. the file with `'use client'`. The backend doesn’t have a _concept_ of state—it starts fresh on every request—so importing `useState` there would be a build error.

However, you can always take a tag like `<section>...</section>` and replace it with a frontend component like `<ExpandedSection>...</ExpandedSection>` that enriches a plain `<section>` with some stateful logic and event handlers.

This might remind you of weaving. You’ve left `children` and `extraContent` as “holes” in `<ExpandedSection>...</ExpandedSection>`, and then you’ve “filled in” those holes with more content _from_ the backend. You’ll see this a lot because it’s the only way to nest more backend stuff _inside_ the frontend stuff.

Get used to it!

* * *

### [A List of Previews](https://overreacted.io/impossible-components/#a-list-of-previews)

Let me add a new `PostList` component that renders an array of `PostPreview`s.

```
import { readFile, readdir } from 'fs/promises';
import matter from 'gray-matter';
 
async function PostList() {
  const entries = await readdir('./public/', { withFileTypes: true });
  const dirs = entries.filter(entry => entry.isDirectory());
  return (
    <div className="mb-8 flex h-72 flex-col gap-2 overflow-scroll font-sans">
      {dirs.map(dir => (
        <PostPreview key={dir.name} slug={dir.name} />
      ))}
    </div>
  );
}
 
async function PostPreview({ slug }) {
  // ...
}
```

It also needs to live on the backend since it uses the filesystem `readdir` API.

Here it is, showing a list of all posts on my blog:

```
<PostList />
```

##### [A Chain Reaction](https://overreacted.io/a-chain-reaction)

_2,452 words_

##### [A Complete Guide to useEffect](https://overreacted.io/a-complete-guide-to-useeffect)

_9,913 words_

##### [Algebraic Effects for the Rest of Us](https://overreacted.io/algebraic-effects-for-the-rest-of-us)

_3,062 words_

##### [Before You memo()](https://overreacted.io/before-you-memo)

_856 words_

##### [Coping with Feedback](https://overreacted.io/coping-with-feedback)

_669 words_

##### [Fix Like No One’s Watching](https://overreacted.io/fix-like-no-ones-watching)

_251 words_

##### [Goodbye, Clean Code](https://overreacted.io/goodbye-clean-code)

_1,196 words_

##### [How Are Function Components Different from Classes?](https://overreacted.io/how-are-function-components-different-from-classes)

_2,519 words_

##### [How Does React Tell a Class from a Function?](https://overreacted.io/how-does-react-tell-a-class-from-a-function)

_3,000 words_

##### [How Does setState Know What to Do?](https://overreacted.io/how-does-setstate-know-what-to-do)

_1,511 words_

##### [How Does the Development Mode Work?](https://overreacted.io/how-does-the-development-mode-work)

_1,930 words_

##### [Impossible Components](https://overreacted.io/impossible-components)

_4,211 words_

##### [JSX Over The Wire](https://overreacted.io/jsx-over-the-wire)

_11,212 words_

##### [Making setInterval Declarative with React Hooks](https://overreacted.io/making-setinterval-declarative-with-react-hooks)

_2,769 words_

##### [My Decade in Review](https://overreacted.io/my-decade-in-review)

_5,866 words_

##### [My Wishlist for Hot Reloading](https://overreacted.io/my-wishlist-for-hot-reloading)

_2,602 words_

##### [Name It, and They Will Come](https://overreacted.io/name-it-and-they-will-come)

_774 words_

##### [npm audit: Broken by Design](https://overreacted.io/npm-audit-broken-by-design)

_2,628 words_

##### [On let vs const](https://overreacted.io/on-let-vs-const)

_673 words_

##### [Optimized for Change](https://overreacted.io/optimized-for-change)

_225 words_

##### [Preparing for a Tech Talk, Part 1: Motivation](https://overreacted.io/preparing-for-tech-talk-part-1-motivation)

_1,122 words_

##### [Preparing for a Tech Talk, Part 2: What, Why, and How](https://overreacted.io/preparing-for-tech-talk-part-2-what-why-and-how)

_891 words_

##### [Preparing for a Tech Talk, Part 3: Content](https://overreacted.io/preparing-for-tech-talk-part-3-content)

_1,401 words_

##### [React as a UI Runtime](https://overreacted.io/react-as-a-ui-runtime)

_6,760 words_

##### [React for Two Computers](https://overreacted.io/react-for-two-computers)

_16,499 words_

##### [The “Bug-O” Notation](https://overreacted.io/the-bug-o-notation)

_1,127 words_

##### [The Elements of UI Engineering](https://overreacted.io/the-elements-of-ui-engineering)

_1,971 words_

##### [The Two Reacts](https://overreacted.io/the-two-reacts)

_1,638 words_

##### [The WET Codebase](https://overreacted.io/the-wet-codebase)

_196 words_

##### [Things I Don’t Know as of 2018](https://overreacted.io/things-i-dont-know-as-of-2018)

_1,198 words_

##### [What Are the React Team Principles?](https://overreacted.io/what-are-the-react-team-principles)

_1,196 words_

##### [What Is JavaScript Made Of?](https://overreacted.io/what-is-javascript-made-of)

_2,899 words_

##### [Why Do React Hooks Rely on Call Order?](https://overreacted.io/why-do-hooks-rely-on-call-order)

_3,891 words_

##### [Why Do React Elements Have a $$typeof Property?](https://overreacted.io/why-do-react-elements-have-typeof-property)

_910 words_

##### [Why Do We Write super(props)?](https://overreacted.io/why-do-we-write-super-props)

_912 words_

##### [Why Isn’t X a Hook?](https://overreacted.io/why-isnt-x-a-hook)

_1,328 words_

##### [Writing Resilient Components](https://overreacted.io/writing-resilient-components)

_4,689 words_

Notice how you can click each card, and it will expand. This is not plain HTML—all of these are interactive React components that got their props from the backend.

* * *

### [A Sortable List of Previews](https://overreacted.io/impossible-components/#a-sortable-list-of-previews)

Now let’s make the list of previews filterable and sortable.

Here’s what we want to end up with:

How hard could it be?

First, let’s dig up the `SortableList` component from earlier. We’re going to take the same exact [code as before](https://overreacted.io/impossible-components/#a-filterable-list) but we’ll assume `items` to be an array of objects shaped like `{ id, content, searchText }` rather than an array of strings:

```
'use client';
 
import { useState } from 'react';
 
export function SortableList({ items }) {
  const [isReversed, setIsReversed] = useState(false);
  const [filterText, setFilterText] = useState('');
  let filteredItems = items;
  if (filterText !== '') {
    filteredItems = items.filter(item =>
      item.searchText.toLowerCase().startsWith(filterText.toLowerCase()),
    );
  }
  const sortedItems = isReversed ? filteredItems.toReversed() : filteredItems;
  return (
    <>
      <button onClick={() => setIsReversed(!isReversed)}>
        Flip order
      </button>
      <input
        value={filterText}
        onChange={(e) => setFilterText(e.target.value)}
        placeholder="Search..."
      />
      <ul>
        {sortedItems.map(item => (
          <li key={item.id}>
            {item.content}
          </li>
        ))}
      </ul>
    </>
  );
}
```

For `SortableFileList`, we’ll keep passing the filename itself as each field:

```
import { SortableList } from './client';
import { readdir } from 'fs/promises';
 
async function SortableFileList({ directory }) {
  const files = await readdir(directory);
  const items = files.map((file) => ({
    id: file,
    content: file,
    searchText: file,
  }));
  return <SortableList items={items} />;
}
```

```
'use client';
 
import { useState } from 'react';
 
export function SortableList({ items }) {
  // ...
}
```

You can see that it continues working just fine:

```
<SortableFileList directory="./public/impossible-components" />
```

*   client.js
*   color.txt
*   color1.txt
*   color2.txt
*   color3.txt
*   components.js
*   index.md
*   server.js

However, now we can reuse `<SortableList>` by passing a list of posts to it:

```
import { SortableList } from './client';
import { readdir } from 'fs/promises';
 
async function SortablePostList() {
  const entries = await readdir('./public/', { withFileTypes: true });
  const dirs = entries.filter((entry) => entry.isDirectory());
  const items = dirs.map((dir) => ({
    id: dir.name,
    searchText: dir.name.replaceAll('-', ' '),
    content: <PostPreview slug={dir.name} />
  }));
  return (
    <div className="mb-8 flex h-72 flex-col gap-2 overflow-scroll font-sans">
      <SortableList items={items} />
    </div>
  );
}
```

```
'use client';
 
import { useState } from 'react';
 
export function SortableList({ items }) {
  // ...
}
```

See for yourself:

```
<SortablePostList />
```

Play with the demo above and make sure you understand what’s going on.

This is a fully interactive React tree. You can click on individual items, and they will expand and collapse thanks to the local state inside `<ExpandingSection>`. In fact, if you expand a card, click “Flip order” and then “Flip order” again, you’ll notice that the card stays expanded—it just moved down and back up in the tree.

You can do the filtering and reordering thanks to `<SortableList>`. Note that the `SortableList` itself is blissfully unaware of _what_ it’s sorting. You can put a list of any content inside it—and it’s fine to pass props to it directly from the backend.

On the backend, the `<PostPreview>` component fully encapsulates reading information for a specific post. It takes care of counting the words and extracting their first sentence, and then passing that down to the `<ExpandingSection>`.

Notice that although there is a single `<PostPreview>` rendered for each of my posts, the data necessary for _this entire page_ is being collected in a single run and served as a single roundtrip. When you visit this page, there are no extra requests. Only the data _used by the UI_ is sent over the wire—i.e. the props for the frontend.

We’re composing self-contained components that each can load their own data or manage their own state. At any point, we can add more encapsulated data loading logic or more encapsulated stateful logic at any point in the tree—as long as we’re doing it in the right world. It takes some skill and practice to learn these patterns, but the reward is making components like `<SortablePostList />` possible.

Local state.

Local data.

Single roundtrip.

_Self-contained._

* * *

### [In Conclusion](https://overreacted.io/impossible-components/#in-conclusion)

Our users don’t care about how any of this stuff works. When people use our websites and apps, they don’t think in terms of the “frontend” and the “backend”. They see the things on the screen: _a section, a header, a post preview, a sortable list._

_But maybe our users are right._

Composable abstractions with self-contained data logic and state logic let us speak the same language as our users. Component APIs like `<PostPreview slug="...">` and `<SortableList items={...}>` map to how we _intuitively_ think about those boxes on the screen. The fact that implementing self-contained `<PostPreview>` and `<SortableList>` without compromises requires running them on different “sides” is not a problem if we can compose them together.

The division between the frontend and the backend is physical. We can’t escape from the fact that we’re writing client/server applications. Some logic is naturally _more suited_ to either side. But one side should not dominate the other. And we shouldn’t have to change the approach whenever we need to move 
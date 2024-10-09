Title: jazz - Instant sync

URL Source: https://jazz.tools/

Markdown Content:
Build your next app with sync.
------------------------------

Jazz is an open-source framework for building local-first apps, removing 90% of the backend and infrastructure complexity. Get real-time sync, storage, auth, permissions, instant UI updates, file uploads, and more — all on day one.

Hard things are easy now.
-------------------------

Ever notice how every stack just reinvents shared state between users and machines?

And far from the simple client-server model, you routinely tackle a mess of moving parts, tech choices and deployment questions.

And your app’s code is all over the place.

Jazz provides a single new abstraction to do the whole job.

It turns the data flow around and gives you mutable local state, solving sync, concurrent editing and permissions under the hood.

All that’s left? What makes your app your app.

Everything you need to ship top-tier apps quickly.
--------------------------------------------------

Features that used to take months to build now work out-of-the-box.

First impressions...
--------------------

A chat app in 174 lines of code.

Jazz Mesh
---------

Serverless sync & storage for Jazz apps

To give you sync and secure collaborative data instantly on a global scale, we're running Jazz Mesh. It works with any Jazz-based app, requires no setup and has straightforward, scale-to-zero pricing.

Jazz Mesh is currently free — and it's set up as the default sync & storage peer in Jazz, letting you start building multi-user apps with persistence right away, no backend needed.

[Learn more about Jazz Mesh \-\>](https://jazz.tools/mesh)

Collaborative Values
--------------------

Your new building blocks.

Based on CRDTs and public-key cryptography, CoValues...

*   Can be read & edited like simple local JSON state
*   Can be created anywhere, are automatically synced & persisted
*   Always keep full edit history & author metadata
*   Automatically resolve most conflicts

Bread-and-butter datastructures
-------------------------------

### `CoMap`

*   Collaborative key-value map
*   Possible values:
    *   Immutable JSON & other CoValues

### `CoList`

*   Collaborative ordered list
*   Possible items:
    *   Immutable JSON & other CoValues

### `CoPlainText` & `CoRichText` Coming soon

*   Collaborative plain-text & rich-text
*   Gracefully prevents most editing conflicts
*   Rendered as markdown, HTML, JSX, etc.

### `CoStream`

*   Collection of independent per-user items streams:
    *   Immutable JSON & other CoValues
*   Great for presence, reactions, polls, replies etc.

First-class files & binary data
-------------------------------

### `BinaryCoStream`

*   Represents a file or live binary stream
*   Can be referenced and synced like any other CoValue
*   Can easily be converted from/to browser `Blob`s
*   `<input type="file"/>` -\> `BinaryCoStream` -\> `Blob` -\> `BlobURL`

### `ImageDefinition`

*   Represents multiple resolutions of the same image
*   Can be progressively loaded, including super fast blur preview & image size info

Secure permissions, authorship & teams
--------------------------------------

### `Group`

*   A scope where specified accounts have roles (`reader`/`writer`/`admin`).
*   A `Group` owns `CoValues`, with access right determined by group roles.
*   Accounts can be added to groups directly or using shareable invite secrets.

### `Account`

*   Represents a single user and their signing/encryption keys.
*   Has a private account root and a public profile
    *   Can contain arbitrary app-specific data

The Jazz Toolkit
----------------

A high-level toolkit for building apps around CoValues.

Supported environments:

*   Browser (sync via WebSockets, IndexedDB persistence)
    *   React
    *   Vanilla JS / framework agnostic base
*   React Native Coming soon
*   NodeJS (sync via WebSockets, SQLite persistence) Coming soon
*   Swift, Kotlin, Rust Coming later

Auto-sub
--------

Let your UI drive data-syncing.

*   Load and auto-subscribe to deeply nested `CoValues` with a reactive hook (or callback).
*   Access properties & metadata as plain JSON.
*   Make granular changes with simple mutators.
*   No queries needed, everything loads on-demand:  
    `profile?.tweets?.map(tweet => tweet?.text)`

Cursors & carets
----------------

Ready-made spatial presence.

*   2D canvas cursors Coming soon
*   Text carets Coming soon
*   Element-based focus-presence Coming soon
*   Scroll-based / out-of-bounds helpers Coming soon

Auth Providers
--------------

Plug and play different kinds of auth.

*   DemoAuth (for quick multi-user demos)
*   WebAuthN (TouchID/FaceID)
*   Auth0, Clerk & Okta Coming soon
*   NextAuth Coming soon

Two-way sync to your DB
-----------------------

Add Jazz to an existing app.

*   Prisma Coming soon
*   Drizzle Coming soon
*   PostgreSQL introspection Coming soon

File upload & download
----------------------

Just use `<input type='file'/>`.

*   Easily convert from and to Browser `Blob`s
*   Super simple progressive image loading

Video presence & calls
----------------------

Stream and record audio & video.

*   Automatic WebRTC connections between `Group` members Coming soon
*   Audio/video recording into `BinaryCoStreams` Coming soon

### Get started

© 2024  
Garden Computing, Inc.

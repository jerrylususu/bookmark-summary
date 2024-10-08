Title: Some notes on upgrading Hugo

URL Source: https://jvns.ca/blog/2024/10/07/some-notes-on-upgrading-hugo/

Markdown Content:
Warning: this is a post about very boring yakshaving, probably only of interest to people who are trying to upgrade Hugo from a very old version to a new version. But what are blogs for if not documenting one’s very boring yakshaves from time to time?

So yesterday I decided to try to upgrade Hugo. There’s no real reason to do this – I’ve been using Hugo version 0.40 to generate this blog since 2018, it works fine, and I don’t have any problems with it. But I thought – maybe it won’t be as hard as I think, and I kind of like a tedious computer task sometimes!

I thought I’d document what I learned along the way in case it’s useful to anyone else doing this very specific migration. I upgraded from Hugo v0.40 (from 2018) to v0.135 (from 2024).

Here are most of the changes I had to make:

### change 1: `template "theme/partials/thing.html` is now `partial thing.html`

I had to replace a bunch of instances of `{{ template "theme/partials/header.html" . }}` with `{{ partial "header.html" . }}`.

This happened in [v0.42](https://github.com/gohugoio/hugo/releases/tag/v0.42):

> We have now virtualized the filesystems for project and theme files. This makes everything simpler, faster and more powerful. But it also means that template lookups on the form {{ template “theme/partials/pagination.html” . }} will not work anymore. That syntax has never been documented, so it’s not expected to be in wide use.

### change 2: `.Data.Pages` is now `site.RegularPages`

This seems to be discussed in the [release notes for 0.57.2](https://github.com/gohugoio/hugo/releases/tag/v0.57.2)

I just needed to replace `.Data.Pages` with `site.RegularPages` in the template on the homepage as well as in my RSS feed template.

### change 3: `.Next` and `.Prev` got flipped

I had this comment in the part of my theme where I link to the next/previous blog post:

> “next” and “previous” in hugo apparently mean the opposite of what I’d think they’d mean intuitively. I’d expect “next” to mean “in the future” and “previous” to mean “in the past” but it’s the opposite

It looks they changed this in [ad705aac064](https://github.com/gohugoio/hugo/commit/ad705aac0649fa3102f7639bc4db65d45e108ee2) so that “next” actually is in the future and “prev” actually is in the past. I definitely find the new behaviour more intuitive.

### downloading the Hugo changelogs with a script

Figuring out why/when all of these changes happened was a little difficult. I ended up hacking together a bash script to [download all of the changelogs from github as text files](https://gist.github.com/jvns/dbe4bd9271a56f1f8562bfe329c2aa9e), which I could then grep to try to figure out what happened. It turns out it’s pretty easy to get all of the changelogs from the GitHub API.

So far everything was not so bad – there was also a change around taxonomies that’s I can’t quite explain, but it was all pretty manageable, but then we got to the really tough one: the markdown renderer.

### change 4: the markdown renderer (blackfriday -\> goldmark)

The blackfriday markdown renderer (which was previously the default) was removed in [v0.100.0](https://github.com/gohugoio/hugo/releases/tag/v0.100.0). This seems pretty reasonable:

> It has been deprecated for a long time, its v1 version is not maintained anymore, and there are many known issues. Goldmark should be a mature replacement by now.

Fixing all my Markdown changes was a huge pain – I ended up having to update 80 different Markdown files (out of 700) so that they would render properly, and I’m not totally sure

### why bother switching renderers?

The obvious question here is – why bother even switching Markdown renderers? My old site was running totally fine and I think it wasn’t necessarily a _good_ use of time, but the one reason I think it might be useful in the future is that the new renderer (goldmark) uses the [CommonMark markdown standard](https://commonmark.org/), which I’m hoping will be somewhat more futureproof. So maybe I won’t have to go through this again? We’ll see.

Also it turned out that the new Goldmark renderer does fix some problems I had (but didn’t know that I had) with smart quotes and how lists/blockquotes interact.

### finding all the Markdown problems: the process

The hard part of this Markdown change was even figuring out what changed. Almost all of the problems (including #2 and #3 above) just silently broke the site, they didn’t cause any errors or anything. So I had to diff the HTML to hunt them down.

Here’s what I ended up doing:

1.  Generate the site with the old version, put it in `public_old`
2.  Generate the new version, put it in `public`
3.  Diff every single HTML file in `public/` and `public_old` with [this diff.sh script](https://gist.github.com/jvns/c7272cfb906e3ed0a3e9f8d361c5b5fc) and put the results in a `diffs/` folder
4.  Run variations on `find diffs -type f | xargs cat | grep -C 5 '(31m|32m)' | less -r` over and over again to look at every single change until I found something that seemed wrong
5.  Update the Markdown to fix the problem
6.  Repeat until everything seemed okay

(the `grep 31m|32m` thing is searching for red/green text in the diff)

This was very time consuming but it was a little bit fun for some reason so I kept doing it until it seemed like nothing too horrible was left.

### the new markdown rules

Here’s a list of every type of Markdown change I had to make. It’s very possible these are all extremely specific to me but it took me a long time to figure them all out so maybe this will be helpful to one other person who finds this in the future.

#### 4.1: mixing HTML and markdown

This doesn’t work anymore (it doesn’t expand the link):

```
<small>
[a link](https://example.com]
</small>
```

I need to do this instead:

```
<small>

[a link](https://example.com]

</small>
```

#### 4.2: `<<` is changed into «

I didn’t want this so I needed to configure:

```
markup:
  goldmark:
    extensions:
      typographer:
        leftAngleQuote: '&lt;&lt;'
        rightAngleQuote: '&gt;&gt;'
```

#### 4.3: nested lists sometimes need 4 space indents

This doesn’t render as a nested list anymore if I only indent by 2 spaces, I need to put 4 spaces.

```
1. a
  * b
  * c
2. b
```

The problem is that the amount of indent needed depends on the size of the list markers. [Here’s a reference in CommonMark for this](https://spec.commonmark.org/0.29/#example-263).

#### 4.4: blockquotes inside lists work better

Previously the `> quote` here didn’t render as a blockquote, and with the new renderer it does.

```
* something
> quote
* something else
```

I found a bunch of Markdown that had been kind of broken (which I hadn’t noticed) that works better with the new renderer, and this is an example of that.

Lists inside blockquotes also seem to work better.

#### 4.5: headings inside lists

Previously this didn’t render as a heading, but now it does. So I needed to replace the `#` with `&#35;`.

```
* # passengers: 20
```

#### 4.6: `+` or `1)` at the beginning of the line makes it a list

I had something which looked like this:

```
`1 / (1
+ exp(-1)) = 0.73`
```

With Blackfriday it rendered like this:

```
<p><code>1 / (1
+ exp(-1)) = 0.73</code></p>
```

and with Goldmark it rendered like this:

```
<p>`1 / (1</p>
<ul>
<li>exp(-1)) = 0.73`</li>
</ul>
```

Same thing if there was an accidental `1)` at the beginning of a line, like in this Markdown snippet

```
I set up a small Hadoop cluster (1 master, 2 workers, replication set to 
1) on 
```

To fix this I just had to rewrap the line so that the `+` wasn’t the first character.

The Markdown is formatted this way because I wrap my Markdown to 80 characters a lot and the wrapping isn’t very context sensitive.

#### 4.7: no more smart quotes in code blocks

There were a bunch of places where the old renderer (Blackfriday) was doing unwanted things in code blocks like replacing `...` with `…` or replacing quotes with smart quotes. I hadn’t realized this was happening and I was very happy to have it fixed.

#### 4.8: better quote management

The way this gets rendered got better:

```
"Oh, *interesting*!"
```

*   old: “Oh, _interesting_!“
*   new: “Oh, _interesting_!”

Before there were two left smart quotes, now the quotes match.

#### 4.9: images are no longer wrapped in a `p` tag

Previously if I had an image like this:

```
<img src="https://jvns.ca/images/rustboot1.png">
```

it would get wrapped in a `<p>` tag, now it doesn’t anymore. I dealt with this just by adding a `margin-bottom: 0.75em` to images in the CSS, hopefully that’ll make them display well enough.

#### 4.10: `<br>` is now wrapped in a `p` tag

Previously this wouldn’t get wrapped in a `p` tag, but now it seems to:

```
<br><br>
```

I just gave up on fixing this though and resigned myself to maybe having some extra space in some cases. Maybe I’ll try to fix it later if I feel like another yakshave.

#### 4.11: some more goldmark settings

I also needed to

*   turn off code highlighting (because it wasn’t working properly and I didn’t have it before anyway)
*   use the old “blackfriday” method to generate heading IDs so they didn’t change
*   allow raw HTML in my markdown

Here’s what I needed to add to my `config.yaml` to do all that:

```
markup:
  highlight:
    codeFences: false
  goldmark:
    renderer:
      unsafe: true
    parser:
      autoHeadingIDType: blackfriday
```

Maybe I’ll try to get syntax highlighting working one day, who knows. I might prefer having it off though.

### a little script to compare blackfriday and goldmark

I also wrote a little program to compare the Blackfriday and Goldmark output for various markdown snippets, [here it is in a gist](https://gist.github.com/jvns/9cc3024ff98433ced5e3a2304c5fc5e4).

It’s not really configured the exact same way Blackfriday and Goldmark were in my Hugo versions, but it was still helpful to have to help me understand what was going on.

### a quick note on maintaining themes

My approach to themes in Hugo has been:

1.  pay someone to make a nice design for the site (for example wizardzines.com was designed by [Melody Starling](https://melody.dev/))
2.  use a totally custom theme
3.  commit that theme to the same Github repo as the site

So I just need to edit the theme files to fix any problems. Also I wrote a lot of the theme myself so I’m pretty familiar with how it works.

Relying on someone else to keep a theme updated feels kind of scary to me, I think if I were using a third-party theme I’d just copy the code into my site’s github repo and then maintain it myself.

### that’s it!

Overall I’ve been happy with Hugo – I [started using it](https://jvns.ca/blog/2016/10/09/switching-to-hugo/) because it had fast build times and it was a static binary, and both of those things are still extremely useful to me.

I find it hard to be too mad about the backwards incompatible changes, most of them were quite a long time ago, Hugo does a great job of making their old releases available so you can use the old release if you want, and the most difficult one is removing support for the `blackfriday` Markdown renderer in favour of using something CommonMark-compliant which seems pretty reasonable to me even if it is a huge pain.

But it did take a long time and I don’t think I’d particularly recommend moving 700 blog posts to a new Markdown renderer unless you’re really in the mood for a lot of computer suffering for some reason.

The new renderer did fix a bunch of problems so I think overall it might be a good thing, even if I’ll have to remember to make 2 changes to how I write Markdown (4.1 and 4.3).

Also I’m still using Hugo 0.54 for [https://wizardzines.com](https://wizardzines.com/) so maybe these notes will be useful to Future Me if I ever feel like upgrading Hugo for that site.

Hopefully I didn’t break too many things on the blog by doing this, let me know if you see anything broken!

Title: A brief history of JavaScript | Deno

URL Source: https://deno.com/blog/history-of-javascript

Markdown Content:
This year, JavaScript turns 30.

Within three decades, JavaScript went from being a weird little scripting language developed in 10 days to the world's most popular programming language. Here are some key moments in its history to show how JavaScript has evolved and where it is headed.

1994
----

December 1994

### Netscape releases Netscape Navigator 1.0

Netscape Navigator 1.0 was a watershed moment for the web. It quickly became the most popular web browser, as it was faster and easier to use than [Mosaic](https://en.wikipedia.org/wiki/NCSA_Mosaic) (a web browser released in 1993). It had a slick graphical UI, unlike many of the earlier text-based browsers. Also it supported emerging standards like HTML 2.0, and eventually... JavaScript.

[![Image 1: Netscape Navigator 1.0](https://deno.com/blog/history-of-javascript/netscape-navigator.webp)](https://www.webdesignmuseum.org/software/netscape-navigator-1-0-in-1994)

1995
----

May 1995

### [Brendan Eich creates the very first version of JavaScript](https://cybercultural.com/p/1995-the-birth-of-javascript/)

Netscape wanted to add interactivity to the early web, which at the time was mostly written in HTML. Around the same time, Sun Microsystems launched Java, and as part of that launch, Netscape licensed Java for use in the browser. But Java was a little too complicated for web designers.

Netscape asked Brendan Eich to develop a scripting language that looks like Java, but be object oriented rather than class based. And in ten short days, the language that powers most of the internet today was born. They arrived at the name “JavaScript” for marketing reasons, as Java, at the time, was the hot new programming language, so the name exploited that popularity.

December 1995

### [Netscape and Sun announce JavaScript](https://www.tech-insider.org/java/research/1995/1204.html), the open, cross-platform object-oriented scripting language for enterprise networks and the internet

JavaScript was introduced as an easy-to-use, lightweight scripting language for adding interactivity to HTML. In this announcement, Netscape and Sun laid out their vision for the new web: Java objects being served to the client, where JavaScript scripts can modify them. Also notable is the industry support from 28 technology companies, ranging from America Online to Toshiba Corporation.

1996
----

March 1996

### Microsoft introduces [JScript](https://cybercultural.com/p/1996-microsoft-activates-the-internet-with-activex-jscript/) in Internet Explorer 3 to compete with Netscape Navigator

JScript, named to avoid the copyrighted word “Java”, was an open implementation of JavaScript molded to the Windows ecosystem. Unlike Netscape's JavaScript, JScript could interact with Window's ActiveXObject, allowing developers to connect from Internet Explorer to an Excel spreadsheet for instance.

```
var ExcelSheet;
ExcelSheet = new ActiveXObject(“Excel.Sheet”);
// Make Excel visible through the Application object.
ExcelSheet.Application.Visible = true;
// Place some text in the first cell of the sheet.
ExcelSheet.ActiveSheet.Cells(1,1).Value = “This is column A, row 1”;
// Save the sheet.
ExcelSheet.SaveAs(“C:TEST.XLS”);
// Close Excel with the Quit method on the Application object.
ExcelSheet.Application.Quit();
// Release the object variable.
ExcelSheet = “”;
```

March 1996

### Netscape Navigator 2.0 is released with JavaScript 1.0

This is JavaScript's debut, landing in millions of homes with Netscape Navigator 2.0. With JavaScript 1.0 came another key innovation that became a fundamental model of the web — the Document Object Model (DOM).

![Image 2](https://deno.com/blog/history-of-javascript/netscape-navigator-2.webp)

1997
----

June 1997

### Netscape submits JavaScript to ECMA International

To avoid a fractured browser ecosystem, with JavaScript and Microsoft's JScript, Netscape submitted JavaScript to [ECMA International](https://ecma-international.org/), aiming to create a vendor-neutral standardized language that everyone can use. The standard spec was called ECMA-262 and the language “ECMAScript” ([not named JavaScript due to trademark issues](https://javascript.tm/)), of which JavaScript and JScript became dialects. Additionally, a technical committee named [TC39](https://tc39.es/) was formed, consisting of representatives from Netscape, Microsoft, Sun Microsystems, and more, to govern the evolution of ECMAScript.

1998
----

January 1998

### Amid declining market share, Netscape open sources Navigator, leading to the creation of [The Mozilla Project](https://www.mozilla.org/en-US/about/history/)

Since Microsoft bundled Internet Explorer with Windows, Netscape Navigator saw a rapid decline in market share. In a bold effort to save the company and compete with Microsoft, Netscape open sources its browser code, “Mozilla” (its internal codename, a portmanteau of “Mosaic” and “killer”), to allow the community to contribute to the development of a more advanced and standards-compliant browser. The next day, [Jamie Zawinksi](https://en.wikipedia.org/wiki/Jamie_Zawinski) of Netscape registered mozilla.org. The Mozilla project created several impactful technologies and products: Firefox, tabbed browsing, browser extensions, and [the programming language, Rust](https://en.wikipedia.org/wiki/Rust_(programming_language)#:~:text=Software%20developer%20Graydon%20Hoare%20created,sponsored%20the%20project%20in%202009.).

![Image 3](https://deno.com/blog/history-of-javascript/mozilla-logo.webp)

September 1998

### Official release of the [first ECMAScript language specification](https://ecma-international.org/wp-content/uploads/ECMA-262_2nd_edition_august_1998.pdf) (ECMAScript 2)

Though no new features were added to the ECMAScript language, it ensured the spec was clean, consistent, and standardized. This set the groundwork for all future editions.

![Image 4](https://deno.com/blog/history-of-javascript/ecmascript2.webp)

1999
----

March 1999

### Microsoft releases Internet Explorer 5, which uses more proprietary technology than before.

More importantly, Microsoft introduces `XMLHttpRequest` — the first practical way to send HTTP requests via JavaScript:

```
// How to send an HTTP request in IE5.

<script type="text/javascript">
  function makeRequest() {
    // Create the ActiveXObject (specific to IE5/IE6)
    var xhr = new ActiveXObject("Microsoft.XMLHTTP");

    // Open a GET request (async = true)
    xhr.open("GET", "https://example.com/data.txt", true);

    // Define a callback to run when the response is ready
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        alert("Response received: " + xhr.responseText);
      }
    };

    // Send the request
    xhr.send();
  }
</script>

<button onclick="makeRequest()">Send HTTP Request</button>
```

April 1999

### [JSDoc](https://jsdoc.app/) debuts

JSDoc, loosely based off [Javadoc](https://en.wikipedia.org/wiki/Javadoc) for Java, introduced a formal structured way to document JavaScript. This brought professionalism to the language, laid the groundwork for IDE support, and enabled documentation generation (it powers [`deno doc`](https://docs.deno.com/runtime/reference/cli/doc/) as well as the docs generation for modules on [jsr.io](https://jsr.io/)).

```
/**
 * Adds two numbers together and returns the result.
 * @param {number} value1 The first value
 * @param {number} value2 The second value
 */
function addNumbers(value1, value2) {
  return value1 + value2;
}
```

December 1999

### [ECMAScript 3](https://www-archive.mozilla.org/js/language/e262-3.pdf) is released with `do-while`, regex, new string methods (`concat`, `match`, `replace`, `slice`, `split`), exception handling, and more

ECMAScript 3 was an important early milestone in JavaScript, as it transformed it from a toy scripting language into a serious programming tool. It would become the baseline language for browser scripting for over a decade, and widely considered as the version of JavaScript that defined the language for the web.

2001
----

April 2001

### The [first JSON message](https://twobithistory.org/2017/09/21/the-rise-and-rise-of-json.html) is sent

And it looks something like this:

```
<html><head><script>
    document.domain = 'fudco';
    parent.session.receive(
        { to: "session", do: "test",
          text: "Hello world" }
    )
</script></head></html>
```

2002
----

June 2002

### [JSLint](https://web.archive.org/web/20180226015758/https://codekitapp.com/help/jslint/), the “grandfather of all JavaScript syntax checkers” is introduced

JSLint, created by Douglas Crockford, was the first major static code analysis tool for JavaScript. At the time, JavaScript was widely used but poorly understood, and written without discipline. JSLint sought to level up the code quality. The strong opinions enforced by JSLint helped form Crockford's book, [“JavaScript, the Good Parts”](https://www.oreilly.com/library/view/javascript-the-good/9780596517748/).

September 2002

### [Mozilla releases Phoenix 0.1](https://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes/en-us/firefox/releases/0.1), precursor to Firefox, to compete with Internet Explorer

Fed up with how slow and bloated the Mozilla Application Suite was, a small team built a minimalist stripped down version of a web browser called Phoenix (to signify the rebirth of the browser from the ashes of Netscape and Mozilla Suite). At the time, Internet Explorer had 90% of market share, and innovation stagnated. Phoenix offered something new to internet users: speed, simple UI, tabbed browsing, and pop-up blockers. This marked the rebirth of user-focused, open-source browsers, became the foundation of Firefox, and broke Microsoft's monopoly on the browser market.

[![Image 5: Phoenix 0.1](https://deno.com/blog/history-of-javascript/2002_phoenix.webp)](https://blog.mozilla.org/community/2013/05/13/milestone-phoenix-0-1-released-first-version-of-firefox/)

2003
----

January 2003

### Apple introduces Safari and WebKit

Apple CEO Steve Jobs announces [Safari](https://www.apple.com/newsroom/2003/01/07Apple-Unveils-Safari/), “a turbo browser for Mac OS X”. Most importantly, it ended Apple's dependence on Microsoft, as before Mac users relied on Internet Explorer for Mac. Additionally, this paved the way for Apple's Mobile Safari a few years later with the iPhone. It is based on WebKit, an internal fork of the KHTML browser engine.

[![Image 6: Safari 1.0](https://deno.com/blog/history-of-javascript/safari.webp)](https://www.howtogeek.com/browsing-the-web-with-safari-1-0/)

2004
----

April 2004

### A beta version of Gmail is released, which uses a new asynchronous JavaScript protocol, “AJAX”

The launch of Gmail was a turning point in web development. AJAX allowed Gmail to offer a highly responsive, interactive user experience that was unprecedented for a web site at the time, ushering a new Web 2.0 era of web applications.

[![Image 7: Gmail](https://deno.com/blog/history-of-javascript/gmail-2004.webp)](https://www.webdesignmuseum.org/gallery/gmail-2004)

2005
----

February 2005

### Jesse James Garrett coins “AJAX” in his white paper, [“Ajax: A New Approach to Web Applications”](https://designftw.mit.edu/lectures/apis/ajax_adaptive_path.pdf)

Ajax, short for asynchronous JavaScript and XML, is a set of client-side techniques to create web apps that can send and receive data from a server asynchronously without needing a page reload. This unlocked a whole new class of web apps, as well as frameworks, that can deliver a rich and seamless user experience.

```
<script type="text/javascript">
  function createXHR() {
    if (window.XMLHttpRequest) {
      // Modern browsers (Mozilla, Safari, IE7+)
      return new XMLHttpRequest();
    } else if (window.ActiveXObject) {
      // Older versions of IE (IE5, IE6)
      try {
        return new ActiveXObject("Msxml2.XMLHTTP");
      } catch (e) {
        try {
          return new ActiveXObject("Microsoft.XMLHTTP");
        } catch (e) {
          alert("AJAX not supported in your browser.");
          return null;
        }
      }
    }
    return null;
  }

  function loadData() {
    var xhr = createXHR();
    if (!xhr) return;

    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          document.getElementById("result").innerHTML = xhr.responseText;
        } else {
          alert("Request failed: " + xhr.status);
        }
      }
    };

    xhr.open("GET", "/messages/latest", true); // Simulated Gmail-style endpoint
    xhr.send(null);
  }
</script>

<button onclick="loadData()">Load Latest Message</button>
<div id="result">Waiting for response...</div>
```

March 2005

### The Mozilla Corporation launches DevMo By Mozilla, which becomes MDN

[Mozilla launches DevMo By Mozilla](https://developer.mozilla.org/en-US/about#our_journey), which later became known as [MDN](https://developer.mozilla.org/en-US/) (Mozilla Developer Network). MDN provided an accurate, vendor-neutral, and standards-based documentation, and functioned as a central place for learning web standards. This came at a critical time when browser incompatibility was a major pain point, and documentation was fragmented, outdated, and inconsistent. MDN quickly became the go-to resource for web developers, and set a new standard for developer documentation.

[![Image 8](https://deno.com/blog/history-of-javascript/mdn-v1.webp)](https://developer.mozilla.org/en-US/about#our_journey)

2006
----

March 2006

### John Resig creates [first commit to a project named jQuery](https://github.com/jquery/jquery/commit/8a4a1edf047f2c272f663866eb7b5fcd644d65b3)

jQuery, a JavaScript library designed to simplify HTML DOM tree traversal, event handling, Ajax, and more, was created to address frustrating issues related to cross-browser compatibility. It also provides a well documented terse API that sets a new standard for the developer experience and remains the most widely used JavaScript library in terms of actual page loads.

```
<script src="https://code.jquery.com/jquery-1.0.0.min.js"></script>
<script type="text/javascript">
  function sendRequest() {
    $.ajax({
        url: "https://example.com/data",
        type: 'GET',
				success: function(res) {
					document.getElementById("result").innerHTML = res;
        },
        error: function(xhr, status, error) {
          alsert("Request failed: " + status);
        }
    });
  }
</script>

<button onclick="sendRequest()">Fetch data</button>
<div id="result">Waiting for response...</div>
```

2007
----

January 2007

### [The first Apple iPhone is released](https://www.apple.com/newsroom/2007/01/09Apple-Reinvents-the-Phone-with-iPhone/) with its mobile safari not supporting Flash

The exclusion of Flash was a deliberate and controversial decision. At the time, Flash was responsible for 90% of interactive multimedia. However, Steve Jobs was against Flash, due to its high resource needs, prone to crashing, and proprietary nature. Developers took this as a sign that the future of mobile web content would not rely on Flash.

[![Image 9: iPhone Safari](https://deno.com/blog/history-of-javascript/iphone-safari.webp)](https://appleinsider.com/articles/16/01/07/apples-safari-browser-turns-13-years-old-today)

2008
----

February 2008

### [Netscape Navigator is sunset](https://techcrunch.com/2007/12/28/a-sad-milestone-aol-to-discontinue-netscape-browser-development/), marking the end of the “First Browser War”

AOL officially discontinues Netscape Navigator, which was a dominant browser in the 90's with over 90% market share at its peak, marking the end of an era for one of the most influential web browsers of the early internet. It lost ground to Internet Explorer, because Microsoft bundled with Windows, which led to a landmark anti-trust lawsuit against Microsoft that reshaped tech regulations.

[![Image 10](https://deno.com/blog/history-of-javascript/browser-wars-1.webp)](https://en.wikipedia.org/wiki/Browser_wars)

May 2008

### Douglas Crockford publishes [“JavaScript: The Good Parts”](https://www.oreilly.com/library/view/javascript-the-good/9780596517748/)

This book reframed JavaScript as a serious language when previously it had been mocked for poor design and confusing behavior.

[![Image 11: JavaScript: The Good Parts](https://deno.com/blog/history-of-javascript/javascript-the-good-parts.webp)](https://www.oreilly.com/library/view/javascript-the-good/9780596517748/)

September 2008

### [Google releases the Chrome browser](https://googleblog.blogspot.com/2008/12/google-chrome-beta.html), the fastest web browser at the time, and with it, the V8 engine.

At the time, browsers like Internet Explorer, Firefox, and Safari were relatively slow, with limited focus on JavaScript execution speed. Chrome was designed with a focus on speed, using the new V8 JavaScript engine. V8 was innovative in that it compiled JavaScript into native machine code before execution, implemented just-in-time compilation, and managed memory more efficiently through garbage collection. Google would soon open source V8, allowing developers to build on top of it, most notably the Node.js project.

[![Image 12: Chrome](https://deno.com/blog/history-of-javascript/chrome-2008.webp)](https://googleblog.blogspot.com/2008/12/google-chrome-beta.html)

2009
----

January 2009

### A specification for sharing JavaScript code, CommonJS (originally named ServerJS), is created

At this point, JavaScript began expanding beyond the browser to the server. Bigger projects were being built and JavaScript needed a better way to handle a lot of source code. It needed modularization. For more information on the history of CommonJS and how we got to where we are today, check out this [blog post](https://deno.com/blog/commonjs-is-hurting-javascript).

March 2009

### Ryan Dahl [begins work on Node.js](https://github.com/nodejs/node/blob/1afe6d26dbcf76de15df7e2c8fc3aadbbb8b117d/README)

Node.js, a cross-platform, open source JavaScript runtime environment, allowed the execution of JavaScript outside a web browser. With the introduction of Node.js, developers were able to create web servers and effectively full stack applications entirely in Javascript. Today, Node is used by [~3.5% of all websites](https://w3techs.com/technologies/details/ws-nodejs) (with known servers) and continues to be a predominant technology for building for the web.

[![Image 13](https://deno.com/blog/history-of-javascript/ryan-introduces-node.webp)](https://www.youtube.com/watch?v=jo_B4LTHi3I)

Ryan introduces Node.js in a talk a few years later. For an in-depth look at the Node.js project, check out [this one hour-long documentary](https://www.youtube.com/watch?v=LB8KwiiUGy0).

April 2009

### [Oracle acquires Sun Microsystems](https://www.oracle.com/corporate/pressrelease/oracle-buys-sun-042009.html), and with it, the JavaScript trademark

Oracle bolsters its position in the enterprise technology market with the purchase of Sun Microsystems and its ownership of Java. As part of the deal, Oracle acquires the trademark for JavaScript, creating confusion for the future of the language. Read more about [our current effort to #FreeJavaScript from Oracle about the trademark.](https://javascript.tm/)

![Image 14](https://deno.com/blog/history-of-javascript/oracle-sun.webp)

June 2009

### The [first commit on Express.js](https://github.com/expressjs/express/commit/9998490f93d3ad3d56c00d23c0aa13fac41c3f6b) is created

Express.js, a minimal, flexible, extensible web framework for Node.js, is one of the most widely used frameworks in the ecosystem. It introduces a modular middleware architecture with a focus on building RESTful APIs. It's influence on the ecosystem is unparalleled, inspiring frameworks like Koa, Nest, Fastify, and more. Though there was a period of time when the Express project did not receive active commits, today, it is on version 5, and is actively maintained.

![Image 15](https://deno.com/blog/history-of-javascript/express.webp)

December 2009

### [ECMAScript 5](https://ecma-international.org/wp-content/uploads/ECMA-262_5th_edition_december_2009.pdf) adds a `strict mode`, getters and setters, new array methods, JSON support, `string.trim()`, trailing commas for object literals

ECMAScript 5 marked the first major update to the language in 10 years, and introduced features that made JavaScript more powerful, secure, and maintainable.

December 2009

### The [first commit](https://github.com/jashkenas/coffeescript/commit/8e9d637985d2dc9b44922076ad54ffef7fa8e9c2) to a project named CoffeeScript is created

CoffeeScript was quickly adopted due to cleaner syntax (less boilerplate), arrow functions (before arrow functions), destructuring before ES6, and other quality of life improvements.

![Image 16](https://deno.com/blog/history-of-javascript/coffee-script.webp)

2010
----

January 2010

### [npm 1.0 is released](https://nodejs.org/en/blog/npm/npm-1-0-released/)

A registry for Node and JavaScript, npm, forever changes the way that JavaScript is shared. Now, it is the biggest open source registry in the world, with over 3 million packages.

![Image 17](https://deno.com/blog/history-of-javascript/npm.webp)

May 2010

### [WebStorm 1.0](https://blog.jetbrains.com/phpstorm/2010/05/phpstorm-1-0-webstorm-1-0-are-public-it-is-official/), a new JavaScript IDE by JetBrains, is released

Prior to WebStorm, text editors provided minimal support for JavaScript. WebStorm was the first dedicated JavaScript IDE that offered advance features like code analysis, error detection, code completion for JS/HTML/CSS, and debugging tools tailored to JavaScript.

October 2010

### AngularJS and [Backbone.js](https://cdn.statically.io/gh/jashkenas/backbone/0.1.0/index.html) are released

As JavaScript improves and developers are searching for newer, faster, easier ways to build more complex servers and applications, two full stack frameworks — AngularJS and Backbone — are released. They become popular for different reasons: Angular was declarative and opinionated; while Backbone was imperative and minimal. This also loosely marks the beginning of the modern Single Page Application (”SPA”) and “Framework churn”, a term that defines the manic emergence and retirement of several JavaScript frameworks in this era.

![Image 18](https://deno.com/blog/history-of-javascript/angular-backbone.webp)

2011
----

June 2011

### Microsoft and Joyent [ported Node.js to Windows](https://nodejs.org/en/blog/uncategorized/porting-node-to-windows-with-microsofts-help)

In 2011, [Ryan Dahl of Joyent and Bert Belder (current Deno co-founder/CTO) ported Node.js to Windows](https://tinyclouds.org/iocp_links), a significant milestone that expanded Node.js’s reach beyond Unix-based systems. One result from this effort was [libuv](https://github.com/libuv/libuv), a library that offers a unified interface for asynchronous networking on Linus, OSX, and Windows. This not only accelerated Node.js’s growth but also set the stage for Microsoft’s broader open-source strategy, ultimately transforming its developer ecosystem and paving the way for future initiatives like TypeScript, VS Code, and Azure Cloud Integration.

![Image 19](https://deno.com/blog/history-of-javascript/libuv.webp)

2012
----

March 2012

### [Webpack, a module bundler, is introduced](https://libraries.io/npm/webpack/0.1.0)

Webpack allowed developers to import anything to the client-side and eventually became the core build system behind React, Angular, Vue, and more. It laid the groundwork for Rollup, Parcel, Vite, and esbuild.

![Image 20](https://deno.com/blog/history-of-javascript/webpack.webp)

October 2012

### [Microsoft makes TypeScript 0.8 available for the public](https://devblogs.microsoft.com/typescript/announcing-typescript-0-8-1/)

In 2010, Anders Heljsberg (who also created C# and Turbo Pascal) began developing a static typed superset of JavaScript, named TypeScript. The goal of this project was to make it easier to write and maintain JavaScript at scale. In 2012, Microsoft makes it available for the public. TypeScript paved the way for enterprise-grade development in the JavaScript ecosystem, influenced the design of ECMAScript itself, and changed how large applications are built with JavaScript.

```
function add(x: number, y: number): number {
  return x + y;
}
```

2013
----

March 2013

### The first commit to Atom Shell (later renamed to Electron) was created

Atom Shell (renamed to [Electron](https://www.electronjs.org/) in 2015) lowered the barrier to building cross-platform desktop applications by using web technologies like HTML, CSS, JavaScript. It uses Node.js and Chromium, so developers could access the filesystem, network, and native OS APIs. Originally built to power GitHub's Atom text editor, which launched in public beta in April 2014, Atom Shell was used by some high profile early adopters, such as Slack. This framework played a pivotal role in ushering in an era where web technologies could be used to create desktop applications.

[![Image 21](https://deno.com/blog/history-of-javascript/electron-downloads.webp)](https://www.electronjs.org/blog/10-years-of-electron#user-content-fn-1-8ed87e)

February 2013

### Mozilla releases asm.js

asm.js is a strict subset of JavaScript designed to bring near-native performance to the web. Before, JavaScript was not considered suitable for CPU-intensive applications like 3D games and video processing. Developers could convert C/C++ code to asm.js, allowing for existing native applications to run in the browser. This was a huge step forward in the evolution of JavaScript as a serious runtime for computationally expensive applications, and paved the way for WebAssembly a few years later.

```
(function Module(stdlib, foreign, heap) {
  "use asm";

  function add(x, y) {
    x = x | 0;
    y = y | 0;
    return (x + y) | 0;
  }

  return { add: add };
})(this, {}, new ArrayBuffer(1024));

console.log(Module.add(10, 20)); // Outputs: 30
```

April 2013

### [Valeri Karpov coins the term “MEAN” stack](https://thecodebarbarian.wordpress.com/2013/04/29/easy-web-prototyping-with-mongodb-and-nodejs/)

The MEAN stack represents a full stack JavaScript framework that includes MongoDB, Express.js, AngularJS, and Node.js. This terminology became highly influential in shaping modern JavaScript-based web development.

![Image 22](https://deno.com/blog/history-of-javascript/mean-stack.webp)

May 2013

### Facebook releases React

[React](https://react.dev/), created by Jordan Walke, a software engineer at Facebook (now Meta), is a JavaScript library for declaratively building user interfaces. It was first introduced in the Facebook Newsfeed in 2011, and open sourced for the public in May 2013 at JSConf US. React’s component-driven approach for building interfaces solidified declarative UI patterns used in apps today.

[![Image 23](https://deno.com/blog/history-of-javascript/react.webp)](https://www.youtube.com/watch?v=GW0rj4sNH2w)

June 2013

### [Work on ESLint begins](https://github.com/eslint/eslint/commit/a658d7b0e7d915750f18d666823d54ef2129a9af)

Nicholas C. Zakas, a prominent JavaScript developer and former lead developer of the Yahoo! User Interface Library (YUI), began work on ESLint, a pluggable and configurable linter tool for identifying and fixing problems in JavaScript code. ESLint quickly became a crucial tool for JavaScript developers, addressing limitations in existing linting tools and setting new standards for code quality and consistency.

![Image 24](https://deno.com/blog/history-of-javascript/eslint.webp)

July 2013

### [Gulp is released](https://libraries.io/npm/gulp/0.0.1)

Eric Schoffstall releases Gulp.js, a streaming build system for automating tasks in web development. Gulp introduced a new way to handle repetitive tasks like minification, compilation, linting, and testing by using a simple, code-centric approach. It quickly gained popularity as a powerful, code-centric alternative to older task runners like Grunt, which was configuration-heavy, and influenced the evolution of modern build tools.

![Image 25](https://deno.com/blog/history-of-javascript/gulpjs.webp)

2014
----

February 2014

### [Vue.js is released](https://github.com/vuejs/vue/releases/tag/v0.10.0)

Evan You, a former Google engineer, releases Vue.js, a progressive JavaScript framework for building user interfaces. Unlike other frameworks of its time, Vue.js was designed to be approachable, incrementally adoptable, and highly performant, making it one of the most popular and influential frameworks in the modern JavaScript ecosystem.

![Image 26](https://deno.com/blog/history-of-javascript/vuejs.webp)

July 2014

### [Strongloop purchases open source framework Express](https://web.archive.org/web/20140801150932/http://strongloop.com/strongblog/tj-holowaychuk-sponsorship-of-express/)

StrongLoop (co-founded by Deno co-founder, Bert Belder), a company specializing in enterprise-grade Node.js solutions, acquired the rights to Express.js, with the goal of integrating it into a broader suite of tools focused on APIs and microservices. The community felt that Express's independence would be lost in the acquisition, which led to creating other frameworks such as Koa. Later, IBM acquired StrongLoop in 2015, and in 2019, Express.js joined the OpenJS Foundation, securing its governance and ensuring its long-term sustainability. After 10 years of being at Express 4.x, [Express 5](https://expressjs.com/2024/10/15/v5-release.html) was finally released in October 2024.

![Image 27](https://deno.com/blog/history-of-javascript/strongloop.webp)

September 2014

### The [first commit to Babel.js](https://github.com/babel/babel/commit/68cf48fd80b526f1ebb26cd7ec45f8d7c95696db) is created

Originally named [6to5](https://babeljs.io/blog/2015/01/12/6to5-esnext), Babel.js is a JavaScript compiler that allows developers to write modern JavaScript and make it backwards-compatible for older browsers and engines. Babel soon established itself as a standard tool in the ecosystem, being integrated into popular frameworks like React, Vue, and Angular, as well as module bundlers like Webpack, Rollup, and Parcel.

![Image 28](https://deno.com/blog/history-of-javascript/babel.webp)

October 2014

### [Meteor reaches 1.0](https://blog.meteor.com/meteor-1-0-d0702aab3ef)

Meteor made a splash in web development communities for being a radically simpler way to build real-time, JavaScript-only, full-stack applications. It played a major role in shaping how developers thought about building modern, reactive, real-time web applications. Although Meteor's overall popularity waned as the ecosystem evolved, it's influence can be seen in React, Redux, Firebase, GraphQL, and more.

![Image 29](https://deno.com/blog/history-of-javascript/meteor.webp)

November 2014

### [Facebook launches Flow](https://engineering.fb.com/2014/11/18/web/flow-a-new-static-type-checker-for-javascript/), a static type checker for JavaScript

Flow is a static type checker for JavaScript that helps developers catch bugs and type errors during development. Facebook developed it as a way to better maintain its massive codebase and improve developer productivity. By the late 2010s, however, TypeScript became the dominant typed JavaScript language, leading to the decline of Flow.

![Image 30](https://deno.com/blog/history-of-javascript/flow.webp)

November 2014

### [Amazon announces AWS Lambda](https://press.aboutamazon.com/2014/11/amazon-web-services-announces-aws-lambda), powered by Node.js

Amazon Web Services, already a market leader in cloud computing, introduces a new serverless paradigm with Lambda, which allows developers to upload code and run it in response to events without provisioning infrastructure. At launch, Lambda functions only supported JavaScript with Node.js, thanks to Node.js’s event-driven, non-blocking model that fit well with Lambda’s stateless and short-lived execution environment. The arrival of AWS Lambda introduced the concept of Function-as-a-Service and kicked off a serverless computing movement, with Google and Microsoft launching their own versions a year or two later.

![Image 31](https://deno.com/blog/history-of-javascript/aws-lambda.webp)

December 2014

### [Fedor Indutny creates io.js](https://blog.risingstack.com/iojs-overview/), a fork of Node.js

Node.js, maintained by Joyent at the time, had slow releases and lacked support for modern JavaScript features due to being on
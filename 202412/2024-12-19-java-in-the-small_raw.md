Title: Cay Horstmann's Unblog

URL Source: https://horstmann.com/unblog/2024-12-11/index.html

Markdown Content:
Java in the Small
-----------------

> Java has many features that make it well suited for large, long-lasting projects. But I find it surprisingly good for small tasks as well. Recent language features make it even better. The killer features are compile-time typing and great tool support.
> 
> This article also appeared in the [Java Advent](https://javaadvent.com/) calendar.

![Image 8: .jpg](https://horstmann.com/unblog/2024-12-11/rc24-duke-java-mascot.jpg)

In my job as author and teacher, I have many repetitive tasks, such as moving files around and transforming their content in tedious ways. In my quest to automate the boring stuff, I look at a task and think “no big deal, I'll write a shell script”. Then the inevitable happens. As more special cases arise, the script turns into a festering mess of bash code. And I wish that I had written it in a real programming language instead.

The “obvious” choice is Python, but the Python API isn't all that wonderful, and dynamic typing means that I spend too much time debugging. So I tried Java. I know the API by heart—at least for collections, files, regex, and so on. Java is statically typed so I am saved early from my foolishness. And the development environments are terrific.

But, I hear you say, really, a separate POM file and `src/main/java` hierarchy for every script? Ugh.

I don't do that. Fortunately, modern Java and tools don't require it. Read on for the details!

Launching without Compiling
---------------------------

Consider a simple, but not too simple, task. As an example, I have a procedure to verify that my backups actually work. I retrieve ten random files once a day, in a scheduled job. (This is a really good idea that has saved me more than once from unreliable backups.) A script randomly picks ten files from a directory tree. It's written in Java. And it sits in a directory with quite a few utility scripts.

Of course, I could compile it. But then my utility script directory would be cluttered with class files. Or I could make a JAR file. But that's work. When you write a script whose value may not yet be evident, who has the patience for JARs and uber JARs?

That's why I love [JEP 330](https://openjdk.org/jeps/330) and [JEP 458](https://openjdk.org/jeps/458). Now I can put my code in a `.java` file and just launch it as

java RandomFiles.java 10 /home/cay/data

The file gets compiled on the fly, every time that I run the script. And that's just the way I want it during development or later tinkering. And I don't care during regular use because it's not that slow. The Python crowd never loses sleep over that, so why should I?

You can compile scripts into native executables with Graal for faster startup time. I have experimented with that, but don't find it makes a meaningful difference for most of my use cases.

Why not use JShell? I love using JShell for quick experiments (most of which seem to involve debugging regular expressions 😿). But it's not great for scripts. The JShell tool itself has a very rudimentary editor integration, and the JShell support in IDEs is poor.

Instance Main Methods and Implicit Classes
------------------------------------------

[JEP 477](https://openjdk.org/jeps/477) reduces the verbosity of writing small Java programs. This effort is motivated by two desires. First, to make it easier to learn Java. And to simplify “other kinds of small programs, such as scripts and command-line utilities”. Having taught Java for many years, I never ran into students who said “my head hurts when I copy/paste the `public static void main` thing”. But I knew plenty of professors who were bothered by it. So it's a good thing it is going away.

And for us scripters, it's nice not to look at clutter.

var someVariable = initialValue;
String helper(int param) { ... }
void main(String\[\] args) {
    ...
}

No pesky class, no `static`.

Technically, any Java file with a top-level `main` method becomes an implicit class whose instance variables and methods are the top-level variables and methods in the file. Note that it is perfectly ok, and even desirable, to have classes, interfaces, enumerations, or records, in an implicit class. They turn into nested types.

As an added, benefit, all of the `java.base` module is automatically imported. Hooray, no more

import java.util.List;

(As it turns out, the class names in `java.base` have been carefully curated not to conflict with each other.)

As of Java 23, three methods are automatically imported from `java.io.IO`: `println`, `print`, `readln`. From a teaching perspective, that's not ideal because it is yet another factoid to remember. But as a scripter, I'll take it.

We get to enjoy these automatic imports only in an implicit class. But that's ok for many scripts.

![Image 9: .png](https://horstmann.com/unblog/2024-12-11/eclipse.png)

Records and Enums
-----------------

Python programmers often use ad-hoc dictionaries (i.e. maps) to aggregate related information. In Java, we have records:

record Window(int id, int desktop, int x, int y, int width, int height, String title) {}

They make the code easier to read, and they become natural spots for methods:

record Window(...) {
   int xmax() { return x + width; }
   int ymax() { return y + height; }
}

The same holds for enumerations:

enum Direction { NORTH, EAST, SOUTH, WEST };

Much nicer than the clunky Python enumerations.

Other Helpful Language Features
-------------------------------

With complex programs, I am conservative with the use of `var` and only use it when the type is blindingly obvious, e.g.

var builder = new StringBuilder();

But in a script, I use `var` liberally. It's almost like in Python, except that you still have compile-time typing. In fact, it is better syntax than Python because you can distinguish between declaration and assignment.

I am also more aggressive with static import:

import static java.lang.Math.\*;

diagonal = sqrt(pow(width, 2) + pow(height, 2));

(It's just an example, you can actually use `hypot(width, height)`.)

Text blocks are nice to keep data with your code. They play the same role as “here documents” in scripts. I hope that interpolation will come back soon, but in the meantime I use `String.formatted` for variable text parts.

Helpful API Features
--------------------

The Java library for strings, regex, collections, and date/time is excellent and extremely well documented. I much prefer it to the equivalent in Python, JavaScript, or (ugh) Bash.

For example, reading a file into a string is simply:

var content = Files.readString(Path.of(filename));

I use a helper for running an external process:

String run(String... cmd) throws Exception {
    var process = new ProcessBuilder(cmd).redirectErrorStream(true).start();
    process.waitFor();
    return new String(process.getInputStream().readAllBytes());
}

Note, by the way, that since [JEP 400](https://openjdk.org/jeps/400), I can rely on UTF-8 as the default encoding.

For HTTP, there is the `HTTPClient` ([JEP 321](https://openjdk.org/jeps/321)) and the simple web server ([JEP 408](https://openjdk.org/jeps/408)).

The XML support is serviceable. The API is antiquated and cumbersome, but at least it works predictably. In Python, you get a multitude of choices, each partially broken in its own way.

There are two things that are sorely missing in the standard library: JSON and command-line processing. For a large Java program, this isn't a big issue. Just add your favorite library, such as Jackson or PicoCLI, to the POM. But it is a roadblock when writing scripts. You don't want to manually get all of the dependencies of Jackson downloaded, and then added to the class path.

One trick is to use really simple libraries that fit into a single file. I've used [Essential JSON](https://github.com/arkanovicz/essential-json) and [JArgs](https://github.com/purcell/jargs). Just toss the file into the same directory as your script.

Checked Exceptions
------------------

Depending on your circumstances, it may well be acceptable if the script terminates with a stack trace when something went wrong. But of course, you still need to declare or catch checked exceptions. In a large program, this makes sense, but it can feel like a burden in a script.

The simplest remedy is to add `throws Exception` to each method that may throw a checked exception, including `main`.

As an aside, this could be another “ceremony reduction” for beginning students. Why not do that automatically in methods of implicit classes? But I don't make the rules.

There is still a problem with checked exceptions in lambda expressions. Scripts do a lot of file handling, and sometimes the API provides streams of file paths. So you want to go on with something like

streamOfPaths.map(Files::readString)

But you can't since the `readString` method may throw an `IOException`.

The correct remedy is, of course, to handle the exception in some way. Return an empty string. Log the exception. Turn it into an `UncheckedIOException`. Only you can make the appropriate decision.

But in a script, you may not care, and just want the program to terminate. There are a number of “sneaky throw” libraries, such as [Sneaky Fun](https://github.com/ciechanowiec/sneakyfun/) to address this problem. They take advantage of a hole in the Java type system. Through a clever use of generics, one can turn a method with `throws` specifiers into one that doesn't have any. The details are, well, sneaky, but you don't need to know them to use the feature. Simply write:

streamOfPaths.map(sneaky(Files::readString))

I am pretty sure this will never be a part of the JDK, because it is arguably bad for large and serious programs. But in a quick and dirty script, why not? Just remember to take it out if your script scales to the point where it no longer quick and dirty.

IDEs and File Organization
--------------------------

You don't want to write a script with a barebones text editor. The whole point of using Java is that it is a statically typed language where the IDE can help you out with code completion and instant display of programming errors.

I usually start with a middle-weight editor such as Visual Studio Code or Emacs with LSP mode. That gives me Java integration, but without the need to set up a separate project for every script. Just open the Java file and start editing.

As I already mentioned, I find it demotivating to start a new `src/main/java` directory structure whenever an idea for a script occurs to me. So, I get going with my favorite editor. Eventually the script grows to the point where I no longer want to debug with print statements. You can debug a Java program inside VS Code, but I don't find it particularly convenient. At that point, I would like the comfort of an actual IDE. But without `src/main/java`.

It is actually possible to coax your heavy-weight IDE into using the project base directory as the source directory. If you “seed” your project base directory with a Java file, and then create a project from existing sources in your IDE, it should recognize your intent automatically. With an existing project, edit the project setup. In Eclipse, right-click on the project name, select Properties and Java Build Path, then the Source tab. In IntelliJ, go to Menu → Project structure... → Modules, remove the “content root”, and add the project base directory as a new “content root” that is marked as “Sources”. It sounds weird but it works.

JBang
-----

The biggest pain point with Java scripting is the use of third party libraries. Why is it that the single-file `java` launcher can't import stuff from Maven? Well, for starters, Java has no idea that Maven exists. There is nothing in the Java language standard that says anything about the Maven ecosystem. This is where Java shows its age. More modern programming languages have a unified mechanism for third party libraries. But I don't think that this is something that Oracle can or wants to fix. So, you need some tooling to integrate with the Maven ecosystem, and it won't be a part of the JDK.

As a quick remedy (adapted from [this hack](https://advancedweb.hu/using-external-libraries-in-jshell/)), I sometimes make a trivial Gradle script with Maven coordinates to get the files fetched, and to print a class path. But that's only when I am not allowed to use JBang. (See [this JavaAdvent article](https://www.javaadvent.com/2021/12/jbang-gift-that-keeps-on-giving.html) for an introduction to JBang.)

The killer feature of JBang is that you can add Maven dependencies right into the source file:

//DEPS org.eclipse.angus:jakarta.mail:2.0.3

Then you can run

jbang MailMerge.java

In Linux and Mac OS, you can also turn the file into an executable script with a “shebang” line:

///usr/bin/env jbang "$0" "$@" ; exit $?

Note that the `//` hide the shebang from Java, and the `exit $?` masks the rest of the Java file from the shell. (Three slashes are used for an [arcane Posix compliance reason](https://pubs.opengroup.org/onlinepubs/000095399/basedefs/xbd_chap04.html#tag_04_11).)

The rest of JBang is just gravy. You can launch JShell with your file and its dependencies loaded. You can launch an IDE with symlinks to your source inside a temporary `src/main/java`. There are many more thoughtful features, but not too many. If you are serious about scripting in Java, and are able to use third-party tools, get JBang.

Notebooks
---------

So far I focused on scripts—short programs that one runs regularly. Another aspect of programming in the small is exploratory programming: writing code once or a few times, to get some result out of a data set. Data scientists favor _notebooks_ for this work. A notebook consists of code and text cells. The result of each code cell is displayed as text, a table, an image, or even as an audio or video clip. The code cells invite a trial-and-error approach. Once the desired result is obtained, the computation can be annotated with the text cells.

Why is this better than JShell? It is much easier to tinker with the cells than with lines of code in JShell. You can see tabular data and graphs. It is easy to save and share notebooks.

The most common notebook in Python is called “Jupyter”. You can run it locally, usually with a web interface, or it can be hosted. A popular hosted service is Google Colab.

Actually, the core Jupyter technology is language independent. One can install different _kernels_ for various programming languages. The kernel installation process can be fussy, but [this JavaAdvent article](https://www.javaadvent.com/2023/12/jupyter-notebooks-and-java.html) describes Jupyter Java Anywhere, a simple mechanism (using JBang) for installing a Java kernel.

Confusingly, there are a number of different Java kernels (including [IJava](https://github.com/SpencerPark/IJava), [JJava](https://github.com/dflib/jjava), [Ganymede](https://github.com/allen-ball/ganymede), and [Rapaio](https://github.com/padreati/rapaio-jupyter-kernel)). Each kernel has its own way for installing Maven dependencies, displaying non-text results, and so on. Juypter Java Anywhere installs the classic IJava kernel, which has some open issues around dependency resolution. It really would be desirable for Oracle or another major vendor to step up, curate a kernel, and even—dare we hope—provide a Colab-like Java notebook service. Something more useful than the [Java playground.](https://dev.java/playground/)

Python notebook coders are blessed with a couple of libraries for number crunching, in particular NumPy and Matplotlib. I have not found either of them to be God's gift in terms of API design, but they are ubiquitous, and therefore StackOverflow and your favorite chatbot will offer suggestions, many of them useful, for tweaking computations and graphs.

Exploratory coding in Java is not (yet) common, and there isn't a deep bench of support libraries. I think [tablesaw](https://github.com/jtablesaw/tablesaw) could be a reasonable NumPy equivalent. It has a wrapper for the well-regarded Plot.ly JavaScript drawing package.

Sven Reimers is developing the [JTaccuino](https://github.com/svenreimers/jtaccuino) notebook to offer a better experience. This is a JavaFX implementation with a friendlier user interface than the web-based Jupyter notebook. It uses JShell under the hood. The project is still in its early stages but worth watching.

![Image 10: .png](https://horstmann.com/unblog/2024-12-11/jtaccuino.png)

For Kotlin, there is the [Kotlin Notebook](https://kotlinlang.org/docs/kotlin-notebook-overview.html) IntelliJ plugin.

While Java notebooks may not be ready for prime time, there is hope for the future.

Conclusion
----------

With the right tooling, Java is a surprisingly effective choice for small programs. For simple scripts that use only the Java API, you can simply launch a Java source file. JBang makes it very easy to launch programs with third-party libraries. You benefit from compile-time typing and an upgrade path for when your programs get more complex, as they often do.

For the same reasons, Java can become an attractive choice for exploratory programming, but the tooling is not yet where it could be.

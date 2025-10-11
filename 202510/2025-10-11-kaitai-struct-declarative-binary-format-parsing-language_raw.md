Title: declarative binary format parsing language

URL Source: https://kaitai.io/

Markdown Content:
![Image 1: [Kaitai logo]](https://kaitai.io/img/kaitai_16x_dark.png)

Kaitai Struct
-------------

A new way to develop parsers for binary structures.

Reading and writing binary formats is hard, especially if it’s an interchange format that should work across a multitude of platforms and languages.

Have you ever found yourself writing repetitive, error-prone and hard-to-debug code that reads binary data structures from files or network streams and somehow represents them in memory for easier access?

Kaitai Struct tries to make this job easier — you only have to describe the binary format once and then everybody can use it from their programming languages — cross-language, cross-platform.

What is Kaitai Struct?
----------------------

Kaitai Struct is a declarative language used to describe various binary data structures, laid out in files or in memory: i.e. binary file formats, network stream packet formats, etc.

The main idea is that a particular format is described in Kaitai Struct language (`.ksy` file) and then can be compiled with `ksc` into source files in one of the supported programming languages. These modules will include a generated code for a parser that can read the described data structure from a file or stream and give access to it in a nice, easy-to-comprehend API.

Using KS in your project
------------------------

Typically, using formats described in KS in your project involves the following steps:

*   Describe the format — i.e. create a `.ksy` file
*   Use a visualizer to debug the format and ensure that it parses data properly
*   Compile the `.ksy` file into a target language source file and include that file into your project 
*   Add the KS runtime library for your particular language into your project (don’t worry, it’s small and it’s there mostly to ensure readability of generated code) 
*   Use the generated class(es) to parse your binary file or stream and access its components 

Check out the [documentation](https://doc.kaitai.io/) for more information.

```
meta:
  id: tcp_segment
  endian: be
seq:
  - id: src_port
    type: u2
  - id: dst_port
    type: u2
  - id: seq_num
    type: u4
  - id: ack_num
    type: u4
```

```
public class TcpSegment extends KaitaiStruct {
    // ...
    private void _read() throws IOException {
        this.srcPort = _io.readU2be();
        this.dstPort = _io.readU2be();
        this.seqNum = _io.readU4be();
        this.ackNum = _io.readU4be();
    }
    // ...
```

Quick start
-----------

Consider this simple `.ksy` format description file that describes the header of a GIF image file:

```
meta:
  id: gif
  file-extension: gif
  endian: le
seq:
  - id: header
    type: header
  - id: logical_screen
    type: logical_screen
types:
  header:
    seq:
      - id: magic
        contents: 'GIF'
      - id: version
        size: 3
  logical_screen:
    seq:
      - id: image_width
        type: u2
      - id: image_height
        type: u2
      - id: flags
        type: u1
      - id: bg_color_index
        type: u1
      - id: pixel_aspect_ratio
        type: u1
```

It declares that a GIF file usually has a `.gif` extension and uses little-endian integer encoding. The file itself starts with two blocks: first comes `header` and then comes `logical_screen`:

*   “Header” consists of a “magic” string of 3 bytes (“GIF”) that identifies that it’s a GIF file starting and then there are 3 more bytes that identify the format version (`87a` or `89a`). 
*    “Logical screen descriptor” is a block of integers: 
    *   `image_width` and `image_height` are 2-byte unsigned ints
    *   `flags`, `bg_color_index` and `pixel_aspect_ratio` take 1-byte unsigned ints each 

This `.ksy` file can be compiled into `gif.cpp` / `Gif.cs` / `gif.go` / `Gif.java` / `Gif.js` / `gif.lua` / `gif.nim` / `Gif.pm` / `Gif.php` / `gif.py` / `gif.rb` and then one can instantly load a .gif file and access, for example, its width and height.

*   [C++/STL](https://kaitai.io/#example-cpp-stl)
*   [C#](https://kaitai.io/#example-csharp)
*   [Go](https://kaitai.io/#example-go)
*   [Java](https://kaitai.io/#example-java)
*   [JavaScript](https://kaitai.io/#example-javascript)
*   [Lua](https://kaitai.io/#example-lua)
*   [Nim](https://kaitai.io/#example-nim)
*   [Perl](https://kaitai.io/#example-perl)
*   [PHP](https://kaitai.io/#example-php)
*   [Python](https://kaitai.io/#example-python)
*   [Ruby](https://kaitai.io/#example-ruby)
*   [Rust](https://kaitai.io/#example-rust)

```
std::ifstream ifs("path/to/some.gif", std::ifstream::binary);
kaitai::kstream ks(&ifs);
gif_t g = gif_t(&ks);

std::cout << "width = " << g.logical_screen()->image_width() << std::endl;
std::cout << "height = " << g.logical_screen()->image_height() << std::endl;
```

```
Gif g = Gif.FromFile("path/to/some.gif");

Console.WriteLine("width = " + g.LogicalScreen.ImageWidth);
Console.WriteLine("height = " + g.LogicalScreen.ImageHeight);
```

```
file, err := os.Open("path/to/some.gif")
g := NewGif()
err = g.Read(kaitai.NewStream(file), nil, g)

fmt.Printf("width = %d\n", g.LogicalScreen.ImageWidth)
fmt.Printf("height = %d\n", g.LogicalScreen.ImageHeight)
```

```
Gif g = Gif.fromFile("path/to/some.gif");

System.out.println("width = " + g.logicalScreen().imageWidth());
System.out.println("height = " + g.logicalScreen().imageHeight());
```

```
var g = new Gif(new KaitaiStream(someArrayBuffer));

console.log("width = " + g.logicalScreen.imageWidth);
console.log("height = " + g.logicalScreen.imageHeight);
```

```
local g = Gif:from_file("path/to/some.gif")

print("width = " .. g.logical_screen.image_width)
print("height = " .. g.logical_screen.image_height)
```

```
let g = Gif.fromFile("path/to/some.gif")

echo "width = " & $g.logicalScreen.imageWidth
echo "height = " & $g.logicalScreen.imageHeight
```

```
my $g = Gif->from_file("path/to/some.gif");

print("width = ", $g->logical_screen()->image_width(), "\n");
print("height = ", $g->logical_screen()->image_height(), "\n");
```

```
$g = Gif::fromFile("path/to/some.gif");

print("width = " . $g->logicalScreen()->imageWidth() . "\n");
print("height = " . $g->logicalScreen()->imageHeight() . "\n");
```

```
g = Gif.from_file("path/to/some.gif")

print("width = %d" % (g.logical_screen.image_width))
print("height = %d" % (g.logical_screen.image_height))
```

```
g = Gif.from_file("path/to/some.gif")

puts "width = #{g.logical_screen.image_width}"
puts "height = #{g.logical_screen.image_height}"
```

```
let bytes = fs::read("path/to/some.gif").unwrap();
let io = BytesReader::from(bytes);
let g: OptRc<Gif> = Gif::read_into(&io, None, None).unwrap();

println!("width = {}", *g.logical_screen().image_width());
println!("height = {}", *g.logical_screen().image_height());
```

Of course, this example shows only a very limited subset of what Kaitai Struct can do. Please refer to the [documentation](https://doc.kaitai.io/) for more insights.

Downloading and installing
--------------------------

#### 2021-05-02 — Temporarily using GitHub Releases for compiler distributions

As of May 2, 2021, JFrog Bintray (distribution service where we hosted the compiler artifacts for years) [has been sunset](https://jfrog.com/blog/into-the-sunset-bintray-jcenter-gocenter-and-chartcenter/), so we moved all stable compiler versions to GitHub Releases [in the kaitai_struct_compiler repository](https://github.com/kaitai-io/kaitai_struct_compiler/releases). The installation commands below have been updated accordingly. Development (unstable) builds that were hosted on Bintray (Linux .deb and Universal .zip) are not available right now (until we set up the new distribution system).

We're currently setting up an alternative repository to replace Bintray, which will be available on a custom domain `packages.kaitai.io` to be future-proof, so stay tuned!

*   [Linux .deb](https://kaitai.io/#download-linux-deb)
*   [macOS - Homebrew](https://kaitai.io/#download-mac-homebrew)
*   [Windows](https://kaitai.io/#download-windows)
*   [Universal .zip](https://kaitai.io/#download-universal)
*   [Source](https://kaitai.io/#download-source)

The stable `kaitai-struct-compiler` versions are currently uploaded to [https://github.com/kaitai-io/kaitai_struct_compiler/releases](https://github.com/kaitai-io/kaitai_struct_compiler/releases) (see [box above](https://kaitai.io/#bintray-sunset-callout)). Just download the `.deb` package and install it:

curl -fsSLO https://github.com/kaitai-io/kaitai_struct_compiler/releases/download/0.11/kaitai-struct-compiler_0.11_all.deb
sudo apt-get install ./kaitai-struct-compiler_0.11_all.deb

#### Requirements

*   .deb-based Linux distribution (Debian, Ubuntu, etc)

There is a [Homebrew formula](https://formulae.brew.sh/formula/kaitai-struct-compiler) that you can use to install `kaitai-struct-compiler`:

brew install kaitai-struct-compiler

Windows versions are available as an MSI format installer. If you want a portable version that requires no installation, download our universal .zip build instead.

[Download](https://github.com/kaitai-io/kaitai_struct_compiler/releases/download/0.11/kaitai-struct-compiler-0.11.msi) — stable v0.11, 8.5 MiB

[Download](https://ci.appveyor.com/project/kaitai-io/kaitai-struct/build/artifacts) — latest development (unstable) build

#### Requirements

*   Windows
*   [Java](https://whichjdk.com/) (the latest LTS version 21 recommended, at least Java 8 required), [JDK or JRE](https://whichjdk.com/#what-is-the-difference-between-jdk-and-jre) at your option

"Universal" builds are downloadable as a .zip file that includes all the required .jar files bundled and launcher scripts for Linux / macOS / Windows systems. No installation required, one can just unpack and run it.

[Download](https://github.com/kaitai-io/kaitai_struct_compiler/releases/download/0.11/kaitai-struct-compiler-0.11.zip) — stable v0.11, 8.2 MiB

[Download](https://kaitai.io/#0) — ~~latest development (unstable) build~~ — currently not available (see [box above](https://kaitai.io/#bintray-sunset-callout))

#### Requirements

*   Linux / macOS / Windows system
*   [Java](https://whichjdk.com/) (the latest LTS version 21 recommended, at least Java 8 required), [JDK or JRE](https://whichjdk.com/#what-is-the-difference-between-jdk-and-jre) at your option

If you prefer to build your tools from source, or just want to see how KS works, the easiest way to check out the whole project is to download the [main (umbrella) repository](https://github.com/kaitai-io/kaitai_struct) that already includes all other parts as submodules. Use:

git clone **--recurse-submodules** https://github.com/kaitai-io/kaitai_struct.git

If you already cloned the project and forgot `--recurse-submodules`, run

git submodule update --init --recursive

Alternatively, one can check out individual sub-projects that consitute the Kaitai Struct suite. See the [GitHub project page](https://github.com/kaitai-io/kaitai_struct) for details.

#### Requirements

*   [git](https://git-scm.com/)
*   [Java](https://whichjdk.com/) (the latest LTS version 21 recommended, at least Java 8 required), [JDK or JRE](https://whichjdk.com/#what-is-the-difference-between-jdk-and-jre) at your option
*   [sbt](http://www.scala-sbt.org/)
*   POSIX shell for test automation

Licensing
---------

Kaitai Struct is free and open-source software, licensed under the following terms:

*   [Compiler](https://github.com/kaitai-io/kaitai_struct_compiler) and [visualizer](https://github.com/kaitai-io/kaitai_struct_visualizer) — GPLv3+
*    Runtime libraries: 
    *   [C++/STL](https://github.com/kaitai-io/kaitai_struct_cpp_stl_runtime) — MIT
    *   [C#](https://github.com/kaitai-io/kaitai_struct_csharp_runtime) — MIT
    *   [Go](https://github.com/kaitai-io/kaitai_struct_go_runtime) — MIT
    *   [Java](https://github.com/kaitai-io/kaitai_struct_java_runtime) — MIT
    *   [JavaScript](https://github.com/kaitai-io/kaitai_struct_javascript_runtime) — Apache v2
    *   [Lua](https://github.com/kaitai-io/kaitai_struct_lua_runtime) — MIT
    *   [Nim](https://github.com/kaitai-io/kaitai_struct_nim_runtime) — MIT
    *   [Perl](https://github.com/kaitai-io/kaitai_struct_perl_runtime) — MIT
    *   [PHP](https://github.com/kaitai-io/kaitai_struct_php_runtime) — MIT
    *   [Python](https://github.com/kaitai-io/kaitai_struct_python_runtime) — MIT
    *   [Ruby](https://github.com/kaitai-io/kaitai_struct_ruby_runtime) — MIT
    *   [Rust](https://github.com/kaitai-io/kaitai_struct_rust_runtime) — MIT
    *   [Swift](https://github.com/kaitai-io/kaitai_struct_swift_runtime) — MIT

work in progress

Built with Kaitai Struct
------------------------

We maintain a growing [free / open source repository](https://github.com/kaitai-io/kaitai_struct_formats) of file formats and protocol specifications. Visit our format gallery to view the showcase of that repository with documentation, block diagrams and ready-made parser libraries in all supported target languages.

[Format Gallery >>](https://formats.kaitai.io/)

Kaitai Struct is used in the following open source projects:

*   [Veles](https://codisec.com/veles/) — binary data visualization and analysis tool
*   [mitmproxy](https://mitmproxy.org/) — an interactive man-in-the-middle traffic inspection and modification tool
*   [Kismet](https://www.kismetwireless.net/) — wireless network detector, sniffer, and intrusion detection system
*   [Beat Link Trigger](https://github.com/Deep-Symmetry/beat-link-trigger) — music performer app to trigger events based on Pioneer CDJs output
*   [Hobbits](https://github.com/Mahlet-Inc/hobbits) — multi-platform GUI for bit-based analysis, processing, and visualization
*   [OWASP ZAP](https://www.zaproxy.org/) — the world's most widely used web app scanner

If your project also uses Kaitai Struct, please drop us a line :)
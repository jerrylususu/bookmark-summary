Title: Filesystem Backed by an LLM

URL Source: https://healeycodes.com/filesystem-backed-by-an-llm

Published Time: Tue, 08 Jul 2025 01:03:52 GMT

Markdown Content:
I came across [a post](https://x.com/simonw/status/1941190140380201431) discussing the [gremllm](https://github.com/awwaiid/gremllm) Python library that hallucinates and then evaluates method implementations as you call them.

I thought this was pretty cool and it reminded me of experiments people tried shortly after GPT-3's launch, where they prompted to hallucinate a Linux system that they could interact with via terminal commands sent in the chat UI. The earliest article I could find on this is [Building A Virtual Machine Inside ChatGPT](https://www.engraved.blog/building-a-virtual-machine-inside/).

I had an idea for a middle ground — not just a hallucinating library, nor an entirely hallucinated system. What if _parts_ of the OS were backed by an LLM?

My idea is a FUSE-based filesystem where every file operation is handled by an LLM. In [llmfs](https://github.com/healeycodes/llmfs), content is generated on the fly by calling out to OpenAI's API.

In the video above, you can see me interacting with this mounted FUSE filesystem. The latency is expected as everything must be run past the LLM.

$ cat generate_20_bytes_of_binary_data.py | python3

b'\x94\xc2(\xbd\x17<|\xd7\x01*\x01\xdeWvM\xaa\x8fX\xfa\xb1'

The resulting data is not stored on disk. It's stored in an in-memory history log of actions.

This means the LLM can remember which data exists at which path.

$ echo "andrew" > my_name.txt

$ cat my_name.txt

andrew

As the LLM handles all file operations, it's free to deny certain actions. The system prompt allows the LLM to deny file operations with UNIX error codes.

For failed operations (only use for actual errors), respond with:

{"error": 13} (where 13 = EACCES for "Permission denied")

Examples:

- Writing passwd: {"error": 13} (system files)

- Writing malicious_script.sh: {"error": 13} (dangerous content)

These error codes are bubbled up through the filesystem.

$ cat secrets.txt

cat: secrets.txt: Permission denied

### Interacting With FUSE

After mounting the filesystem with the Go library [bazil.org/fuse](http://basil.org/fuse), the kernel intercepts Virtual File System (VFS) calls like open/read/write and forwards them through `/dev/fuse` to the userspace daemon.

import "bazil.org/fuse"

mnt := os.Args[1]

c, err := fuse.Mount(

mnt,

fuse.FSName("llmfs"),

fuse.Subtype("llmfs"),

fuse.AllowOther(),

)

The library reads from `/dev/fuse`, services each request, and writes the reply back to the same device.

My Go code, which implements interfaces like `fs.Node`, handles the file operations and provides file contents, metadata, and error codes.

func (h *fileHandle) Write(

_ context.Context, req *fuse.WriteRequest, resp *fuse.WriteResponse,

) error {

appendHistory("user",

fmt.Sprintf("Write %s offset %d data %q", h.name, req.Offset, string(req.Data)))

prompt := buildPrompt()

rc := StreamLLM(prompt)

llmResp, err := ParseLLMResponse(rc)

_ = rc.Close()

if err != nil {

return fuse.Errno(syscall.EIO)

}

if ferr := FuseError(llmResp); ferr != nil {

return fuse.Errno(ferr.(syscall.Errno))

}

appendHistory("assistant", "ok")

resp.Size = len(req.Data)

return nil

}

These responses are written back to `/dev/fuse`, and the kernel then continues processing the syscall from the original process.

Given there are delays of _hundreds_ of milliseconds for each operation, I'm not too worried about performance. Instead of per-inode locks I simply serialise everything behind `llmMu`.

var llmMu sync.Mutex // global – one request at a time

type lockedReader struct {

io.Reader

once sync.Once

}

func (lr *lockedReader) Close() error {

lr.once.Do(llmMu.Unlock)

return nil

}

LLM Context
-----------

File system operations append actions to the history log.

user: Read nums.txt

assistant: Data nums.txt content "123456\n"

A new prompt is generated for each file operation. It starts with the system prompt, which begins with the following:

system: You are a filesystem that generates file content on demand.

IMPORTANT: You must respond with EXACTLY ONE valid JSON object. No other text.

When a file is requested:

- If it's a new file, create content based on the filename, extension, and context

- If it's an existing file, return the content of the file

After this, the entire history log is appended. So, if the user has sent two different writes to a file, the LLM will be able to understand these actions, and generate the correct file, even though the complete file is not explicitly stored.

user: Write nums.txt offset 0 data "123\n"

assistant: ok

user: Write nums.txt offset 4 data "456\n"

assistant: ok

user: Read nums.txt

assistant: Data nums.txt content "123456\n"

File errors also need to be stored so that they are consistently handled.

user: Read private

assistant: error 13

JSON Schema
-----------

My interactions with the LLM are simple enough that I didn't reach for any special tools and just rolled my own JSON parsing. This seemed to work well with various GPT-4 models.

// LLMResponse should match the JSON schema:

//

// { "data": "<utf-8 text>" }

// { "error": <errno> }

//

// Exactly one of Data or Error is non-nil

type LLMResponse struct {

Data *string `json:"data,omitempty"`

Error *int `json:"error,omitempty"`

}

Let's take file creation for example. First we append the user action like `Create nums.txt` to the history, and then we make the LLM call.

func (rootDir) Create(

_ context.Context, req *fuse.CreateRequest, resp *fuse.CreateResponse,

) (fs.Node, fs.Handle, error) {

appendHistory("user", fmt.Sprintf("Create %s", req.Name))

prompt := buildPrompt()

rc := StreamLLM(prompt)

llmResp, err := ParseLLMResponse(rc) // (LLMResponse, error)

// ..

We block on the call and the parsing of the response. The prompt steers the LLM towards JSON by requesting it directly as well as providing examples.

The schema is quite loose in that I re-use the `data` field to report that operations like creating files are successful, as seen in the examples that are part of the system prompt:

When writing to a file:

- Accept the write operation and acknowledge it was successful

- Only reject writes that are clearly malicious or dangerous

- For successful writes, respond with: {"data": "ok\n"}

For successful operations, respond with:

{"data": "content of the file\n"} (for reads)

{"data": "ok\n"} (for writes)

For failed operations (only use for actual errors), respond with:

{"error": 13} (where 13 = EACCES for "Permission denied")

Examples:

- Reading hello_world.txt: {"data": "Hello, World!\n"}

- Reading config.json: {"data": "{\"version\": \"1.0\", \"magic\": true}\n"}

- Reading print_hello.py: {"data": "print('Hello, World!')\n"}

- Writing some_file.txt: {"data": "ok\n"}

- Writing passwd: {"error": 13} (system files)

- Writing malicious_script.sh: {"error": 13} (dangerous content)

Example error codes:

- 5 (EIO): I/O error

- 13 (EACCES): Permission denied

Writing at offsets is supported:

- user: Write nums.txt offset 0 data "123\n"

- assistant: ok

- user: Write nums.txt offset 5 data "456\n"

- assistant: ok

One issue that I thought I'd run into, was data encoding. When I was running some tests to generate script files, I thought that the LLM would reply with invalid JSON when there were unescaped characters in the response like `{"data": "\"}` which would then bubble up into a file error.

However, GPT-4 models understand the context (we're generating JSON) and escape it automatically by returning things like `{"data": "\\"}`.

cat a_single_backslash.txt

\

# history log:

# user: Read a_single_backslash.txt

# assistant: Data a_single_backslash.txt content "\\"

# raw response:

# {"data": "\\"}

A more robust solution might look like: returning a single character to indicate the type of response, followed by pure data.

What's Next
-----------

I'm pretty happy with this demo. I set out to intercept and handle file operations with an LLM and it works better than I expected.

To extend support for _all_ file operations, like a good filesystem, I think I'll need to rethink my schema design. In fact, I'd like to throw it all away and remove this mapping layer altogether.

In order to support more features, I'm wondering if I can de-/serialize entire [bazil.org/fuse](http://bazil.org/fuse) library objects so everything works out of the box. My gut says this could work with the latest LLM models with a good setup.

Let me know if you have other ideas! The demo repo is [https://github.com/healeycodes/llmfs](https://github.com/healeycodes/llmfs).

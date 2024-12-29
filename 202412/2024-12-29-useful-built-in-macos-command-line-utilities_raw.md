Title: Useful built-in macOS command-line utilities

URL Source: https://weiyen.net/articles/useful-macos-cmd-line-utilities/

Markdown Content:
Sometimes when I'm bored, I like to look at the list of [macOS Bash commands](https://ss64.com/mac/). Here's some commands that I found interesting:

Access your Keychain programmatically[](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#access-your-keychain-programmatically)
-------------------------------------------------------------------------------------------------------------------------------------------

If you store your secrets in the Keychain (and you should!), you can access them programmatically using `security`.

```
security find-internet-password -s "https://example.com"
```

I found this useful for writing automated scripts that used locally-stored credentials.

Link: [https://ss64.com/mac/security.html](https://ss64.com/mac/security.html)

Bonus tip: If you are using 1Password, there is a [1Password CLI](https://developer.1password.com/docs/cli/get-started/) that you can use to access your 1Password items from the command line.

Open files from the terminal[](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#open-files-from-the-terminal)
-------------------------------------------------------------------------------------------------------------------------

If you want to open a file from the terminal, you can use the `open` command.

```
open file.txt
```

This will open the file in the default application for that file type, as if you had double-clicked it in the Finder.

Link: [https://ss64.com/mac/open.html](https://ss64.com/mac/open.html)

Copy and paste[](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#copy-and-paste)
---------------------------------------------------------------------------------------------

`pbcopy` and `pbpaste` are command-line utilities that allow you to copy and paste text to the pasteboard (what other operating systems might call the "clipboard").

`pbcopy` takes whatever was given in the standard input, and places it in the pasteboard.

```
echo "Hello, world!" | pbcopy;
```

`pbpaste` takes whatever is in the pasteboard and prints it to the standard output.

```
pbpaste
>> Hello, world!
```

This is very useful for getting data from files into the browser, or other GUI applications.

#### Links:[](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#links)

*   [https://ss64.com/mac/pbcopy.html](https://ss64.com/mac/pbcopy.html)
*   [https://ss64.com/mac/pbpaste.html](https://ss64.com/mac/pbpaste.html)

UTC date[](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#utc-date)
---------------------------------------------------------------------------------

If you work with servers a lot, it can be useful to know the current time in UTC, when e.g. looking at server logs.

This is a one-liner in the terminal:

```
date -u
```

Alternatively, you can use

```
TZ=UTC date
```

Link: [https://ss64.com/mac/date.html](https://ss64.com/mac/date.html)

Internet speedtest[](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#internet-speedtest)
-----------------------------------------------------------------------------------------------------

If you want to run an Internet speedtest, you can run one directly from the terminal with

```
networkQuality  # Note the capital "Q"!
```

Link: [https://ss64.com/mac/networkquality.html](https://ss64.com/mac/networkquality.html)

Prevent your Mac from sleeping[](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#prevent-your-mac-from-sleeping)
-----------------------------------------------------------------------------------------------------------------------------

If you want to keep your Mac from sleeping, you can run `caffeinate` in the terminal.

```
caffeinate
```

`caffeinate` will keep your Mac awake until you stop it, e.g. by pressing Ctrl+C. `caffeinate` used to be a third-party tool, but it is now built-in to macOS.

I use this mostly to prevent my Mac from sleeping when I am running a server.

Link: [https://ss64.com/mac/caffeinate.html](https://ss64.com/mac/caffeinate.html)

Generate UUIDs[](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#generate-uuids)
---------------------------------------------------------------------------------------------

If you need to generate a UUID, you can use the `uuidgen` command.

```
uuidgen
```

By default `uuidgen` outputs a UUID in uppercase. You can combine this with `tr` and `pbcopy` to copy the UUID to the clipboard in lowercase.

```
uuidgen | tr '[:upper:]' '[:lower:]' | pbcopy
```

I use this a lot when writing unit tests that require IDs.

Link: [https://ss64.com/mac/uuidgen.html](https://ss64.com/mac/uuidgen.html)

Honourable mentions[](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#honourable-mentions)
-------------------------------------------------------------------------------------------------------

*   `mdfind`: Spotlight search, but in the terminal. I generally use Spotlight itself (or rather the excellent [Raycast](https://www.raycast.com/)). [Link](https://ss64.com/mac/mdfind.html)
*   `say`: This command makes your Mac speak the text you give it. [Link](https://ss64.com/mac/say.html)
*   `screencapture`: This command allows you to take screenshots and save them to a file. I prefer using `cmd-shift-5` for this. [Link](https://ss64.com/mac/screencapture.html)
*   `networksetup`: This command allows you to configure your network settings programmatically. I found its API very intimidating, and so I haven't really used it much. [Link](https://ss64.com/mac/networksetup.html)

* * *

Update \[9 Nov 2024\][](https://weiyen.net/articles/useful-macos-cmd-line-utilities/#update-9-nov-2024)
-------------------------------------------------------------------------------------------------------

After posting this article on [Hacker News](https://news.ycombinator.com/item?id=42057431) and making it to #2 on the front page(!), the folks over there suggested many _many_ more interesting utilities.

Here are some of my favourites:

*   `sips`: The Scriptable Image Processing System, for converting between various image formats. [Link](https://ss64.com/mac/sips.html)
*   `afinfo`: To probe metadata of audio files. [Link](https://ss64.com/mac/afinfo.html)
*   `mdls`: To probe metadata of all kinds of files. [Link](https://ss64.com/mac/mdls.html)
*   `afconvert`: For converting between various audio formats. [Link](https://ss64.com/mac/afconvert.html)
*   `diskutil`: For managing disk volumes, and a solid alternative to the built-in"Disk Utility" app. [Link](https://ss64.com/mac/diskutil.html)
*   `powermetrics`: For monitoring system power consumption. [Link](https://ss64.com/mac/powermetrics.html)
*   `pmset`: For power management tasks, e.g. to automatically turn your Mac on or off. [Link](https://ss64.com/mac/pmset.html)
*   `dot_clean`: Removes dot\_underscore files. Useful when sharing files with non-Mac machines. [Link](https://ss64.com/mac/dot_clean.html)

(Apologies if I missed your suggestion, there were just so many!)

There are also a couple of other people who made similar lists that are worth checking out, e.g.

*   [https://saurabhs.org/advanced-macos-commands](https://saurabhs.org/advanced-macos-commands)
*   [https://notes.billmill.org/computer\_usage/mac\_os/mac\_os\_command\_line\_programs.html](https://notes.billmill.org/computer_usage/mac_os/mac_os_command_line_programs.html)

_Like this article? Follow me on [Bluesky](https://bsky.app/profile/weiyen.net) or subscribe to the [RSS feed](https://weiyen.net/feed/all) to get notified about new articles._

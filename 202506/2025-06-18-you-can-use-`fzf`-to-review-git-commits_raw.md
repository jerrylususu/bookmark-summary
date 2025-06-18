Title: You can use `fzf` to review git commits

URL Source: https://jvns.ca/til/fzf-preview-git-commits/

Markdown Content:
[Julia Evans](https://jvns.ca/)
-------------------------------

[« back to all TILs](https://jvns.ca/til/)

### [You can use `fzf` to review git commits](https://jvns.ca/til/fzf-preview-git-commits/)Jun 17 2025

`fzf` is a tool that you can use to select items from a list. I think it’s most popularly used to search your shell history (as a `Ctrl+R` replacement in bash).

I’ve honestly still never found a use for `fzf` myself (other than [fzf.vim](https://github.com/junegunn/fzf.vim) which is amazing) but I just learned that you can use it to review a git commit like this and I thought that was really cool. You can scroll up and down through the files on the left and it’ll display the diff on the right:

```
#!/bin/bash
commit=${1:-HEAD}
git show --stat=120 --format="" "$commit" | \
           grep -E '^\s*\S+.*\|' | \
           fzf --ansi \
               --disabled \
               --bind 'j:down,k:up,q:abort' \
               --preview="echo {} | sed 's/|.*//' | xargs -I% git show --color=always $commit -- %" \
               --preview-window=right:60%
```

![Image 1](https://jvns.ca/images/fzf-git.png)

You can also use `fzf` as a sort of “jq playground” like this:

```
#!/bin/bash

printf '' | fzf --print-query \
  --preview "jq -C {q} '$1' 2>&1" \
  --preview-window=up:80%
```

![Image 2](https://jvns.ca/images/fzf-jq.png)

I think it’s really cool that you can use fzf (which is theoretically a search tool) to implement lots of UIs that aren’t doing search at all, like these two!

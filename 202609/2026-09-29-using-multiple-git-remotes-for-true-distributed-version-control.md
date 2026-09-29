# Using multiple git remotes for true distributed version control
- URL: https://optimizedbyotto.com/post/multiple-git-remotes/
- Added At: 2026-09-29 14:10:00
- Tags: #read #git

## TL;DR
文章主张充分利用 Git 多远程，把代码同时托管到多个平台：为一个远程添加多个推送 URL，一次推送即可镜像到 GitHub、GitLab 等，提升可用性、协作者自由和无痛迁移，但需注意 CI 重复与强制推送风险。

## Summary
Git 本身被设计成一个分布式版本控制系统，天生支持多个远程仓库，但大多数人只配置一个 `origin`，把 Git 用成了集中式系统。这篇文章的核心主张就是：充分利用 Git 的多远程能力，把代码同时托管到多个平台。

**基本操作**

默认克隆后只有一个 `origin`。你可以给它改名，再添加其他远程：

```
git remote rename origin github
git remote add gitlab https://gitlab.com/ottok/debcraft.git
```

这样就有了 `github` 和 `gitlab` 两个远程。可以单独拉取或推送，也可以用 `git pull --all` 一次性从所有远程拉取。推送时用 `git push gitlab dev` 指定目标，或者用 `git push --set-upstream gitlab dev` 设置默认推送目标，之后直接 `git push` 就行。

另外 `remote.pushDefault` 可以为没有单独配置的分支指定默认推送远程。用 `git branch -vv` 查看每个分支关联的远程，用 `git fetch --all --prune` 刷新所有远程的分支引用。

**一个远程配多个推送 URL**

这是作者最推崇的技巧。用 `git remote set-url --add --push` 可以给一个远程添加多个推送 URL，这样一次 `git push` 会依次推送到所有 URL。`git remote -v` 会为每个推送 URL 显示一行。

作者在 Debcraft 项目中的实际配置是：`origin` 从 Salsa 拉取，但推送到 Salsa、GitLab、GitHub 三个地方；`otto` 这个远程则推送到五个平台（Salsa、GitLab、GitHub、Sourcehut、Codeberg）。分支 `main` 关联 `origin`，分支 `dev` 关联 `otto`。这样在不同分支上工作，拉取来源和推送目标都不同，非常灵活。

**三个使用场景**

一是提高可用性。主站（比如 salsa.debian.org）经常过载或不可用，推送了多个平台后，协作者可以从其他镜像拉取代码。主站恢复后，下次推送会自动补齐。

二是让协作者用自己喜欢的平台。有人没有 Salsa 账号，但可以在 GitLab 或 GitHub 上提交合并请求/PR。

三是代码托管迁移。想逐步弃用 GitHub 时，可以配置成从旧地址拉取、同时推送到新旧两个地方，让还没迁移的人不受影响。

**自动化脚本**

作者写了一个 bash 脚本，把从 Salsa 克隆的仓库自动配置成同时推送到 GitLab 和 GitHub。脚本会解析 Salsa URL，添加推送 URL，然后推送当前分支、所有分支和标签。如果装了 `glab`，还会自动把新建的 GitLab 项目设为公开并加上镜像描述。

**注意事项**

每次推送都会写到所有 URL，所以如果三个平台都配了 CI，CI 会跑三次，成本大约翻三倍。如果某个推送 URL 失败（比如主机暂时不可达），Git 会报错并停止，排在失败项后面的远程不会收到新提交。等主机恢复后重新推送即可，已经收到的会显示 `Everything up-to-date`。另外绝不要只对其中一个远程强制推送，那会让镜像和本地仓库永久不同步。

**避免拉取过多**

默认克隆会跟踪所有分支，对开源项目来说会拉进大量临时开发分支。更好的做法是用 `git clone --single-branch --branch main` 只拉取需要的分支。如果仓库已经克隆了，可以配置 `remote.upstream.fetch` 只跟踪特定分支，需要时再逐个添加。

**总结**

把代码分发到多个代码托管平台，配置成本几乎为零，换来的是可用性、协作者的选择自由，以及无痛迁移的能力。给现有远程加上推送 URL，推一次，就完成了。

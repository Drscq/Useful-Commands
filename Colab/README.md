# Google Colab CLI

Google Colab CLI 是 Google 官方维护的命令行工具，可从本地终端创建 Colab 云端 runtime、执行 Python、管理远端文件。它适用于 macOS 和 Linux；Windows 当前不受支持。本目录记录这台 Apple Silicon Mac 上的本地安装结果、待办事项，以及供 Claude Code、Codex 等终端 agent 参考的操作边界。

本机已安装 `google-colab-cli` 0.7.4，并确认 `colab version` 与 `colab --help` 可运行。首次 Google OAuth 授权和云端 CPU runtime 尚未完成，所以这里没有声称云端执行已验证。

## 最短 CPU 流程

首次使用时先启动 OAuth2 授权。你需要在浏览器中选择 Google 账号并同意授权，再把页面返回的代码粘贴到本地终端。此步骤不会创建 runtime：

```sh
colab --auth=oauth2 sessions
```

授权完成后，下面的示例创建一个具名 CPU 会话、运行一行 Python、查看状态并停止会话：

```sh
colab --auth=oauth2 new -s useful-commands-smoke
printf 'print(1 + 1)\n' | colab --auth=oauth2 exec -s useful-commands-smoke
colab --auth=oauth2 status -s useful-commands-smoke
colab --auth=oauth2 stop -s useful-commands-smoke
```

会话会占用 Colab 计算资源；任务结束后务必停止。使用 `colab run` 执行一次性脚本时，不带 `--keep` 会在运行后自动释放 runtime。GPU、TPU、高内存和会话时限受账号资格、额度与当时资源供应影响；免费且无正计算额度的托管 runtime 不允许 SSH shell 等远程控制用途。详见 [agent-usage.md](./agent-usage.md)。

## 本目录

- [installation.md](./installation.md)：本机环境、安装、授权方式、验证结果、升级与卸载。
- [TODO.md](./TODO.md)：已完成的本地检查和仍待本人执行的授权、云端验证事项。
- [agent-usage.md](./agent-usage.md)：agent 调用命令的示例和边界。

## 官方资料

- [Google Colab CLI 仓库与 README](https://github.com/googlecolab/google-colab-cli)
- [Colab CLI Operator skill](https://github.com/googlecolab/google-colab-cli/blob/main/skills/colab-operator/SKILL.md)
- [Google Developers：Introducing the Google Colab CLI](https://developers.googleblog.com/introducing-the-google-colab-cli/)
- [Google Colab FAQ：运行时、使用限制和资源供应](https://research.google.com/colaboratory/faq.html)
- [Colab 本地 runtime 说明](https://research.google.com/colaboratory/local-runtimes.html)

# 使用 Colab CLI 执行 agent 任务

Claude Code、Codex 等只要有本地终端权限，就能调用本机的 `colab` 命令，不需要专门的 agent connector。CLI 使用本机已授权并缓存的 Google 身份；账号选择和首次 OAuth 同意必须由本人在浏览器和终端中完成。agent 还需要得到访问相关本地脚本、输入文件和输出目录的终端权限。

## 一次性脚本

如果任务只需运行一个脚本，可使用 `colab run`。默认申请 CPU runtime，不加 `--keep` 时命令会在执行后释放 runtime：

```sh
colab --auth=oauth2 run ./analysis.py
```

## 具名会话和文件传输

需要多步操作时，使用明确的会话名，完成后停止它。`colab exec -f` 会读取本地脚本并将脚本内容发送给远端 Colab kernel 执行；检查文件中是否包含私密数据后再运行。远端生成的文件应在停止会话前下载：

```sh
colab --auth=oauth2 new -s useful-commands-agent
colab --auth=oauth2 exec -s useful-commands-agent -f ./analysis.py
colab --auth=oauth2 download -s useful-commands-agent /content/result.csv ./result.csv
colab --auth=oauth2 stop -s useful-commands-agent
```

上例假设脚本在 `/content/result.csv` 写出结果。只运行 Python 时也可以将代码通过标准输入传给 `colab exec`。本地文件传输和远端执行要按向第三方云端发送数据来对待；不要上传凭据、token、私密数据或未经检查的脚本。

## 给 agent 的任务提示

```text
请用本机 Google Colab CLI 运行 ./analysis.py。使用 CPU 和具名会话 useful-commands-agent；
不要挂载 Drive，不要读取或上传凭据。先检查脚本和输入文件，再执行。
把 /content/result.csv 下载到当前目录，报告结果，然后停止会话并确认清理命令已执行。
如果账号授权尚未完成、资源无法分配或需要升级/付费资源，请停止并告诉我需要我处理的事项。
```

若用户仅要求一次性计算，可将提示改为使用 `colab run`，且不要传入 `--keep`。默认从 CPU 开始；只有任务明确需要并且账号允许时才考虑 GPU、TPU 或高内存形状。

## 身份、交互和命令边界

- CLI 使用当前本机用户配置中的身份。首次 OAuth 需要用户在浏览器选账号、同意授权，并在本地终端粘贴返回代码。不要让 agent 读取或回显缓存 token；token 位于 `~/.config/colab-cli/token.json`。
- `colab auth` 是给远端 VM 注入 GCP 凭据，使 VM 内代码能调用 Google Cloud 服务；它与本地 CLI 的 OAuth/ADC 登录不同。它不能修复 CLI 本身的认证问题。
- `colab auth` 和 `colab drivemount` 需要人在可交互的 TTY 终端完成交互；Drive mount 会访问用户云端文件。需要时应先由用户决定并操作。终端 agent 不应等待这类交互命令。
- `colab console`、`colab repl` 和 `colab ssh` 提供交互式连接，agent 的非交互命令流程不应依赖它们。CLI 虽支持 `colab ssh`，但 Google 对免费且没有正 Colab compute-unit 余额的托管 runtime 禁止 SSH shell、远程桌面等远程控制；不要把免费 Colab session 当成常驻 shell 或 unattended agent server。
- 远端会话占用计算资源，结束后使用 `colab stop -s <会话名>`；`colab run` 不带 `--keep` 会自动释放。脚本失败时也要检查并停止自己创建的会话。

## 资源与运行限制

GPU 和 TPU 是否可用取决于账号套餐、配额和当时资源供应；高内存 machine shape 受付费订阅和 compute-unit 余额等条件限制。会话可能因空闲或 Colab 强制的最大生命周期而结束。Google 说明总体用量限制、空闲超时、最长 VM 生命周期和 GPU 型号会随时间改变且不公开；免费 runtime 通常最多运行 12 小时，实际时长取决于供应和使用情况。所有计算资源都应当视为临时资源，重要结果应在会话结束前下载。

Colab 面向交互式计算。使用前检查当前套餐和额度；不要请求用户未授权的付费或加速资源，也不要试图绕开 Colab 的服务限制。

## 官方资料

- [Google Colab CLI 仓库与命令参考](https://github.com/googlecolab/google-colab-cli)
- [Colab CLI Operator skill](https://github.com/googlecolab/google-colab-cli/blob/main/skills/colab-operator/SKILL.md)
- [Google Colab FAQ：资源供应、时限和远程控制限制](https://research.google.com/colaboratory/faq.html)
- [Google Developers：Introducing the Google Colab CLI](https://developers.googleblog.com/introducing-the-google-colab-cli/)

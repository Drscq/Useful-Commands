# Google Colab CLI 项目资料设计

## 目标

在现有 `Useful-Commands` 项目中，为 Google Colab CLI 建立一组中文操作资料，并在本机安装官方 CLI。资料需要记录实际完成的安装步骤、认证和验证方式、常用命令、待办事项，以及 Claude Code 和 Codex 如何通过本地终端调用 CLI 和相关限制。

## 项目背景

仓库目前按主题保存命令笔记，例如 `Linux/`、`Windows/`、`VM/` 和 `dockerRelated.md`。用户使用 macOS Apple Silicon；检查时系统有 Python 3.12 和 Homebrew，尚未检测到 `uv`、`colab` 或 `gcloud`。因此安装记录应基于实际操作更新，不能预先写成已经成功。

## 目录与文件

新增 `Colab/` 目录，包含：

- `README.md`：说明 Colab CLI 的用途、项目内文件入口和最短使用流程。
- `TODO.md`：记录尚未完成的账号授权、示例验证和后续维护事项，并在完成后更新状态。
- `installation.md`：记录本机环境、安装选择、每一步执行的命令、验证结果、认证流程和卸载/升级方法。只记录最终采用且成功的过程，不记录已排除的错误尝试。
- `agent-usage.md`：说明 Claude Code、Codex 等具备终端能力的 agent 如何调用 `colab`，给出安全的任务提示范例，解释认证、资源/套餐、运行时、交互式命令和本地文件传输限制。

文档以中文编写，命令、选项和官方产品名称保留原文。令牌、OAuth 密钥和用户隐私信息不写入仓库。

## 安装与验证方案

使用 Google 官方维护的 `googlecolab/google-colab-cli` 包。优先使用官方推荐的 `uv tool install google-colab-cli`，避免把 CLI 装进项目 Python 环境；若缺少 `uv`，先通过 Homebrew 安装 `uv`。随后检查 `colab --version` 和 `colab --help`。认证采用官方 CLI 当前默认方案；如果需要 Google Cloud ADC 或用户浏览器交互授权，则记录实际采用的认证步骤，并让用户亲自完成必须由本人确认的浏览器登录。

只有在已认证且确认资源可用后，才申请一个短时 CPU 会话做最小验证：运行简单 Python 代码，查看会话，再停止会话释放计算资源。未获得用户授权或没有可用账号认证时，文档应清楚记录为未完成，不应声称云端会话测试已通过。

## Agent 使用边界与限制

Agent 在本地终端具备执行命令权限时，可像用户一样调用 `colab` 命令；不需要专门的 Claude/Codex 插件才能进行基本 CLI 操作。需要说明 agent 使用哪一个本地 Google 身份、如何准备 ADC、GPU/TPU 配额和可用性依套餐及当时资源而变化、远程会话会消耗计算额度且要及时停止，以及本地脚本会被发送到远程 runtime 执行。交互式命令和 Google 登录/Drive 授权可能需要用户在终端或浏览器中完成。

## 官方参考

- CLI 仓库与 README：<https://github.com/googlecolab/google-colab-cli>
- Google Developers CLI 介绍：<https://developers.googleblog.com/introducing-the-google-colab-cli/>
- Colab 本地 runtime 说明（用于区分浏览器 Colab、CLI 和本地 runtime）：<https://research.google.com/colaboratory/local-runtimes.html>

## 完成条件

1. 官方 CLI 安装在本机独立工具环境中，版本与帮助命令可运行。
2. `Colab/` 下四份资料准确反映实际执行步骤和验证结果，不保存认证秘密。
3. TODO 明确列出后续由用户决定或执行的事项。
4. 如能完成云端验证，短时 session 已停止；如不能，限制与未完成状态写明。

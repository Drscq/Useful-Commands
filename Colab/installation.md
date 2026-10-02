# Google Colab CLI 安装记录

## 本机环境

本记录对应 macOS Apple Silicon 环境。安装时已有 Python 3.12.2 和 Homebrew 6.0.17；安装后验证得到 `uv` 0.12.22、`google-colab-cli` 0.7.4。`colab` 可执行文件位于用户级 `~/.local/bin/colab`，该目录已在 `PATH` 中。

## 安装

CLI 使用 `uv tool` 安装在独立的用户级工具环境中，没有安装到项目的 Python 环境：

```sh
brew install uv
uv tool install google-colab-cli
```

本机检查结果：

```text
uv --version       → uv 0.12.22
colab version      → Version: 0.7.4
colab --help       → 成功；列出 sessions、new、exec、download、stop 等命令
```

## 首次授权

安装版 `colab --help` 列出 `--auth <oauth2|adc>`，并显示默认值为 `oauth2`。本机推荐显式传入 OAuth2：

```sh
colab --auth=oauth2 sessions
```

首次运行会显示 Google 授权链接。用户需在浏览器中选择账号并完成同意流程，然后将页面给出的代码粘贴到发起命令的本地终端。`sessions` 用于列出会话；这个首次授权流程不需要先创建 VM。OAuth token 缓存在 `~/.config/colab-cli/token.json`。不要把授权代码、token 或凭据文件复制到仓库、日志或提示词中。

OAuth2 还需要 CLI 能读取 OAuth client JSON 配置。`colab --help` 提供 `--client-oauth-config`（短选项 `-c`）；bundled skill 列出的默认位置是 `~/.colab-cli-oauth-config.json`。该配置和 token 都留在本机，不要放进仓库。

安装版帮助和 `colab skill` 中提到的默认认证方式存在差异：后者的文本写 ADC 为默认值，而本机 `colab --help` 明确报告 OAuth2 是默认值。对本机已安装的 0.7.4，按照实际帮助使用 `--auth=oauth2`，并在升级后重新查看 `colab --help`。

如果已有 Google Cloud SDK 和 ADC 环境，也可以显式选择 ADC，并按 Colab 所需 scopes 登录：

```sh
gcloud auth application-default login --scopes=openid,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/colaboratory
colab --auth=adc sessions
```

本机没有安装 `gcloud`。使用上面的 OAuth2 流程不需要安装 Google Cloud SDK，因此没有为此任务安装它。

## 验证边界

本机确认了安装、版本命令和 CLI 帮助。尚未执行首次 Google OAuth 授权，也没有创建或运行云端 runtime；`gcloud` 不存在。云端 CPU smoke test 留在 [TODO.md](./TODO.md) 中，不能将本地 CLI 验证当作云端验证结果。

## 升级与卸载

升级 CLI：

```sh
uv tool upgrade google-colab-cli
```

卸载 CLI：

```sh
uv tool uninstall google-colab-cli
```

Homebrew 安装的 `uv` 可单独升级：

```sh
brew upgrade uv
```

## 官方资料

- [Google Colab CLI 仓库](https://github.com/googlecolab/google-colab-cli)
- [Colab CLI Operator skill](https://github.com/googlecolab/google-colab-cli/blob/main/skills/colab-operator/SKILL.md)
- [Google Developers：Introducing the Google Colab CLI](https://developers.googleblog.com/introducing-the-google-colab-cli/)

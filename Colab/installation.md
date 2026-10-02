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

本机不需要另行准备 OAuth client JSON。安装版源码在默认外部配置 `~/.colab-cli-oauth-config.json` 不存在时，会回退到随包提供的 `colab_cli/oauth_config.json`；本机使用这份 bundled 配置。`--client-oauth-config`（短选项 `-c`）可用于显式指定自定义配置文件，是可选覆盖项。

安装版帮助和 `colab skill` 文本存在两处差异：本机 `colab --help` 报告 OAuth2 为默认认证方式，但 bundled skill 写 ADC 为默认方式，并称 OAuth client JSON 是必需的。已安装的 0.7.4 源码显示外部 JSON 缺失时会回退到包内配置，因此该 JSON 要求也与本机实现不符。按本机帮助显式使用 `--auth=oauth2`，升级后重新查看 `colab --help` 和对应版本的实现。

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

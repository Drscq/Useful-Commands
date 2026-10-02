# Google Colab CLI 待办

## 当前使用状态

尚未完成 Google OAuth 授权或创建云端 runtime；目前没有请求或使用任何付费、GPU、TPU 或 high-memory 资源。

## 已完成

- [x] 在 macOS Apple Silicon 上使用 Homebrew 安装 `uv` 0.12.22。
- [x] 使用 `uv tool install google-colab-cli` 安装官方 CLI 0.7.4。
- [x] 确认 `~/.local/bin/colab` 已在 `PATH` 中。
- [x] 本地检查 `uv --version`、`colab version` 和 `colab --help`。
- [x] 核对 `colab --help` 中的认证选项，确认该安装版本默认使用 OAuth2；确认本机没有 `gcloud`。OAuth2 流程不依赖安装 gcloud。

## 尚待本人操作

- [ ] **首次 Google OAuth2 授权**：在本机终端运行下列命令；打开显示的 Google 授权链接，选择账号并同意，然后把网页返回的代码粘贴回该终端。这个步骤只认证并列出会话，不会创建 VM；此安装使用包内 OAuth client 配置，无需另行准备 JSON 文件。

  ```sh
  colab --auth=oauth2 sessions
  ```

- [ ] **CPU 云端 smoke test**：首次授权完成后逐条运行下列命令。确认输出为 `2`，检查状态，再停止具名会话释放资源。若授权或分配失败，不要把测试标记为通过。

  ```sh
  colab --auth=oauth2 new -s useful-commands-smoke
  printf 'print(1 + 1)\n' | colab --auth=oauth2 exec -s useful-commands-smoke
  colab --auth=oauth2 status -s useful-commands-smoke
  colab --auth=oauth2 stop -s useful-commands-smoke
  ```

## 后续评估

- [ ] 如需 GPU、TPU 或 high-memory runtime，先在 Colab 账号中查看当前套餐资格、compute-unit 余额和预期消耗，再做短时验证。硬件供应与时限会变动，不能假设某种设备始终可用。

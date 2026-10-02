# Google Colab CLI 待办

## 当前使用状态

Google OAuth2 授权已完成，CPU smoke test 已通过并停止。本次测试只申请了标准 CPU runtime，没有请求 GPU、TPU 或 high-memory 资源。测试前后 `colab sessions` 都显示一个此前已存在、标记为 `[?]` 的 A100 高内存会话；本次操作未创建或停止该会话。

## 已完成

- [x] 在 macOS Apple Silicon 上使用 Homebrew 安装 `uv` 0.12.22。
- [x] 使用 `uv tool install google-colab-cli` 安装官方 CLI 0.7.4。
- [x] 确认 `~/.local/bin/colab` 已在 `PATH` 中。
- [x] 本地检查 `uv --version`、`colab version` 和 `colab --help`。
- [x] 核对 `colab --help` 中的认证选项，确认该安装版本默认使用 OAuth2；确认本机没有 `gcloud`。OAuth2 流程不依赖安装 gcloud。
- [x] 完成首次 Google OAuth2 授权，并运行 `colab --auth=oauth2 sessions` 确认能读取当前会话。
- [x] 创建 `useful-commands-smoke` 标准 CPU 会话，执行 `print(1 + 1)` 得到 `2`，确认状态为 IDLE 后停止会话；后续会话列表中不再显示该 smoke test 会话。

## 尚待本人确认

- [ ] **确认遗留 A100 会话**：查看 Google Colab 是否仍在使用 A100 高内存会话。CLI 将没有本地 session 记录的服务端 assignment 标记为 `[?]`；如果该会话不是你正在使用的，请在确认后自行停止，避免继续占用额度。

## 后续评估

- [ ] 如需 GPU、TPU 或 high-memory runtime，先在 Colab 账号中查看当前套餐资格、compute-unit 余额和预期消耗，再做短时验证。硬件供应与时限会变动，不能假设某种设备始终可用。

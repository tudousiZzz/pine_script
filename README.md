# Pine Script 开发工具集 / Pine Script Development Tools

A collection of Pine Script indicators and strategies for TradingView, with a complete development environment setup.

## 目录结构 / Project Structure

```
pine_script/
├── .github/
│   └── workflows/
│       └── copilot-setup-steps.yml   # Copilot 开发环境配置
├── .vscode/
│   ├── extensions.json               # VS Code 插件推荐
│   └── settings.json                 # VS Code 工作区配置
├── indicators/                       # 指标脚本
│   ├── ma_crossover.pine             # 均线交叉指标
│   └── rsi_ob_os.pine                # RSI 超买超卖指标
├── strategies/                       # 策略脚本
│   └── ma_crossover_strategy.pine    # 均线交叉策略
├── .editorconfig                     # 编辑器配置
├── .gitignore
└── README.md
```

## 开发工具 / Development Tools

### VS Code 插件 / VS Code Extensions

安装以下推荐插件以获得最佳开发体验：

- **Pine Script Syntax Highlighter** (`pine-lovers.pine-script-syntax-highlighter`) — Pine Script 语法高亮
- **Pine Script** (`anovileanu.pine-script`) — Pine Script 语言支持
- **GitLens** (`eamodio.gitlens`) — 增强的 Git 功能
- **EditorConfig** (`editorconfig.editorconfig`) — 统一代码格式

打开项目后，VS Code 会自动提示安装推荐插件。

### 环境依赖 / Environment Dependencies

| 工具 | 版本 | 用途 |
|------|------|------|
| Node.js | ≥ 20 | Pine Script 相关工具链 |
| Python | ≥ 3.11 | 脚本分析与辅助工具 |
| npm | 随 Node.js | 包管理 |
| pip | 随 Python | 包管理 |

### Copilot 云端环境 / Copilot Cloud Agent Setup

`.github/workflows/copilot-setup-steps.yml` 会自动在 GitHub Copilot 云端环境中安装所有必要工具，包括：

- Node.js 20
- Python 3.11
- Pine Script lint 工具
- 常用 Python 分析库 (requests, beautifulsoup4, lxml)

## 脚本说明 / Scripts Overview

### 指标 / Indicators

| 文件 | 描述 |
|------|------|
| `indicators/ma_crossover.pine` | 多类型均线交叉指标，支持 EMA/SMA/WMA，含金叉死叉提醒 |
| `indicators/rsi_ob_os.pine` | RSI 超买超卖指标，含区域填充和信号提醒 |

### 策略 / Strategies

| 文件 | 描述 |
|------|------|
| `strategies/ma_crossover_strategy.pine` | 均线交叉回测策略，支持日期过滤和手续费设置 |

## 使用方法 / Usage

1. 在 [TradingView](https://www.tradingview.com) 打开图表
2. 点击 **Pine Editor** 面板
3. 将 `.pine` 文件内容粘贴到编辑器中
4. 点击 **Add to chart** 添加到图表

## 版本要求 / Version Requirements

所有脚本使用 **Pine Script v5**，需要 TradingView 平台支持。

## 参考资料 / References

- [Pine Script v5 官方文档](https://www.tradingview.com/pine-script-docs/en/v5/Introduction.html)
- [Pine Script 语言参考](https://www.tradingview.com/pine-script-reference/v5/)
- [TradingView 社区脚本](https://www.tradingview.com/scripts/)

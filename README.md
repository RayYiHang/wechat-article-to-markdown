# wechat-article-to-markdown

Fetch WeChat Official Account articles and convert them to clean Markdown.

[English](#features) | [中文](#功能特性)

## Features

- Anti-detection fetching with Camoufox
- Extract article metadata (title, account name, publish time, source URL)
- Convert WeChat article HTML to Markdown
- Download article images to local `images/` and rewrite links
- Handle WeChat `code-snippet` blocks with language fences

## Installation

```bash
# Recommended: pipx
pipx install wechat-article-to-markdown

# Or: uv tool
uv tool install wechat-article-to-markdown
```

Or from source:

```bash
git clone git@github.com:jackwener/wechat-article-to-markdown.git
cd wechat-article-to-markdown
uv sync
```

## Usage

```bash
# Installed CLI
wechat-article-to-markdown "https://mp.weixin.qq.com/s/xxxxxxxx"

# Run in repo with uv
uv run wechat-article-to-markdown "https://mp.weixin.qq.com/s/xxxxxxxx"

# Backward-compatible local entry
uv run main.py "https://mp.weixin.qq.com/s/xxxxxxxx"
```

Output structure:

```text
output/
└── <article-title>/
    ├── <article-title>.md
    └── images/
        ├── img_001.png
        ├── img_002.png
        └── ...
```

## Use as AI Agent Skill

This project ships with [`SKILL.md`](./SKILL.md), so AI agents can discover and use this tool workflow.

### Claude Code / Antigravity

```bash
# Clone into your project's skills directory
mkdir -p .agents/skills
git clone git@github.com:jackwener/wechat-article-to-markdown.git \
  .agents/skills/wechat-article-to-markdown

# Or copy SKILL.md only
curl -o .agents/skills/wechat-article-to-markdown/SKILL.md \
  https://raw.githubusercontent.com/jackwener/wechat-article-to-markdown/main/SKILL.md
```

### OpenClaw / ClawHub

Officially supports [OpenClaw](https://openclaw.ai) and [ClawHub](https://docs.openclaw.ai/tools/clawhub):

```bash
clawhub install wechat-article-to-markdown
```

## PyPI Publishing (GitHub Actions)

Repository: `jackwener/wechat-article-to-markdown`
Workflow: `.github/workflows/publish.yml`
Environment: `pypi`

`publish.yml` triggers on `v*` tags and `workflow_dispatch`, builds with `uv build`, then publishes with trusted publishing (`id-token: write`).

---

## 功能特性

- 使用 Camoufox 进行反检测抓取
- 提取标题、公众号名称、发布时间、原文链接
- 将微信公众号文章 HTML 转换为 Markdown
- 下载图片到本地 `images/` 并自动替换链接
- 处理微信 `code-snippet` 代码块并保留语言标识

## 安装

```bash
# 推荐：pipx
pipx install wechat-article-to-markdown

# 或者：uv tool
uv tool install wechat-article-to-markdown
```

## 使用示例

```bash
wechat-article-to-markdown "https://mp.weixin.qq.com/s/xxxxxxxx"
```

## 作为 AI Agent Skill 使用

项目自带 [`SKILL.md`](./SKILL.md)，可供支持 `.agents/skills/` 约定的 Agent 自动发现。

### OpenClaw / ClawHub

```bash
clawhub install wechat-article-to-markdown
```

## License

MIT

# wechat-article-to-markdown

微信公众号文章抓取 & Markdown 转换工具。

使用 **Camoufox (反检测浏览器) + BeautifulSoup + markdownify** 将微信公众号文章转换为干净的 Markdown 文件，图片自动下载到本地。

## 功能

- 🦊 **反检测抓取** — 使用 Camoufox 反检测浏览器，避免微信 "环境异常" 验证页面
- 📄 **文章抓取** — 输入 URL，输出结构化 Markdown
- 🖼 **图片本地化** — 微信 CDN 图片并发下载到本地，Markdown 引用相对路径
- 💻 **代码块提取** — 正确处理微信 `code-snippet` 代码块，保留语言标识
- 📅 **元数据保留** — 标题、公众号名称、发布时间、原文链接
- 🧹 **格式清理** — 去除 `&nbsp;`、多余空行、行尾空格
- 🤖 **MCP 支持** — 通过 FastMCP 将抓取功能暴露为 MCP 工具，可被 AI 客户端调用

## 快速开始

### 推荐：使用 uv（零配置）

```bash
# 首次运行会自动安装依赖和 Camoufox 浏览器
uv run main.py "https://mp.weixin.qq.com/s/xxxxxxxx"
```

### 手动安装

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m camoufox fetch
python main.py "https://mp.weixin.qq.com/s/xxxxxxxx"
```

输出目录结构：

```
output/
└── 文章标题/
    ├── 文章标题.md
    └── images/
        ├── img_001.png
        ├── img_002.png
        └── ...
```

## 输出示例

```markdown
# 文章标题

> 公众号: xxx
> 发布时间: 2026-02-28 11:42
> 原文链接: https://mp.weixin.qq.com/s/...

---

正文内容...

![](images/img_001.png)
```

## MCP 服务

本项目支持 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)，可以被 Claude Desktop、Cursor 等 AI 客户端直接调用。

### 启动 MCP 服务

```bash
# stdio 模式 (默认，用于 Claude Desktop 等)
python mcp_server.py

# SSE 模式
python mcp_server.py --sse
```

### Claude Desktop 配置

在 Claude Desktop 配置文件中添加：

```json
{
  "mcpServers": {
    "wechat-article-to-markdown": {
      "command": "python",
      "args": ["/path/to/mcp_server.py"]
    }
  }
}
```

### 提供的工具

| 工具名 | 说明 | 参数 |
|--------|------|------|
| `fetch_wechat_article` | 抓取微信文章并转为 Markdown | `url` (必填), `download_images` (可选, 默认 true), `output_dir` (可选) |

> 说明：当传入 `output_dir` 时，会将 Markdown 文件与图片保存到该目录下，并在返回内容中提示保存路径。

## 技术方案

| 功能 | 方案 |
|------|------|
| 页面抓取 | Camoufox (反检测 Firefox + Playwright) |
| HTML 解析 | BeautifulSoup |
| HTML → Markdown | markdownify |
| 图片下载 | httpx async + Semaphore 并发控制 |
| MCP 服务 | FastMCP |

### 微信文章 HTML 关键结构

| 元素 | 选择器 |
|------|--------|
| 标题 | `#activity-name` |
| 公众号名 | `#js_name` |
| 发布时间 | JS 变量 `create_time` |
| 正文 | `#js_content` |
| 图片 | `img[data-src]` (懒加载) |
| 代码块 | `.code-snippet__fix` |

## JS 版本

原始 JavaScript 版本保留在 [`js-version`](https://github.com/jackwener/wechat-article-to-markdown/tree/js-version) 分支。

## License

MIT

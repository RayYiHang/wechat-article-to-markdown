"""
MCP Server — 通过 FastMCP 将微信文章转 Markdown 功能暴露为 MCP 工具。

启动方式:
    python mcp_server.py          # stdio 模式 (默认)
    python mcp_server.py --sse    # SSE 模式
"""

from __future__ import annotations

from fastmcp import FastMCP

from main import fetch_article_as_markdown

mcp = FastMCP("wechat-article-to-markdown")


@mcp.tool()
async def fetch_wechat_article(url: str, download_images: bool = True) -> str:
    """抓取微信公众号文章并转换为 Markdown。

    Args:
        url: 微信公众号文章链接 (https://mp.weixin.qq.com/s/...)
        download_images: 是否下载图片到本地，默认 True
    """
    if not url.startswith("https://mp.weixin.qq.com/"):
        return "❌ 请输入有效的微信文章 URL (https://mp.weixin.qq.com/...)"

    try:
        markdown = await fetch_article_as_markdown(
            url, download_images=download_images,
        )
    except RuntimeError as e:
        return f"❌ 抓取失败: {e}"
    except Exception as e:
        return f"❌ 抓取失败: {e}"

    return markdown


if __name__ == "__main__":
    mcp.run()

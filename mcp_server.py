"""
MCP Server — 通过 FastMCP 将微信文章转 Markdown 功能暴露为 MCP 工具。

启动方式:
    python mcp_server.py          # stdio 模式 (默认)
    python mcp_server.py --sse    # SSE 模式
"""

from __future__ import annotations

import re
from pathlib import Path

from fastmcp import FastMCP

from main import _fetch_article_core

mcp = FastMCP("wechat-article-to-markdown")


@mcp.tool()
async def fetch_wechat_article(
    url: str,
    download_images: bool = True,
    output_dir: str | None = None,
) -> str:
    """抓取微信公众号文章并转换为 Markdown。

    Args:
        url: 微信公众号文章链接 (https://mp.weixin.qq.com/s/...)
        download_images: 是否下载图片到本地，默认 True
        output_dir: 指定输出目录（保存 .md + images/）。为空则不保存 .md，仅返回 Markdown 文本。
    """
    if not url.startswith("https://mp.weixin.qq.com/"):
        return "❌ 请输入有效的微信文章 URL (https://mp.weixin.qq.com/...)"

    output_dir = output_dir.strip() if output_dir else None

    try:
        base_dir: Path | None = (
            Path(output_dir).expanduser() if output_dir else None
        )
        if base_dir is not None:
            base_dir.mkdir(parents=True, exist_ok=True)

        markdown, meta = await _fetch_article_core(
            url,
            download_images=download_images,
            output_dir=base_dir,
        )
    except Exception as e:
        return f"❌ 抓取失败: {e}"

    if base_dir is None:
        return markdown

    title = meta.get("title") or "untitled"
    safe_title = re.sub(r'[/\\?%*:|"<>]', "_", title)[:80] or "untitled"
    article_dir = base_dir / safe_title
    article_dir.mkdir(parents=True, exist_ok=True)

    md_path = article_dir / f"{safe_title}.md"
    md_path.write_text(markdown, encoding="utf-8")

    return f"✅ 已保存: {md_path}\n\n{markdown}"


if __name__ == "__main__":
    mcp.run()

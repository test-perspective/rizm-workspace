#!/usr/bin/env python3
"""Generate a local HTML preview for README.md and README.ja.md."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "preview-readme.html"
CSS = "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-light.min.css"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Rizm README Preview</title>
  <link rel="stylesheet" href="{css}" />
  <style>
    body {{ margin: 0; background: #f6f8fa; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .toolbar {{ position: sticky; top: 0; z-index: 10; display: flex; gap: 8px; padding: 12px 16px; background: #24292f; color: #fff; align-items: center; }}
    .toolbar button {{ border: 0; border-radius: 6px; padding: 8px 14px; cursor: pointer; background: #30363d; color: #fff; }}
    .toolbar button.active {{ background: #0969da; }}
    .panel {{ display: none; }}
    .panel.active {{ display: block; }}
    .markdown-body {{ box-sizing: border-box; max-width: 980px; margin: 0 auto; padding: 32px 45px 64px; background: #fff; min-height: calc(100vh - 52px); }}
    .note {{ max-width: 980px; margin: 16px auto 0; padding: 0 16px; color: #57606a; font-size: 14px; }}
  </style>
</head>
<body>
  <div class="toolbar">
    <strong>README Preview</strong>
    <button type="button" class="tab active" data-target="en">English</button>
    <button type="button" class="tab" data-target="ja">日本語</button>
  </div>
  <p class="note">Local preview (GitHub-like styling). Badges and images load from the network.</p>
  <section id="en" class="panel active"><article class="markdown-body">{en_body}</article></section>
  <section id="ja" class="panel"><article class="markdown-body">{ja_body}</article></section>
  <script>
    document.querySelectorAll(".tab").forEach((btn) => {{
      btn.addEventListener("click", () => {{
        document.querySelectorAll(".tab").forEach((b) => b.classList.remove("active"));
        document.querySelectorAll(".panel").forEach((p) => p.classList.remove("active"));
        btn.classList.add("active");
        document.getElementById(btn.dataset.target).classList.add("active");
      }});
    }});
  </script>
</body>
</html>
"""


def main() -> None:
    en_body = (ROOT / ".preview-readme-body.html").read_text(encoding="utf-8")
    ja_body = (ROOT / ".preview-readme-ja-body.html").read_text(encoding="utf-8")
    OUT.write_text(
        TEMPLATE.format(css=CSS, en_body=en_body, ja_body=ja_body),
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

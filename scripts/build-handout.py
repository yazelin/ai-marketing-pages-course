#!/usr/bin/env python3
"""把 course/ 全部講義組成單一印刷版 HTML(handout.html),供 headless Chrome 轉 PDF。"""
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
ORDER = [
    ("00-overview.md", "課程總覽"),
    ("00b-setup.md", "模組 0 — 行前準備"),
    ("01-first-landing-page.md", "模組 1 — 第一個活動頁"),
    ("02-ai-visual-assets.md", "模組 2 — AI 視覺資產"),
    ("03-interactive-effects.md", "模組 3 — 互動特效"),
    ("04-marketing-games.md", "模組 4 — 行銷遊戲"),
    ("05-deployment.md", "模組 5 — 上線"),
    ("06-live-ai-on-page.md", "模組 6(進階)— 頁面即時呼叫 AI"),
    ("07-automation.md", "模組 7(進階)— 讓活動頁自己更新"),
    ("08-prompt-playbook.md", "模組 8 — Prompt 兵法"),
]

CSS = """
@page{size:A4; margin:12mm 0}
*{box-sizing:border-box}
body{font-family:"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;
  color:#1c2b26; margin:0; font-size:10.5pt; line-height:1.85}
.cover{height:96vh; display:flex; flex-direction:column; justify-content:center;
  background:#10221d; color:#f4efe4; padding:0 18mm; page-break-after:always;
  -webkit-print-color-adjust:exact; print-color-adjust:exact}
.cover .kicker{font-size:9pt; letter-spacing:.5em; color:#c98f4e; margin-bottom:8mm}
.cover h1{font-family:"Noto Serif TC",serif; font-size:30pt; font-weight:600; margin:0 0 6mm; line-height:1.4; color:#f4efe4 !important}
.cover p{color:#9db8ae; max-width:30em; line-height:2}
.toc{padding:10mm 18mm; page-break-after:always}
.toc h2{font-family:"Noto Serif TC",serif; color:#1d4438}
.toc ol{line-height:2.4; color:#1c2b26}
.module{padding:6mm 18mm; page-break-before:always}
.module:first-of-type{page-break-before:auto}
h1,h2,h3,h4{font-family:"Noto Serif TC","PMingLiU",serif; color:#1d4438; line-height:1.5}
.module > h1{font-size:17pt; border-bottom:2.5px solid #c98f4e; padding-bottom:3mm; margin-top:0}
h2{font-size:13pt; margin-top:9mm}
h3{font-size:11.5pt; color:#2e5c4d}
blockquote{margin:4mm 0; padding:2mm 6mm; border-left:3px solid #c98f4e;
  background:#f4efe4; color:#3c4f48; -webkit-print-color-adjust:exact}
blockquote p{margin:1mm 0}
pre{background:#10221d; color:#ece5d4; border-radius:4px; padding:4mm 5mm;
  font-family:"JetBrains Mono","Courier New",monospace; font-size:8.5pt; line-height:1.7;
  white-space:pre-wrap; word-break:break-all;
  -webkit-print-color-adjust:exact; print-color-adjust:exact; page-break-inside:avoid}
code{font-family:"JetBrains Mono","Courier New",monospace; font-size:.92em;
  background:#ece5d4; padding:.5px 4px; border-radius:3px; -webkit-print-color-adjust:exact}
pre code{background:none; padding:0}
table{border-collapse:collapse; width:100%; margin:4mm 0; font-size:9pt; page-break-inside:avoid}
th,td{border:1px solid #c8d4cd; padding:2mm 3mm; text-align:left; vertical-align:top; line-height:1.7}
th{background:#1d4438; color:#f4efe4; -webkit-print-color-adjust:exact; print-color-adjust:exact}
tr:nth-child(even) td{background:#f4f1e8; -webkit-print-color-adjust:exact}
li{margin:1.2mm 0}
a{color:#a8743a; text-decoration:none}
hr{border:none; border-top:1px solid #c8d4cd; margin:6mm 0}
.footer-note{color:#7d8d86; font-size:8pt; letter-spacing:.1em; margin-top:8mm}
"""

md = markdown.Markdown(extensions=["tables", "fenced_code"])
sections = []
for fname, label in ORDER:
    text = (ROOT / "course" / fname).read_text(encoding="utf-8")
    md.reset()
    sections.append(f'<section class="module">{md.convert(text)}</section>')

toc = "".join(f"<li>{label}</li>" for _, label in ORDER)
html = f"""<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="UTF-8">
<title>講義 — AI 互動行銷頁實作課</title><style>{CSS}</style></head><body>
<div class="cover">
  <p class="kicker">AI MARKETING PAGES COURSE — HANDOUT</p>
  <h1>AI 互動行銷頁實作課<br>上課講義</h1>
  <p>不寫程式,做出會動、會玩、能上線的活動網頁。<br>
  含全部模組講義、prompt 範本、常見坑與驗收清單。<br>
  Demo 對照:repo 內 demos/index.html(雙擊即開)。</p>
  <p class="footer-note">2026-06 · SANWU COFFEE 為課程虛構品牌</p>
</div>
<div class="toc"><h2>目錄</h2><ol>{toc}</ol></div>
{"".join(sections)}
</body></html>"""

out = ROOT / "pdf" / "handout.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"wrote {out} ({len(html)} chars, {len(sections)} modules)")

# 執行日誌

## 2026-06-10 — 一次完成:研究、決策、課程、demo、驗證

1. **盤點**:`gh repo list` 篩出 2026-04-10 後有 push 的約 55 個 repo,逐一評估與「行銷人做 AI 互動行銷頁」的相關性,實地讀了 web-effects-collector / gemini-image-starter / ai-tarot-companion / catime / yazelin-courses / j303 的本機 clone 確認技術細節。→ `docs/research/01-repo-survey.md`
2. **決策**:三份 ADR 定案受眾範圍、技術選型(每項都對應一個近兩個月的真實 repo)、部署教法(決策樹 + GitHub Pages 主線)。→ `docs/decisions/`
3. **設計**:課程 8 模組地圖 + demo 規格 + 驗收標準。→ `docs/design.md`
4. **課程**:寫完模組 0-7 講義(course/),每模組含「學完能做什麼 / 步驟 / 給 AI 的 prompt 範本 / 常見坑」;進階模組附可整段照抄的 Cloudflare Worker 與 GitHub Actions 範本。
5. **Demo**:四個零依賴純靜態頁(demos/),粒子、confetti、分享圖卡全部自寫 canvas,離線雙擊可開;視覺走深墨綠 + 奶油白 + 銅棕的霧感極簡,拉霸符號用 inline SVG。
6. **驗證**(Chrome DevTools 實測,截圖在 docs/verification/):
   - demo 01:粒子 canvas 非透明像素 73,806;倒數正確(距 6/20 約 9 天 23 時);OG tags 4 個齊;捲動後 CTA bar 出現、三張亮點卡進場。
   - demo 01 手機(390x844 模擬):抓到 `.fog` 水平溢出與 `.dates` 詞中折行兩個 bug,修復後 scrollWidth=390 無溢出。
   - demo 02:機率表調 100% 大獎驗證 rigging 生效(三輪對齊咖啡)、優惠碼格式 `SANWU-XXXX` 正確、confetti 非透明像素 10,354、重新整理後仍鎖「今天抽過了」;`?reset` 參數可清除供測試。
   - demo 03:全選第一選項 → 加權計分得「儀式感型」(R=6 符合預期);分享圖卡 canvas 1,458,000/1,458,000 像素全有繪製、`toDataURL` 正常(下載可用);截圖確認排版無爆框。
   - 四頁 console 零錯誤(補了 inline SVG favicon 解掉預設 404)、手機寬度皆無水平溢出。
7. **發佈**:private repo `yazelin/ai-marketing-pages-course` 建立並推送。

## 已知未做(留待拍板)

- 課程影片腳本化(目前是講義形式,結構已照「可轉影片」安排)。
- demo 部署到線上(repo 是 private;若要 live demo 需另開 public repo 或開 Pages)。
- 模組 2 的實圖範例(可用 nanobanana / codex-imagegen 生成後補進 demos/01-landing)。

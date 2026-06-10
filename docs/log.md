# 執行日誌

## 2026-06-10(下午)— v2:簡報 + PDF + demo 質感升級 + 模組 8

使用者三項回饋:課程要 HTML 簡報 + 講義 PDF;demo 咖啡品牌感不夠(規格卡寫的熱拿鐵與蒸氣沒做出來);課程要含完整 prompt / context / 圖片技巧。

1. **「蒸氣去哪了」調查**:非程式錯誤——NOTES.md 規格卡當初只當模組 2 教材範例,demo 為零依賴刻意用漸層粒子代替,落差屬實。
2. **真的生圖**:nanobanana(Gemini)403 被擋 → 改用 codex-imagegen skill(Codex CLI $imagegen,ChatGPT 訂閱額度)生成兩張:hero 窗景熱拿鐵(16:9)、俯視拉花(1:1)。PIL 壓成 hero.jpg 108K / latte-top.jpg 76K(實踐模組 2 的 500KB 紀律)。
3. **demo 升級**:
   - 01:hero 改「左標題 + 右窗景照片」;照片容器維持原比例,CSS 三縷蒸氣絲錨定杯口 76%/60%(紅色定位法校過位);亮點卡加咖啡 SVG 線圖示。
   - 02:拉花圓徽 + 蒸氣動畫進場。
   - 03:開場圓徽;分享圖卡 canvas 畫入拉花照——以 base64 內嵌(file:// 直開時外部圖會汙染 canvas,toDataURL 下載會掛)。
   - 驗證:medallion 載入、圖卡 1,458,000 像素全繪、圖卡中心像素為奶泡色、toDataURL 正常、四種結果型路徑可達。
4. **模組 8 Prompt 兵法**(course/08 + slides/08):四層結構 / 品牌規格卡等四種 context / 圖片雙向(生圖規格卡、截圖參照)/ 聊天式 vs agent 式 / 驗收清單寫進指令 / demo 01 prompt 鏈實戰回放。
5. **HTML 簡報**:slides/ 共用 deck.css + deck.js(鍵盤、點擊、觸控翻頁,hash 記頁,print 模式攤平),10 份 deck + 目錄頁。驗證:翻頁/計數/邊界正常、console 乾淨、全部 200。
6. **講義 PDF**:scripts/build-handout.py(python-markdown 組 10 份講義 + 印刷 CSS)→ pdf/handout.html → headless google-chrome → **handout.pdf(25 頁 A4)**。修過一輪封面標題色被內文規則蓋掉的問題。


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

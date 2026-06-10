# AI 互動行銷頁實作課

教不會寫程式的行銷人,用 AI 做出「會動、會玩、能上線」的活動網頁。技術全部取材自 yazelin 2026-04 ~ 2026-06 的活躍 repo(web-effects-collector、gemini-image-starter、ai-tarot-companion、emoji-slot-machine、catime、j303 等),每一項都有真實上線的成品當證據。

本 repo 是這門課的完整記錄:研究、決策、課程內容、demo、驗證,全在這裡。

## 結構

```
docs/
  research/01-repo-survey.md     近兩個月 repo 技術盤點(選材依據)
  decisions/ADR-001 ~ 003        受眾範圍 / 技術選型 / 部署教法
  design.md                      課程設計文件(模組地圖 + demo 規格 + 驗收標準)
  log.md                         執行日誌與已知未做事項
  verification/                  驗證截圖
course/
  00-overview.md                 課程總覽
  00b-setup.md                   模組 0 行前準備
  01-first-landing-page.md       模組 1 AI 對話生整頁
  02-ai-visual-assets.md         模組 2 結構化 prompt 生圖
  03-interactive-effects.md      模組 3 互動特效
  04-marketing-games.md          模組 4 抽獎 / 刮刮樂 / 測驗
  05-deployment.md               模組 5 部署決策樹 + GitHub Pages
  06-live-ai-on-page.md          模組 6(進階)頁面即時呼叫 AI
  07-automation.md               模組 7(進階)GitHub Actions 自動更新
  08-prompt-playbook.md          模組 8 Prompt 兵法(prompt / context / 圖片 / 驗收)
slides/
  index.html                     簡報目錄(上課用,F11 全螢幕)
  deck.css / deck.js             共用簡報框架(鍵盤、觸控翻頁、print 攤平)
  00-overview ~ 08 共 10 份 deck
handout.pdf                      上課講義 PDF(25 頁 A4,全模組)
scripts/build-handout.py         講義 PDF 產生器(md → 印刷 HTML → headless Chrome)
pdf/handout.html                 PDF 的中間印刷版(可自行重印)
demos/
  index.html                     demo 總覽入口
  assets/latte-top.jpg           AI 生成俯視拉花(02/03 品牌圓徽用)
  01-landing/                    活動 landing(AI 生成窗景 hero + 杯口蒸氣 + 粒子 + 倒數)
  02-lucky-draw/                 拉霸抽獎(機率表 + 優惠碼 + 防重抽 + confetti)
  03-ai-quiz/                    心理測驗(加權計分 + canvas 分享圖卡含拉花照)
```

## 怎麼驗證成果

零 build、零依賴,兩種方式擇一:

```bash
# 方式一:直接雙擊 demos/index.html(離線也能跑)
# 方式二:本機 server
python3 -m http.server 8911
# 開 http://localhost:8911/demos/
```

逐項驗證清單(2026-06-10 已全數實測通過,過程見 docs/log.md):

- [ ] `demos/index.html` 開啟,三張卡片可點進各 demo
- [ ] demo 01:hero 粒子在動、倒數顯示距 6/20 的正確天數、捲動一屏後置底 CTA bar 滑出
- [ ] demo 01 手機寬度:無水平捲動、日期列整行換行
- [ ] demo 02:按「拉一把」三輪依序停下、中獎顯示 `SANWU-XXXX` 優惠碼、大獎撒彩帶;重新整理後按鈕鎖定「今天抽過了」;網址加 `?reset` 可重測;要驗機率表就改 `PRIZES` 裡的 weight(就在 script 最上方)
- [ ] demo 03:五題答完出結果型、按「儲存結果圖卡」下載 1080x1350 PNG、「再測一次」可重來
- [ ] 四頁 F12 Console 無紅字

## 課程閱讀順序

`course/00-overview.md` → 00b → 01 → … → 07。每模組末尾都標了對照的 demo。

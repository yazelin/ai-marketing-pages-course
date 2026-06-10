# 設計文件 — 「AI 互動行銷頁」線上課

日期:2026-06-10
依據:docs/research/01-repo-survey.md、ADR-001 ~ ADR-003

## 課程定位

- 名稱(暫):**AI 互動行銷頁實作課 — 不寫程式,做出會動、會玩、能上線的活動網頁**
- 受眾:不會寫程式的行銷人(ADR-001)
- 成果承諾:完課後能獨立產出「AI 視覺 + 互動特效 + 抽獎遊戲 + 已上線」的活動頁
- 教學語言:繁體中文;形式:模組講義(markdown,可轉影片腳本)+ 每模組一個可開啟驗證的 demo

## 模組地圖(8 模組,主線 6 + 進階 2)

| # | 模組 | 取材 | Demo |
|---|---|---|---|
| 0 | 行前準備:工具與心態 | — | — |
| 1 | 第一個活動頁:用 AI 對話生出整頁 | j303 / LeShePhoto | demos/01-landing |
| 2 | AI 視覺資產:從許願到可控 | gemini-image-starter | (講義內 prompt 配方) |
| 3 | 互動特效:讓頁面活起來 | web-effects-collector | demos/01-landing(粒子 hero) |
| 4 | 行銷遊戲:抽獎、刮刮樂、測驗 | emoji-slot-machine | demos/02-lucky-draw、demos/03-ai-quiz |
| 5 | 上線:部署決策樹 + GitHub Pages 實作 | yazelin.github.io / mori-canvas / ai-tarot | (部署 demos 本身) |
| 6 | 進階:頁面即時呼叫 AI | ai-tarot-companion | (講義附完整 Worker 範本) |
| 7 | 進階:讓活動頁自己更新 | catime | (講義附完整 workflow 範本) |

## Demo 規格(全部零 build、雙擊可開)

1. **01-landing** — 虛構「山霧咖啡 開幕週」活動頁:粒子 hero、倒數計時、活動資訊、CTA、OG tags。教 vibe coding 產物長什麼樣。
2. **02-lucky-draw** — 拉霸抽獎頁:三輪 emoji 拉霸、中獎機率表(可改)、優惠碼發放、localStorage 防重抽。
3. **03-ai-quiz** — 「你是哪一型行銷人」心理測驗:題庫 JSON(教學員用 AI 生題庫)、結果頁 canvas 自動產生分享圖卡(可下載)。
4. **demos/index.html** — demo 總覽入口,對應模組編號。

虛構品牌,不用真實客戶名稱。配色與文案走質感路線(LeShePhoto 標準),不可有 AI 樣板感。

## 驗收標準

- 每個 demo 在本機 http server 下:頁面載入無 console error、canvas 特效非透明像素 > 0、互動流程(抽獎 / 答題)可走完。
- 講義每模組含:學完能做什麼 / 步驟 / 給 AI 的 prompt 範本 / 常見坑。
- 全部記錄(研究、ADR、設計、執行日誌)+ 課程 + demo 推上 private repo `yazelin/ai-marketing-pages-course`。

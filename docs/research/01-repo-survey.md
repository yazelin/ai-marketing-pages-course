# 研究記錄 01 — 近兩個月活躍 repo 技術盤點

日期:2026-06-10
方法:`gh repo list yazelin --json pushedAt` 篩選 2026-04-10 之後有 push 的 repo(約 55 個),再對課程主題(教行銷人做 AI / 互動行銷活動網頁)逐一評估相關性,並實際讀取本機 clone 的 README / 結構確認技術細節。

## 高度相關(課程直接取材)

| Repo | 技術 | 對課程的價值 |
|---|---|---|
| web-effects-collector | 純靜態 SPA、90 個特效目錄、tsParticles / Vanta / three.js 本機化、GitHub Pages | 互動特效模組的素材庫與「零 build 直接開」的範本;已驗證過 tsParticles 兩個雷(需 loadAll()、fullScreen 預設 true) |
| emoji-slot-machine | 3x3 emoji 拉霸 → FB 分享影片、GitHub Pages | 行銷小遊戲(抽獎 / 拉霸)的直接原型 |
| ai-tarot-companion | GitHub Pages 前端 + Cloudflare Workers 後端 + D1 + Groq Whisper,全免費 tier | 「頁面即時呼叫 AI」的安全架構範本(API key 藏在 Worker,不放前端) |
| gemini-image-starter | naive prompt → structured prompt 的教學法(Part 1 vs Part 2)、Gemini 生圖 | AI 視覺資產模組整套教學法直接沿用:核心魔法是 prompt 設計 |
| catime | GitHub Actions cron 每小時 AI 生圖自動 commit | 自動化模組:讓活動頁內容自己更新 |
| j303 / LeShePhoto / yazelin-courses | 純 HTML+CSS 單檔行銷頁、零依賴、GitHub Pages 直接 serve | 「AI 一次生成整頁」的成品證據;yazelin-courses 同時是課程頁版型前例 |
| line-sticker-studio / ai-sticker-starter | 一張圖 → AI 生成貼圖 → 打包下載 | AI 產出行銷素材的工作流案例 |
| mori-canvas | Rust 後端部署在 Render、BYO-AI | Render 部署實例(何時需要真後端的對照組) |
| 5 個 CTA starter repos | 「README 教學 + CTA 頁」的課程式 repo 格式 | 課程 repo 的編排格式參考 |

## 相關但不選入主線的技術(記錄排除理由)

- **Rust / Tauri(mori-desktop、mori-ear、agentos 等)**:桌面應用與系統整合,對「行銷人做活動網頁」沒有直接用途;且需要工具鏈安裝,違反受眾「零安裝」原則。列為課程尾聲的「之後可以去哪裡」延伸閱讀。
- **webgl-flow-simulation**:流體 hero 很驚艷,但 WebGL shader 對非工程師除錯成本太高;改由 web-effects-collector 的 Vanta / tsParticles 提供「一行式」等級的替代。
- **fishtool-tw(Astro)**:有 build step,對受眾是額外負擔;課程主線堅持零 build。
- **jaba-ai / linebot 系列**:LINE Bot 是另一個產品形態,不是「網頁」,超出本課範圍。

## 結論

近兩個月的 repo 已涵蓋一條完整的「行銷活動頁」生產線:
AI 生頁(j303 / LeShePhoto 模式)→ AI 生圖(gemini-image-starter)→ 互動特效(web-effects-collector)→ 行銷遊戲(emoji-slot-machine)→ 部署(GitHub Pages / Render / Cloudflare Workers 三種實例)→ 自動化(catime)。課程設計只需把這條線翻譯成行銷人能走的階梯。

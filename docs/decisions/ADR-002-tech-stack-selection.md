# ADR-002 技術選型(從近兩個月 repo 中取材)

日期:2026-06-10 / 狀態:Accepted

## 決策

| 課程能力 | 選用技術 | 取材 repo | 排除的替代方案 |
|---|---|---|---|
| 生成整頁 | AI 對話式 vibe coding → 單檔 HTML+CSS+JS | j303、LeShePhoto、yazelin-courses | Astro / Jekyll(有 build step) |
| 視覺資產 | 結構化 prompt 生圖(Gemini / 任一生圖工具) | gemini-image-starter、nanobanana-py | 教學員架生圖 API(超出受眾) |
| 互動特效 | tsParticles、Vanta(CDN 一行式)、原生 canvas | web-effects-collector | three.js / GLSL 手寫(除錯成本高) |
| 行銷遊戲 | 原生 JS:拉霸、刮刮樂、心理測驗 + canvas 分享卡 | emoji-slot-machine | 遊戲框架(Phaser 等,殺雞用牛刀) |
| 部署 | GitHub Pages 為主線;Vercel / Render / Cloudflare 以決策樹講解 | yazelin.github.io、mori-canvas(Render)、ai-tarot(Workers) | 自架 VPS(維運成本) |
| 即時 AI(進階) | Cloudflare Worker 代理 + 前端 fetch | ai-tarot-companion | 前端直連 AI API(key 外洩) |
| 自動化(進階) | GitHub Actions cron | catime | 自架排程器 |

## 理由

每一項都有「近兩個月內自己跑過、上過線」的 repo 當證據,課程裡可以直接展示真實成品與真實 commit 歷史,不是紙上談兵。零 build / 免費 tier / 單檔優先三原則貫穿(見 ADR-001)。

## 已知雷點(寫進講義,避免學員踩)

- tsParticles v3 bundle 要先 `loadAll()`,且 `fullScreen` 預設 true 會蓋住整頁,要明確關掉。
- 特效是否真的有畫東西,要看 canvas 非透明像素數,不能只看「canvas 元素存在」。
- 手機 in-app browser(LINE / FB / IG)對 sessionStorage 不可靠,需要存狀態時用 localStorage。
- 行銷頁常被從 LINE / FB 點開,OG meta tags 是必修不是選修。

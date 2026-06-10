# Demo 06 製作筆記(對應模組 6)

## 一個 UI,兩種接法

| 模式 | 路徑 | 給誰用 |
|---|---|---|
| A. Worker 代理 | 頁面 → 你的 workers.dev → Groq | 正式活動(key 藏在 Worker Secret) |
| B. BYO key 直連 | 頁面 → Groq(CORS 開放,實測 `access-control-allow-origin: *`) | 學員立即體驗,不用先架 Worker |

B 模式的 key 只存在訪客自己的 localStorage、直連 Groq,頁面原始碼裡沒有任何 key——
所以這個 demo 可以放心放在公開的 GitHub Pages 上。但正式活動不能叫訪客自己貼 key,
請走 A 模式(模組 6 三步驟,`worker.js` 是完整可貼版)。

2026-06-10 起 A 模式預填課程示範 Worker `sanwu-ai-helper.yazelinj303.workers.dev`
(wrangler 部署,GROQ_API_KEY 在 Worker Secret;部署版多了每 IP 每分鐘 8 次 +
每 isolate 每小時 600 次的限流,原始碼在 dev repo `worker-deploy/`),demo 開箱即聊。

## 防呆設計(對應模組 6 的兩道閘門)

- 前端 maxlength 200 + 500 字硬限制;Worker 端同樣有 500 字限制(雙層)。
- system prompt 限定只answer活動相關、不得編造優惠;活動資訊直接寫死在 prompt 裡。
- 錯誤分類提示:沒填網址 / Worker 非 200 / key 401,各給白話指引。

## 驗收

- 不設定就送出 → 顯示「先貼上…」的系統訊息(不會卡死)。
- B 模式貼有效 key → 問「買一送一怎麼算」應答出「較低價那杯招待」;問無關問題應被婉拒。
- F12 Network:A 模式只連 workers.dev;B 模式只連 api.groq.com(Authorization 是你自己貼的 key)。

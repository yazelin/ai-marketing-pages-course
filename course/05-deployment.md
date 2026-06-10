# 模組 5 — 上線:部署決策樹 + GitHub Pages 實作

## 學完能做什麼

把做好的活動頁變成一個真實網址,而且懂得依需求選平台,不會被帳單或休眠嚇到。

## 部署決策樹

從上往下走,停在第一個符合的:

```text
你的頁面需要伺服器隨時運算嗎?
├─ 不用,就是靜態頁(本課 90% 情境:landing、抽獎、測驗)
│   → GitHub Pages(免費、不會產生帳單、repo 即備份)
├─ 需要收表單 / 一點點後端函式(例如名單寫進試算表)
│   → Vercel(git push 即部署,免費函式額度對活動綽綽有餘)
├─ 需要幫「頁面即時呼叫 AI」藏 API key(模組 6)
│   → Cloudflare Workers(免費額度每天十萬次,專門做輕量代理)
└─ 需要常駐後端:資料庫、即時連線、會員系統
    → Render(可跑完整伺服器;注意免費版 15 分鐘沒人用會休眠,
       第一個訪客要等它醒來,正式活動期建議升級或預熱)
```

三個免費 tier 陷阱先講明:**Pages** 只能靜態(沒有後端就是沒有);**Vercel** 免費版有流量上限,爆紅貼文等級的活動要先看額度;**Render** 免費版會休眠。

真實案例對照:本課的 demo 與 web-effects-collector 全在 GitHub Pages;ai-tarot-companion 用 Pages + Workers 組合;mori-canvas 因為要跑完整後端所以在 Render。

## GitHub Pages 手把手

### 1. 建 repo 並上傳

1. 登入 GitHub → New repository → 名稱取 `coffee-opening`(會變成網址的一部分,用英文小寫加連字號)→ Public → Create。
2. 「uploading an existing file」→ 把 `index.html` 和圖片拖進去 → Commit changes。

### 2. 開啟 Pages

Settings → Pages → Source 選 `Deploy from a branch` → Branch 選 `main`、資料夾 `/ (root)` → Save。等一兩分鐘,頁面上方會出現網址:

`https://你的帳號.github.io/coffee-opening/`

### 3. 上線驗收清單

- 無痕視窗開網址(避免快取騙你)。
- 手機實機開一次(不是模擬,真手機)。
- 把網址貼到 LINE 給自己:**分享預覽卡片**有沒有出現你的 OG 標題和圖?沒有的話檢查 `og:image` 是不是寫成相對路徑——OG 圖必須是完整網址(`https://...` 開頭)。(OG / SEO / 給 AI 看的頁面,完整一章在模組 10。)
- 圖片全部有出現(常見錯誤:檔名大小寫不一致,`Hero.JPG` 與 `hero.jpg` 在 GitHub 上是兩個不同檔案)。

### 4. 更新頁面

改版就是重新上傳同名檔案 commit 一次,一兩分鐘後生效。每次 commit 都有紀錄,改壞了隨時可以回去看舊版內容。

### 5. 自訂網域(選配)

活動要用 `event.你的品牌.com`:Settings → Pages → Custom domain 填入網域,再到你的 DNS 商把該子網域 CNAME 指向 `你的帳號.github.io`,等生效後勾 Enforce HTTPS。

## 另外三個分支的最短路徑

走到決策樹其他分支時,第一次部署長這樣(都是免費起步):

**Vercel(收表單 / serverless)**
1. 用 GitHub 帳號登入 vercel.com → Add New → Project → 選你的 GitHub repo → Deploy,一分鐘拿到 `xxx.vercel.app` 網址。
2. 之後 git push 就自動重新部署,跟 Pages 一樣的節奏。
3. 何時選它:需要 `/api/xxx` 這種輕後端(例如表單寫進 Google Sheet)。靜態頁放 Vercel 也行,但 Pages 就夠了。

**Render(常駐後端)**
1. 用 GitHub 帳號登入 render.com → New → Web Service → 選 repo → 它會問啟動指令(這已經是工程師領域,通常是接手別人寫好的後端)。
2. 免費版 15 分鐘沒流量會休眠,第一個訪客要等它醒(約半分鐘)——正式活動期升級付費或接受這件事。
3. 何時選它:資料庫、會員、即時連線。行銷活動頁 99% 用不到;真用到了,這一步建議跟工程師協作。

**Cloudflare Workers(AI 代理)**
完整流程在模組 6;它不是拿來放網頁的,是放「幫頁面跑腿的小程式」。

## 進階捷徑:用 AI agent + gh CLI 一句話部署

上面的網頁點按流程是基本功;如果你已經在用 agent 式 AI(Claude Code / Codex CLI,見模組 8),部署可以變成一句話的事。原理:GitHub 官方有個命令列工具 `gh`,**你授權一次,agent 之後就能代替你操作 GitHub**。

一次性準備(自己做,兩分鐘):

1. 安裝 gh:Windows 用 `winget install GitHub.cli`,Mac 用 `brew install gh`(官網 https://cli.github.com 也有安裝檔)。
2. 授權:終端機輸入 `gh auth login`,選 GitHub.com → HTTPS → Login with a web browser,瀏覽器按確認即完成。

之後在 Claude Code / Codex 裡,部署 prompt 長這樣:

```text
幫我把這個資料夾發佈成 GitHub Pages:
1. 用 gh repo create coffee-opening --public --source=. --remote=origin --push 建 repo 並推上去
2. 用 gh api 啟用 Pages(main branch 根目錄)
3. 等部署完成後,驗證網址回 200,把最終網址給我
```

agent 會自己跑 `git init`、commit、建 repo、開 Pages、輪詢到網站上線,最後丟網址給你——本課這個課程站本身就是這樣發佈的。注意兩件事:**prompt 裡永遠不需要出現任何密碼或 token**(授權存在 gh 自己的設定裡);agent 執行 `gh` 指令前通常會先問你一次,看清楚再放行,特別是 `--public` 這種會把程式碼公開的旗標。

### 四個平台都有官方 CLI,同一套邏輯

「授權一次,agent 代你部署」不是 GitHub 限定——決策樹上每個平台都有官方 CLI:

| 平台 | CLI | 一次性授權 | agent 部署指令 |
|---|---|---|---|
| GitHub Pages | `gh` | `gh auth login` | `gh repo create … --push` + 開 Pages |
| Cloudflare Workers | `wrangler` | `wrangler login` | `wrangler deploy`(見模組 6) |
| Vercel | `vercel` | `vercel login` | `vercel`(預覽)/ `vercel --prod`(正式) |
| Render | `render` | `render login` | 建好服務後 git push 自動部署;CLI 可觸發部署、看 log |

通則三條:授權都是「跑一次 login、瀏覽器按確認」;**key / token 永遠不進對話**;部署這種對外動作,agent 動手前看一眼它要跑的指令再放行。順帶一提,Vercel 甚至有 `vercel agent init` 指令,專門幫 coding agent 在專案裡生一份部署須知——平台們已經在迎接「AI 替你部署」這件事了。

## 常見坑

1. **網址 404**:repo 裡沒有 `index.html`(放在子資料夾裡了),或 Pages 還在建置中。檔案要在 repo 根目錄。
2. **OG 預覽不更新**:LINE / FB 會快取舊預覽。FB 有 Sharing Debugger 可以強制重抓;LINE 只能等或換網址參數。
3. **公開 repo 的心理關**:Pages 免費版 repo 是公開的——本來就會公開上線的活動頁無妨,但優惠碼邏輯等於公開(呼應模組 4 坑 4:高價券別用純前端)。
4. **改了沒生效**:瀏覽器快取。無痕視窗或強制重新整理(Ctrl+Shift+R)再判斷。

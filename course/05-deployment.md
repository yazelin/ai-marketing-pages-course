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
- 把網址貼到 LINE 給自己:**分享預覽卡片**有沒有出現你的 OG 標題和圖?沒有的話檢查 `og:image` 是不是寫成相對路徑——OG 圖必須是完整網址(`https://...` 開頭)。
- 圖片全部有出現(常見錯誤:檔名大小寫不一致,`Hero.JPG` 與 `hero.jpg` 在 GitHub 上是兩個不同檔案)。

### 4. 更新頁面

改版就是重新上傳同名檔案 commit 一次,一兩分鐘後生效。每次 commit 都有紀錄,改壞了隨時可以回去看舊版內容。

### 5. 自訂網域(選配)

活動要用 `event.你的品牌.com`:Settings → Pages → Custom domain 填入網域,再到你的 DNS 商把該子網域 CNAME 指向 `你的帳號.github.io`,等生效後勾 Enforce HTTPS。

## 常見坑

1. **網址 404**:repo 裡沒有 `index.html`(放在子資料夾裡了),或 Pages 還在建置中。檔案要在 repo 根目錄。
2. **OG 預覽不更新**:LINE / FB 會快取舊預覽。FB 有 Sharing Debugger 可以強制重抓;LINE 只能等或換網址參數。
3. **公開 repo 的心理關**:Pages 免費版 repo 是公開的——本來就會公開上線的活動頁無妨,但優惠碼邏輯等於公開(呼應模組 4 坑 4:高價券別用純前端)。
4. **改了沒生效**:瀏覽器快取。無痕視窗或強制重新整理(Ctrl+Shift+R)再判斷。

# 模組 9 — 收 email 名單:行銷人最該先做的一件事

## 為什麼這章最實用

社群觸及是租來的(平台改演算法,你的貼文就沒人看);**email 名單是你自己的**。一個會持續長大的名單,是行銷人手上最保值的資產。這章教你做一個會員/開幕通知報名頁,而且名單是**真的存起來、看得到、匯得出**——不是填完就消失。

## 學完能做什麼

做出一個報名頁(收 email + 稱呼),後端把名單存進資料庫,再做一個只有你進得去的後台看名單、一鍵匯出 CSV(就能丟進 email 工具群發)。全部免費 tier。

## 兩條路:先選你的難度

| | A. 不部署任何東西 | B. 自己的 Worker + 資料庫 |
|---|---|---|
| 做法 | Google 表單 / Formspree / Tally 等現成服務 | Cloudflare Worker + D1 資料庫(本章主線) |
| 名單存哪 | 在那個服務的後台 / Google Sheet | 你自己的資料庫,完全掌控 |
| 適合 | 只想快、量不大、不介意掛別人服務 | 要客製報名頁外觀、名單要自己擁有、之後要接其他系統 |
| 成本 | 免費(有筆數/功能上限) | 免費 tier(D1 每天五百萬次讀寫,活動綽綽有餘) |

**先說 A,因為它可能就夠你用了。**

## 路線 A:零部署,把表單塞進你的頁面

1. **Google 表單**:建一個表單(email + 稱呼)→ 取得連結 → 在你的活動頁放一顆「立即報名」按鈕連過去。名單自動進 Google Sheet,Sheet 就是你的後台,還能直接「下載成 CSV」。最省事。
2. **Formspree / Tally / Typeform**:想讓報名框長在自己頁面裡(不跳轉),這類服務給你一段 form 程式碼貼上即可,送出的資料進它們的後台。

A 路線的代價:報名框外觀受限於服務、名單放在別人家、量大或要進階功能要付費。對多數小活動,這完全夠。

## 路線 B:自己的報名後端(本章主線)

當你想要「報名頁完全照自己的設計、名單百分百自己擁有、之後能接 AI 或其他系統」,就走這條。架構是模組 6 的延伸——多了一個資料庫:

```text
報名頁(GitHub Pages)──POST email──> Worker ──寫入──> D1 資料庫
                                        ↑
你的後台頁 ──GET ?token=管理密碼──────┘ ──回傳名單──> 看名單 / 匯 CSV
```

三個零件:
- **報名頁**:純前端,把 email 用 fetch POST 給 Worker。
- **Worker**:驗證 email、擋機器人、限流、去重,寫進 D1;另開一個帶密碼的讀取入口給後台。
- **D1**:Cloudflare 的免費 SQL 資料庫,名單就存這。

### 給 AI 的 prompt(照模組 8 的四層結構 + agent 驗收清單)

```text
做一個「開幕通知報名」的 Cloudflare Worker(worker.js)+ D1:
1. D1 一張表 signups:id、email(唯一)、name、created_at、ip
2. POST 收 {email, name, company}:
   - company 是 honeypot,有值就當機器人,假裝成功但不寫入
   - email 格式驗證、轉小寫;每 IP 每分鐘最多 5 次
   - email 重複(UNIQUE 衝突)當「已報名」處理,不報錯也不洩漏
3. GET /list?token=xxx:token 比對 Secret ADMIN_TOKEN,對了才回名單 JSON
4. 全程加 CORS
做完用 curl 測:正常報名、重複報名、honeypot、爛 email、錯 token,
五種都符合預期才算完成。
```

### 部署(wrangler,跟模組 6 同一套)

```bash
wrangler d1 create sanwu-signups            # 建資料庫,記下印出的 database_id
# 把 database_id 填進 wrangler.toml 的 [[d1_databases]]
wrangler d1 execute sanwu-signups --remote --file ./schema.sql   # 建表
wrangler deploy                             # 部署 Worker
wrangler secret put ADMIN_TOKEN             # 設後台密碼(自己想一組長字串)
```

`ADMIN_TOKEN` 是你後台的鑰匙,藏在 Worker 的 Secret 裡,永遠不寫進任何網頁。

### 後台頁

一個 `admin.html`:輸入密碼 → 帶著密碼打 `GET /list` → 把名單畫成表格 → 「匯出 CSV」按鈕(前端把 JSON 轉 CSV 下載)。密碼記在你瀏覽器的 localStorage,下次免再輸。CSV 拿到後就能匯進任何 email 群發工具。

## 後台登入怎麼防護:兩種做法,從基本到實名

後台等於你整份名單的入口,這道門怎麼鎖很重要。本章給兩層,按名單的敏感度選。

### 做法一:token 走 Authorization 標頭(基本功,本章已採用)

最先要做對的一件事:**密碼別放進網址**。`GET /list?token=密碼` 看起來會動,但網址會被瀏覽器歷史、CDN 日誌、甚至 referer 標頭記下來——等於把鑰匙到處留印子。正確做法是放進 HTTP 的 `Authorization` 標頭:

```js
// 後台頁:把密碼放標頭,不放網址
fetch(API + "/list", { headers: { Authorization: "Bearer " + token } });
```

```js
// Worker:從標頭讀、跟 Secret 裡的 ADMIN_TOKEN 比對
const auth = request.headers.get("Authorization") || "";
const token = auth.startsWith("Bearer ") ? auth.slice(7) : "";
if (token !== env.ADMIN_TOKEN) return json({ error: "unauthorized" }, 401);
```

這叫 **token gate**:一把共享鑰匙,誰有誰能看。對「活動報名名單、自己一個人看」這種情境**夠用**。它的本質限制要心裡有數:只有一把鑰匙、不會自己過期、外洩了要手動換(`wrangler secret put ADMIN_TOKEN` 設一組新的,然後重新發給該知道的人)。

### 做法二:Cloudflare Access 實名門禁(進階,放真實客戶資料才需要)

當名單裡是真實客戶個資、或要給團隊多人看,一把共享鑰匙就不夠了。Cloudflare Access 把「鑰匙」換成「實名門禁」:每個人各自用自己的 email(收一次性碼)或 Google 帳號登入,你指定誰能進、誰要踢出即時生效、而且每次存取都有紀錄可查。

**但有個前提一定要先講清楚**:Cloudflare Access 只能保護「**在 Cloudflare 經手的域名底下**」的頁面。本章的 `admin.html` 放在 GitHub Pages(`yazelin.github.io`),那不是你的 Cloudflare 域名,**Access 罩不住它**。所以要用 Access,得先把後台搬到 Cloudflare,兩步:

1. **把後台移上 Cloudflare**:讓 Worker 自己吐出後台 HTML(加一個 `GET /` 回傳 admin 頁),或用 Cloudflare Pages 放後台。
2. **掛一個 DNS 託管在 Cloudflare 的自訂網域**給它(例如 `admin.你的品牌.com`)——這是 Access 能介入的條件。

接著在 Cloudflare 後台設定(Zero Trust 是免費 tier 就有的產品):

1. Cloudflare Dashboard → **Zero Trust → Access → Applications → Add an application → Self-hosted**
2. 填你後台的那個 Cloudflare 網域
3. 加一條 **Policy**:Action 選 `Allow`,Include 選 `Emails`,填你自己的 email(要給團隊就填多個或用 Email domain)
4. 登入方式選 **Email OTP**(寄一次性碼,零設定)或接 Google / Microsoft
5. 存檔。之後任何人打開那個後台網址,都會先被 Cloudflare 攔一道登入,只有你授權的 email 收得到碼、進得來

這道門擋在最前面,後面的 token gate 可留可拿。

### 怎麼選

| | 做法一:token 標頭 | 做法二:Cloudflare Access |
|---|---|---|
| 門檻 | 一把共享密碼 | 每個人實名登入 |
| 適合 | 活動報名名單、自己看 | 真實客戶個資、多人、要稽核 |
| 成本 | 零,本章已內建 | 後台得搬上 Cloudflare + 一個自訂網域 |
| 踢人 | 換 token,全員重給一次 | 後台移除某 email,即時生效 |
| 有沒有存取紀錄 | 沒有 | 有,每次登入都記錄 |

一句話:**自己看的活動名單,做法一就好;要對客戶負責的名單,升級做法二。** 別把真實客戶個資長期只靠一把共享 token 守著。

## 名單拿到了,然後呢

收名單只是第一步,真正的行銷是「寄信給他們」。CSV 匯出後可以:
- 匯進 **MailerLite / Mailchimp**(免費 tier 都能群發數百到數千封)做開幕通知。
- 或在 Worker 端接 email 寄送 API(Resend、Postmark 等),報名當下就自動寄一封歡迎信——這是進階,本章先做到「收得到、看得到、匯得出」。

## 常見坑

1. **裸表單沒擋機器人**:公開的 email 收集端點一定會被灌垃圾。本章三道防線:honeypot 隱形欄位、每 IP 限流、email 格式驗證。要更強可加 Cloudflare Turnstile(免費人機驗證)。
2. **去重沒做**:同一人按三次送出,名單就三筆。靠資料庫的 UNIQUE 約束擋,而且回應不要洩漏「這個 email 在不在名單」(隱私)。
3. **管理密碼放進前端 / 放進網址**:後台密碼一旦寫進 admin.html 就等於公開;放進網址 `?token=` 則會被瀏覽器歷史與 CDN 日誌記下。密碼只存在 Worker 的 Secret,前端是「使用者輸入 → 放 Authorization 標頭傳給 Worker 比對」(見上面「後台登入怎麼防護」)。
4. **個資責任**:收了 email 就有保管責任。報名頁寫清楚用途與退訂方式;不需要的個資不要收;名單別外流。
5. **沒有退訂機制**:正式營運的名單要能退訂(法規與商譽)。本章 demo 未做,正式上線前補上。

## 對照成品

- 報名頁:`demos/09-email-signup/index.html`(已接真的 Worker + D1,送出會真的進名單)
- 後台:`demos/09-email-signup/admin.html`(輸入管理密碼看名單、匯 CSV)
- Worker + schema:dev repo 的 `worker-deploy/email/`

報名頁送一筆,再開後台輸入密碼,就會看到自己剛剛那筆——完整的「收集 → 儲存 → 後台」一條龍。

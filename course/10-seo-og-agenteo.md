# 模組 10 — 被看見:SEO、社群分享卡(OG)、給 AI 看的頁面(AEO / GEO)

## 為什麼這章

做得再好的活動頁,**沒人看見等於沒做**。頁面被看見有三條路,這章一次補齊:

1. 有人 Google 搜尋 → **SEO**(搜尋引擎優化)
2. 有人把連結貼到 LINE / FB / IG → **OG**(社群分享卡)
3. 有人問 ChatGPT / Claude / Perplexity「OO 有什麼活動」→ **AEO / GEO**(讓 AI 找得到、引用得到你)

第三條是 2026 越來越重要的新管道:很多人已經不 Google 了,直接問 AI。你的頁面要讓 AI 講得出來。

> **名詞釐清**:這條線業界有兩個常見說法,目標相近、常被合稱:
> - **AEO(Answer Engine Optimization,答案引擎優化)**:讓內容被 AI 的直接答案、精選摘要、語音助理引用。
> - **GEO(Generative Engine Optimization,生成引擎優化)**:讓 ChatGPT / Claude / Perplexity 這類大模型在生成回答時引用你。
>
> 兩者吃的訊號高度重疊(結構化資料、清楚文字、可被爬),所以下面的做法對兩者都有用。(沒有「Agent EO」這個正式術語——若看到,當它是 AEO/GEO 的口語說法即可。)

## 一、SEO 基本功(給搜尋引擎)

- `<title>`:每頁不同,放關鍵字 + 品牌名
- `<meta name="description">`:一兩句,是搜尋結果裡的摘要,寫得讓人想點
- 語意化 HTML:一頁一個 `<h1>`、標題層級清楚
- `sitemap.xml`:列出你所有公開頁,丟進 Google Search Console
- `robots.txt`:允許爬、指向 sitemap;不想被收錄的頁(後台、感謝頁)用 `<meta name="robots" content="noindex">` 擋

## 二、社群分享卡 OG(給 LINE / FB / IG)

活動頁最常被從 LINE / FB 點開,分享出去長什麼樣,由 OG tags 決定:

```html
<meta property="og:title" content="山霧咖啡 開幕週 — 整週買一送一">
<meta property="og:description" content="6/20 至 6/26,霧還沒散,咖啡先香了。">
<meta property="og:image" content="https://你的網域/og.jpg">   <!-- 完整網址! -->
<meta property="og:url" content="https://你的網域/活動頁/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://你的網域/og.jpg">
```

鐵則:

- og:image 必須是**完整 https 網址**,不能相對路徑(LINE / FB 抓不到)
- 圖 **1200x630**、壓到 200KB 內
- 別留 `example.com` 假網址——本課第一版 demo 就犯過這個,分享出來是破圖(這就是為什麼有了這一章)
- 改了 OG,平台會快取舊的;FB 有 **Sharing Debugger** 可強制重抓:https://developers.facebook.com/tools/debug/ (貼網址 → 按 Scrape Again)

**怎麼做 OG 圖,不用設計軟體**:寫一個 1200x630 的 HTML(品牌底圖 + 標題字),用瀏覽器截圖即可。本課的兩張 OG 圖就是 headless 瀏覽器截出來的,中文字靠瀏覽器字體,品質穩定。

## 三、AEO / GEO:給 AI 看的頁面(新管道)

越來越多人問 AI 而不是 Google。要讓 AI 正確講出你的活動,給它讀得懂的訊號:

### 1. 結構化資料 JSON-LD(schema.org)

用機器讀得懂的格式,明白告訴 AI 與搜尋引擎「這頁是什麼」。活動頁用 `Event`,課程用 `Course`,實體店用 `LocalBusiness`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "山霧咖啡 開幕週",
  "startDate": "2026-06-20T08:00:00+08:00",
  "endDate": "2026-06-26T18:00:00+08:00",
  "location": { "@type": "Place", "name": "山霧咖啡", "address": "霧峰山路 36 號" },
  "offers": { "@type": "Offer", "description": "全品項買一送一" }
}
</script>
```

AI 與 Google 都吃這個。Google 會拿它做「複合式搜尋結果」(rich result),AI 會用它精準回答你的活動何時、在哪、有什麼優惠。

### 2. llms.txt

放在網站根目錄的純文字說明書,**專門寫給 LLM**:一句話講你是誰 + 重要頁面連結。AI 抓你的站時先看它。格式很簡單:一個標題、一段 `>` 摘要、幾組分節連結。

### 3. 把重要資訊用「文字」寫出來

AI 讀的是文字。日期、地點、優惠這些關鍵資訊,一定要用**文字**寫在頁面上,別只放在圖片裡——圖裡的字 AI(和搜尋引擎)讀不到。這也呼應模組 2:圖負責氛圍,字用網頁層。

## 驗收

- **SEO**:Google 搜「site:你的網址」看有沒有被收錄;Search Console 提交 sitemap
- **OG**:把網址貼到 LINE 給自己,看預覽卡有沒有出現你的標題和圖;FB Sharing Debugger(https://developers.facebook.com/tools/debug/ )看平台抓到什麼、按 Scrape Again 強制重抓
- **AEO / GEO**:把網址貼給 ChatGPT / Claude:「這個頁面在講什麼活動?」,看它講得對不對、講不講得出日期優惠;用 Google Rich Results Test(https://search.google.com/test/rich-results )驗 JSON-LD 合不合法
- **線上 AI 可見性檢查工具**:有不少免費工具一鍵掃描你的網址,檢查 robots.txt / llms.txt / 結構化資料 / AI 爬蟲存取是否就緒,給一個「AI 健康度」評分。可用的有:
  - CrawlerCheck(crawlercheck.com)— 專查 robots.txt / meta robots / 各家 AI 爬蟲 user-agent 是否被擋
  - ClayHog GEO Audit、AI Rank Lab、Web Aloha、Ayzeo — 抓首頁 + robots/llms.txt + schema,綜合評 AEO/GEO 就緒度
  - 用法:貼上你上線的網址,看它標紅的項目逐條補。(這些是第三方服務,送出等於把你的網址給它們——對公開的活動頁無妨。)
- **後台別外洩**:admin / 感謝頁加 noindex、不進 sitemap

## 常見坑

1. **og:image 相對路徑或假網址**:分享破圖。必須完整 https 網址。
2. **改了 OG 沒重抓**:平台快取舊的,用 Sharing Debugger(https://developers.facebook.com/tools/debug/ )強制重抓。
3. **JSON-LD 跟頁面內容對不上**:亂填會被搜尋引擎懲罰。schema 寫的要跟頁面真的一致。
4. **重要資訊只放在圖裡**:AI 與搜尋引擎讀不到。日期、地點、優惠用文字也寫一遍。
5. **後台 / 感謝頁被索引**:加 `<meta name="robots" content="noindex">`。
6. **專案頁的 robots / llms 在子路徑、不在網域根**:GitHub Pages 專案頁(`github.io/你的repo/`)的 `robots.txt`、`llms.txt` 只能放子路徑,爬蟲讀的是網域根。要完整 SEO,得用自訂網域(呼應模組 5)。

## 真實案例:為什麼「專案頁」AEO 分數低,根域才是解法

把網址丟進 AI 可見性檢測工具(如 isitagentready.com),如果你的站是 GitHub Pages **專案頁**(`帳號.github.io/repo名/`),分數常常很低——但問題往往不是你沒做優化,是工具掃的是**網域根** `帳號.github.io/`,不是你專案的子路徑。

這門課自己就踩到這個,實測數據(同一個帳號,根域 vs 課程站子路徑):

| 訊號 | 網域根(檢測工具掃的) | 專案子路徑(你做了優化的) |
|---|---|---|
| llms.txt | 404 沒有 | 200 有 |
| 首頁 JSON-LD | 0 個 | 有 |
| meta description | 空 | 有 |

工具掃根域,看到的是你的 Profile / 部落格首頁,沒有你在子專案做的那一套——分數當然低。三條解法:

1. **自訂網域**:把專案掛上自己的網域,優化就在網域根,工具掃得到。最徹底(呼應模組 5)。
2. **把根域站(個人 Profile / 部落格)的 AEO 做好**,並在它的 `llms.txt` 列出你所有專案——讓 AI 從根域一次發現你全部的子站。這是**不買網域時的最佳解**。
3. **接受專案頁的限制**:靠站內 meta(每頁完整 OG / description / JSON-LD)讓「個別頁面」被 AI 讀懂。本課 demo 已驗證:單頁貼給 AI,它讀得懂是什麼活動——即使整站的根域分數不漂亮。

教訓:**AEO 檢測分數要看「它掃的是哪個 URL」**。專案頁拿低分,先確認工具是不是只掃了網域根,再決定要不要為它自訂網域。

## 對照成品

本課**整站就是這一章的案例**:

- 每個 demo 頁有完整 OG tags + JSON-LD(活動頁 `Event`、課程站 `Course`)
- 兩張真實 OG 圖(headless 瀏覽器截的,不是 example.com 占位)
- 站點有 `sitemap.xml` 與 `llms.txt`(`/ai-marketing-pages-course/llms.txt`)
- 後台頁 `admin.html` / `admin-google.html` 都 noindex

把任一 demo 網址貼給 AI 問「這在講什麼」,它應該答得出是山霧咖啡的什麼活動——那就是 AEO / GEO 生效了。

## 做完了?用「行銷頁健檢器」自檢

把這一章(以及整門課:OG、SEO、CTA、圖片速度、體質、追蹤)該檢查的事做成了一個免費工具——**行銷頁健檢器**:

> https://yazelin.github.io/marketing-page-checker/

貼上你做好的活動頁網址,30 秒給你一個分數 + 各面向的綠/黃/紅 + 一份「先修這幾個」的白話清單(每項還附可直接複製貼給 AI 的修正 prompt)。**做完你的頁就貼進去自檢,照它的紅燈逐條修。**

而且這個健檢器本身就是用本課教的東西做的:**GitHub Pages 前端 + Cloudflare Worker 後端**(模組 5、6),Worker 抓你的頁、解析、評分。它是「學 → 做 → 自檢」這個閉環的最後一塊,也是 Worker 架構的真實範例。

# 模組 10 — 被看見:SEO、社群分享卡(OG)、給 AI 看的頁面(Agent EO)

## 為什麼這章

做得再好的活動頁,**沒人看見等於沒做**。頁面被看見有三條路,這章一次補齊:

1. 有人 Google 搜尋 → **SEO**(搜尋引擎優化)
2. 有人把連結貼到 LINE / FB / IG → **OG**(社群分享卡)
3. 有人問 ChatGPT / Claude / Perplexity「OO 有什麼活動」→ **Agent EO**(給 AI 看的頁面)

第三條是 2026 越來越重要的新管道:很多人已經不 Google 了,直接問 AI。你的頁面要讓 AI 講得出來。

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
- 改了 OG,平台會快取舊的;FB 有 **Sharing Debugger** 可強制重抓

**怎麼做 OG 圖,不用設計軟體**:寫一個 1200x630 的 HTML(品牌底圖 + 標題字),用瀏覽器截圖即可。本課的兩張 OG 圖就是 headless 瀏覽器截出來的,中文字靠瀏覽器字體,品質穩定。

## 三、Agent EO:給 AI 看的頁面(新管道)

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
- **OG**:把網址貼到 LINE 給自己,看預覽卡有沒有出現你的標題和圖;FB Sharing Debugger 看平台抓到什麼
- **Agent EO**:把網址貼給 ChatGPT / Claude:「這個頁面在講什麼活動?」,看它講得對不對、講不講得出日期優惠;用 Google Rich Results Test 驗 JSON-LD 合不合法
- **後台別外洩**:admin / 感謝頁加 noindex、不進 sitemap

## 常見坑

1. **og:image 相對路徑或假網址**:分享破圖。必須完整 https 網址。
2. **改了 OG 沒重抓**:平台快取舊的,用 Sharing Debugger 強制重抓。
3. **JSON-LD 跟頁面內容對不上**:亂填會被搜尋引擎懲罰。schema 寫的要跟頁面真的一致。
4. **重要資訊只放在圖裡**:AI 與搜尋引擎讀不到。日期、地點、優惠用文字也寫一遍。
5. **後台 / 感謝頁被索引**:加 `<meta name="robots" content="noindex">`。
6. **專案頁的 robots / llms 在子路徑、不在網域根**:GitHub Pages 專案頁(`github.io/你的repo/`)的 `robots.txt`、`llms.txt` 只能放子路徑,爬蟲讀的是網域根。要完整 SEO,得用自訂網域(呼應模組 5)。

## 對照成品

本課**整站就是這一章的案例**:

- 每個 demo 頁有完整 OG tags + JSON-LD(活動頁 `Event`、課程站 `Course`)
- 兩張真實 OG 圖(headless 瀏覽器截的,不是 example.com 占位)
- 站點有 `sitemap.xml` 與 `llms.txt`(`/ai-marketing-pages-course/llms.txt`)
- 後台頁 `admin.html` / `admin-google.html` 都 noindex

把任一 demo 網址貼給 AI 問「這在講什麼」,它應該答得出是山霧咖啡的什麼活動——那就是 Agent EO 生效了。

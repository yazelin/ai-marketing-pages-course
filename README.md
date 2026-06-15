# AI 互動行銷頁實作課

> 分享目前規劃的「AI & 行銷人」主題 AI Coding 課程內容

不寫程式,做出會動、會玩、能上線的活動網頁。
給行銷人的 AI 實作課。

課程方法論:**甲方思維** — AI 時代你升格成甲方,AI 是重做不加價的乙方;用「AI 發包法」三步走完整門課:開規格(模組 S)、下發包(模組 1–7)、做驗收(模組 8)。

- 課程首頁 : https://yazelin.github.io/ai-marketing-pages-course/ 
- 線上課程簡報 : https://yazelin.github.io/ai-marketing-pages-course/slides/ 
- 下載課程講義 PDF : https://yazelin.github.io/ai-marketing-pages-course/handout.pdf 
- 實作 Demo 總覽 : https://yazelin.github.io/ai-marketing-pages-course/demos/ 
- 行銷頁健檢器(做完自檢用) : https://yazelin.github.io/marketing-page-checker/ 

## 內容

```
index.html      課程站首頁
slides/         上課簡報(14 份,瀏覽器直接放映,← → 翻頁)
handout.pdf     講義 PDF(A4,模組 0-11 + 模組 S)
course/         全部模組講義 markdown(模組 0-11 + 模組 S 甲方思維)
demos/          山霧咖啡 demo 六件套,全部零 build
  01-landing/      活動 landing(AI 生成 hero + 蒸氣 + 粒子 + 倒數)
  02-lucky-draw/   拉霸抽獎(機率表 + 優惠碼 + 防重抽)
  03-ai-quiz/      心理測驗(加權計分 + canvas 分享圖卡)
  06-ai-helper/    AI 活動小幫手(Worker 代理 / BYO key,附 worker.js)
  07-auto-update/  自動更新頁(本 repo 的 Actions 排程真的在跑)
  09-email-signup/ 收 email 名單(報名頁 + Worker + D1 + 後台)
```

## 延伸:行銷頁健檢器

做完你的活動頁,貼網址到 [行銷頁健檢器](https://yazelin.github.io/marketing-page-checker/) 自檢——OG/SEO/CTA/速度/體質/追蹤給分數與白話修法。它本身就是用本課教的 GitHub Pages + Cloudflare Worker 架構做的,是「學 → 做 → 自檢」閉環的最後一塊。

## 在自己電腦上玩

```bash
git clone https://github.com/yazelin/ai-marketing-pages-course.git
# 雙擊 demos/index.html 即可;或:
python3 -m http.server 8000   # 開 http://localhost:8000
```

所有 demo 零依賴、可離線開啟。SANWU COFFEE 山霧咖啡為課程虛構品牌。

## 關於

課程:林亞澤 yazelin。本 repo 為發佈版教材;研究與開發記錄在另一個私有 repo 維護。

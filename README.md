# AI 互動行銷頁實作課 — 公開教材

不寫程式,做出會動、會玩、能上線的活動網頁。給行銷人的 AI 實作課。

- 課程站:https://yazelin.github.io/ai-marketing-pages-course/ 
- 上課簡報:https://yazelin.github.io/ai-marketing-pages-course/slides/ 
- 講義 PDF:https://yazelin.github.io/ai-marketing-pages-course/handout.pdf 
- Demo 總覽:https://yazelin.github.io/ai-marketing-pages-course/demos/ 

## 內容

```
index.html      課程站首頁
slides/         上課簡報(10 份,瀏覽器直接放映,← → 翻頁)
handout.pdf     講義 PDF(26 頁 A4)
course/         全部模組講義 markdown(模組 0-8)
demos/          山霧咖啡五件套 demo,全部零 build
  01-landing/      活動 landing(AI 生成 hero + 蒸氣 + 粒子 + 倒數)
  02-lucky-draw/   拉霸抽獎(機率表 + 優惠碼 + 防重抽)
  03-ai-quiz/      心理測驗(加權計分 + canvas 分享圖卡)
  06-ai-helper/    AI 活動小幫手(Worker 代理 / BYO key,附 worker.js)
  07-auto-update/  自動更新頁(本 repo 的 Actions 每天台北 08:00 真的在跑)
```

## 在自己電腦上玩

```bash
git clone https://github.com/yazelin/ai-marketing-pages-course.git
# 雙擊 demos/index.html 即可;或:
python3 -m http.server 8000   # 開 http://localhost:8000
```

所有 demo 零依賴、可離線開啟。SANWU COFFEE 山霧咖啡為課程虛構品牌。

## 關於

課程:林亞澤 yazelin。本 repo 為發佈版教材;研究與開發記錄在另一個私有 repo 維護。

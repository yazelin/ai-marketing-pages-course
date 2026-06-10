# ADR-001 受眾與課程範圍

日期:2026-06-10 / 狀態:Accepted

## 決策

受眾定為「會用 ChatGPT / Claude / Gemini 聊天,但不會寫程式的行銷人」。課程承諾:上完課能獨立做出一個有 AI 視覺、有互動特效、有抽獎遊戲的行銷活動網頁,並自己上線到免費平台。

範圍刻意排除:JS 框架(React / Vue)、build 工具、後端程式撰寫、資料庫設計。進階模組(即時 AI 對話、自動化)以「照著抄能動」為標準,不要求理解原理。

## 理由

- 近兩個月 repo 裡最成功的行銷頁(j303、LeShePhoto、yazelin-courses)全是零依賴純 HTML,證明這條路線足以做出有質感的成品。
- 受眾的核心資產是「會描述需求」,所以課程主軸放在 prompt 設計(沿用 gemini-image-starter 的 naive → structured 教學法),而不是教語法。
- 每多一個安裝步驟就流失一批學員;零 build、瀏覽器直接開,是完課率的關鍵。

## 後果

- 所有 demo 必須雙擊 index.html 就能跑(或一行 python http server)。
- 第三方特效函式庫採 CDN 或單檔內嵌,不用 npm。
- 即時 AI 模組只能教「免費代理」架構(Cloudflare Worker),不能教學員把 API key 放進前端。

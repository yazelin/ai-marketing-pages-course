# ADR-003 部署平台的教法

日期:2026-06-10 / 狀態:Accepted

## 決策

不教「哪個平台最好」,教一棵決策樹,並以 GitHub Pages 為唯一手把手實作的主線:

1. 純靜態頁(本課 90% 情境)→ **GitHub Pages**:免費、無流量帳單意外、跟版本控制同一個地方。
2. 需要表單收名單 / 簡單 serverless → **Vercel**:git push 即部署,函式免費額度夠活動用。
3. 需要常駐後端(資料庫、長連線)→ **Render**:mori-canvas 實例,免費 tier 會休眠要知道。
4. 需要幫 AI API 藏 key 的輕量代理 → **Cloudflare Workers**:ai-tarot-companion 實例,免費額度極大。

## 理由

行銷人最常見的失敗不是「選錯平台」而是「被平台帳單或休眠嚇到」。決策樹把每個平台的免費 tier 陷阱講明(Render 休眠、Vercel 流量上限、Pages 只能靜態),學員按需求走分支即可。GitHub Pages 作主線是因為課程成品(單檔靜態頁)天然契合,且 repo 即作品集。

## 後果

- 課程模組 5 只實作 GitHub Pages(含自訂網域 CNAME 一節)。
- Vercel / Render / Workers 各附一頁「什麼時候才需要我 + 第一次部署的最短路徑」,不展開成完整實作。

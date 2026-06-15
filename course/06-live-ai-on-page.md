# 模組 6(進階)— 頁面即時呼叫 AI

## 學完能做什麼

讓活動頁「現場」跟 AI 互動:AI 抽籤解語、AI 客製祝福文、AI 回答活動 QA。標準是「照著抄能動」,不要求理解每一行。

## 先講清楚:為什麼不能把 API key 放進網頁

前面所有模組的 AI 都是「製作期」用的(AI 幫你做頁面)。本模組是「使用期」AI(訪客跟 AI 互動),這需要呼叫 AI API,而 API key 等於你的信用卡——網頁的程式碼任何人按 F12 都看得到,**key 放前端 = 把信用卡貼在店門口**。

解法:中間加一個免費的「代理」(Cloudflare Worker)。網頁呼叫代理、代理拿著藏好的 key 呼叫 AI、把答案傳回來。真實案例:ai-tarot-companion(https://yazelin.github.io/ai-tarot-companion/ )整站就是這個架構,前端 GitHub Pages、代理 Cloudflare Workers,全部免費 tier。

```text
訪客瀏覽器 ──> Cloudflare Worker(key 藏在這)──> AI API
   GitHub Pages          免費 10 萬次/天
```

## 照著抄:三步驟

### 1. 建 Worker

註冊 Cloudflare(免費)→ Workers & Pages → Create Worker → 把下面整段貼進去取代預設程式碼:

```js
export default {
  async fetch(request, env) {
    const cors = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };
    if (request.method === "OPTIONS") return new Response(null, { headers: cors });
    if (request.method !== "POST")
      return new Response("POST only", { status: 405, headers: cors });

    const { message } = await request.json();
    if (!message || message.length > 500)
      return new Response(JSON.stringify({ error: "訊息空白或太長" }),
        { status: 400, headers: { ...cors, "Content-Type": "application/json" } });

    const r = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${env.GROQ_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: "llama-3.3-70b-versatile",
        max_tokens: 300,
        messages: [
          { role: "system", content: "你是山霧咖啡的活動小幫手,用繁體中文、兩三句話內溫暖回答。只回答咖啡與本次開幕活動相關問題,其他一律婉拒。" },
          { role: "user", content: message },
        ],
      }),
    });
    const data = await r.json();
    const reply = data.choices?.[0]?.message?.content ?? "我恍神了,再問一次好嗎?";
    return new Response(JSON.stringify({ reply }),
      { headers: { ...cors, "Content-Type": "application/json" } });
  },
};
```

### 2. 藏 key

申請一把免費的 Groq API key(https://console.groq.com ,免費額度對活動互動很夠)。回到 Worker → Settings → Variables and Secrets → 新增 Secret,名稱 `GROQ_API_KEY`,值貼上你的 key。**key 只存在這裡,永遠不出現在網頁程式碼。**

### 3. 網頁端接上

把 Worker 網址(形如 `https://xxx.你的帳號.workers.dev` )交給 AI:

```text
在我的活動頁加一個「問 AI 小幫手」對話框:
輸入框 + 送出鈕,送出時 POST 到 https://xxx.workers.dev ,
body 是 {"message": 使用者輸入},回應的 JSON 裡 reply 欄位顯示成對話泡泡。
等待時顯示打字中動畫;錯誤時顯示「小幫手忙線中」。風格沿用本頁配色。
```

## 驗收

- 自己問三題活動相關問題,回答合理。
- 問一題無關問題(例如「幫我寫作業」),確認 system prompt 有婉拒。
- 按 F12 → Network 看請求:確認瀏覽器只連 workers.dev,**看不到任何 API key**。

## 常見坑

1. **CORS 錯誤**(Console 紅字含 "CORS"):上面範本已含 CORS 處理,通常是你改壞了 headers 區塊,整段還原即可。
2. **沒設長度限制與題目範圍**:會被當免費 ChatGPT 玩,額度被吸乾。範本裡 500 字限制與 system prompt 範圍限制就是在防這個。
3. **把 key 貼進前端 prompt**:給 AI 組頁面時,prompt 裡只能出現 Worker 網址,不能出現 Groq key。
4. **想要更高品質的回答**:把 Worker 裡的 Groq 換成其他供應商(Claude、OpenAI)只需改 fetch 那段的網址、模型名與 key,架構完全相同。

## 進階捷徑:wrangler CLI(配 AI agent 用)

上面三步驟是網頁點按路線,人人能走。如果你已經在用 Claude Code / Codex(模組 8 的 agent 式),Cloudflare 也有官方 CLI 叫 **wrangler**,跟模組 5 的 gh 同一個邏輯:**授權一次,agent 之後代你部署**。

1. 一次性準備:`npm install -g wrangler` → `wrangler login`(瀏覽器按確認)。
2. 之後給 agent 的 prompt:

```text
幫我把這份 worker.js 部署成 Cloudflare Worker:
1. 建 wrangler.toml(名稱 my-event-ai,main 指向 worker.js)
2. wrangler deploy,把網址給我
3. 我會自己跑 wrangler secret put GROQ_API_KEY 貼 key
   (key 不進對話,跟模組 8 的紀律一致)
4. 部署完用 curl 測一題活動問題、一題無關問題,確認範圍限制有效
```

本課的示範 Worker 就是這樣部署的。秘訣同模組 8:**驗收清單寫進指令**(第 4 點),agent 測完才交。

## 動手做

**任務**:照本章三步驟建一個 Cloudflare Worker AI 代理,在你的頁面加一個「問 AI」對話框。
**預期成果**:問活動相關問題會得到合理回答;F12 → Network 翻過每個請求,看不到任何 API key。
**卡關怎麼辦**:Console 出現含 CORS 的紅字,把 Worker 的 headers 區塊整段還原成範本。

## 對照成品

`demos/06-ai-helper/` — 完整的「問山霧」聊天頁,**開箱即聊**:A 模式已預填課程示範 Worker(真的在 Cloudflare 上跑,key 在它的 Secret 裡,含每分鐘 8 次限流),也可換成你自己的;B 模式貼自己的 Groq key 直連體驗(key 只存你的瀏覽器)。示範 Worker 的部署版原始碼(多了限流)在 dev repo 的 `worker-deploy/`。

真實世界版見 [K-Rider case study](https://github.com/yazelin/k-rider/tree/main/docs/case-study ):同樣是前端網頁透過 Cloudflare Worker 把藏好 key 的 AI 接上來,只是把這個「頁面即時呼叫 AI」的代理架構放進一個產品級遊戲裡跑。

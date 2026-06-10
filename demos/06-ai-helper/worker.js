/* 模組 6 — Cloudflare Worker 代理(完整可貼版)
   用法:Cloudflare → Workers → Create → 整段貼上取代預設碼
   → Settings → Variables and Secrets → 新增 Secret:GROQ_API_KEY
   → 把 workers.dev 網址貼回 demo 06 的 A 模式輸入框 */
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
          { role: "system", content: "你是山霧咖啡(SANWU COFFEE)的活動小幫手。用繁體中文、兩三句話內溫暖回答。已知資訊:開幕週 2026/6/20(六)到 6/26(五),每日 08:00-18:00,全品項買一送一(以較低價那杯為招待,不與其他優惠併用);地點是霧峰山路 36 號(虛構地址);開幕限定「霧色」配方豆每日限量三十包;每日 14:00 主理人吧台手沖示範。只回答咖啡與本次開幕活動相關問題,其他話題溫柔婉拒。不要編造沒有的優惠或服務。" },
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

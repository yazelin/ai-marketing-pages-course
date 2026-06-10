# 模組 7(進階)— 讓活動頁自己更新

## 學完能做什麼

讓已上線的活動頁定時自己變:每天換一句活動標語、倒數天數自動更新、甚至每天自動換一張 AI 生成的圖。標準同模組 6:照著抄能動。

## 核心觀念:GitHub 不只存檔,還能定時幫你做事

GitHub 有個免費功能叫 Actions:你放一個「排程指令檔」進 repo,GitHub 就會按表操課(每小時、每天、每週)自動執行,執行結果 commit 回 repo → Pages 自動更新 → 訪客看到新內容。全程不需要你的電腦開機。

真實案例:catime(https://github.com/yazelin/catime )每小時自動生成一張新的 AI 貓圖並發布,整個系統就是一個排程檔 + 一支腳本,跑在免費額度內。

## 照著抄:每天自動換標語

### 1. 把頁面裡要變的部分抽成資料檔

讓 AI 改造你的頁面:「把 hero 的標語改成從 `daily.json` 讀取 `slogan` 欄位顯示」。repo 裡新增 `daily.json`:

```json
{ "slogan": "開幕週第一天,霧還沒散,咖啡先香了。" }
```

### 2. 放排程檔

在 repo 建立檔案 `.github/workflows/daily.yml`(路徑要一字不差):

```yaml
name: Daily Update
on:
  schedule:
    - cron: "0 0 * * *"   # 每天 UTC 00:00 = 台北 08:00
  workflow_dispatch:        # 留一顆手動按鈕方便測試
permissions:
  contents: write
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Pick today slogan
        run: |
          python3 - <<'EOF'
          import json, datetime
          slogans = [
            "開幕週第一天,霧還沒散,咖啡先香了。",
            "今天的山霧,配今天的拿鐵。",
            "第三天了,熟客都開始有自己的位子。",
            "週四,適合一個人的吧台時光。",
            "週五晚上,咖啡因換成故事。",
            "週末第一杯,留給早起的你。",
            "最後一天,買一送一,送給還沒來的那個人。",
          ]
          i = datetime.date.today().toordinal() % len(slogans)
          json.dump({"slogan": slogans[i]}, open("daily.json", "w"), ensure_ascii=False)
          EOF
      - name: Commit
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add daily.json
          git diff --cached --quiet || git commit -m "daily: update slogan"
          git push
```

### 3. 測試

repo → Actions 頁籤 → Daily Update → Run workflow(這就是 `workflow_dispatch` 留的手動按鈕)→ 跑完後看 `daily.json` 內容變了、過一兩分鐘頁面上的標語跟著變。

## 重要:GitHub 排程不保證準時,也可能整次跳過

這是 GitHub Actions 排程**官方文件就寫明**的限制:`schedule` 觸發在尖峰時段會延遲,高負載時甚至**整次被丟棄不執行**。對「每天換句標語」影響不大,但如果你拿它做「開賣那一刻自動上架」這種要準的事,會出包。三種應對,由簡到難:

### 招式 1:把內容寫成「冪等」,讓漏跑自動痊癒(最重要)

冪等 = 跑一次跟跑十次結果一樣、晚跑也算對。做法是讓腳本**從日期算出今天該顯示什麼**,而不是「在昨天基礎上 +1」。

看上面範本的這行:

```python
i = now.date().toordinal() % len(slogans)   # 從「今天是哪天」直接算出索引
```

這就是冪等:不管這個排程今天跑了一次、跑了三次、還是中午才補跑,算出來的標語都一樣、都正確。對照之下,如果你寫成「讀上次的索引 +1」,漏跑一天就永遠錯一格。**先把內容設計成冪等,一半的排程可靠性問題就消失了。**

### 招式 2:跑得比需要的更頻繁 +「沒變就不做事」(catime 的做法)

我們的 catime 專案排程是**每小時**跑一次(不是每天),搭配兩個設計:
- 每次都重新計算「現在該是什麼內容」(冪等),所以某個整點漏跑,下個整點自動補上,使用者最多看到一小時的延遲,不會永久卡住。
- 範本裡的 `git diff --cached --quiet || git commit` ——**內容沒變就不 commit**,所以跑再多次也不會洗版、不會產生一堆空 commit。

把 daily.yml 的 cron 從 `0 0 * * *`(每天一次)改成 `0 */6 * * *`(每六小時一次),漏跑的風險就從「整天沒更新」降到「最多晚六小時」,而且因為冪等 + 沒變不 commit,不會有任何副作用。這是 GitHub 排程最務實的加固法。

### 招式 3:乾脆不靠排程——能在前端算的就別放後端

最穩的「排程」是根本不排程。我們 demo 07 的**倒數天數**就是純前端用今天的日期即時算出來的(看 `index.html` 裡的 countdown),不依賴任何排程、永遠準。凡是「能從當下時間直接推算」的內容(倒數、第幾天、營業中/已打烊),都讓瀏覽器自己算,比任何排程都可靠。

## 更準時的選擇:Cloudflare Cron Triggers

如果你已經在用 Cloudflare Worker(模組 6、9),它內建的 **Cron Triggers** 比 GitHub 排程準時得多,而且免費方案就有。設定:在 `wrangler.toml` 加幾行,Worker 裡用 `scheduled` handler 接:

```toml
# wrangler.toml
[triggers]
crons = ["0 0 * * *"]   # 一樣是 UTC,台北 08:00
```

```js
// worker.js —— 排程一到,Cloudflare 自動呼叫這個 scheduled
export default {
  async scheduled(controller, env, ctx) {
    const slogans = ["霧還沒散,咖啡先香了。", "今天的山霧,配今天的拿鐵。", /* … */];
    const i = Math.floor(Date.now() / 86400000) % slogans.length;
    await env.DB.prepare("UPDATE site SET slogan=? WHERE id=1").bind(slogans[i]).run();
  },
};
```

差別:Cloudflare 在它自己的基礎設施上跑,準時性遠勝 GitHub 排程(GitHub 那套本來就標明「不保證」);代價是內容得存在它能存的地方(D1、KV),不像 GitHub 是直接改 repo 裡的檔案。**決策很簡單:已經在用 Cloudflare、又在意準時 → 用 Cron Triggers;只是每天換句無關緊要的文案、想跟 repo 綁一起 → GitHub Actions + 上面三招加固就夠。** 注意:剛改完 cron 設定,Cloudflare 端最長要 15 分鐘才生效。

## 延伸玩法(原理完全相同)

- **倒數天數**:腳本算「距離活動結束還剩 N 天」寫進 json(或如招式 3,直接前端算)。
- **每日 AI 圖**(catime 模式):排程腳本呼叫生圖 API(key 放 repo Settings → Secrets,跟模組 6 同一個觀念),存圖 commit。
- **自動抓資料**:每天抓天氣寫進頁面:「山上 16 度,適合熱拿鐵」。

## 對照成品

`demos/07-auto-update/` — 「今日山霧」頁,標語來自 `daily.json`;本 repo 的 `.github/workflows/daily.yml` 每天台北 08:00 自動改寫它(跟上面範本同一套)。到 repo 的 Actions 頁籤可以看到每天的執行紀錄,也可以按 Run workflow 現場示範。

## 常見坑

1. **cron 是 UTC 時區**:`0 0 * * *` 是台北早上八點,不是半夜。要台北時間 X 點,寫 X-8(負數就 +24)。
2. **以為排程一定會跑**:GitHub 排程會延遲、會跳過(見上面整節)。別承諾「整點準時」;用冪等 + 高頻率 + 沒變不 commit 加固,或要準就用 Cloudflare Cron。
3. **忘了 `permissions: contents: write`**:Actions 預設不能改 repo,push 會失敗,紅勾勾點進去看 log 就會看到 Permission denied。
4. **活動結束忘了關**:排程會一直跑下去。活動收攤時把 `daily.yml` 刪掉或在 Actions 頁面 Disable workflow。
5. **排程靜悄悄壞掉沒人發現**:Actions 失敗預設會寄信給 repo 擁有者;別把通知關掉,不然某天 key 過期、排程連續失敗你卻不知道。重要的排程值得偶爾去 Actions 頁籤看一眼最近幾次是不是綠的。

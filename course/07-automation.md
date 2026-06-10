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

## 延伸玩法(原理完全相同)

- **倒數天數**:腳本算「距離活動結束還剩 N 天」寫進 json。
- **每日 AI 圖**(catime 模式):排程腳本呼叫生圖 API(key 放 repo Settings → Secrets,跟模組 6 同一個觀念),存圖 commit。
- **自動抓資料**:每天抓天氣寫進頁面:「山上 16 度,適合熱拿鐵」。

## 常見坑

1. **cron 是 UTC 時區**:`0 0 * * *` 是台北早上八點,不是半夜。要台北時間 X 點,寫 X-8(負數就 +24)。
2. **排程不準時**:GitHub 免費排程尖峰時可能晚幾分鐘到幾十分鐘,行銷文案別承諾「整點準時」。
3. **忘了 `permissions: contents: write`**:Actions 預設不能改 repo,push 會失敗,紅勾勾點進去看 log 就會看到 Permission denied。
4. **活動結束忘了關**:排程會一直跑下去。活動收攤時把 `daily.yml` 刪掉或在 Actions 頁面 Disable workflow。

# 模組 11 — 成效追蹤:裝分析與廣告 Pixel

## 學完能做什麼

幫活動頁裝上「網站分析」(知道多少人來、從哪來、有沒有完成報名)和「廣告 Pixel」(要投 FB/IG 廣告時,才追得到轉換、做得了再行銷)。都是貼一段 script 的事,不用寫程式。

## 為什麼一定要裝

行銷最怕「做了卻不知道有沒有效」。沒有分析,你不知道:這波貼文帶來幾個人?大家從手機還是電腦來?有多少人滑到報名按鈕卻沒按?**裝了分析,下次活動才有依據優化;沒裝,就是憑感覺。** 這也是健檢器會檢查「追蹤」這一項的原因。

## 一、網站分析(每個活動頁都該裝)

選一個,貼一段 script 到 `<head>`:

### 選項 A:Google Analytics 4(最主流、免費)
1. 到 analytics.google.com 建一個「資源」,拿到一段 `G-XXXXXXX` 的代碼。
2. 它會給你一段 script,貼進你頁面的 `<head>`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXX');
</script>
```
3. 換成你自己的 `G-XXXXXXX`。上線後,GA 後台就會看到即時人數、來源、裝置。

### 選項 B:Plausible / Umami(隱私友善、更簡單)
不想用 Google、或在意隱私,可以用 Plausible(付費,介面極簡)或 Umami(可自架免費)。同樣是貼一段 script。對小活動,GA 免費版已經很夠。

給 AI 的 prompt:
```text
幫我把這段 Google Analytics 代碼正確貼進我頁面的 <head>:[貼上 GA 給你的 script]
確認 measurement id 是 G-XXXXXXX,放在 <head> 結束前。
```

## 二、追「報名成功」這個關鍵動作(事件追蹤)

只知道「有人來」還不夠,你要知道「有幾個人真的報名了」。在報名成功時送一個事件給 GA:
```html
<!-- 在報名表單送出成功後執行 -->
<script>gtag('event', 'signup', { event_category: '開幕週' });</script>
```
這樣 GA 後台就能看到「轉換數」,算得出轉換率(報名數 ÷ 來訪數)。給 AI:「我的報名表單送出成功時,幫我呼叫 gtag 送一個名為 signup 的事件。」

## 三、廣告 Pixel(只有要投廣告才需要)

如果你要在 FB/IG 下廣告,**Meta Pixel** 是必裝——沒有它,你無法知道哪個廣告帶來報名、也無法做「再行銷」(把廣告投給來過但沒報名的人)。

1. 到 Meta 商務管理工具建立 Pixel,拿到一段含 `fbq('init', '你的PixelID')` 的代碼。
2. 貼進 `<head>`(Meta 會給完整 script,照貼)。
3. 在報名成功時加一行 `fbq('track', 'Lead');` 或 `fbq('track', 'CompleteRegistration');` 追轉換。

不投廣告就不用裝(健檢器對 Pixel 缺少只給「提醒」不扣硬分,就是這個道理)。

## 隱私與法規(別忽略)

- 裝了追蹤就有在蒐集行為資料,頁面該有簡短的隱私說明或 cookie 提示(尤其面向歐盟訪客要考慮 GDPR / cookie 同意)。
- 不要追蹤你不需要的東西;能匿名就匿名。
- email 名單(模組 9)那種個資,保管責任更重——別把分析資料跟個資隨意串接。

## 常見坑

1. **裝了沒驗證**:貼完 script 要實際開頁面,在 GA「即時」報表看到自己這一次造訪,才算真的通。
2. **只追流量、不追轉換**:知道一千人來、卻不知道幾個報名,等於沒抓到重點。一定要設「報名成功」事件。
3. **Pixel 裝了卻沒在轉換點觸發**:只 init 不 track,廣告後台看不到轉換,再行銷也做不了。
4. **把追蹤碼貼錯位置**:GA/Pixel 主代碼放 `<head>`;事件 `track` 放在「動作真的完成」的那一刻(表單送出成功後),不是頁面一載入就送。
5. **忘了隱私揭露**:蒐集資料卻沒說,法規與信任都有風險。

## 對照

健檢器(見模組 10 結尾)的「追蹤」類別就是檢查這兩件:有沒有裝分析、有沒有廣告 Pixel。做完本模組,把你的頁貼進健檢器,追蹤那一格應該變綠。

## 動手做

**任務**:給你的頁裝 Google Analytics,開頁面後到 GA「即時」報表看到自己這次造訪;在報名成功時送一個名為 `signup` 的事件。
**預期成果**:GA 即時報表看到 1 位使用者;事件清單裡出現 `signup`。
**卡關怎麼辦**:即時沒看到,確認 `G-XXXXXXX` 換成你自己的、追蹤碼貼在 `<head>` 裡。
**自檢**:把你的頁貼進行銷頁健檢器(https://yazelin.github.io/marketing-page-checker/ )看相關項目是否變綠

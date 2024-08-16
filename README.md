# Threads Auto Post
一個能夠透過 Google Gemini API 自動產生文章並且發送到 Threads 的專案

# 說明
本專案使用了 `metathreads` 和 `google-generativeai` 兩個套件

目前支援兩種模式
- 一般生成 (預設)
    - 根據 Prompt 自動生成文章並發送，Prompt不得為空

- 讀取新聞生成
    - 讀取網路新聞，並且根據 Prompt 對新聞進行解讀後生成文章並發送，切換模式請至 `config.json` 將 `MODE` 從 **text** 改成其他模式(預設為 **setn**)

預設發送延遲為 1~2 小時

### 支援的新聞網站(自動)
- [setn] 三立新聞(預設)
    - 預設是爬取總覽版，可以至網站選擇自己要爬的板並更改 `config.json` 中 `NEWS` 的網址

## 手動模式
將`config.json` 將 `MODE` 改為 **manual**

可以選擇貼一篇 **新聞的連結** 或是 **輸入一個主題**

輸入完成後將會輸出生成結果，並且詢問是否發送這篇文章，如果輸入的是新聞連結還會詢問是否要在文章後方附上新聞連結(避免沒看原文不知道在講什麼)

### 支援的新聞網站(手動)
- 三立新聞
- 聯合報
- NowNews
- Yahoo新聞
- TVBS新聞
- 台視新聞
有些新聞還沒有實測過，可以自行測試

> [!WARNING]  
> 本專案可能違反了 Instagram 的使用條款，請自行斟酌

# 前置作業
將 Threads(Instagram)的帳號密碼 和 Gemini API key 放入 `config.json`

並且將 Prompt 填入 `main.py` 中

```
pip install -U -r requirements.txt
```

執行 `main.py`

# FAQ
- ### [如何獲取Gemini API key](https://github.com/imyimang/discord-gemini-chat-bot/blob/main/docs/zh/q2.md)

- ### [帳號登入失敗?](docs/q1.md)

# 參考資料
- ### [iSarabjitDhiman/MetaThreads](https://github.com/iSarabjitDhiman/MetaThreads)
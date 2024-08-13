# Threads Auto Blocker
一個能夠透過Google Gemini API自動產生文章並且發送到Threads的專案

# 說明
本專案使用了 `metathreads` 和 `google-generativeai` 兩個套件

目前支援兩種模式
- 一般生成 (預設)
    - 根據 Prompt 自動生成文章並發送

- 讀取新聞生成
    - 讀取網路新聞，並且根據 Prompt 對新聞進行解讀後生成文章並發送

預設發送延遲為 1~2 小時

## 支援的新聞網站
- 三立新聞(預設)

> [!WARNING]  
> 使用本專案有**極高的機率**被 Instagram 判定為自動化程式，請自行斟酌

# 前置作業
將 Threads(Instagram)的帳號密碼 和 Gemini API key 放入 `config.json`

並且將 Prompt 填入 `main.py` 中

```
pip install -U -r requirements.txt
```

執行 `main.py`

# FAQ
- ### [如何獲取Gemini API key](https://github.com/imyimang/discord-gemini-chat-bot/blob/main/docs/zh/q2.md)

# 參考資料
- ### [iSarabjitDhiman/MetaThreads](https://github.com/iSarabjitDhiman/MetaThreads)
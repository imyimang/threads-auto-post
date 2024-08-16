import google.generativeai as genai
import asyncio
from metathreads import MetaThreads
from spider import getnews,setn_fetch_url
import random
import json
import re

data = json.load(open("config.json", encoding="utf-8")) 

ACCOUNT = data["ACCOUNT"]
PASSWORD = data["PASSWORD"]
API_KEY = data["API_KEY"]
NEWS = data["NEWS"]
MODE = data["MODE"]


#  Prompt填這裡
##########################
prompt = """
嗨
"""
##########################

while True:
    if MODE in ['setn', 'text']: break

    MODE = input('不明的模式，模式應為 "setn" 或 "text"\n輸入執行模式: ')

print("正在登入...")
threads = MetaThreads()
threads.login(ACCOUNT,PASSWORD)

genai.configure(api_key=API_KEY)

generation_config = {
    'temperature': 1,
    'top_p': 0.95,
    'top_k': 64,
    'max_output_tokens': 2048,
}

safety_settings = [
    {
        'category': 'HARM_CATEGORY_HARASSMENT',
        'threshold': 'block_none'
    },
    {
        'category': 'HARM_CATEGORY_HATE_SPEECH',
        'threshold': 'block_none'
    },
    {
        'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
        'threshold': 'block_none'
    },
    {
        'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
        'threshold': 'block_none'
    },
]

model = genai.GenerativeModel(model_name='gemini-1.0-pro', generation_config=generation_config, safety_settings=safety_settings) 


async def text_api(msg: str) -> str | None:
    '''
    呼叫 api 並回傳我的回應
    '''
    convo = model.start_chat(history=[
    ])

    if not msg:return '這段訊息是空的'

    await convo.send_message_async(msg)
    reply_text = convo.last.text
    return reply_text 

async def text_auto_post():
    while True:
        reply_text = await text_api(prompt)
        print("\n生成結果:" + reply_text)

        print("\n\n正在發送貼文")
        threads.post_thread(thread_caption = reply_text)
        print("成功發送文章!")    
    
        await asyncio.sleep(60 + random.randint(10,60))


async def setn_auto_post(url):
    while True:
        news_url = await setn_fetch_url(url)
        try:
            with open('cache.txt', 'r') as file:
                cached_url = file.read().strip()
        except FileNotFoundError:
            with open('cache.txt', 'w') as file:
                file.write("") 
            cached_url = ""

        if cached_url == f"https://www.setn.com{news_url}":
            print("URL 相同，跳過後續流程")
        else:
            with open('cache.txt', 'w') as file:
                file.write(f"https://www.setn.com{news_url}")

            news = await getnews(f"https://www.setn.com{news_url}")
            print("\n\n新聞內容:", news)

            reply_text = await text_api(prompt + " ".join(news))
            print("\n生成結果:" + reply_text)

            print("\n\n正在發送貼文")
            threads.post_thread(thread_caption = reply_text)
            print("成功發送文章!")    
        
        await asyncio.sleep(60 + random.randint(10,60))
        
async def manual():
    url = input("輸入新聞網址/主題:")
    pattern = r'https://[^\s]+'
    if re.match(pattern,url):
        news = await getnews(url)
        print("\n新聞內容:",news)
        reply_text = await text_api(prompt + " ".join(news))
        print("\n生成結果:" + reply_text)
    else:
        reply_text = await text_api(prompt + url)
        print("\n生成結果:" + reply_text)

    yes_or_no = input("\n你要發這篇文嗎: ")
    if yes_or_no == "yes" or yes_or_no == "y":
        if re.match(pattern,url):
            yes_or_no = input("要附連結嗎:")
            if yes_or_no == "yes" or yes_or_no == "y":
                print("正在發送貼文")
                threads.post_thread(thread_caption=f"{reply_text}\n\n{url}")
                print("成功發送文章!")
            else:
                print("正在發送貼文")
                threads.post_thread(thread_caption=f"{reply_text}")
                print("成功發送文章!")     
        else:
            print("正在發送貼文")
            threads.post_thread(thread_caption=f"{reply_text}")
            print("成功發送文章!")     

        await manual()
    else:
        await manual()


if MODE == "setn": asyncio.run(setn_auto_post(NEWS))
if MODE == "text": asyncio.run(text_auto_post())
if MODE == "manual": asyncio.run(manual())
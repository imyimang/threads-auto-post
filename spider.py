from bs4 import BeautifulSoup
import aiohttp

async def getnews(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as inner_response:
            if inner_response.status == 200:
                inner_html = await inner_response.text()

                soup = BeautifulSoup(inner_html, 'html.parser')
                word = soup.find_all('article')

                titles1 = []
                for title_tag in word:
                    title1 = title_tag.text.strip()
                    remove = "我是廣告 請繼續往下閱讀"
                    title1 = title1.replace(remove, "")
                    lines = title1.splitlines()
                    title1 = '\n'.join(line for line in lines if line.strip())
                    titles1.append(title1)

                return(titles1)
            else:
                print(f"無法獲取網頁內容，狀態碼：{inner_response.status}")
                return ["讀取失敗"]


async def setn_fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                a_tag = soup.find('h3', class_='view-li-title').find('a')
                if a_tag:
                    href = a_tag['href']
                    return href
                return None
            else:
                print('網頁載入失敗:', response.status)
                return None
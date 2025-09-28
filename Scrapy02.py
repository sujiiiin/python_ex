import requests
from bs4 import BeautifulSoup

keyword = input("키워드 입력: ")
url = f"https://kin.naver.com/search/list.naver?query={keyword}"

header_info = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36'}

r = requests.get(url, headers=header_info)

soup = BeautifulSoup(r.text, 'html.parser')

titles = soup.select("#s_content > div.section > ul > li > dl > dt > a")
dates = soup.select("#s_content > div.section > ul > li > dl > dd.txt_inline")

for date, title in zip(dates, titles):
    print(f"날짜: {date.text}")
    print(f"질문: {title.text}")

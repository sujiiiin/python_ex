import requests
from bs4 import BeautifulSoup

url = "https://zdnet.co.kr/"

header_info={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36'}

r=requests.get(url, headers=header_info) # 지정한 url에서 웹 스크래핑 해와라. 헤더의 정보는 위에 적은거와 같다. 

soup=BeautifulSoup(r.text,'html.parser') # html파서를 텍스트 형태로 정리해라.

links = soup.select("body > div.contentWrapper > div > div.left_cont > div.news1_box > div.news_list > div > div.assetText > a > h4")

for link in links:
  print(link.string)
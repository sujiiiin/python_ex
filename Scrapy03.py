#https://www.malware-traffic-analysis.net/2023/index.html 를 크롤링 해서
#1. 제목 주소를 가져오시오.
#2. 링크 정보를 전체 URL 형식으로 출력하세요. (https://www.malware-traffic-analysis.net 로 시작)
#3. 결과 값을 txt 파일로 저장하세요.!!

import requests
from bs4 import BeautifulSoup

url = 'https://www.malware-traffic-analysis.net/2023/index.html'

header_info={'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36'}

r=requests.get(url,headers=header_info,verify=False)
soup = BeautifulSoup(r.text,'html.parser')

tags=soup.select('#main_content > div.content > ul > li > a.main_menu')
# <a class="main_menu" href="01/04/index.html">Astaroth (Guildma) malware infections</a>

result=[]

for tag in tags:
  title=tag.text
  title_link=f"https://www.malware-traffic-analysis.net/2023/{tag.get('href')}"
  result.append(f"{title}\n{title_link}\n")

with open('scrapy.txt','w',encoding='utf-8') as file:
  for f in result:
    file.write(f)
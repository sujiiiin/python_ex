# uploads폴더에 새로운 파일 탐지 → 보고탐지.txt 파일에 추가
import os
from datetime import datetime 
import time

folder_path='uploads'
all_files=set(os.listdir(folder_path)) # 결과 : {'test02.py', 'test.py', 'file.txt', 'test.txt', 'test1.txt', 'test01.py'}

while True:
  now=datetime.now()
  day=now.strftime("%Y-%m-%d")
  hour=now.strftime("%H:%M:%S")
  
  current_file=set(os.listdir(folder_path))
  new_file=all_files-current_file
  
  for filename in new_file:
    print(f"새로운 파일 탐지 : {filename}")
    with open(f'{day}탐지 보고서.txt','a',encoding='utf-8') as file:
      file.write("작성자 : 홍길동\n")
      file.write("주요 내용 : 새로운 파일 탐지\n")
      file.write(f"시간 {hour}, 파일 이름 : {filename}\n")
  
  all_files=current_file
  print("모니터링중")
  time.sleep(1)
  
  



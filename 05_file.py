#기능 추가01 - readlines() 읽어서 줄 단위로 검사!!
#기능 추가02 - 파일 앞쪽에 # 나 // 주석처리 된 것을 찾아내시오. startswith("#")
#기능 추가03 - 출력 예제는 "파일경로(이름) : 1번째 라인 탐지 : 내용"

import os

file_path='uploads'
all_files=os.listdir(file_path)
# 결과 : ['file.txt', 'test.py', 'test.txt', 'test01.py', 'test02.py']

txt_file=[]

for file in all_files:
  if file.endswith('.txt'):
    txt_file.append(file)
    
# 결과 : ['file.txt', 'test.txt']


for filename in txt_file:
  filepath=os.path.join(file_path, filename) # 결과 : uploads\file.txt       uploads\test.txt
  # os.path.join을 쓰는 이유는 현재 파일과 탐지하려는 파일의 경로(uploads내 파일)가 맞지 않아서 with open을 할 때 경로를 맞춰줘야하기 때문이다.
  with open(filepath,'r',encoding='utf-8') as file:
    lines=file.readlines() # 결과 : ['#admin/1234\n', '\n', 'a.com\n', '010-2323-2323']  ['//test/1234\n', '<!--- test/1234---!>\n', 'a@a.com']
    for index, value in enumerate(lines):
      if value.startswith("#") or value.startswith("//"):
        print(f"{filepath} : {index+1}번째 라인 탐지 : {value}")
      


#uploads 폴더의 디렉터리 정보를 수집
#파일 확장자가 txt 인 것을 리스트화
#txt 파일을 열어서 출력
import os

dir_path='uploads'
all_files=os.listdir(dir_path) # all_file=[01_file.py, test.txt, 02_file.py ...]

txt_list=[]
total_list=[]

for file in all_files:
  if file.endswith(".txt"):
    txt_list.append(file)
    

for filename in txt_list:
  file_path=os.path.join(dir_path,filename)
  with open(file_path, 'r', encoding='utf-8') as f:
    print(f"{filename} 내용 : ")
    print(f.read())
    print("-" * 40)
  

#upoloads 폴더를 모니터링(감시)
#새로운 파일이 업로드가 되면 탐지!!
#(나중에 추가) 업로드된 새로운 파일에 개인정보가 포함되면 탐지!!
import os
import time

dir_path='uploads'
all_files=set(os.listdir(dir_path)) # 리스트끼리는 연산을 할 수 없기 때문에 set()함수로 집합 형태로 만들어 리스트끼리 연산할 수 있게한다.

while True:
  current_file=set(os.listdir(dir_path))
  new_file=current_file-all_files
  print(f"새로 생성된 파일 : {new_file}")
  
  all_files=current_file
  
  time.sleep(1)
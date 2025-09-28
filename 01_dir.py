import os
current_directory = os.getcwd()
print("Current working directory:", current_directory)

file_path="file.txt"
if os.path.isfile(file_path):
  print(f"{file_path}는 파일이다.")
else:
  print(f"{file_path}는 파일이 아니다.")
  
if os.path.isdir(file_path):
  print(f"{file_path}는 디렉터리다.")
else:
  print(f"{file_path}는 디렉터리가 아니다.")
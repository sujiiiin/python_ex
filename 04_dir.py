import os

dir_path="uploads"
all_files=os.listdir(dir_path)

txt_files=[]

for file in all_files:
  if file.endswith('txt'):
    txt_files.append(file)

print(txt_files)

  
with open('example.txt','r',encoding='utf-8') as f:
  content= f.readlines()
  for line in content:
    print(line, end='')

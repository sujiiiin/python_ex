# 아래는 5명의 학생들의 성적을 입력 받아서
# 최고값, 최소값, 평균값, 90점 이상의 count 프로그램
# 5명의 학생들의 성적을 입력 -> list [] 에 저장

STUDENT=5
stu=[]
print("5명 학생의 성적을 입력하시오. ")

for i in range(STUDENT):
  value=int(input(f"{i+1}성적을 입력하시오."))
  stu.append(value)
  
print(f"최고값 : {max(stu)}")
print(f"최소값 : {min(stu)}")
print(f"평균값 : {sum(stu)/STUDENT}")

count=0
for j in stu:
  if j>=90:
    count=count+1
    
print(f"90점 이상 학생 수 : {count}")
menus = {"아메리카노":4000, "카페라떼": 4500, "카푸치노": 5000}

print("=====메뉴판=====")

for menu, price in menus.items():
  print(f"{menu}:{price}원")
  
print("===========")

select=input("메뉴를 선택하시오. ")
pay=int(input("내실 금액을 입력하시오. "))

#메뉴를 선택하고, 거스름돈을 출력하는 기능!! get() 함수 사용해도 좋음

price=menus.get(select)
change = pay-price

if price==None:
  print("메뉴를 선택하지 않았습니다.")
else:
  if change >= 0:
    print(f"잔돈은 {change}원입니다.")
  else:
    print("잔액이 부족합니다.")
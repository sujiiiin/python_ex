#while 반복 while True 사용
#메뉴를 선택한다. (여러개의 메뉴를 선택 한다.)
#구매한 메뉴를 리스트로 보관도 해야 한다.
#현금을 넣는다.
#구매한후에 거스름돈을 받는다.
#구매했던 리스트와 총 구매가격? 출력!!!

menus = {"아메리카노":4000, "카페라떼": 4500, "카푸치노": 5000}

order_list=[]
total_price=0

for menu, price in menus.items():
  print(f"{menu}: {price}원")

print("=================")

while True:
  order=input("주문하실 메뉴를 선택하세요.")
  price=menus.get(order)
  
  if price != None:
    order_list.append(order)
    total_price=total_price+price
  elif order == 'q':
    print("주문을 종료합니다.")
    break
  else:
    print("메뉴가 없습니다.")
    

print(f"주문하신 메뉴는 {order_list}입니다.")
  
print(f"총 금액 : {total_price}")
  
money=int(input("지불하실 금액을 입력하세요."))
change=money-total_price

print(f"총 금액은 {total_price}이고, 잔돈은 {change}입니다.")
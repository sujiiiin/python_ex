my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict["email"] = "john@example.com"  # 새로운 키와 값 추가
my_dict["age"] = 31  # 기존 키의 값 수정

del my_dict["city"]

age=my_dict.pop("age")
print("Removed age:", age)

print(my_dict)
# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살 입니다." % 20) #정수
print("나는 %s을 좋아해요." %"파이썬") #문자열
print("Apple 은 %c로 시작해요." % "A") #문자 하나
# %s가 대부분 문자열 출력가능

print("나는 %s색과 %s색을 좋아해요." %("파란", "빨강"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨강"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨강"))

# 방법 4
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요--")


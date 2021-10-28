python = "Python is Amazingnnn"
print(python.lower()) # 문자열 소문자
print(python.upper()) # 문자열 대문자
print(python[0].isupper()) # 파이썬 문자열의 첫번째 문자가 대문자인지 판별
print(len(python)) #파이썬 변수 문자열의 전체 길이
print(python.replace("Python", "Jave")) # 파이썬 변수 안에 Python이라는 문자를 Jave로 변환

index = python.index("n") # n이 나오는 인덱스 값 리턴
print(index)
index = python.index("n", index + 1) # 첫번째 인덱스 다음의 위치 값 리턴
print(index)

print(python.find("Java")) # 자바라는 단어가 포함되있는지 판단
# print(python.index("java"))
print(python.find("Java"))
print("hi")

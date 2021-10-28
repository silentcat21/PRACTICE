print("백문이 불여일견,\n백견이 불여일타") #줄바꿈 문자

print("""저는 "최상민"입니다.""")
print("저는 \"최상민\"입니다.")

# \\ : 문장 내에서 \만 출력
print("C:\Practice\Python")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

"""Quiz 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외
규칙2 : 처음 만나는 점(.) 이후 부분은 제외
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

예) 생성된 비밀번호 : nav51!
"""
# password = "http://naver.com"
# password2 = str(password[7,10])
# password3 = str(len(password[7:]) - 4)
# password4 = str(password.find("e"))

# print(f"비밀번호가 생성되었습니다 : {password2}{password3}{password4}!")

url = "http://google.com"
my_str = url.replace("http://", "") # 규칙 1
print(my_str)
my_str = my_str[:my_str.index(".")] # my_str[0:5] 
print(my_str) # 규칙 2

password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(f"{url}의 비밀번호는 {password} 입니다.")
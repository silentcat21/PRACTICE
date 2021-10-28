# 애완동물 소개
animal = "고양이"
name = "나로"
age = 6
hobby = "산책"
is_adult = age >= 3


print("우리집" + animal + "의 이름은" + name +"에요")
hobby = '공놀이'  #중간에 변수를 바꾸면 최신꺼로 전환됨
print(name +"는" + str(age) + "살이며, " + hobby + "을 좋아하지 않아요")
print("나로는 어른일까요?" + str(is_adult))

#주석#######주석
'''이렇게 하면
줄바꿈 주석도 가능'''

'''Quiz 변수를 이용하여 다음 문장을 출력하시오

변수명
: station

변수값
: 사당, 신도림, 인천공항 순서대로 입력

출력 문장
: xx행 열차가 들어오고 있습니다.
'''

print('------Quiz------')
station = "사당"
print(station,"행 열차가 들어오고 있습니다.")
print(station+"행 열차가 들어오고 있습니다.")

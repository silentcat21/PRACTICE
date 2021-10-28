# 리스트 [] : 순서를 가지는 객체의 집합
# 지하철 칸별로 10명, 20명, 30명
subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타있는가
print(subway.index("조세호")+1)

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # 리스트 뒤에 객체를 추가함
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈") # 인덱스 1의 값에 객체를 추가함
print(subway)
print("--------")
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [4,1,3,65,45, -14]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)
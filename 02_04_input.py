#  입력 (input)
# 주의) 사용자 입력은 항상 "문자열"
# 형식: 변수 = input("안내문구: ")
# name = input("이름: ")
# age = input("나이: ")
# print(name)

# 형변환 - int(), float(), str()
# print(age+ 1)
# print(int(age) + 1)  # int() 형변환 후 연산

# 실습
# birth_year = int(input("태어난 해를 입력하시오:"))
# age = 2026 - birth_year + 1
# print("나이:", age, "세")
# height = float("173.5")
# print(height, type(height))

# print("나이:" + str(30))

# 실습
# name = input("국가: ")
# city = input("도시: ")
# print(name, city)

#실습
# a = int(input("수1: "))
# b = int(input("수2: "))
# print("곱셈:", a * b)
# print("나눗셈:", a / b)

# 실습
# temp = int(input("온도: "))
# print("60 이상?", temp >= 60)
# print("0 이하?", temp <= 0)

# 실습
x = int(input("점수1: "))
y = int(input("점수2: "))
z = int(input("점수3: "))
avg = (x + y + z) / 3
print("70 이상?", avg >= 70)

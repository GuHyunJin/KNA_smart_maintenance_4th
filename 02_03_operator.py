# 연산자
# - 산술, 비교, 논리연산자

# 산술 연산자
# 형식 : +, -, *, /, // (몫), % (나머지)

# 우선순위
# - 곱셈, 나눗셈 등이 우선, 괄호를 이용하여 변경 가능

# 복합 할당
# 형식: score += 10 <-> score = score + 10
score = 100
score += 10
print(score)
#  -=, *=, /=

# 문자열 연산
# +, * 가능
print("안녕" + "하세요")
print("-" * 4)
# 주의 ) 자료형이 같은 것끼리 연산 할 수 있다

# 실습1
a = 17
b = 5
print(17 + 5)
print(17 - 5)
print(17 * 5)
print(17 / 5)
print(17 // 5)
print(17 % 5)
print(17 ** 5)

# 실습2
x = 10
y = 20 
z = 30
print((x + y + z) / 3)
side = 7
print(side ** 2)
print(3 * 4 * 5)

# 실습3
print(6 == 6)
print(6 != 3)
print(6 > 5)
print(6 < 5)
print(6 >= 6)
print(6 <= 6)

# 실습4
temp = 85
print(temp >= 60 and temp <= 90 )
press = 5
print(press >= 3 and press <= 7 )

# 실습5
재고 = 100
print(재고)
재고 += 50
print(재고)
재고 -= 30
print(재고)
재고 += 5
print(재고)

# 실습6
total = 500
defect = 23
print(defect / total * 100, "%")
run_h = 21
all_h = 24
print(run_h / all_h * 100, "%")

# 실습7
minutes = 500
print(minutes // 60)
print(minutes % 60)
print(minutes // 60, "시간", minutes % 60, "분")
# 조건문
# if 기본 구조 - 콜론과 들여쓰기(코드 블록)
# 형식: 
# if 조건식:
#     실행할 코드 (들여쓰기)
# temp = 80
# if temp > 80:                    #콜론: 블록 시작 신호
#     print("온도 주의")           #들여쓰기 안: 조건 참
#     print("점검 요망")           
# print("측정 종료")               #들여쓰기 끝: 조건 상관없이 실행

# else - 조건 거짓일 때
# 형식:
# if 조건문:
#     참일 때 코드
# else:
#     거짓일 때 코드

# score = 55
# if score >= 60:
#     print("합격")
# else:
#     print("불합격")    

# 실습1
# age = 18
# if age >= 19:
#     print("성인입니다")
# else:
#     print("미성년자입니다")


# elif
# 형식:
# if ... elif ... else (위에서부터 검사, 처음 참만 실행)

# score = 82
# if score >= 90:
#     print("우수")
# elif score >= 70:
#     print("보통")
# else:
#     print("미흡")

# 실습2 
# score = 69
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")

# 실습3
# temp = int(input("측정 온도를 입력하세요: "))
# if temp > 80: print("위험")
# elif temp > 60: print("주의")
# else:
#     print("정상")

# 실습4
# correct_id = "admin"
# correct_passward = 1234
# id = input("아이디: ")
# passward = input("비밀번호: ")
# if id == correct_id and passward == correct_passward: print("로그인 성공")
# else:
#      print("로그인 실패")

# 실습5
temp = int(input("온도: "))
vib = float(input("진동: "))
elc = int(input("전류: "))
if temp > 80 or vib > 4.0: print("위험:즉시 정지")
else: 
   if elc > 60 and temp > 70: print("주의:부하 점검")
if vib > 2.5: print("주의:진동 관찰")
else:
      print("정상")
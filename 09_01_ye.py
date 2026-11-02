# temp = int("스물")
# result = 10 / 0
# print(undefinded_var)



# try-excpet 구조
# try:
#   temp = int("스물")
# except ValueError:
#     print("ValueError")

# try:
#   result = 10 / 0
# except ZeroDivisionError:
#     print("ZeroDivisionError")

# try:
#   print(undefinded_var)
# except NameError:
#     print("NameError")


# 실습2
# try:
#   temp = int(input("온도: "))
#   print("온도는 ", temp)
# except ValueError:
#     print("숫자를 입력하세요")
# print("프로그램 계속")


# 여러 except 
# row = "P-01,102".split(",")
# try:
#   cod_no = int(row[3])
# except ValueError:
#     print("숫자 아님")
# except IndexError:
#     print("칸 부족")


# 실습3
try:
    value = int(input("측정값: "))
    print(100 / value)
except ValueError:
     print("숫자가 아닙니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")


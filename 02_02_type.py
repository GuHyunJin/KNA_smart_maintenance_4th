# 자료형

count = 3      # int 정수
temp = 25.5    # float 실수
name = "센서A"  # str 문자열

ok = True       # bool 불린형 - 참/거짓
no = False      

# type() -> 자료형을 알려줌
print(type(25))             
print(type("센서A"))
print(type(ok))

# 자료형마다 다른 동작
print(3 + 5)
print("3" + "5")          # 35 (글자 더하기 = 이어붙이기)

# 실습1
count = 7  
temp = 30  
name = "센서B" 
is_ok = True   
print(count, temp, name, is_ok)

# 실습2
print(type(count), type(temp), type(name), type(is_ok))

# 실습4
print(3 + 5)
print("3" + "5")

# 실습5
print(3 > 2)
print(5 == 5)
print(type(3 > 2))

# 실습6
count = 3
print(count, type(count))
count = 3.0
print(count, type(count))
count = "3"
print(count, type(count))

# 실습7
device_temp = 25.5
check_count = 12
device_name = "펌프A"
is_normal = True
print(device_temp, check_count, device_name, is_normal)


print(True and False)
print(True and False)
print(not True)

name = input("안녕하세요: 님!")
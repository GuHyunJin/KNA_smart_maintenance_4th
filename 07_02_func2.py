# 매개변수와 반환값

# 매개변수와 인자
# 형식:
# def 함수이름(매개변수):
#  ....
# 호출
# 함수이름(인자)

# def check(name):                #name = 매개변수
#     print(name +" 점검을 시작합니다.")

# check("압축기1")                # "압축기1" = 인자
# check("펌프1")
# check("A", "B")

# 실습2
# def report(name, temp):
#     print (name, temp, "도")

# report("모터", 78)
# report("펌프", 92)

# 실습3
# def report(name, temp):
#     print (name, temp)

# report("모터", 78)
# report("펌프", 92)

# return
# - print: 사람이 확인할 수 있게 출력 / return : 값을 프로그램에게 돌려줘서 이어 쓸 수 있게 한다
# def add(a, b):
#     return a+b

# total = add(3, 4)
# print(total)

# 실습4
# def add(a, b):
#     return a+b

# total = add(3, 4)
# print(total)
# print(total + 3)

# 여러 값 반환 / 언패킹
# - 쉼표로 여러 값을 return 하면 튜플로 묶여서 돌아옴
# def min_max(values):
#     return min(values), max(values)

# print(min_max([75, 10, 100]))        #(10, 100)
# low, high = min_max([75, 10,100])
# print(low, high)

# none = report("펌프", 10)


# 실습5
def stats(v):
    return min(v), max(v), sum(v) / len(v)

lo, hi, avg = stats([78,92,85])

print(lo, hi, avg)

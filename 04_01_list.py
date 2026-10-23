# 리스트
# 형식: 이름 = [값1, 값2, ...]
#  - 리스트는 여러 값을 '순서대로' 한 이름에 담는다.

# temps = [25, 26, 27, 28, 29]
machines = ["펌프", "모터", "압축기"]
# mixed = ["펌프", 87, True]    #종류가 달라도 한 리스트에 담을 수 있음

# print(len(temps))
# print(len([]))

# 실습1
# temps = [25, 26, 24, 27, 26]
# print(temps)
# print(len(temps))
# print(len([]))

# 실습2
# temps = [25, 26, 24, 27, 26]
# print(temps[0])
# print(temps[2])
# print(temps[4])

# 실습3
# lines = [250, 260, 240, 270, 230]
# print(lines[0])
# print(lines[4])
# print(lines[0] + lines[4])
# print(lines[0] + lines[4] /2)

# 실습4
# temps = [25, 26, 24, 27, 26, 20, 21, 22, 18, 19]
# print(temps[:3])
# print(temps[-3:])
# print(len(temps[:3]))

# 실습5
# list = [25, 26, 24, 27, 26, 20, 21, 22, 18, 19, 17, 12]
# print(list[:6])
# print(list[-6:])
# print(len(list[:6]))
# print(len(list[-6:]))
# print(list)


# 값 바꾸기 / in 존재 확인
# 형식: 리스트[번호] = 새 값 / 값 in 리스트
# nums = [25, 26, 24, 28, 27]
# nums[2] = 99
# print(nums)
# print("모터" in machines)


# 값 추가 - append, insert, extend
# 형식: 리스트.append(값) / 리스트.insert(위치, 값) / 리스트.extend(다른 리스트)
# data = [25, 26, 24]
# data.append(28)
# data.insert(1, 99)
# data.extend([30, 31])
# print(data)

# 실습6
# temps = [25, 26, 240, 28, 27]
# temps[2] = 24
# print("모터" in machines)
# print(temps)
# print("체중계" in machines)

# 실습7
# data = []
# data.append(30)
# print(data)
# data.insert(0, 28)
# print(data)
# data.extend([31, 32])
# print(data)

# 값 삭제 - remove, pop, del
# 형식: 리스트.remove(값) / 꺼낸 값 = 리스트.pop(위치) / del 리스트[위치]
# d = [25, 26, 24, 28, 27]
# d.remove(24)
# print(d)
# got = d.pop(1)
# print(got,d)        #26 [25, 28, 27]
# del d[0]
# print(d)            #[28, 27]

# 정렬, 탐색 - sort, reverse / count, index
# 형식: 리스트.sort() 리스트.reverse()  리스트.count()
# l = [27, 24, 30, 22, 26]
# l.sort()                #[22, 24, 26, 27, 30]
# l.sort(reverse=True)    #[30, 27, 26, 24, 22]
# l.reverse()               #[26, 22, 30, 24, 27]
# print(l)

# r = ["정상", "이상", "정상", "정상", "이상"]
# print(r.count("정상"), r.index("이상"))   #3 1

# 실습8
# d = [25, 26, 999, 24, 28, 27]
# d.remove(999)
# print(d)
# got = d.pop(1)
# print(got,d)
# del d[0]
# print(d)

# 실습9
l = [30, 22, 28, 24, 27, 24, 26]
l.sort()
print(l)
l.reverse()
print(l)
print(l.count(24), l.index(24))
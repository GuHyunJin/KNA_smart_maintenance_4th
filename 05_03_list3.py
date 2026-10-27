# 실습1
# temps = [26, 28, 30, 33, 17]
# for t in temps:
#     if t >= 30:
#         print("고온: ", t)

# # 실습2
# hours = [2, 8, 3, 7, 9]
# for h in hours:
#     if h >= 5 and h <= 10:
#         print(h)



# 최대, 최소
# temps = [25, 32, 28, 36, 27, 31]
# biggest = temps[0]
# for t in temps:
#     if t > biggest:
#         biggest = t
# print(biggest)

# # 반 리스트 채우기
# doubled = []
# for t in temps:
#     doubled.append(t * 2)
# print(doubled)              #[50, 64, 56, 72, 54, 62]


# 실습3
# temps = [26, 28, 30, 33, 17]
# total = 0
# count = 0
# for t in temps:
#     if t > 30:
#         total += t
#         count += 1
# print("고온 평균:", total/count)


# 실습4
# temps = [26, 28, 30, 33, 17, 34, 35]
# hot = []
# for t in temps:
#     if t > 30:
#         hot.append(t)
# print(hot)
# print(len(hot))

# 실습5
# temps = [75.0, 79.3, 81.2, 83.1, 77.5]
# doubled = []
# for t in temps:
#     doubled.append(t * 1.8 + 32)
# print(doubled)

# 중첩 리스트 - 리스트 안에 리스트
# - 표(행,열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행', 안쪽 인덱스로 '열'
# rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
# for row in rows:
#     print(row[0], "온도", row[1])

# 실습6
temps = [25, 32, 28, 35, 27, 31, 24, 33, 29, 36]
total = 0
hot = []
for t in temps:
  total += t
  
  if t > 30:
    hot.append(t)
  
hot_total = 0
for h in hot:
  hot_total += h
print("전체 평균:", total / len(temps))
print("고온 평균:", hot_total / len(hot))    


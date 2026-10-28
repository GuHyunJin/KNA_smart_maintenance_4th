#  셋 - 중복 자동 제거
# 형식: (값, 값2)또는 set(리스트)
# - 빈 셋 set()
# logs = ["s01", "s02", "s01", "s03"]
# unique_logs = set(logs)
# print(unique_logs)                     # #{'s02', 's01', 's03'}
# print(sorted(unique_logs))             #['s01', 's02', 's03']   #셋은 순서가 없어 인덱싱 불가

# # add
# alerts = {"s01", "s02"}
# alerts.add("s03")
# print(alerts)
# alerts.add("s02")
# print(alerts)

# 실습4
# logs = ["s01", "s02", "s01", "s03"]
# unique_logs = set(logs)
# print(sorted(unique_logs))
# print(len(unique_logs))


# 집합 연산 - union(전체) / intersection(공통) / difference(차이)
# line_a = {"S01", "S02", "S03"}
# line_b = {"S03", "S04"}
# print(line_a.union(line_b))
# print(line_a.intersection(line_b))
# print(line_a.difference(line_b))

# 실습5
# line_a = {"S01", "S02", "S03", "S05"}
# line_b = {"S03", "S04", "S05"}
# print(line_a.union(line_b))
# print(line_a.intersection(line_b))
# print(line_a.difference(line_b))
# print(line_b.difference(line_a))

# 실습6
line_a = {"S02", "S03"}
line_b = {"S02", "S03", "S05"}
print(line_b.difference(line_a))
print(line_a.intersection(line_b))
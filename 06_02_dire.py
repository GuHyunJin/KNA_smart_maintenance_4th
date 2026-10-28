# 
# 
# sensors = {"모터온도": 78, "진동": 0.5}
# print(sensors)
# print(sensors["모터온도"])   #78
# print(type(sensors))         #<class 'dict'>
# # print(sensors["유량"])     # error

# # 추가 / 수정 / 삭제
# # 형식: 딕셔너리[키] = 값 (없는 키 - 추가, 있는 키 - 수정)
# # 형식: (삭제) del 딕셔너리[키]

# sensors["펌프압력"] = 95         #추가
# sensors["모터온도"] = 80         #수정
# del sensors["진동"]              #삭제
# print(sensors)                  #{'모터온도': 80, '펌프압력': 95}

# # get / in
# # 형식: 딕셔너리.get(키, 기본값)   / 키 in 딕셔너리
# print(sensors.get("유량"))          #None
# print(sensors.get("유량", 0))       #0
# print("모터온도" in sensors)         #True
# print(80 in sensors)                #False(값 확인 안됨)

# 실습1
# sensors = {"키": 78, "측정값": 0.5}
# print(sensors["키"])
# print(sensors.get("진동", 0))
# print("키" in sensors)

# keys / values / items / len
# sensors = {"모터온도": 78, "진동": 0.5}
# print(list(sensors.keys()))             #['모터온도', '진동']
# print(list(sensors.values()))           #[78, 0.5]
# avg = sum(sensors.values()) / len(sensors)
# print(avg)                              #39.25

# for name, value in sensors.items():
#     print(name, value)

# for k in sensors.keys()
# for v in sensors.values() 

# # update - 여러 항목 한번에 갱신(키가 있으면 수정, 없으면 추가)
# d = {"온도": 80}
# d.update({"온도": 80, "압력": 95})
# print(d)

# 실습2
# sensors = {"모터온도": 78, "진동": 0.5}
# new_data = {"모터온도": 81, "압력": 95} 
# sensors.update(new_data)
# print(sensors)
# del sensors["진동"]
# print("센서 수:", len(sensors))


# # 실습3
# sensors = {"온도": 80, "진동": 55, "압력": 95}
# avg = sum(sensors.values()) / len(sensors)
# print("평균:", round(avg, 1))

# top = ""
# high = 0
# for name, vaule in sensors.items():
#     if vaule > high:
#         high = vaule
#         top = name

# print("최댓값 센서:", top, high)

# zip : 센서명 - 값 매핑하기
# names = ["온도", "진동", "압력"]
# values [78, 0.5, 95]
# sensors = dict(zip(names, values))
# print(sensors)

# # 딕셔너리의 값에 리스트/딕셔너리 - 중첩 딕셔너리
# plant = {
#     "1번모터": {"온도": 78, "상태":, "정상"}
#     "2번모터": {"압력": 95, "상태":, "경고"}
# }

# print(plant["2번펌프"]["압력"])   #95

# 실습4
# names = ["온도", "진동", "압력"]
# values = [78, 0.5, 95]
# sensors = dict(zip(names, values))
# print(sensors)
# for name, value in sensors.items():
#     print(name, value)

# 실습5
# values = {"온도": 78, "상태": "정상"}
# limits = {"온도": 78, "상태": "정상"}
# warning = []
# for name, value in values.items():
#     if value > limits[name]:
#         warning.append(name)
# print("경고 센서:", warning)

# 실습6
# plant = {
#      "1번모터": {"온도": 78, "상태": "정상"},
#      "2번펌프": {"압력": 95, "상태": "경고"}
#  }

# print(plant["2번펌프"]["압력"])
# for name, info in plant.items():
#     if info["상태"] == "경고":
#         print(name, "점검 필요")

# 실습7
rows = ["온도,78", "압력,95", "진동,0.5"]
sensors = {}
for row in rows:
  name, value = row.split(",")
  sensors[name] = float(value)
print(sensors)

# 실습8
sensors = {"온도": 95, "압력": 96}
limits = {"온도": 90, "압력": 90}

# values() 이용한 평균
avg = sum(sensors.values()) / len(sensors)
print("평균:", round(avg, 1))

# items() 순회 -> 임계값 비교 -> 초과한 값은 셋에 담기(키 값 담기)
danger = set()
for name, v in sensors.items():
  if v > limits[name]:
    danger.add(name)

# 셋 정렬하여 출력
print("위험 센서:", sorted(danger))
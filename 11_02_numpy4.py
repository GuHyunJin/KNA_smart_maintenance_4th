import numpy as np

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)


# isnan - 걸측값 위치 찾기
# - 결측값: 값이 빈 칸 - 0이 아니라 값을 모름

# x = np.array([2.0, np.nan, 4.0])
# print(np.isnan(x))
# print(np.isnan(x).sum())

# # nanmean, nanstd - 결측값을 무시
# temp = np.array([70.1, np.nan, 71.2, 70.8])
# print(np.mean(temp))
# print(round(np.nanmean(temp), 2))

# nanmean, nanmax, nanmin

# 실습1
# vib = col(2)
# print(np.isnan(vib).sum())
# print(round(np.isnan(vib).mean(), 2))
# print(round(np.nanmean(vib), 3))
# print(np.mean(vib))


# 백분위수, 사분위수 - percentile, quantile
# - 데이터를 크기순으로 줄 세웠을 때 특정 위치의 값
# - 25, 50, 75 백분위수 - 1사분위, 중앙값, 3사분위
# - 평균과 달리 극단적인 이상값에 휘둘리지 않음

vib_s = np.array([2.0, 2.2, 2.5, 2.8, 3.0, 6.5])
print(np.round(float(np.percentile(vib_s, 25)), 2))
print(np.round(float(np.percentile(vib_s, 75)), 2))

# 여러 자리 한번에
print(np.round(np.percentile(vib_s, [25, 50, 75]), 2))

# quantile : 25 - 0.25
print(np.round(float(np.percentile(vib_s, 0.25)), 2))

# 사분위 기반 이상치 범위 - IQR

q1, q3 = np.percentile(vib_s, [25,75])
iqr = q3 - q1
upper = q3 + 1.5 iqr
print(vib_s[vib_s > upper])


# 평균/표준편차로 정규화 - z-score
# - 부호의 의미: 양수는 평균보다 위, 음수는 아래
# - 방향 무시하고 크기만 보려면 절댓값 필요

z = (vib_s - np.mean(vib_s)) / np.std(vib_s)
print(vib_s[np.abs(z) > 2])

# 실습2
temp = col(1)
q1, q3 = np.percentile(temp, [25,75])
upper = q3 + 1.5 * (q3 - q1)
print(temp[temp > upper])
print(int((temp > upper).sum()))




# 실습3
cyc = col(0)
temp = col(1)

z = (temp - np.nanmean(temp)) / np.nanstd(temp)
abnormal = np.abs(z) > 2
print(cy[abnormal].astype(int))
print(round(np.abs(z).max(), 2))


# 실습4
cyc = col(0)
temp = col(1)

high = np.namean(temp) + 3 * np.nanstd(temp)
print(round(high, 2))
print(cyc[temp > high].astype(int))


# 센서 간 상관관계 - corrcoef
# - 세기는 절댓값이 정함. +0.99와 -0.99는 세기가 똑같고 방향만 반대
# - 양수: 한쪽이 오르면 다른 한쪽도 오름 / 음수는 반대
# - 0에 가까움 - 관계가 없는 상태

temp = np.array([70, 72, 74, 76, 78])
vib = np.array([2.0, 2.2, 2.5, 2.7, 3.0])
print(np.round(float(np.corrcoef(temp, vib)[0, 1]), 3))

# 
print(np.round(np.corrcoef(temp, vib), 3))

data = np.array([[70., 72., 74.], [2.0, 2.2, 2.5]])
print(np.round(np.mean(data, axis = 1), 2))
print(np.round(np.mean(data, axis = 0), 2))

# 실습5
temp = col(1)
ce = col(3)

corr = np.corrcoef(temp, ce)
print(round(corr[0, 1], 2))
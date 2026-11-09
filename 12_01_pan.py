# 변화적 탐지
# - 누적 합으로 찾는 원리
# - 각 값에서  전체 평균을 빼면 평균보다 작은 값은 음수, 큰 값은 양수
# - 해당 값들을 앞에서부터 누적하면 평균보다 낮은 구간에서는 계속 내려가고,
# - 평균보다 높은 구간에서는 계속 올라감
# - 그래서 누적 곡선이 가장 낮아지는 자리가 내려가기를 멈추고 올라가기 시작한 자리

v = np.array([2.0, 2.1, 2.0, 5.0, 5.2, 5.1])
cs = np.cumsum(v - np.mean(v))
print(np.argmin(cs))

# 실습7
cyc = col(0)
temp = col(1)

cs = np.cumsum(temp - np.nanmean(temp))
k = np.argmin(cs)
print(int(cyc[k]), round(cs[k], 1))

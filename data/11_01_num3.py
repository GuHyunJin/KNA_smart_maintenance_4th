import numpy as np

F = 'data/11_diecasting_series.csv'

# ct = np.genfromtxt(F, delimiter=",", skip_header=1, usecols=1)
# print(ct.shape, ct.dtype)

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# 자리 찾기
# fancy indexing : 여러 위치 한번에 추출 가능 (떨어진 자리도 한번에 가능)

# vib = np.array([2.1, 2.3, 2.0, 5.8])
# pick = np.array([0, 3])
# print(vib[pick])

# 정렬과 정렬 순서
# - sort, argsort : 원래 자리 번호 돌려줌

# print(np.sort(vib))
# print(np.argsort(vib))

# 실습1
cyc = col(0)
ct = col(1)

idx = ct.argmax()
print(cyc[idx], ct[idx])

# diff
vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
change = np.diff(vib)
print(np.round(change, 1))
print(np.argmax(change))
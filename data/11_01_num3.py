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
# cyc = col(0)
# ct = col(1)

# idx = ct.argmax()
# print(cyc[idx], ct[idx])

# # diff
# vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
# change = np.diff(vib)
# print(np.round(change, 1))
# print(np.argmax(change))

# 실습2
# cyc = col(0)
# ct = (0)

# change = np.abs(np.diff(ct))
# j = change.argmax()
# print(int(cyc[j]), int(cyc[j], idx(cyc[j])))


# clip
# pres = np.array([4.5, 9999.0, 4.6, -1.0])
# fixed = np.clip(pres, 0, 10)
# print(fixed)       #[ 4.5 10.   4.6  0. ]


# # cumsum - 누적 합
# defects = np.array([0, 1, 0, 2, 3, 5])
# print(np.cumsum(defects))

# np.where 심화
# vib = np.array([2.1, 3.5, 2.0, 6.2])
# label = np.where(vib >= 5, 2, np.where(vib >= 3, 1, 0))  # 5 이상: 2, 3 이상: 1, 나머지: 0
# print(label)   #[0 1 0 2]

# # unique - 중복 정리
# # - return_counts 옵션: 각 종류의 개수 확인
# status = np.array([0,0,1,0,2,1,0])
# kinds, counts = np.unique(status, return_counts=True)
# print(kinds)   #[0 1 2]
# print(counts)  #[4 2 1]


# 실습3
# cyl = col(2)
# cyl[0] = 9999
# print(round(cyl.mean(), 1))

# fixed = np.clip(cyl, 100, 300)
# print(round(fixed.mean(), 1))

# # 실습4
# ct = col(1)
# label= np.where(ct >= 1000, 2, np.where(ct >= 50, 1, 0))

# kinds, counts = np.unique(label, return_counts=True)
# print(kinds, count)
# print(count / count.sum())



# # any, all - 조건 충족 여부 판정
# # - any: 하나라도 만족하면 True
# # - all: 모두 만족해야 True

# vib = np.array([2.1, 3.5, 2.0, 6.2])
# print(np.any(vib > 5))
# print(np.all(vib < 10))

# # concatenate, stack - 배열 합치기
# am = np.array([2.0, 2.1, 2.2])
# pm = np.array([2.3, 2.4, 2.5])
# print(np.concatenate([am, pm]))
# print(np.stack([am, pm]))


# 실습5
# M = np.stack([col(1), col(2), col(3), col(4)])
# print(M.shape)

# recent = M[:, -10:]
# print(recent.shape)

# 실습6
cyc, ct, cyl = col(0), col(1), col(2)
i = ct.argmax()
print(int(cyc[i]), ct[i])
ch = np.abs(np.diff(ct))
j = ch.argmax()
print(int(cyc[j]), int(cyc[j+1]))

warn = np.where((ct >= 50) , (cyl < 150), 1, 0)
print(round(warn.mean(), 2))

top = np.argsort(ct)[::-1][:3]
print(top)
print(cyc[top])

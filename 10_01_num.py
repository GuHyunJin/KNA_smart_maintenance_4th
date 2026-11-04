import numpy as np

# 리스트 vs 배열
# 1. 리스트
# - 서로 다른 자료형도 같이 존재 가능
# - 계산 느리고 반복문을 돌아야 함
list = [70, 72, 71]
print(list*2)
print(v * 2 for v in list)


temp = np.array([70,72,71])
print(temp)     #[70 72 71]

print(temp + 2)  #[72 74 73]

# 튜플로 배열 만들기
print(np.array((1, 2, 3)))

# 실습1
temp = np.array([70,72,71,78,79,80])
print("측정 온도:", temp)

print("화씨", temp * 1.8 + 32)


# 배열 생성
# np.arange(시작, 끝, 간격) : 연속 정수
# - 끝값은 포함되지 않음
print(np.arange(5))           #[0 1 2 3 4]
print(np.arange(0, 10, 2))    ##[0 2 4 6 8]

# np.linspace(시작, 끝, 개수) : 균등 분할
# - 끝값 포함
print(np.linspace(0, 1, 5))    #
print(np.linspace(0, 10, 5))

# 실습2
scale = np.linspace(0, 70, 8)
print(scale)

# 실습3
idx = np.arange(0, 40, 5)
print(idx)


# 배열 속성
# - ndim, shape, size, dtype
# - 속성은 괄호x

a = np.array([1,2,3])
b = np.array([[1,2,3], [4,5,6]])

print("dim:", a.ndim, b.ndim)
print("shape:", a.shape, b.shape)
print("size:", a.size, b.size)

# 실습4
# 4시점 x 2센서
data = np.array([[30, 15.44], [30,18.69]])
data = np.array([[30, 62.48], [30,18.37]])
print(data.ndim)
print(data.shape)
print(data.size)

# 실습5
amp = np.array([15.44, 18.69, 62.48, 18.37])
print(amp.dtype)
cut = amp.astype(int)
print(cut)

# reshape()로 바꾸기
# - -1 사용 시 자동 계산
c = np.arange(12)
print(c.reshape(3, 4))

# faltten() - 1차원 만듬
b3 = np.array([[1,2,3], [4,5,6]])
print(b3.flatten())

# 실습6
ct = np.array([21156, 15611, 15633, 15601,
               15607, 15557, 15557, 15636,
               15600, 15634, 21207, 15554])
print(ct.reshape(3, 4))


# 실습 7
# 4시점 × 3센서(온도, 전류, 회전수)를 한 줄로 이어 놓은 상태
flat = np.array([30, 15.44, 4603, 30, 18.69, 4603,
                 30, 62.48, 4967, 30, 18.37, 4603])

table = flat.reshape(4, 3)
print(table)
print(table.flatten())

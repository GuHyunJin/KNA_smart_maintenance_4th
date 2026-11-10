import pandas as pd
import numpy as np

F = 'data/12_metro_compressor.csv'
FD = 'data/12_metro_digital.csv'

df = pd.read_csv(F)


df = pd.read_csv(F)

# 데이터 미리보기 및 구조 파악
# )1 앞 부분 미리보기
# - df.head() - 위에서 5줄, 숫자 지정 가능
# print(df.head())

# # 2 뒷 부분 미리보기
# # - df.tail() - 밑에서 5줄, 숫자 지정 가능
# print(df.tail())

# # 3 행/열 크기
# # - df.shpae
# print(df.shape)

# # 4 열 이름 목록
# # - df.columns          - 인덱스 형태로 출력
# # - df.columns.tolist() - 목록으로 보기 좋게
# print(df.columns.tolist())

# # 5 행 번호표
# # - df.index
# # print(df.index)   #RangeIndex(start=0, stop=200, step=1)
# # ㄴ 0부터 시작, 199까지 1씩

# # 6 열별 자료형
# # - df.dtypes
# print(df.dtypes)
# print("-------------------------------")
# print(pd.read_csv(FD).dtypes)
# # 측정시각       str
# # 압축기      int64
# # 타워       int64
# # 저압스위치    int64
# # dtype: object
# df2 = pd.read_csv(FD, dtype={"압축기": str})

# 7 전체 구조
# - df.info()
# df.info()
# print(df.info())

# 기초 통계 요약
# - 숫자 열들의 평균/최대/최소 등을 한번에 자동 계산. 글자 열은 자동으로 빠짐

# print(df.describe().round(2))

# # 특정 조건에서의 통계 필요 시
# state = df["가동상태"].values
# cur = df["모터전류"].values
# print(round(float(np.mean(cur[state =="가동"]))))

# 

# 실습1
# df = pd.read_csv(F)
# print(df.head())
# print(df.tail())

# 실습2
# df = pd.read_csv(F)
# print(df.shape)
# print(df.columns.tolist())
# print(df.dtypes)
# print(df.head())


# 실습3
# df = pd.read_csv(F)
# print(df.info())

# 실습4
# df = pd.read_csv(F)
# print(df.describe().round(2))

# 실습6
FS = 'data/12_metro_small.csv'
df = pd.read_csv(FS)
print(df.head(3))
print('크기:', df.shape)
print(df.info())

stats = df.describe()

miss = int(df["오일온도"].isna().sum())
print('오일온도 결측:', miss, '건')

mean_current = round(float(stats["모터전류"]["mean"]), 2)
median_current = round(float(stats["모터전류"]["50%"]), 2)
print("모터전류 평균/중앙값:", mean_current, median_current)
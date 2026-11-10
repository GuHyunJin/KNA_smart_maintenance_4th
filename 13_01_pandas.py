import pandas as pd

F_SMALL = 'data/13_diecasting_small.csv'
F_SHOT = 'data/13_diecasting_shot.csv'

# 열 골라내기
# - 열 이름
# df = pd.read_csv(F_SMALL)

# print("이름으로 앞 3개:", df["실린더압력"].head(3).tolist())

# # 단일 열 선택
# # - df["실린더압력"]
# print(df["실린더압력"])

# # 복수 열 선택
# # - 여러 열은 이름들을 리스트로 묶어서 넣는다
# # - 결과 값은 DataFrame
# print(df[["형체력", "실린더압력"]])



# 실습1
print(df["실린더압력"])
print(df[["형체력", "실린더압력"]])


# 실습2
print(df.loc[0, '샷'])
print(df.loc[0] ['샷'])

sorted = df.sort_values('형체력', ascending=False)
print(sorted.loc[0, '샷'])
print(sorted.iloc[0] ['샷'])

# 실습3
print(list(df.columns))

a = df.loc[0:4, ['실린더압력', '형체력']]
print(a.shape)

b = df.iloc[0:5, [2,6]]
print(b.shape)
print(a.equals(b))

# 실습4
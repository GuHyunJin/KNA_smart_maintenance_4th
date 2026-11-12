import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)
print(df.shape, qc.shape)

# # 1. 빈도
# # - value_counts
# # - pd.cut

# print(df['냉각기상태'].value_counts())

# print(df['밸브상태'].value_counts())

# # 개수 - 비율 : normalize
# counts = df["result"].value_counts()
# ratios = df["result"].value_counts(normalize=True)
# print(counts)
# print(ratios.round(3))
# print((ratios * 100).round(1))

# # pd.cut
# band = pd.cut(df["온도"], bins=[0, 40, 50 , 200], labels=["낮음", "보통", "높음"], right=True)
# print(band.value_counts(sort=False))




# print(df.shape)
# valve_counts = df["밸브상태"].value_counts()
# load_counts = df["운전부하"].value_counts()
# print(valve_counts)
# print(df["밸브상태"].value_counts(normalize=True).round(3))
# print(load_counts)
# print(df["운전부하"].value_counts(normalize=True).round(3))

# for counts in [valve_counts, load_counts]:
#     print("가장 많은 값:", counts[counts == counts.max()])
#     print("가장 적은 값:", counts[counts == counts.min()])


# counts = qc["검사결과"].value_counts()
# ratios = qc["검사결과"].value_counts(normalize=True)
# print(counts, ratios.round(3))
# print("불합격 비율:", round(ratios.loc["불합격"] * 100, 1), "%")


# print(df["진동"].min(), df["진동"].max())
# band_v = pd.cut(
#     df["진동"], bins=[0, 0.6, 0.7, 10],
#     labels=["약함", "보통", "강함"], right=True
# )

# counts = band_v.value_counts()
# print(counts)
# print("검산:", counts.sum(), "구간 미지정:", band_v.isna().sum())
# print("최대 구간:", counts[counts == counts.max()])
# print("최소 구간:", counts[counts == counts.min()])

# means = df.groupby("냉각기상태")["온도"].mean()
# print(means.round(2))

# print(df.groupby("냉각기상태")["온도"].max())


# counts = df.groupby("냉각기상태").size()
# means = df.groupby("냉각기상태")["온도"].mean()
# maxima = df.groupby("냉각기상태")["온도"].max()
# print(counts)
# print(means.round(2))
# print(maxima)
# print("평균 차이:", round(means.max()-means.min(), 2))


total = df["밸브상태"].value_counts()
print(total)

broken = df[df["result"] == "고장"]
broken_counts = broken.groupby("밸브상태").size()
print(broken_counts)

broken_counts = broken_counts.reindex(total.index, fill_value = 0)
ratios = broken_counts / total
print(ratios.sort_values(ascending=False).round(3))


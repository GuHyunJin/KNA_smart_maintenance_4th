import pandas as pd

F = 'data/12_metro_compressor.csv'

# 실습2
sel = pd.read_csv(F, usecols=["측정시각", "오일온도", "모터전류"])
print(sel.shape)

part = pd.read_csv(F, nrows=20)
print(part.shape)

# 실습3
a = pd.read_csv(FS)
print(a.shape)

b = pd.fread_csv(FS, sep=";", encoding="utf-8")
print(b.shpae)
print(b.columns.tolist())

# 실습4

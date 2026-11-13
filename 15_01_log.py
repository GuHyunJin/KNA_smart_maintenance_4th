import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)

# s = pd.Series([10, None, 20])
# print(s.mean())
# print(s + 1)

# 실습1
log_raw = pd.read_csv(F_LOG)
print(log_raw.shape)
print(log_raw.isna().sum())
print(int(log_raw["사출압력"].eq(0).sum()))
print(int(log_raw["스크루속도"].eq(-999).sum()))
print(int(log_raw["배럴온도"].eq(999).sum()))
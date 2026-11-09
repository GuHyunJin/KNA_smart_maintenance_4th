import numpy as np

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# 실습1
vib = col(2)
print(np.isnan(vib).sum())
print(round(np.isnan(vib).mean(), 2))
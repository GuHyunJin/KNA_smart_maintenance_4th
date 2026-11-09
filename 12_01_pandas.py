import numpy as np
import pandas as pd

F = 'data/12_metro_compressor.csv'

df = pd.read_csv(F)
print("데이터 크기:", df.shape)
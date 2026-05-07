#INSTAL LIBRARY PYTHON DASAR
import numpy as np
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
print(raw_data['Pendapatan'].quantile(q = 0.5))
print(np.quantile(raw_data['Pendapatan'],q=0.5))
print(raw_data[['Pendapatan','Harga']].agg(['mean', 'median']))
print(raw_data[['Pendapatan','Harga','Produk']].groupby('Produk').agg(['mean', 'median']))
print(raw_data.corr(numeric_only=True))
print(raw_data.corr(method= 'kendall', numeric_only=True))
print(raw_data.corr(method= 'spearman', numeric_only=True))

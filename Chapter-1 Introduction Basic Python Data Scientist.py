#instal library pyhton dasar
import pandas as pandas
import numpy as np
import matplotlib as pyplot
import scikit-learn as sns

#stats in python fundamental
import pandas as pd
import numpy as np
#DATASET CSV.XSL.XLSX
raw_data =pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
print (raw_data)
print (raw_data.head(10))
print (raw_data.tail(5))
print (raw_data.columns)
#METODE SHAPE
print (raw_data.shape)
print (raw_data.shape[0])
#method columns:
print (raw_data.columns)
#method isna missing value(DATASET HILANG)
print (raw_data.isna())
print (raw_data.isna().sum())
#STATISTIK DESKRIPTIF
print (raw_data.describe())
raw_data.max()
raw_data ['Harga'].max()
raw_data ['Harga'].min()
#JUMLAHKAN DENGAN SUM
print (raw_data.sum())
print (raw_data.sum(numeric_only=True))
print (raw_data[['Harga', 'Pendapatan']].sum())
#MEMILIH JENIS COLUMNS DAN BARIS
print (raw_data['Pendapatan'])
print (raw_data[['Jenis Kelamin','Pendapatan']])

# Mengambil data dari baris pertama (indeks 0) hingga baris ke-9 (indeks 9), yaitu sebanyak 10 baris
print (raw_data[:10])
# Mengambil data dari baris ke-4 (indeks 3) hingga baris ke-5 (indeks 4)
print (raw_data[3:5])
# Mengambil data dari baris ke-2 (indeks 1), baris ke-4 (indeks 3), dan baris ke-11 (indeks 10)
print (raw_data.loc[[1,3,10]])
# Mengambil kolom 'Jenis Kelamin' dan 'Pendapatan' dari baris ke-2 (indeks 1) hingga baris ke-10 (indeks 9)
print (raw_data[['Jenis Kelamin', 'Pendapatan']][1:10])
# Mengambil kolom 'Harga' dan 'Tingkat Kepuasan' dari baris ke-2 (indeks 1), baris ke-11 (indeks 10), dan baris ke-16 (indeks 15)
print (raw_data[['Harga', 'Tingkat Kepuasan']].loc[[1,10,15]])
#MEAN() NILAI RATA-RATA
# mengambil hanya data untuk produk 'A'
produk_A = raw_data[raw_data['Produk'] == 'A']
# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame
print (produk_A['Pendapatan'].mean())
# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame dengan numpy
print (np.mean(produk_A['Pendapatan']))

# MEDIAN() NILAI TENGAH
produk_A = raw_data[raw_data['Produk'] == 'A']
print (produk_A['Pendapatan'].median())
print (np.median(produk_A['Pendapatan']))

#VALUE COUNTS
# Melihat jumlah dari masing-masing produk
print (raw_data['Produk'].value_counts())
# mencari median atau 50% dari data menggunakan pandas
print (produk_A['Pendapatan'].quantile(q = 0.5))
# mencari median atau 50% dari data menggunakan numpy
print (np.quantile(produk_A['Pendapatan'],q = 0.5))



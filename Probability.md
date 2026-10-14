# Framework Probabilitas untuk Data Science

Framework ini memandu pembelajaran probabilitas dari konsep dasar sampai penggunaannya dalam analisis data, eksperimen, dan model machine learning. Tujuannya bukan hanya menghitung peluang, tetapi juga menafsirkan ketidakpastian untuk mengambil keputusan yang terukur.

## Hasil Belajar

Setelah mengikuti framework ini, pembelajar diharapkan mampu:

- Mendefinisikan kejadian dan menghitung peluang empiris maupun teoretis.
- Menggunakan peluang gabungan, bersyarat, independensi, dan Teorema Bayes.
- Memilih distribusi probabilitas yang sesuai dengan bentuk data.
- Menafsirkan nilai harapan, varians, interval kepercayaan, dan uji hipotesis.
- Menghubungkan probabilitas dengan eksperimen, klasifikasi, kalibrasi, dan keputusan bisnis.

## Peta Belajar

Ikuti urutan berikut. Setiap tahap menjadi dasar untuk tahap sesudahnya.

1. Eksperimen acak, ruang sampel, kejadian, dan peluang.
2. Aturan penjumlahan, perkalian, komplemen, dan peluang bersyarat.
3. Independensi dan Teorema Bayes.
4. Variabel acak, distribusi, nilai harapan, dan varians.
5. Sampling, hukum bilangan besar, dan teorema limit pusat.
6. Estimasi, interval kepercayaan, dan uji hipotesis.
7. Penerapan pada data science dan model machine learning.

## 1. Dasar Probabilitas

Eksperimen acak adalah proses yang hasilnya belum diketahui sebelum dilakukan, seperti memilih satu pelanggan atau mengamati apakah transaksi berhasil.

- **Ruang sampel** ($\Omega$): semua hasil yang mungkin.
- **Kejadian** ($A$): himpunan hasil yang menjadi perhatian.
- **Peluang** ($P(A)$): ukuran kemungkinan kejadian, bernilai antara 0 dan 1.

Untuk hasil yang sama-sama mungkin:

$$
P(A) = \frac{\text{jumlah hasil yang memenuhi } A}{\text{jumlah seluruh hasil yang mungkin}}
$$

Dalam data, peluang sering diestimasi sebagai proporsi kejadian:

$$
\hat{P}(A) = \frac{\text{jumlah observasi dengan kejadian } A}{n}
$$

Contoh: jika 42 dari 100 transaksi berhasil, estimasi tingkat keberhasilan adalah $42/100 = 0{,}42$ atau 42%. Selalu jelaskan unit observasi, periode pengamatan, dan definisi “berhasil”.

## 2. Aturan Peluang

### Komplemen

Peluang kejadian tidak terjadi:

$$
P(A^c) = 1 - P(A)
$$

### Gabungan

Peluang $A$ atau $B$ terjadi:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

Jika $A$ dan $B$ saling lepas, maka $P(A \cap B)=0$.

### Peluang Bersyarat

Peluang $A$ terjadi ketika $B$ diketahui terjadi:

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B)>0
$$

### Aturan Perkalian

$$
P(A \cap B) = P(A \mid B)P(B)
$$

## 3. Independensi dan Teorema Bayes

Dua kejadian independen jika mengetahui kejadian yang satu tidak mengubah peluang kejadian yang lain:

$$
P(A \mid B) = P(A)
\quad\Longleftrightarrow\quad
P(A \cap B) = P(A)P(B)
$$

Jangan menyamakan “tidak berkorelasi” dengan independen secara umum. Independensi adalah asumsi yang lebih kuat.

Teorema Bayes membalik peluang bersyarat:

$$
P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}
$$

Dalam konteks klasifikasi:

- $P(A)$ adalah prior, misalnya proporsi pelanggan churn sebelum fitur diperiksa.
- $P(B \mid A)$ adalah likelihood, misalnya peluang melihat pola tertentu pada pelanggan churn.
- $P(A \mid B)$ adalah posterior, yaitu peluang churn setelah pola tersebut diketahui.

Perhatikan **base rate**. Model atau tes dengan sensitivitas tinggi belum tentu menghasilkan probabilitas positif yang tinggi jika kejadian yang dicari sangat langka.

## 4. Variabel Acak dan Distribusi

Variabel acak memetakan hasil eksperimen ke nilai numerik. Distribusi probabilitas menjelaskan nilai yang mungkin dan peluangnya.

- **Diskret**: nilai terhitung, misalnya jumlah transaksi gagal.
- **Kontinu**: nilai dalam rentang, misalnya waktu pengiriman.
- **PMF**: peluang untuk nilai diskret.
- **PDF**: kepadatan untuk nilai kontinu; peluang dihitung sebagai luas pada interval.
- **CDF**: $F(x)=P(X\leq x)$, berlaku untuk variabel diskret maupun kontinu.

| Distribusi | Parameter | Contoh penggunaan |
|---|---|---|
| Bernoulli | $p$ | Satu transaksi berhasil atau gagal |
| Binomial | $n, p$ | Jumlah keberhasilan dalam $n$ percobaan independen |
| Poisson | $\lambda$ | Jumlah kejadian dalam interval waktu atau area |
| Uniform | $a, b$ | Nilai dengan kepadatan konstan pada rentang tertentu |
| Normal | $\mu, \sigma$ | Variasi pengukuran yang mendekati bentuk lonceng |

Jangan memilih distribusi hanya karena bentuk grafik tampak mirip. Periksa bagaimana data dikumpulkan, rentang nilai, asumsi independensi, dan kesesuaian parameter.

## 5. Nilai Harapan dan Varians

Nilai harapan adalah rata-rata jangka panjang dari variabel acak:

$$
E[X] = \sum_x xP(X=x)
\quad\text{atau}\quad
E[X] = \int_{-\infty}^{\infty} x f_X(x)\,dx
$$

Varians dan simpangan baku mengukur sebaran nilai:

$$
\operatorname{Var}(X)=E[(X-E[X])^2],
\qquad
\sigma_X=\sqrt{\operatorname{Var}(X)}
$$

Untuk dua variabel acak, kovarians menunjukkan arah perubahan bersama. Korelasi menstandarkan kovarians ke rentang $[-1,1]$, tetapi korelasi tidak membuktikan hubungan sebab-akibat.

## 6. Sampling dan Distribusi Sampling

- **Hukum bilangan besar**: rata-rata sampel cenderung mendekati nilai harapan saat jumlah observasi meningkat, dengan asumsi sampling yang sesuai.
- **Teorema limit pusat**: dalam kondisi umum, distribusi rata-rata sampel mendekati distribusi normal ketika ukuran sampel cukup besar.
- Ukuran sampel besar tidak memperbaiki bias akibat sampling yang buruk, definisi label yang keliru, atau data yang tidak representatif.

Bedakan distribusi nilai individual dari distribusi statistik sampel. Interval kepercayaan untuk rata-rata, misalnya, menggambarkan ketidakpastian estimasi rata-rata populasi, bukan sebaran sebagian besar individu.

## 7. Estimasi dan Uji Hipotesis

### Interval Kepercayaan

Interval kepercayaan merangkum ketidakpastian estimasi. Interval 95% dari prosedur yang sama akan mencakup parameter populasi pada sekitar 95% pengulangan sampling jangka panjang, dengan asumsi metode dan sampling terpenuhi.

Laporkan estimasi, interval, ukuran sampel, dan satuan. Jangan hanya melaporkan apakah interval “signifikan”.

### Uji Hipotesis

1. Rumuskan hipotesis nol ($H_0$) dan alternatif ($H_1$) sebelum melihat hasil.
2. Pilih statistik uji berdasarkan pertanyaan, tipe data, desain sampling, dan asumsi.
3. Tentukan tingkat signifikansi ($\alpha$) sebelum analisis.
4. Laporkan p-value bersama ukuran efek dan interval kepercayaan.
5. Periksa ukuran sampel, asumsi, banyaknya pengujian, serta relevansi praktis.

P-value bukan peluang bahwa $H_0$ benar dan bukan ukuran besar efek. Hasil “tidak signifikan” juga tidak membuktikan bahwa efek sama dengan nol.

## 8. Penerapan dalam Data Science

### Probabilitas Empiris dengan Dataset Iris

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
data = iris.frame.copy()
data["species"] = data["target"].map(dict(enumerate(iris.target_names)))

probability_virginica = data["species"].eq("virginica").mean()
probability_long_petal = data["petal length (cm)"].gt(5).mean()
probability_long_petal_given_virginica = data.loc[
    data["species"].eq("virginica"), "petal length (cm)"
].gt(5).mean()

print(f"P(virginica): {probability_virginica:.3f}")
print(f"P(petal length > 5 cm): {probability_long_petal:.3f}")
print(
    "P(petal length > 5 cm | virginica): "
    f"{probability_long_petal_given_virginica:.3f}"
)
```

### Bayes dan Base Rate

Contoh tes dengan prevalensi kejadian 1%, sensitivitas 95%, dan spesifisitas 90%:

```python
prevalence = 0.01
sensitivity = 0.95
specificity = 0.90

positive_predictive_value = (
    sensitivity * prevalence
    / (
        sensitivity * prevalence
        + (1 - specificity) * (1 - prevalence)
    )
)
print(f"P(kejadian | hasil tes positif): {positive_predictive_value:.1%}")
```

Walaupun sensitivitasnya 95%, nilai prediktif positifnya hanya sekitar 8,8% karena prevalensi rendah dan ada false positive. Angka ini mengilustrasikan mengapa base rate penting.

### Distribusi Binomial dan Interval Proporsi

```python
from scipy.stats import binom, binomtest

# Peluang memperoleh minimal 8 keberhasilan dari 10 percobaan,
# jika peluang berhasil pada tiap percobaan adalah 0,7.
probability_at_least_eight = binom.sf(7, n=10, p=0.7)
print(f"P(X >= 8): {probability_at_least_eight:.3f}")

# Interval proporsi Wilson dari 56 keberhasilan dalam 100 percobaan.
confidence_interval = binomtest(56, 100).proportion_ci(
    confidence_level=0.95,
    method="wilson",
)
print(confidence_interval)
```

## 9. Probabilitas dalam Machine Learning

Untuk klasifikasi probabilistik, model memperkirakan $P(Y=k\mid X=x)$. Gunakan probabilitas tersebut dengan memperhatikan:

- **Pemisahan data**: fit preprocessing hanya pada data train; evaluasi akhir pada data test yang tidak dipakai untuk pemilihan model.
- **Stratifikasi**: pertahankan proporsi kelas ketika sesuai, terutama untuk target yang tidak seimbang.
- **Kalibrasi**: probabilitas prediksi 0,8 idealnya sesuai dengan tingkat kejadian sekitar 80% pada kelompok prediksi serupa.
- **Ambang keputusan**: pilih threshold berdasarkan biaya false positive, false negative, kapasitas operasional, dan tujuan bisnis; threshold 0,5 tidak selalu optimal.
- **Ketidakseimbangan kelas**: accuracy dapat menyesatkan. Tambahkan precision, recall, F1, PR-AUC, dan confusion matrix sesuai konteks.
- **Perubahan distribusi**: pantau perubahan fitur, base rate, dan performa setelah model diterapkan.

Pada scikit-learn, `predict_proba` menghasilkan probabilitas kelas untuk estimator yang mendukungnya. Periksa urutan kelas melalui `model.classes_` dan evaluasi kualitas probabilitas dengan calibration curve, Brier score, atau log loss.

## Checklist Analisis Probabilitas

- Apakah kejadian, unit analisis, populasi, dan periode sudah didefinisikan?
- Apakah angka yang dilaporkan peluang teoretis atau estimasi dari sampel?
- Apakah asumsi independensi dan mekanisme sampling masuk akal?
- Apakah ukuran sampel dan ketidakpastian estimasi disertakan?
- Apakah base rate, ketidakseimbangan kelas, dan biaya kesalahan dipertimbangkan?
- Apakah probabilitas model sudah dikalibrasi dan diuji pada data terpisah?
- Apakah kesimpulan membedakan asosiasi, prediksi, dan sebab-akibat?

## Referensi Praktik Python

- `numpy.random.Generator`: simulasi dengan seed yang dapat direproduksi.
- `pandas`: menghitung frekuensi dan proporsi dari data aktual.
- `scipy.stats`: distribusi probabilitas, uji statistik, dan interval proporsi.
- `scikit-learn`: split data, model probabilistik, kalibrasi, dan metrik evaluasi.

# Framework Aljabar Linear untuk Data Science

Dokumen ini menghubungkan konsep aljabar linear dengan representasi data, regresi, reduksi dimensi, dan model machine learning. Fokusnya adalah memilih operasi yang tepat, memahami bentuk data, dan menjaga proses komputasi tetap stabil serta dapat direproduksi.

## Hasil Belajar

Setelah mengikuti framework ini, pembelajar diharapkan mampu:

- Membaca bentuk dan dimensi scalar, vector, matrix, serta tensor.
- Menggunakan perkalian dot, perkalian matriks, transpose, dan norma dengan benar.
- Menafsirkan rank, independensi linear, proyeksi, dan least squares.
- Memahami hubungan aljabar linear dengan regresi, regularisasi, dan PCA.
- Menyusun pipeline data yang konsisten, bebas leakage, dan terukur.

## Persiapan Environment

Contoh Python pada dokumen ini menggunakan NumPy dan scikit-learn:

```bash
python -m pip install numpy scikit-learn
```

## Peta Belajar

Ikuti urutan berikut dari fondasi matematika ke penerapan model.

1. Skalar, vector, matrix, tensor, dan notasi shape.
2. Operasi vector: penjumlahan, dot product, norma, dan cosine similarity.
3. Operasi matrix: transpose, perkalian, transformasi, dan sistem persamaan linear.
4. Rank, basis, independensi linear, proyeksi, dan least squares.
5. Nilai eigen, singular value decomposition, dan PCA.
6. Penerapan ke regresi, regularisasi, klasifikasi, dan embedding.
7. Arsitektur pipeline data science dan pemeriksaan numerik.

## 1. Representasi Data dan Shape

| Objek | Notasi | Contoh di NumPy | Makna |
|---|---|---|---|
| Skalar | $a \in \mathbb{R}$ | `3.14` | Satu nilai |
| Vector | $x \in \mathbb{R}^{p}$ | `np.array([1, 2, 3])` | $p$ fitur atau koordinat |
| Matrix | $X \in \mathbb{R}^{n \times p}$ | `np.array([[...], [...]])` | $n$ baris observasi dan $p$ kolom fitur |
| Tensor | $T \in \mathbb{R}^{d_1 \times \cdots \times d_k}$ | array berdimensi lebih dari dua | Data multi-dimensi, misalnya batch gambar |

Dalam data tabular, konvensi umumnya adalah:

- Baris menyatakan observasi atau sampel.
- Kolom menyatakan fitur.
- Matriks fitur memiliki shape `(jumlah_sampel, jumlah_fitur)`.
- Target klasifikasi biasanya vector panjang `jumlah_sampel`; target regresi dapat berupa vector atau matrix keluaran.

Selalu cek shape sebelum operasi. Banyak bug numerik berasal dari orientasi vector atau urutan kolom yang tidak konsisten.

```python
import numpy as np

features = np.array(
    [
        [5.1, 3.5, 1.4, 0.2],
        [4.9, 3.0, 1.4, 0.2],
    ]
)
print("Shape fitur:", features.shape)  # (2 sampel, 4 fitur)
print("Jumlah sampel:", features.shape[0])
print("Jumlah fitur:", features.shape[1])
```

## 2. Operasi Vector

### Penjumlahan dan Perkalian Skalar

Operasi dilakukan per elemen untuk vector dengan shape yang kompatibel:

$$
x + y = (x_1+y_1, \ldots, x_p+y_p),
\qquad
cx = (cx_1, \ldots, cx_p)
$$

### Dot Product

Dot product mengalikan komponen yang bersesuaian lalu menjumlahkannya:

$$
x^T y = \sum_{j=1}^{p} x_j y_j
$$

Untuk model linear, prediksi satu sampel sering ditulis sebagai $\hat{y}=w^T x+b$.

### Norma dan Jarak

Norma L2 mengukur panjang vector:

$$
\lVert x \rVert_2 = \sqrt{\sum_{j=1}^{p}x_j^2}
$$

Jarak Euclidean antara dua sampel adalah $\lVert x-y \rVert_2$. Cosine similarity membandingkan arah vector:

$$
\operatorname{cosine}(x,y)=\frac{x^T y}{\lVert x \rVert_2\lVert y \rVert_2}
$$

Normalisasi fitur penting untuk jarak dan dot product ketika skala antarfitur berbeda.

```python
first_vector = np.array([1.0, 2.0, 3.0])
second_vector = np.array([2.0, 1.0, 3.0])

dot_product = first_vector @ second_vector
euclidean_distance = np.linalg.norm(first_vector - second_vector)
cosine_similarity = dot_product / (
    np.linalg.norm(first_vector) * np.linalg.norm(second_vector)
)
print(dot_product, euclidean_distance, cosine_similarity)
```

## 3. Operasi Matrix dan Transformasi Linear

Jika $A$ memiliki shape $(m,k)$ dan $B$ memiliki shape $(k,n)$, maka:

$$
AB \in \mathbb{R}^{m \times n}
$$

Dimensi dalam harus sama. Dalam NumPy, operator `@` menyatakan perkalian matriks; `*` menyatakan perkalian elemen demi elemen.

- **Transpose** $A^T$ menukar baris dan kolom.
- **Identity** $I$ memenuhi $AI=IA=A$.
- **Transformasi linear** memetakan vector $x$ menjadi $Ax$.
- **Broadcasting** mengizinkan operasi pada shape tertentu; pastikan broadcasting memang sesuai makna data.

Contoh: matriks $X$ berukuran $(n,p)$ dan bobot $w$ berukuran $(p,)$ menghasilkan prediksi $Xw$ berukuran $(n,)$.

```python
matrix = np.array([[1.0, 2.0], [3.0, 4.0]])
weights = np.array([0.5, 1.5])

predictions = matrix @ weights
print("Shape matrix:", matrix.shape)
print("Shape weights:", weights.shape)
print("Prediksi:", predictions)
print("Transpose:\n", matrix.T)
```

## 4. Sistem Linear, Rank, dan Least Squares

Sistem persamaan linear ditulis sebagai:

$$
Ax=b
$$

Untuk matrix dengan n kolom, sistem Ax=b memiliki solusi unik jika rank(A)=n dan sistem konsisten. Jika rank(A)<n, sistem dapat tidak memiliki solusi atau memiliki banyak solusi. Kolom yang redundan atau fitur yang berkorelasi sempurna dapat membuat solusi tidak unik atau sensitif terhadap noise.

Untuk regresi, solusi sering dicari dengan meminimalkan jumlah kuadrat residual:

$$
\hat{\beta}=\underset{\beta}{\arg\min}\;\lVert X\beta-y\rVert_2^2
$$

Solusi least squares dapat dihitung dengan dekomposisi numerik. Hindari menghitung $\left(X^T X\right)^{-1}X^T y$ secara manual: pembentukan inverse dapat memperburuk error pembulatan dan kondisi numerik.

```python
# Kolom pertama adalah intercept; kolom kedua adalah satu fitur.
design_matrix = np.array(
    [
        [1.0, 1.0],
        [1.0, 2.0],
        [1.0, 3.0],
        [1.0, 4.0],
    ]
)
target = np.array([3.0, 5.0, 7.0, 9.0])

coefficients, _, rank, _ = np.linalg.lstsq(
    design_matrix,
    target,
    rcond=None,
)
predictions = design_matrix @ coefficients
mean_squared_error = np.mean((target - predictions) ** 2)

print(f"Intercept: {coefficients[0]:.2f}")
print(f"Slope: {coefficients[1]:.2f}")
print(f"Rank matrix: {rank}")
print(f"Mean squared error: {mean_squared_error:.2f}")
```

## 5. Geometri: Span, Proyeksi, dan Residual

- **Span** adalah seluruh kombinasi linear yang dapat dibentuk dari sekumpulan vector.
- **Basis** adalah kumpulan vector independen linear yang membentuk ruang tersebut.
- **Rank** adalah jumlah dimensi independen pada matrix.
- **Proyeksi** memetakan vector ke ruang yang dibentuk kolom-kolom matrix.
- **Residual** $r=y-X\hat{\beta}$ adalah bagian target yang tidak dijelaskan model.

Pada regresi least squares, residual tegak lurus terhadap ruang kolom $X$ (dengan asumsi solusi dan bentuk model yang sesuai). Interpretasi ini menjelaskan mengapa least squares memilih proyeksi target ke ruang prediksi model.

## 6. Nilai Eigen, SVD, dan PCA

Untuk matrix persegi $A$, vector eigen $v$ dan nilai eigen $\lambda$ memenuhi:

$$
Av=\lambda v
$$

Singular value decomposition memecah matrix menjadi:

$$
X=U\Sigma V^T
$$

SVD menjadi dasar banyak metode numerik, termasuk least squares dan reduksi dimensi. PCA mencari arah yang menangkap variasi terbesar pada fitur yang telah dipusatkan; skala fitur perlu dipertimbangkan sebelum PCA.

Alur PCA yang aman:

1. Pisahkan train dan test terlebih dahulu.
2. Fit imputasi, scaling, dan PCA hanya pada train.
3. Transformasikan test memakai parameter train yang sama.
4. Pilih jumlah komponen berdasarkan explained variance serta kebutuhan model.
5. Periksa interpretabilitas dan performa downstream, bukan hanya plot dua dimensi.

## 7. Penerapan pada Model Data Science

| Konsep aljabar linear | Penerapan |
|---|---|
| Dot product | Prediksi linear $Xw+b$ dan skor model |
| Norma/jarak | KNN, clustering, nearest neighbors, regularisasi |
| Perkalian matrix | Batch prediksi, transformasi fitur, neural network |
| Least squares | Regresi linear dan fitting parameter |
| Rank/dependensi | Deteksi fitur redundan atau multikolinearitas |
| Eigen/SVD | PCA, kompresi, analisis struktur data |
| Norm L1/L2 | Regularisasi sparse atau pengendalian besar bobot |

Untuk Ridge, objective umum adalah:

$$
\underset{\beta}{\min}\;\lVert X\beta-y\rVert_2^2 + \alpha\lVert\beta\rVert_2^2
$$

Untuk Lasso, penalti L2 diganti dengan $\alpha\lVert\beta\rVert_1$, yang dapat mendorong sebagian koefisien menjadi nol. Parameter regularisasi harus dipilih hanya menggunakan data train atau validasi, bukan test akhir.

## 8. Arsitektur Pipeline Data Science

```text
Data mentah
    -> validasi skema, tipe data, missing value, dan unit
    -> tentukan X (fitur) dan y (target)
    -> split train / validation / test
    -> fit preprocessing pada train saja
    -> transformasi fitur dengan urutan kolom yang konsisten
    -> fit model dan lakukan tuning pada train/validation
    -> evaluasi satu kali pada test yang tidak tersentuh
    -> catat metrik, versi data, parameter, dan asumsi
```

Prinsip implementasi:

- Simpan nama dan urutan fitur sebagai bagian dari kontrak model.
- Gunakan `Pipeline` atau `ColumnTransformer` agar scaling/imputasi ikut terfit pada train saja.
- Jangan menghitung inverse matrix secara manual untuk menyelesaikan regresi.
- Periksa `shape`, rank, nilai non-finite, skala, dan kondisi matrix bila hasil tidak stabil.
- Gunakan regularisasi atau kurangi fitur redundan ketika multikolinearitas bermasalah.
- Simpan seed, pembagian data, metrik, dan konfigurasi untuk reproduksibilitas.

Contoh pipeline regresi pada fitur numerik:

```python
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

regression_pipeline = make_pipeline(
    StandardScaler(),
    LinearRegression(),
)
regression_pipeline.fit(X_train, y_train)
predictions = regression_pipeline.predict(X_test)
```

Standardisasi di dalam pipeline mencegah parameter scaling dihitung dari test set. Untuk model linear tanpa regularisasi, scaling tidak selalu mengubah prediksi ideal, tetapi membantu konsistensi skala dan menjadi penting bagi banyak algoritma berbasis jarak atau penalti.

## Checklist Sebelum Memodelkan

- Apakah setiap baris benar-benar satu observasi dan setiap kolom satu fitur yang terdefinisi?
- Apakah shape $X$ dan $y$ sesuai serta urutan fitur konsisten?
- Apakah fitur memiliki skala yang masuk akal untuk algoritma yang digunakan?
- Apakah ada kolom redundan, rank rendah, atau multikolinearitas?
- Apakah seluruh preprocessing hanya di-fit pada train?
- Apakah solusi menggunakan metode numerik stabil dan regularisasi bila diperlukan?
- Apakah evaluasi memakai metrik yang sesuai dengan tujuan analisis?

## Referensi Praktik Python

- `numpy.ndarray`, `@`, `np.linalg.norm`, dan `np.linalg.lstsq` untuk operasi numerik.
- `pandas.DataFrame` untuk menjaga nama fitur dan urutan kolom.
- `scikit-learn` `Pipeline`, `StandardScaler`, PCA, dan estimator linear untuk workflow model.

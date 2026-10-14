# Project Data Scientist

Repositori pembelajaran data science berbasis Python. Materi disusun dari fondasi matematika dan pemrograman menuju pengolahan data, eksplorasi, pengumpulan data, dan pemodelan machine learning.

## Latar Belakang

Pekerjaan data science menggabungkan pemahaman domain, kualitas data, statistik, aljabar linear, pemrograman, dan evaluasi model. Proyek ini menjadi ruang latihan bertahap untuk menghubungkan konsep-konsep tersebut dengan analisis yang dapat dijalankan, bukan hanya kumpulan teori atau potongan kode.

Contoh di repositori ini bersifat edukatif. Dataset Iris dan data sintetis digunakan untuk menjelaskan alur kerja; hasilnya tidak otomatis mewakili performa produksi atau populasi bisnis.

## Tujuan

- Memahami fondasi matematika yang mendukung analisis dan machine learning.
- Mengolah dan memvalidasi data dengan Python, NumPy, dan pandas.
- Menggunakan visualisasi untuk mengeksplorasi distribusi, hubungan, dan anomali.
- Menyusun pembagian data, pipeline, model, dan evaluasi secara benar.
- Membangun kebiasaan kerja yang dapat direproduksi dan menghindari data leakage.

## Framework Pembelajaran

| Tahap | Fokus | Materi proyek |
|---|---|---|
| 1. Fondasi | Python, tipe data, struktur data, dan alur program | [Pengantar Python](Chapter-1%20Introduction%20Basic%20Python%20Data%20Scientist.py) |
| 2. Matematika | Probabilitas, statistik, dan aljabar linear | [Probabilitas](Probability.md), [Aljabar linear](Algebra-linear.md), [Mean, median, dan modus](MEAN-MEDIAN-MODUS.py) |
| 3. Komputasi data | Array, DataFrame, indeks, agregasi, dan membaca dataset | [NumPy](Numpy.py), [Pandas](Pandas.py) |
| 4. Akuisisi data | Request HTTP, parsing HTML, dan ekstraksi judul | [Web scraping](Webscrpng.py) |
| 5. Analisis data | Inspeksi, visualisasi, missing values, duplikasi, dan outlier | [Latihan analisis Iris](pratice_analisis_dasar_data_scientist_ml_komdigi.ipynb) |
| 6. Pemodelan | Regresi, fitur, train/test split, metrik, dan interpretasi hasil | [Studi kasus regresi linear](CASE_STUDY_MODEL_REGRESI_LINEAR.ipynb), [Latihan analisis Iris](pratice_analisis_dasar_data_scientist_ml_komdigi.ipynb) |

Urutan dapat disesuaikan dengan kebutuhan, tetapi fondasi matematika dan pemahaman data sebaiknya mendahului tuning model.

## Arsitektur Alur Kerja

```text
Pertanyaan domain
    -> akuisisi dan definisi sumber data
    -> validasi skema, tipe, missing values, duplikasi, dan rentang
    -> eksplorasi data dan visualisasi
    -> pemilihan target, fitur, dan strategi pembagian data
    -> preprocessing dan model dalam pipeline
    -> evaluasi dengan metrik yang sesuai
    -> interpretasi, dokumentasi asumsi, dan iterasi
```

### Lapisan Proyek

- **Konsep**: dokumen Markdown untuk probabilitas dan aljabar linear.
- **Eksperimen**: notebook untuk narasi analisis, visualisasi, dan evaluasi.
- **Contoh terfokus**: file Python untuk latihan NumPy, pandas, statistik dasar, dan scraping.
- **Environment**: virtual environment terpisah agar dependensi proyek tidak bercampur dengan Python sistem.

## Struktur Proyek

```text
.
├── Algebra-linear.md
├── Probability.md
├── Chapter-1 Introduction Basic Python Data Scientist.py
├── MEAN-MEDIAN-MODUS.py
├── Numpy.py
├── Pandas.py
├── Webscrpng.py
├── CASE_STUDY_MODEL_REGRESI_LINEAR.ipynb
├── pratice_analisis_dasar_data_scientist_ml_komdigi.ipynb
└── README.md
```

## Stack dan Tools

| Teknologi | Peran |
|---|---|
| Python 3 | Bahasa utama untuk latihan dan analisis |
| NumPy | Array, operasi numerik, dan aljabar linear |
| pandas | DataFrame, pembacaan, pembersihan, dan agregasi data |
| SciPy | Distribusi dan fungsi statistik |
| Matplotlib | Grafik dan visualisasi dasar |
| Seaborn | Visualisasi statistik dan eksplorasi multivariat |
| scikit-learn | Dataset latihan, preprocessing, model, split, dan evaluasi |
| requests dan Beautiful Soup | HTTP dan parsing HTML untuk contoh scraping |
| Jupyter Notebook / VS Code | Menjalankan notebook secara interaktif |
| Git dan GitHub | Version control dan publikasi repositori |

## Memulai

### 1. Siapkan environment

Contoh berikut untuk Linux atau macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy pandas scipy matplotlib seaborn scikit-learn requests beautifulsoup4 jupyter
```

Di Windows PowerShell, aktifkan environment dengan:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Jalankan contoh

```bash
python Numpy.py
python Pandas.py
python "Chapter-1 Introduction Basic Python Data Scientist.py"
python MEAN-MEDIAN-MODUS.py
python Webscrpng.py
jupyter lab
```

Buka notebook dari JupyterLab atau VS Code, pilih kernel dari `.venv`, lalu jalankan sel dari atas ke bawah. Beberapa contoh notebook memakai dataset bawaan scikit-learn; contoh lain dapat memerlukan akses internet.

## Praktik Data yang Digunakan

- Periksa nama kolom, tipe data, missing values, duplikasi, dan rentang nilai sebelum analisis.
- Jangan menghapus outlier secara otomatis; tentukan apakah nilai tersebut salah atau observasi yang valid.
- Pisahkan train dan test sebelum fit preprocessing. Gunakan `Pipeline` agar scaling dan transformasi lain tidak mempelajari informasi test.
- Gunakan stratifikasi untuk klasifikasi jika distribusi kelas perlu dipertahankan.
- Pilih metrik sesuai tujuan; accuracy saja tidak cukup untuk semua masalah.
- Catat seed, sumber data, asumsi, dan batasan eksperimen.
- Untuk scraping, patuhi ketentuan situs, robots policy, batas request, dan privasi data.

## Catatan Data dan Batasan

- Dataset dan contoh dibuat untuk pembelajaran, bukan sebagai benchmark produksi.
- URL dataset eksternal dan struktur halaman web dapat berubah atau tidak tersedia. Verifikasi sumber sebelum menjalankan contoh yang mengakses internet.
- Notebook sebaiknya dijalankan ulang dari atas setelah kernel di-restart agar urutan state konsisten.
- Repositori ini belum menetapkan `requirements.txt` atau `pyproject.toml`; daftar instalasi di atas adalah environment dasar untuk materi yang tersedia.

## Kontribusi

Perubahan materi sebaiknya menjaga contoh tetap dapat dijalankan, menyebutkan dependensi dan asumsi, serta menjelaskan sumber atau perubahan skema data. Untuk perubahan notebook, jalankan sel secara berurutan dan pastikan output tidak menyimpan hasil yang sudah kedaluwarsa.

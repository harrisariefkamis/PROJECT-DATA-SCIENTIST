"""Contoh analisis statistik dasar menggunakan pandas dan NumPy."""

# Instal dependensi dari terminal: python -m pip install pandas numpy
from urllib.error import URLError

import numpy as np
import pandas as pd


DATASET_URL = "https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv"
CSV_SEPARATOR = ";"
PRODUCT_NAME = "A"
REQUIRED_COLUMNS = {
	"Harga",
	"Pendapatan",
	"Jenis Kelamin",
	"Tingkat Kepuasan",
	"Produk",
}


def load_dataset() -> pd.DataFrame:
	"""Muat dataset statistik dari sumber CSV."""
	try:
		return pd.read_csv(DATASET_URL, sep=CSV_SEPARATOR)
	except (OSError, URLError, pd.errors.ParserError) as error:
		raise RuntimeError(f"Gagal memuat dataset: {error}") from error


def validate_dataset(data: pd.DataFrame) -> None:
	"""Pastikan kolom yang diperlukan tersedia sebelum analisis."""
	missing_columns = REQUIRED_COLUMNS.difference(data.columns)
	if missing_columns:
		missing_names = ", ".join(sorted(missing_columns))
		raise ValueError(f"Kolom dataset tidak ditemukan: {missing_names}")


def show_dataset_overview(data: pd.DataFrame) -> None:
	"""Tampilkan struktur, missing values, dan statistik dataset."""
	print("=== Ringkasan dataset ===")
	print("Ukuran (baris, kolom):", data.shape)
	print("Jumlah baris:", data.shape[0])
	print("Nama kolom:", data.columns.tolist())
	print("\nLima baris pertama:")
	print(data.head())
	print("\nLima baris terakhir:")
	print(data.tail())

	print("\nMissing values per kolom:")
	print(data.isna().sum())

	print("\nStatistik deskriptif:")
	print(data.describe())
	print("\nNilai maksimum harga:", data["Harga"].max())
	print("Nilai minimum harga:", data["Harga"].min())


def show_data_selections(data: pd.DataFrame) -> None:
	"""Contoh pemilihan kolom dan baris berdasarkan posisi."""
	print("\n=== Pemilihan data ===")
	print("Kolom pendapatan:")
	print(data["Pendapatan"])
	print("\nKolom jenis kelamin dan pendapatan:")
	print(data[["Jenis Kelamin", "Pendapatan"]])

	print("\nSepuluh baris pertama:")
	print(data.iloc[:10])
	print("\nBaris posisi ke-4 dan ke-5:")
	print(data.iloc[3:5])

	selected_positions = [position for position in (1, 3, 10) if position < len(data)]
	print("\nBaris pada posisi 2, 4, dan 11 yang tersedia:")
	print(data.iloc[selected_positions])

	print("\nKolom jenis kelamin dan pendapatan pada posisi 2 sampai 10:")
	print(data.loc[:, ["Jenis Kelamin", "Pendapatan"]].iloc[1:10])

	selected_positions = [position for position in (1, 10, 15) if position < len(data)]
	print("\nHarga dan tingkat kepuasan pada posisi 2, 11, dan 16 yang tersedia:")
	print(data.iloc[selected_positions][["Harga", "Tingkat Kepuasan"]])


def show_product_statistics(data: pd.DataFrame) -> None:
	"""Hitung statistik pendapatan untuk produk yang dipilih."""
	print("\n=== Statistik produk ===")
	print("Jumlah setiap produk:")
	print(data["Produk"].value_counts())

	product_income = data.loc[
		data["Produk"].eq(PRODUCT_NAME),
		"Pendapatan",
	]
	if product_income.empty:
		print(f"Tidak ada data untuk produk {PRODUCT_NAME}.")
		return

	print(f"\nRata-rata pendapatan produk {PRODUCT_NAME} (pandas):")
	print(product_income.mean())
	print("Rata-rata pendapatan (NumPy):")
	print(np.mean(product_income))

	print(f"\nMedian pendapatan produk {PRODUCT_NAME} (pandas):")
	print(product_income.median())
	print("Median pendapatan (NumPy):")
	print(np.median(product_income))

	print("Median melalui quantile (pandas):", product_income.quantile(0.5))
	print("Median melalui quantile (NumPy):", np.quantile(product_income, 0.5))


def main() -> None:
	"""Jalankan seluruh contoh analisis secara berurutan."""
	try:
		data = load_dataset()
		validate_dataset(data)
	except (RuntimeError, ValueError) as error:
		print(error)
		return

	show_dataset_overview(data)
	show_data_selections(data)
	show_product_statistics(data)


if __name__ == "__main__":
	main()



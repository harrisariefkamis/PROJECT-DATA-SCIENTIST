"""Contoh median, agregasi, dan korelasi dengan pandas dan NumPy."""

# Instal dependensi dari terminal: python -m pip install pandas numpy scipy
from urllib.error import URLError

import numpy as np
import pandas as pd


DATASET_URL = "https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv"
CSV_SEPARATOR = ";"
REQUIRED_COLUMNS = {"Pendapatan", "Harga", "Produk"}


def load_dataset() -> pd.DataFrame:
	"""Muat dataset statistik dari sumber CSV."""
	try:
		return pd.read_csv(DATASET_URL, sep=CSV_SEPARATOR)
	except (OSError, URLError, pd.errors.ParserError) as error:
		raise RuntimeError(f"Gagal memuat dataset: {error}") from error


def validate_dataset(data: pd.DataFrame) -> None:
	"""Pastikan kolom yang dibutuhkan analisis tersedia."""
	missing_columns = REQUIRED_COLUMNS.difference(data.columns)
	if missing_columns:
		missing_names = ", ".join(sorted(missing_columns))
		raise ValueError(f"Kolom dataset tidak ditemukan: {missing_names}")


def show_median(data: pd.DataFrame) -> None:
	"""Bandingkan perhitungan median menggunakan pandas dan NumPy."""
	income = data["Pendapatan"].dropna()
	if income.empty:
		print("Kolom Pendapatan tidak memiliki nilai untuk menghitung median.")
		return

	print("=== Median pendapatan ===")
	print("Pandas:", income.median())
	print("NumPy:", np.median(income))


def show_aggregations(data: pd.DataFrame) -> None:
	"""Tampilkan mean dan median keseluruhan serta per produk."""
	print("\n=== Mean dan median ===")
	print("Keseluruhan:")
	print(data[["Pendapatan", "Harga"]].agg(["mean", "median"]))

	print("\nBerdasarkan produk:")
	product_summary = data.groupby("Produk")[["Pendapatan", "Harga"]].agg(
		["mean", "median"]
	)
	print(product_summary)


def show_correlations(data: pd.DataFrame) -> None:
	"""Tampilkan matriks korelasi untuk kolom numerik."""
	numeric_data = data.select_dtypes(include="number")
	if numeric_data.shape[1] < 2:
		print("\nKorelasi tidak dapat dihitung: diperlukan minimal dua kolom numerik.")
		return

	print("\n=== Korelasi ===")
	for method in ("pearson", "kendall", "spearman"):
		print(f"\nMetode {method.title()}:")
		print(numeric_data.corr(method=method))


def main() -> None:
	"""Jalankan seluruh contoh analisis statistik."""
	try:
		data = load_dataset()
		validate_dataset(data)
	except (RuntimeError, ValueError) as error:
		print(error)
		return

	show_median(data)
	show_aggregations(data)
	show_correlations(data)


if __name__ == "__main__":
	main()

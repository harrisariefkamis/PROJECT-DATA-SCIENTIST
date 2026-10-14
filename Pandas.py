"""Contoh dasar penggunaan pandas untuk mengolah data."""

from pathlib import Path

import pandas as pd


CSV_PATH = Path("data.csv")
DATA = {
    "Nama": ["Haris", "Alex", "Indah"],
    "Usia": [25, 20, 21],
    "Kota": ["Jakarta", "Bandung", "Bogor"],
    "Profit": [3_000_000, 7_000_000, 9_000_000],
}
INDEX = ["Orang1", "Orang2", "Orang3"]


def main() -> None:
    """Tampilkan contoh DataFrame, Series, dan pembacaan CSV."""
    dataframe = pd.DataFrame(DATA, index=INDEX)

    print("DataFrame:")
    print(dataframe)

    print("\nKolom usia (Series):")
    print(dataframe["Usia"])

    print("\nUkuran DataFrame:", dataframe.shape)
    print("\nLima baris pertama:")
    print(dataframe.head())

    if CSV_PATH.is_file():
        csv_dataframe = pd.read_csv(CSV_PATH)
        print(f"\nData dari {CSV_PATH}:")
        print(csv_dataframe.head())
        print("Ukuran dataset:", csv_dataframe.shape)
    else:
        print(f"\nFile {CSV_PATH} tidak ditemukan; contoh pembacaan CSV dilewati.")


if __name__ == "__main__":
    main()

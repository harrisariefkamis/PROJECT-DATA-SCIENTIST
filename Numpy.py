"""Contoh dasar operasi array dengan NumPy."""

# Instal dependensi dari terminal: python -m pip install numpy
import numpy as np


RANDOM_SEED = 42


def show_array_creation(random_generator: np.random.Generator) -> None:
	"""Tampilkan beberapa cara membuat array NumPy."""
	print("=== Membuat array ===")
	one_dimensional = np.array([1, 2, 3, 4])
	two_dimensional = np.array([[1, 2], [3, 4]])
	print("Array 1D:", one_dimensional)
	print("Array 2D:\n", two_dimensional, sep="")

	random_array = random_generator.random((2, 3))
	range_array = np.arange(0, 10, 2)
	evenly_spaced_array = np.linspace(0, 1, 5)
	print("\nArray acak 2x3:\n", random_array, sep="")
	print("Rentang angka:", range_array)
	print("Angka dengan jarak merata:", evenly_spaced_array)


def show_array_operations() -> None:
	"""Tampilkan operasi aritmetika elemen demi elemen."""
	print("\n=== Operasi aritmetika ===")
	first_array = np.array([1, 2, 3])
	second_array = np.array([4, 5, 6])
	print("Penjumlahan:", first_array + second_array)
	print("Perkalian:", first_array * second_array)
	print("Pengurangan:", first_array - second_array)
	print("Pembagian:", first_array / second_array)


def show_indexing_and_reshaping() -> None:
	"""Tampilkan pengaksesan elemen dan perubahan bentuk array."""
	print("\n=== Indeks dan bentuk array ===")
	values = np.array([10, 20, 30, 40, 50])
	print("Elemen pertama:", values[0])
	print("Irisan indeks 1 sampai 3:", values[1:4])
	print("Elemen terakhir:", values[-1])

	reshaped_values = np.arange(6).reshape(2, 3)
	print("Array 2x3:\n", reshaped_values, sep="")


def show_combining_and_statistics() -> None:
	"""Tampilkan penggabungan array dan statistik deskriptif."""
	print("\n=== Penggabungan dan statistik ===")
	first_array = np.array([1, 2, 3])
	second_array = np.array([4, 5, 6])
	vertical_stack = np.vstack((first_array, second_array))
	combined_array = np.concatenate((first_array, second_array))
	print("Gabungan vertikal:\n", vertical_stack, sep="")
	print("Gabungan horizontal:", combined_array)

	values = np.array([1, 2, 3, 4, 5])
	print("Median:", np.median(values))
	print("Rata-rata:", np.mean(values))
	print("Simpangan baku:", np.std(values))
	print("Jumlah:", np.sum(values))


def show_matrix_operations(random_generator: np.random.Generator) -> None:
	"""Tampilkan perkalian matriks dan contoh data nilai ujian."""
	print("\n=== Operasi matriks ===")
	first_matrix = np.array([[1, 2], [3, 4]])
	second_matrix = np.array([[5, 6], [7, 8]])
	print("Hasil perkalian matriks:\n", np.matmul(first_matrix, second_matrix), sep="")

	transformation_matrix = np.array([[1, 0], [0, -1]])
	rotation_matrix = np.array([[0, -1], [1, 0]])
	print(
		"\nHasil perkalian matriks transformasi:\n",
		np.matmul(transformation_matrix, rotation_matrix),
		sep="",
	)

	scores = random_generator.uniform(0, 100, size=(5, 3))
	subject_medians = np.median(scores, axis=0)
	print("\nNilai untuk 5 siswa dan 3 mata pelajaran:\n", scores, sep="")
	print("Median setiap mata pelajaran:", subject_medians)


def main() -> None:
	"""Jalankan seluruh contoh NumPy secara berurutan."""
	random_generator = np.random.default_rng(RANDOM_SEED)
	show_array_creation(random_generator)
	show_array_operations()
	show_indexing_and_reshaping()
	show_combining_and_statistics()
	show_matrix_operations(random_generator)


if __name__ == "__main__":
	main()

#instal numpy python
pip instal numpy 
#pip instal numpy
#import numpy as np
import numpy as np
data1=np.array([1,2,3,4])
data2=np.array([[1,2],[3,4]])
print(data1)
print(data2)
#np.random
random_array = np.random.rand(2, 3)  # Array 2x3 nilai acak
print(random_array)
range_array = np.arange(0, 10, 2)  # Nilai dari 0 hingga 8 dengan langkah 2
print(range_array)  # Output: [0 2 4 6 8]
linspace_array = np.linspace(0, 1, 5)  # 5 nilai dari 0 hingga 1
print(linspace_array)  # Output: [0.   0.25 0.5  0.75 1.  ]
#Math numpy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # Output: [5 7 9]
print(a * b)  # Output: [4 10 18]
print(a - b)  # Output: [-3 -3 -3]
print(a / b)  # Output: [0.25 0.4  0.5 ]
#indeks numpy
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])       # Output: 10
print(arr[1:4])     # Output: [20 30 40]
print(arr[-1])      # Output: 50 (elemen terakhir)

#Ubah dimensi Array tanpa mengubah data:
arr = np.arange(6)  # [0 1 2 3 4 5]
reshaped_arr = arr.reshape(2, 3)  # Ubah ke bentuk 2x3
print(reshaped_arr)

#Gabungkan Array secara vertikal atau horizontal:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
stacked = np.vstack((a, b))  # Penumpukan vertikal
print(stacked)
# Output:
# [[1 2 3]
#  [4 5 6]]

concatenated = np.concatenate((a, b))  # Horizontal concatenation
print(concatenated)  # Output: [1 2 3 4 5 6]

#Hitung statistik deskriptif:
arr = np.array([1, 2, 3, 4, 5])

median = np.median(arr)  # Median: 3
mean = np.mean(arr)      # Rata-rata: 3.0
std_dev = np.std(arr)    # Standar deviasi: ~1.414
total = np.sum(arr)      # Jumlah: 15

print(median, mean, std_dev, total)

#Lakukan perkalian matriks (matrix multiplication):
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.dot(a, b)  # Perkalian matriks
print(result)
# Output:
# [[19 22]
#  [43 50]]

#Hasilkan skor ujian acak:
scores = np.random.rand(5, 3) * 100  # Skala ke 0-100
print(scores)
# Contoh Output:
# [[23.4 56.7 89.1]
#  [12.3 45.6 78.9]
#  [34.5 67.8 90.1]
#  [45.6 78.9 12.3]
#  [56.7 89.1 23.4]]

#Hitung median untuk setiap subjek:
subject_medians = np.median(scores, axis=0)
print(subject_medians)
# Contoh Output: [Median for each subject]
#Perkalian Matriks Transformasi:
#Kalikan matriks transformasi:
transformation1 = np.array([[1, 0], [0, -1]])
transformation2 = np.array([[0, -1], [1, 0]])
result = np.dot(transformation1, transformation2)
print(result)
# Output:
# [[ 0 -1]
#  [-1  0]]

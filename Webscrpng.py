#install pandas
#install bs4
#install beatifulsoup
#install selenium
import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL yang ingin di-scrape
url = 'https://www.kompas.com/'

# Mengirim permintaan GET ke URL
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
  # Membuat objek BeautifulSoup dari konten HTML
  soup = BeautifulSoup(response.content, 'html.parser')

  # Mencari semua berita utama (misalnya, dengan tag h3 most title)
  berita_utama = soup.find_all('h3', class_='most__title')

  # Menyimpan judul berita ke dalam list
  judul_berita = []
  for berita in berita_utama:
    judul_berita.append(berita.text.strip())

  # Membuat DataFrame pandas dari list judul berita
  df_berita = pd.DataFrame({'Judul Berita': judul_berita})


  # Menampilkan DataFrame
  print(df_berita)

else:
  print(f'Gagal mengakses URL. Kode status: {response.status_code}')

import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL yang ingin di-scrape
url = 'https://www.kompas.com/'

# Mengirim permintaan GET ke URL
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
  # Membuat objek BeautifulSoup dari konten HTML
  soup = BeautifulSoup(response.content, 'html.parser')

  # Mencari semua berita utama (misalnya, dengan tag h3 most title)
  berita_utama = soup.find_all('h3', class_='most__title')

  # Menyimpan judul berita ke dalam list
  judul_berita = []
  for berita in berita_utama:
    judul_berita.append(berita.text.strip())

  # Membuat DataFrame pandas dari list judul berita
  df_berita = pd.DataFrame({'Judul Berita': judul_berita})


  # Menampilkan DataFrame
  print(df_berita)

else:
  print(f'Gagal mengakses URL. Kode status: {response.status_code}')

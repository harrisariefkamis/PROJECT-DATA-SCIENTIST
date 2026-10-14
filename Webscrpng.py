"""Ambil judul berita dari halaman utama Kompas.com."""

# Instal dependensi dari terminal: python -m pip install pandas requests beautifulsoup4
import pandas as pd
import requests
from bs4 import BeautifulSoup


URL = "https://www.kompas.com/"
HEADLINE_SELECTOR = "h3.most__title"
REQUEST_TIMEOUT_SECONDS = 15
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0)"
}


def scrape_headline_titles(url: str) -> list[str]:
    """Ambil judul berita utama dari URL yang diberikan."""
    response = requests.get(
        url,
        headers=REQUEST_HEADERS,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    return [
        headline.get_text(" ", strip=True)
        for headline in soup.select(HEADLINE_SELECTOR)
        if headline.get_text(" ", strip=True)
    ]


def main() -> None:
    """Jalankan scraper dan tampilkan hasilnya sebagai tabel."""
    try:
        titles = scrape_headline_titles(URL)
    except requests.RequestException as error:
        print(f"Gagal mengambil data dari {URL}: {error}")
        return

    if not titles:
        print("Tidak ada judul berita yang ditemukan.")
        return

    headlines = pd.DataFrame({"Judul Berita": titles})
    print(headlines.to_string(index=False))


if __name__ == "__main__":
    main()

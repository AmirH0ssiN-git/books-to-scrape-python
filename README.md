# Books to Scrape

A Python web scraper for http://books.toscrape.com/ that exports scraped book data to JSON or CSV.

## Features
* Extracts book titles, prices, ratings, and availability across all pages.
* Interactive CLI prompt to choose export format (JSON or CSV).
* 1-second delay between requests to avoid overloading the target server.

## Requirements
* Python 3.8+
* `requests`
* `beautifulsoup4`
* `questionary`

## Project Structure
```text
books-to-scrape-python/
├── data/               # Output files (books.json, books.csv)
├── src/
│   └── book_scraper.py # Main scraper script
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Setup & Usage

1. Clone the repository and navigate into it:
   ```bash
   git clone https://github.com/AmirH0ssiN-git/books-to-scrape-python.git
   cd books-to-scrape-python
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the scraper:
   ```bash
   python src/book_scraper.py
   ```

# 📚 Books to Scrape - Python Web Scraper

A lightweight, efficient Python web scraper designed to extract book information from [books.toscrape.com](http://books.toscrape.com/). It parses the HTML structure and offers an interactive CLI to export data in either `JSON` or `CSV` format.

---

## ✨ Features

- **Automated Data Extraction:** Scrapes book titles, prices, availability, and ratings.
- **Interactive CLI Selection:** Choose between `JSON` and `CSV` export formats dynamically.
- **Structured Output:** Cleanly exports extracted data into `data/books.json` or `data/books.csv`.
- **Error Handling & Rate Limiting:** Built-in sleep intervals and resilient session handling.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **[Requests](https://requests.readthedocs.io/):** For making HTTP requests to target pages.
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/):** For parsing HTML and extracting target element data.
- **[Questionary](https://questionary.readthedocs.io/):** For interactive CLI user prompts.

---
## 📂 Project Structure

```text
books-to-scrape-python/
├── data/
│   ├── books.json          # Scraped output data (JSON format)
│   └── books.csv           # Scraped output data (CSV format)
├── src/
│   └── book_scraper.py     # Main web scraping script
├── .gitignore              # Ignored files (e.g., venv)
├── LICENSE                 # MIT License
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```
---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/books-to-scrape-python.git](https://github.com/YOUR_USERNAME/books-to-scrape-python.git)
   cd books-to-scrape-python
   ```

2. **Create and activate a virtual environment:**
   - **Windows:**
     ```cmd
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃 Usage

Run the main scraper script from the root directory:

```bash
python src/book_scraper.py
```

Upon execution, an interactive prompt will ask you to select the export format (`JSON` or `CSV`). The output file will be generated inside the `data/` directory.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

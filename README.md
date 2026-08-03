# 📚 Books to Scrape - Python Web Scraper

A lightweight, efficient Python web scraper designed to extract book information from [books.toscrape.com](http://books.toscrape.com/). It parses the HTML structure and exports the collected data into a structured `JSON` format.

---

## ✨ Features

- **Automated Data Extraction:** Scrapes book titles, prices, availability, and ratings.
- **Structured Output:** Cleanly exports extracted data into `data/books.json`.
- **Error Handling & Rate Limiting:** Built-in sleep intervals to respect server load.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **[Requests](https://requests.readthedocs.io/):** For making HTTP requests to target pages.
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/):** For parsing HTML and extracting target element data.

---

## 📂 Project Structure

books-to-scrape-python/
│
├── data/
│   └── books.json          # Scraped output data
├── src/
│   └── scraper.py          # Main web scraping script
├── .gitignore              # Ignored files (e.g., venv)
├── LICENSE                 # MIT License
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies

---

## 🚀 Getting Started

(###) Prerequisites
Make sure you have Python installed on your system.

(###) Installation

1. **Clone the repository:**
   git clone [https://github.com/YOUR_USERNAME/books-to-scrape-python.git](https://github.com/YOUR_USERNAME/books-to-scrape-python.git)
   cd books-to-scrape-python

2. **Create and activate a virtual environment:**
   - **Windows:**
     python -m venv venv
     .\venv\Scripts\activate
   - **Linux/macOS:**
     python3 -m venv venv
     source venv/bin/activate

3. **Install dependencies:**
   pip install -r requirements.txt

---

## 🏃 Usage

Run the main scraper script from the root directory:

python src/scraper.py

Upon execution, the output will be generated inside the `data/books.json` file.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
import csv
import json
import os
import time
import questionary
import requests
from bs4 import BeautifulSoup

# Using http to avoid TLS/HTTPS blocking issues
BASE_URL = "http://books.toscrape.com/"
current_url = BASE_URL

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

extracted_data = []

# Path setup
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
data_dir = os.path.join(project_dir, "data")
os.makedirs(data_dir, exist_ok=True)

page_counter = 1

session = requests.Session()
session.headers.update(headers)

while current_url:
    print(f"Scraping page {page_counter}: {current_url}")

    try:
        response = session.get(current_url, timeout=15)
        if response.status_code != 200:
            print(f"Server returned status code: {response.status_code}")
            break
    except requests.exceptions.RequestException as e:
        print(f"Connection error on page {page_counter}: {e}")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("article", class_="product_pod")

    # Extract details for each book on the current page
    for product in products:
        title = product.h3.a["title"]

        # Clean up the price text to convert it into a float
        price_text = product.find("p", class_="price_color").text
        price = float(price_text.replace("£", "").replace("Â", ""))

        # Build absolute URLs for book links and images
        relative_link = product.h3.a["href"]
        full_link = (
            BASE_URL + relative_link
            if "catalogue/" in relative_link
            else BASE_URL + "catalogue/" + relative_link
        )

        image_relative_src = product.find("div", class_="image_container").img["src"]
        image_full_url = BASE_URL + image_relative_src.replace("../", "")

        rating_classes = product.find("p", class_="star-rating")["class"]
        rating_word = rating_classes[1]

        extracted_data.append({
            "title": title,
            "price_GBP": price,
            "rating": rating_word,
            "url": full_link,
            "image_url": image_full_url,
        })

    # Check for pagination and construct the URL for the next page
    next_btn = soup.find("li", class_="next")

    if next_btn:
        next_page_rel = next_btn.a["href"]
        if "catalogue/" in next_page_rel:
            current_url = BASE_URL + next_page_rel
        else:
            current_url = BASE_URL + "catalogue/" + next_page_rel

        page_counter += 1
        time.sleep(1)
    else:
        current_url = None

# Avoid saving empty files on network failure
if not extracted_data:
    print("Scraping failed: 0 items extracted. Exiting without saving.")
    exit()

# Export format selection
user_choice = questionary.select(
    "Select export format:", choices=["JSON", "CSV"]
).ask()

if not user_choice:
    print("Cancelled by user.")
    exit()

file_extension = user_choice.lower()
file_path = os.path.join(data_dir, f"books.{file_extension}")

if user_choice == "JSON":
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)

elif user_choice == "CSV":
    fieldnames = ["title", "price_GBP", "rating", "url", "image_url"]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(extracted_data)

print(f"\nDone! Scraped {len(extracted_data)} items across {page_counter} pages.")
print(f"File saved to: {file_path}")
import json
import os
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
current_url = BASE_URL

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

extracted_data = []


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "products.json")

page_counter = 1

while current_url:
    print(f"Scraping page {page_counter}: {current_url}")

    
    try:
        response = requests.get(current_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            break
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred on page {page_counter}: {e}")
        print("Retrying or stopping gracefully...")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("article", class_="product_pod")

    for product in products:
        title = product.h3.a["title"]

        price_text = product.find("p", class_="price_color").text
        price = float(price_text.replace("£", "").replace("Â", ""))

        relative_link = product.h3.a["href"]
        full_link = (
            BASE_URL + relative_link
            if "catalogue/" in relative_link
            else BASE_URL + "catalogue/" + relative_link
        )

        image_relative_src = product.find("div", class_="image_container").img[
            "src"
        ]
        image_full_url = BASE_URL + image_relative_src.replace("../", "")

        rating_classes = product.find("p", class_="star-rating")["class"]
        rating_word = rating_classes[1]

        item = {
            "title": title,
            "price_GBP": price,
            "rating": rating_word,
            "url": full_link,
            "image_url": image_full_url,
        }
        extracted_data.append(item)

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


with open(file_path, "w", encoding="utf-8") as f:
    json.dump(extracted_data, f, ensure_ascii=False, indent=4)

print("\n" + "=" * 50)
print(
    f"SUCCESS! Scraped {len(extracted_data)} items across {page_counter} pages."
)
print(f"File saved cleanly at: {file_path}")
print("=" * 50)
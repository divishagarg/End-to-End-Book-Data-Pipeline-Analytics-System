import requests
from bs4 import BeautifulSoup


URL = "https://books.toscrape.com/"


def scrape_books():
    response = requests.get(URL)

    if response.status_code != 200:
        print("Failed to fetch website")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")[:20]

    book_data = []

    for book in books:
        # Title
        title = book.h3.a["title"]

        # Price
        price_text = book.select_one(".price_color").text.strip()
        price = float(price_text.replace("£", "").replace("Â", ""))

        # Availability
        availability = book.select_one(".availability").get_text(strip=True)
        in_stock = "In stock" in availability

        # Rating
        rating_class = book.select_one(".star-rating")["class"]
        rating_word = rating_class[1]

        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

        rating = rating_map[rating_word]

        book_data.append({
            "title": title,
            "price": price,
            "in_stock": in_stock,
            "rating": rating
        })

    return book_data


if __name__ == "__main__":
    books = scrape_books()

    for book in books:
        print(book)
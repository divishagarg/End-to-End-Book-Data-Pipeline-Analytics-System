from scraper import scrape_books
from database import BookDatabaseManager


books = scrape_books()

db = BookDatabaseManager()

for book in books:
    db.create_book(
        book["title"],
        book["price"],
        book["in_stock"],
        book["rating"]
    )

print("Books successfully added to database.")

all_books = db.get_all_books()

for book in all_books:
    print(book)
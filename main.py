from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import BookDatabaseManager


app = FastAPI()

db = BookDatabaseManager()


class Book(BaseModel):
    title: str
    price: float
    in_stock: bool
    rating: int


@app.get("/books")
def get_books():
    books = db.get_all_books()

    result = []

    for book in books:
        result.append({
            "id": book[0],
            "title": book[1],
            "price": book[2],
            "in_stock": bool(book[3]),
            "rating": book[4]
        })

    return result


@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = db.get_book(book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "id": book[0],
        "title": book[1],
        "price": book[2],
        "in_stock": bool(book[3]),
        "rating": book[4]
    }


@app.post("/books")
def create_book(book: Book):
    db.create_book(
        book.title,
        book.price,
        book.in_stock,
        book.rating
    )

    return {
        "message": "Book created successfully"
    }


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    existing_book = db.get_book(book_id)

    if existing_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.update_book(
        book_id,
        book.title,
        book.price,
        book.in_stock,
        book.rating
    )

    return {
        "message": "Book updated successfully"
    }


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    existing_book = db.get_book(book_id)

    if existing_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete_book(book_id)

    return {
        "message": "Book deleted successfully"
    }
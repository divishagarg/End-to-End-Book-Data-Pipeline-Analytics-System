import sqlite3


class BookDatabaseManager:

    def __init__(self, database_name="books.db"):
        self.database_name = database_name
        self.create_table()

    def create_table(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                price REAL NOT NULL,
                in_stock BOOLEAN NOT NULL,
                rating INTEGER NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    def create_book(self, title, price, in_stock, rating):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO books (title, price, in_stock, rating)
            VALUES (?, ?, ?, ?)
        """, (title, price, in_stock, rating))

        connection.commit()
        connection.close()

    def get_all_books(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")

        books = cursor.fetchall()

        connection.close()

        return books

    def get_book(self, book_id):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        )

        book = cursor.fetchone()

        connection.close()

        return book

    def update_book(self, book_id, title, price, in_stock, rating):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE books
            SET title = ?, price = ?, in_stock = ?, rating = ?
            WHERE id = ?
        """, (title, price, in_stock, rating, book_id))

        connection.commit()
        connection.close()

    def delete_book(self, book_id):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM books WHERE id = ?",
            (book_id,)
        )

        connection.commit()
        connection.close()





# if __name__ == "__main__":

#         db = BookDatabaseManager()

#         db.create_book(
#             "Test Book",
#             25.50,
#             True,
#             4
#         )

# books = db.get_all_books()

# for book in books:
#         print(book)
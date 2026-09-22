import requests
import pandas as pd


API_URL = "http://127.0.0.1:8000/books"


response = requests.get(API_URL)

if response.status_code == 200:

    books = response.json()

    df = pd.DataFrame(books)

    print(df)

    df.to_csv("exported_books.csv", index=False)

    print("\nData exported successfully to exported_books.csv")

else:
    print("Failed to fetch books from API")
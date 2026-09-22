# 📚 Book Data Pipeline

A Python-based Book Data Pipeline that scrapes book information from a website, stores the data in a SQLite database, provides CRUD operations through a FastAPI REST API, exports data to CSV, and generates a price-vs-rating visualization.

## 🚀 Features

- Web scraping using BeautifulSoup
- Data cleaning and conversion
- SQLite database storage
- CRUD operations for books
- FastAPI REST API
- Interactive Swagger API documentation
- CSV data export
- Price vs Rating visualization
- Simple Python client for API interaction

## 🛠️ Tech Stack

- Python
- BeautifulSoup
- Requests
- SQLite
- FastAPI
- Uvicorn
- Pandas
- Matplotlib

## 📂 Project Structure

```text
Book Data Pipeline/
│
├── scraper.py
├── database.py
├── load_books.py
├── main.py
├── client.py
├── plot.py
├── exported_books.csv
├── price_vs_rating.png
├── books.db
├── requirements.txt
├── .gitignore
└── README.md

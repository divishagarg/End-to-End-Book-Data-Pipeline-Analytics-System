Book Data Pipeline & Analytics System

An end-to-end Python project that scrapes book data, stores it in SQLite, exposes it through a FastAPI REST API, and performs basic data analysis and visualization.

Project Overview

This project processes the first 20 books from Books to Scrape.

The pipeline works as follows:

Books to Scrape
      ↓
   scraper.py
      ↓
   20 book records
      ↓
  load_books.py
      ↓
    SQLite
   books.db
      ↓
    main.py
   FastAPI API
      ↓
    client.py
      ↓
 Pandas DataFrame
      ↓
exported_books.csv

Data
  ↓
plot.py
  ↓
price_vs_rating.png

Features

Scrapes the first 20 books from Books to Scrape

Extracts:

Book title

Price

Stock availability

Rating from 1 to 5

Stores book records in SQLite

Uses an object-oriented database manager for CRUD operations

Provides REST API endpoints using FastAPI

Uses Requests and Pandas to consume the API

Exports data to CSV

Generates a price-vs-rating scatter plot using Matplotlib

Technologies Used

Python

Requests

BeautifulSoup4

SQLite

FastAPI

Uvicorn

Pandas

Matplotlib

Project Structure

Book Data Pipeline/
│
├── scraper.py              # Scrapes the first 20 books
├── database.py             # SQLite database and CRUD operations
├── load_books.py           # Loads scraped books into the database
├── main.py                 # FastAPI REST API
├── client.py               # API client and CSV export
├── plot.py                 # Scatter plot generation
│
├── exported_books.csv      # Exported book data
├── price_vs_rating.png     # Price vs Rating visualization
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files
└── README.md               # Project documentation

Setup

1. Clone the repository

git clone <your-repository-url>
cd Book-Data-Pipeline

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

Run the Project

Step 1: Scrape and load the books

Run:

python load_books.py

This scrapes the first 20 books and stores them in the SQLite database.

Step 2: Start the FastAPI server

Run:

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

Step 3: Open API documentation

FastAPI automatically provides interactive Swagger documentation:

http://127.0.0.1:8000/docs

API Endpoints

Method

Endpoint

Description

GET

/books

Get all books

GET

/books/{book_id}

Get one book by ID

POST

/books

Create a new book

PUT

/books/{book_id}

Update an existing book

DELETE

/books/{book_id}

Delete a book

Client Application

With the FastAPI server running, execute:

python client.py

The client:

Sends a GET request to /books

Receives the book data

Loads the response into a Pandas DataFrame

Prints the DataFrame

Exports the data to exported_books.csv

Data Visualization

Run:

python plot.py

This generates a scatter plot with:

X-axis: Price

Y-axis: Rating

The output is saved as:

price_vs_rating.png

Database Design

The SQLite database stores each book with the following fields:

Field

Description

id

Unique book ID

title

Full book title

price

Book price as a float

in_stock

Availability status

rating

Rating from 1 to 5

The BookDatabaseManager class handles CRUD operations:

Create

Read

Update

Delete

End-to-End Workflow

Scrape
  ↓
Store
  ↓
Expose through REST API
  ↓
Consume API
  ↓
Create DataFrame
  ↓
Export CSV
  ↓
Visualize

Author

Divisha Garg

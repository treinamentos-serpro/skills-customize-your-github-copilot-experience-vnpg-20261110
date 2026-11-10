import sqlite3
from contextlib import contextmanager

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

DATABASE_PATH = "books.db"

app = FastAPI(title="Books API with SQLite")


class BookInput(BaseModel):
    title: str
    author: str


@contextmanager
def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()


def initialize_database():
    with get_connection() as connection:
        # TODO: Create the books table if it does not exist.
        pass


initialize_database()


@app.get("/books")
def list_books():
    # TODO: Select all books and return each row as a dictionary.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Select one book by ID and return 404 if it does not exist.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    # TODO: Insert a book with parameters and return the created record.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # TODO: Update a book with parameters and return 404 if it does not exist.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete a book and return 404 if it does not exist.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")
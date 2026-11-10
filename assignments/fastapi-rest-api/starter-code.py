from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Frankenstein", "author": "Mary Shelley"},
]
next_book_id = 3


class BookInput(BaseModel):
    title: str
    author: str


@app.get("/health")
def get_health():
    # TODO: Return a JSON object indicating that the API is running.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.get("/books")
def list_books():
    # TODO: Return all books.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return the book, or respond with 404.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    # TODO: Create a book with a unique ID and return it.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # TODO: Update the book, or respond with 404 if it does not exist.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete the book, or respond with 404 if it does not exist.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")
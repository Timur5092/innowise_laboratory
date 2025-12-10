from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreate

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book

def update_book(db: Session, book_id: int, book_data: BookCreate):
    book = get_book(db, book_id)
    if book:
        for key, value in book_data.dict().items():
            setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book

def search_books(db: Session, query: str):
    return db.query(Book).filter(
        (Book.title.contains(query)) |
        (Book.author.contains(query)) |
        (Book.year == query if query.isdigit() else False)
    ).all()

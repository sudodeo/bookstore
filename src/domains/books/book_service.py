from typing import List
from sqlalchemy.orm import Session

from ...database import models
from ...database.schemas import CreateBook, UpdateBook


def create_book(db: Session, payload: CreateBook) -> models.Book:
    new_book = models.Book(**payload.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


def get_books(db: Session, skip: int = 0, limit: int = 10) -> List[models.Book]:
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int) -> models.Book:
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def update_book(db: Session, book_id: int, payload: UpdateBook) -> models.Book:
    book_query = db.query(models.Book).filter(models.Book.id == book_id)
    book = book_query.first()
    if not book:
        return None

    updated_book = payload.model_dump(exclude_unset=True)
    if not updated_book:
        return book

    book_query.update(updated_book)

    db.commit()
    db.refresh(book)

    return book


def delete_book(db: Session, book_id: int) -> None:
    db.query(models.Book).filter(models.Book.id == book_id).delete()
    db.commit()

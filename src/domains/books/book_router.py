from fastapi import Body, Path, Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from ...database.db import get_db
from ...database.schemas import CreateBook, ListResponse, Response, UpdateBook

from . import book_service

from ...swagger.book_request import (
    create_book_examples,
    update_book_examples,
    book_id_examples,
)

router = APIRouter(prefix="/books", tags=["Books"])


@router.get(
    "/",
    response_model=ListResponse,
    status_code=status.HTTP_200_OK,
    summary="Returns a list of all books in the bookstore.",
    # responses=
)
async def list_books(db: Session = Depends(get_db)):
    books = book_service.get_books(db)
    book_responses = [book.to_dict() for book in books]
    print(book_responses)
    return ListResponse(
        success=True,
        message="Books retrieved successfully",
        books=book_responses,
    )


@router.get(
    "/{book_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Returns a single book with the given book_id.",
)
def get_book(
    book_id: int = Path(openapi_examples=book_id_examples),
    db: Session = Depends(get_db),
):
    book = book_service.get_book(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} does not exist",
        )

    return Response(
        success=True, message="Book retrieved successfully", book=book.to_dict()
    )


@router.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
    summary="Creates a new book.",
)
async def create_book(
    book: CreateBook = Body(
        openapi_examples=create_book_examples,
    ),
    db: Session = Depends(get_db),
):
    new_book = book_service.create_book(db, book)
    return Response(
        success=True, message="Book created successfully", book=new_book.to_dict()
    )


@router.put(
    "/{book_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Updates a book with the given book_id.",
)
def update_book(
    book_id: int = Path(openapi_examples=book_id_examples),
    update_book: UpdateBook = Body(openapi_examples=update_book_examples),
    db: Session = Depends(get_db),
):
    book = book_service.get_book(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} does not exist",
        )

    updated_book = book_service.update_book(db, book_id, update_book)
    return Response(
        success=True, message="Book updated successfully", book=updated_book.to_dict()
    )


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletes a book with the given book_id.",
)
def delete_book(
    book_id: int = Path(openapi_examples=book_id_examples),
    db: Session = Depends(get_db),
):
    book = book_service.get_book(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} does not exist",
        )

    book_service.delete_book(db, book_id)
    return Response(success=True, message="Book deleted successfully")

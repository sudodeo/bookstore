from typing import List, Optional, Union
from pydantic import BaseModel, field_validator
from datetime import datetime


class BookBase(BaseModel):
    title: str
    author: str
    year: int
    isbn: str

    @field_validator("year")
    def validate_year(cls, value):
        current_year = datetime.now().year
        if value < 1000 or value > current_year:
            raise (ValueError("invalid year"))

        return value


class CreateBook(BookBase):
    pass


class UpdateBook(BookBase):
    title: Optional[str]
    author: Optional[str]
    year: Optional[int]
    isbn: Optional[str]


class BookResponse(BookBase):
    id: int
    created_at: datetime
    updated_at: datetime


class Response(BaseModel):
    success: bool
    message: str
    book: Union[BookResponse, None] = None

class ListResponse(BaseModel):
    success: bool
    message: str
    books: List[BookResponse] = []
from sqlalchemy import Column, Integer, String, func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    isbn = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

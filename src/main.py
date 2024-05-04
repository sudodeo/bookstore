from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .domains.books import book_router as books
from .database import models
from .database.db import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    root_path="/api/v1",
    version="3.0.0",
    title="Bookstore API",
    description="API to perform CRUD operations on books in a store",
)

SENSITIVE_HEADERS = ["server"]

origins = ["*"]
allowed_methods = ["GET", "POST", "PUT", "DELETE"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=allowed_methods)


@app.get("/")
async def get_home():
    return {"Documentation endpoint": "/docs"}


app.include_router(books.router)

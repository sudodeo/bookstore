# Bookstore API

This is a simple API for a bookstore. It allows you to create, read, update, and delete books.

## Endpoints

### GET /books

Returns a list of all books in the bookstore.

### GET /books/:id

Returns a single book with the given ID.

### POST /books

Creates a new book.

### PUT /books/:id

Updates a book with the given ID.

### DELETE /books/:id

Deletes a book with the given ID.

## Setup

- Clone this repository.

```bash
git clone https://github.com/sudodeo/bookstore.git
```

- Change into the project directory.

```bash
cd bookstore
```

- Setup environment variables.

```bash
cp .env.example .env
```

### Manual

- Create a virtual environment and activate it. (Optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install the dependencies.

```bash
pip install -r requirements.txt
```

- Run the application in dev mode.

```bash
make start-dev # if you have make installed
# or
uvicorn src.main:app --reload
```

### Docker

- Make sure you have Docker installed on your machine.

- Build and run the Docker image.

```bash
make docker-start # if you have make installed
# or
docker build -t bookstore-api . && docker run -p 8000:8000 --network="host" --env-file .env bookstore-api
```

- Open your browser and navigate to `http://localhost:8000/docs` to see the API documentation.

## Testing

To run the tests, use the following command:

```bash
make test # if you have make installed
# or
pytest
```

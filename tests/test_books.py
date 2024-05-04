from test_main import test_client, test_app


def test_create_book(test_client):
    response = test_client.post(
        "/books/",
        json={
            "title": "The Art of Computer Programming",
            "author": "Donald Knuth",
            "year": 1968,
            "isbn": "0-201-03801-3",
        },
    )
    assert response.status_code == 201
    assert response.json()["success"] is True
    assert response.json()["message"] == "Book created successfully"
    assert response.json()["book"]["title"] == "The Art of Computer Programming"
    assert response.json()["book"]["author"] == "Donald Knuth"
    assert response.json()["book"]["year"] == 1968
    assert response.json()["book"]["isbn"] == "0-201-03801-3"
    assert "id" in response.json()["book"]
    assert "created_at" in response.json()["book"]
    assert "updated_at" in response.json()["book"]


def test_create_book_invalid_payload(test_client):
    response = test_client.post("/books/", json={})
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Field required"
    assert response.json()["detail"][0]["type"] == "missing"
    assert response.json()["detail"][0]["loc"] == ["body", "title"]
    assert response.json()["detail"][1]["msg"] == "Field required"
    assert response.json()["detail"][1]["type"] == "missing"
    assert response.json()["detail"][1]["loc"] == ["body", "author"]
    assert response.json()["detail"][2]["msg"] == "Field required"
    assert response.json()["detail"][2]["type"] == "missing"
    assert response.json()["detail"][2]["loc"] == ["body", "year"]
    assert response.json()["detail"][3]["msg"] == "Field required"
    assert response.json()["detail"][3]["type"] == "missing"
    assert response.json()["detail"][3]["loc"] == ["body", "isbn"]


def test_get_books(test_client):
    response = test_client.get("/books/")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Books retrieved successfully"
    assert len(response.json()["books"]) == 1
    assert response.json()["books"][0]["title"] == "The Art of Computer Programming"
    assert response.json()["books"][0]["author"] == "Donald Knuth"
    assert response.json()["books"][0]["year"] == 1968
    assert response.json()["books"][0]["isbn"] == "0-201-03801-3"
    assert "id" in response.json()["books"][0]
    assert "created_at" in response.json()["books"][0]
    assert "updated_at" in response.json()["books"][0]


def test_get_book(test_client):
    response = test_client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Book retrieved successfully"
    assert response.json()["book"]["title"] == "The Art of Computer Programming"
    assert response.json()["book"]["author"] == "Donald Knuth"
    assert response.json()["book"]["year"] == 1968
    assert response.json()["book"]["isbn"] == "0-201-03801-3"
    assert "id" in response.json()["book"]
    assert "created_at" in response.json()["book"]
    assert "updated_at" in response.json()["book"]


def test_get_book_not_found(test_client):
    response = test_client.get("/books/0")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book with id 0 does not exist"


def test_update_book(test_client):
    response = test_client.put(
        "/books/1",
        json={
            "title": "The Art of Computer Programming",
            "author": "Donald Knuth",
            "year": 1969,
            "isbn": "0-201-03801-3",
        },
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Book updated successfully"
    assert response.json()["book"]["title"] == "The Art of Computer Programming"
    assert response.json()["book"]["author"] == "Donald Knuth"
    assert response.json()["book"]["year"] == 1969
    assert response.json()["book"]["isbn"] == "0-201-03801-3"
    assert "id" in response.json()["book"]
    assert "created_at" in response.json()["book"]
    assert "updated_at" in response.json()["book"]


def test_update_book_not_found(test_client):
    response = test_client.put(
        "/books/0",
        json={
            "title": "The Art of Computer Programming",
            "author": "Donald Knuth",
            "year": 1969,
            "isbn": "0-201-03801-3",
        },
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Book with id 0 does not exist"


def test_update_book_invalid_payload(test_client):
    response = test_client.put(
        "/books/1",
        json={
            "title": 15,
        },
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Input should be a valid string"
    assert response.json()["detail"][0]["type"] == "string_type"
    assert response.json()["detail"][0]["loc"] == ["body", "title"]


def test_delete_book(test_client):
    response = test_client.delete("/books/1")
    assert response.status_code == 204
    assert response.text == ""


def test_delete_book_not_found(test_client):
    response = test_client.delete("/books/0")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book with id 0 does not exist"


def test_delete_book_invalid_id(test_client):
    response = test_client.delete("/books/invalid")
    assert response.status_code == 422
    print(response.json())
    assert (
        response.json()["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )
    assert response.json()["detail"][0]["type"] == "int_parsing"
    assert response.json()["detail"][0]["loc"] == ["path", "book_id"]

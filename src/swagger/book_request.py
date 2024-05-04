create_book_examples = {
    "valid request body": {
        "summary": "Valid request payload",
        "value": {
            "title": "Beauty and the beast",
            "author": "Disney",
            "year": 2008,
            "isbn": "DIS1904482",
        },
    },
    "invalid year": {
        "summary": "Payload with invalid year",
        "value": {
            "title": "Beauty and the beast",
            "author": "Disney",
            "year": 0,
            "isbn": "DIS1904482",
        },
    },
}

update_book_examples = {
    "valid request body": {
        "summary": "Valid request payload",
        "value": {
            "title": "Beauty and the beast",
            "author": "Disney",
            "year": 2015,
            "isbn": "DIS1904482",
        },
    },
    "invalid data": {
        "summary": "Payload with invalid data",
        "value": {
            "title": "Beauty and the beast",
            "author": "Disney",
            "year": 2008,
            "isbn": 15,
        },
    },
}

book_id_examples = {
    "valid id": {
        "summary": "Valid id request returns 200",
        "value": 1,
    },
    "invalid id": {
        "summary": "Invalid id request returns 404",
        "value": 0,
    },
}

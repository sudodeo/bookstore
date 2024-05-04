import sys
from pathlib import Path

import pytest

root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(root_path))

import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.database.db import drop_test_database


@pytest.fixture(scope="module")
def test_app():
    return app


@pytest.fixture(scope="module")
def test_client(test_app):
    with TestClient(test_app) as client:
        yield client
    drop_test_database()


def test_read_main(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Documentation endpoint": "/docs"}

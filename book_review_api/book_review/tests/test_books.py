from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/books/", json={"title": "Book 1", "author": "Author 1"})
    assert response.status_code == 200
    assert response.json()["title"] == "Book 1"

def test_cache_miss():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

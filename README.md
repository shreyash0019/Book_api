# 📚 Book Review API

A simple and scalable Book Review API built with **FastAPI**, **PostgreSQL**, **Redis**, and **SQLAlchemy**. It provides RESTful endpoints to manage books and their reviews, with caching and basic testing included.

---

## 🚀 Features

* `GET /books`: List all books (with Redis cache)
* `POST /books`: Add a new book
* `GET /books/{id}/reviews`: Get reviews for a specific book
* `POST /books/{id}/reviews`: Add a review to a book
* Redis cache integration for listing books
* PostgreSQL database using SQLAlchemy ORM
* Alembic-ready structure for migrations
* Swagger/OpenAPI auto-docs
* Unit and integration tests using Pytest

---

## 📦 Installation

```bash
git clone https://github.com/shreyash0019/Book_api.git
cd book_api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 🛠️ Environment Setup

Make sure PostgreSQL and Redis are running locally.

Edit `app/db.py` if you want to change the DB URL:

```python
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/bookdb"
```

---

## 🗃️ Database Migrations (Alembic)

```bash
alembic init alembic
# Configure alembic.ini and env.py
alembic revision --autogenerate -m "init"
alembic upgrade head
```

---

## 🚀 Run the Server

```bash
uvicorn app.main:app --reload
```

Visit the docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ Running Tests

```bash
pytest
```

---

## 🧱 Project Structure

```
book_review/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── db.py
│   ├── cache.py
│   ├── dependencies.py
│   └── routes/
│       └── books.py
├── tests/
│   └── test_books.py
├── requirements.txt
```

---

## 📌 Notes

* Redis cache is used to speed up book listing.
* Reviews are fetched directly from DB with optimized access.
* Book reviews are tied by a foreign key and relational model.
* Swagger UI and Redoc are available out-of-the-box via FastAPI.

---

## 🤝 Contributing

Feel free to fork, raise issues, and open PRs. This project is a good starting point for scalable API design using FastAPI.

---



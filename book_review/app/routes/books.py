from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.dependencies import get_db
from app.cache import get_books_cache, set_books_cache
import json

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[schemas.Book])
async def read_books(db: Session = Depends(get_db)):
    cached = await get_books_cache()
    if cached:
        return json.loads(cached)
    books = crud.get_books(db)
    await set_books_cache(json.dumps([schemas.Book.from_orm(b).dict() for b in books]))
    return books

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.get("/{book_id}/reviews", response_model=list[schemas.Review])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews(db, book_id)

@router.post("/{book_id}/reviews", response_model=schemas.Review)
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, book_id, review)

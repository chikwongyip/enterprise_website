from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.news import News
from schemas.news import NewsCreate, News

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/api/news", response_model=list[News])
def get_news(db: Session = Depends(get_db)):
    return db.query(News).all()


@router.post("/api/news", response_model=News)
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    db_news = News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news


@router.put("/api/news/{news_id}", response_model=News)
def update_news(news_id: int, news: NewsCreate, db: Session = Depends(get_db)):
    db_news = db.query(News).filter(News.id == news_id).first()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    for key, value in news.dict().items():
        setattr(db_news, key, value)
    db.commit()
    db.refresh(db_news)
    return db_news


@router.delete("/api/news/{news_id}")
def delete_news(news_id: int, db: Session = Depends(get_db)):
    db_news = db.query(News).filter(News.id == news_id).first()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    db.delete(db_news)
    db.commit()
    return {"message": "News deleted successfully"}

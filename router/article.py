from auth.oauth2 import oauth2_scheme, get_current_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from schemas import ArticleCreate, Article
from db import db_article
from db.database import get_db
from schemas import UserBase


router = APIRouter(
    prefix = '/article',
    tags = ['article']
)

@router.post("/", response_model=Article)
def create_article(*, article: ArticleCreate, db: Session = Depends(get_db), user_id: int, current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, article, user_id)

@router.get('/{id}')#, response_model=Article)
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        'data': db_article.get_article(db, id),
        'current_user': current_user
    }
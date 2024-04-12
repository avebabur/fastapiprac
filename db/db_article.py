from .models import DbArticle
from schemas import ArticleCreate
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from exceptions import StoryException


def create_article(db: Session, article: ArticleCreate, user_id: int):
    if article.content.startswith('Once upon a time'):
        raise StoryException('No stories allowed!')
    new_article = DbArticle(
    title = article.title,
    content = article.content,
    published = article.published,
    user_id = user_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_article(db: Session, article_id: int):
    article = db.query(DbArticle).filter(DbArticle.id==article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {article_id} not found")
    return article

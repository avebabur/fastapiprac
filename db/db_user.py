import email
from click import password_option
from db.hash import Hash
from schemas import UserCreate
from sqlalchemy.orm.session import Session
from db.models import DbUser
from fastapi import HTTPException, status


def create_user(db: Session, user: UserCreate):
    new_user = DbUser(
        username = user.username,
        email = user.email,
        password = Hash.bcrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_user(db: Session, id:int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username {username} not found")
    return user

def update_user(db: Session, id: int, user: UserCreate):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    user.update({
        DbUser.username: user.username,
        DbUser.email: user.email,
        DbUser.password: Hash.bcrypt(user.password)
    })
    db.commit()
    return 'ok'

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return 'ok'

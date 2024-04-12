from gettext import dpgettext
from typing import List
from click import password_option
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserBase, User, UserCreate
from db.database import get_db
from db import db_user
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)

#create user
@router.post('/', response_model=User)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

#read user
# read all
@router.get('/', response_model=List[UserBase])
def get_all_users(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user) ):
    return db_user.get_all_users(db)

#read one
@router.get('/{id}', response_model=UserBase)
def get_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_user(db, id)


#update user
@router.post('/{id}/update')
def update_user(id: int, request: UserCreate, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.update_user(db, id, request)


#delete user
@router.get('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.delete_user(db, id)

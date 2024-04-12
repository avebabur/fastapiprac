from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    user_id: int


    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: list[Article] = []


    class Config:
        orm_mode = True


# class Article(BaseModel):
#     title: str
#     content: str
#     published: bool


# class UserBase(BaseModel):
#     username: str
#     email: str
#     password: str


# class UserDisplay(BaseModel):
#     username: str
#     email: str
#     items: list[Article] = []
#     class Config():
#         orm_mode = True

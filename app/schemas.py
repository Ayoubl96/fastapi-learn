from pydantic import BaseModel, EmailStr, conint
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: str


class UserOut(BaseModel):
    id: int
    create_at: datetime
    email: EmailStr

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    old_password: str
    password: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostVote(BaseModel):
    post_id: int
    dir: conint(le=1)


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    create_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None

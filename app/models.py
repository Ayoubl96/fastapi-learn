from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Integer, nullable=True, server_default='0')
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    owner_id = Column(Integer, ForeignKey('Users.id', ondelete="CASCADE"), nullable=False)
    owner = relationship("User")


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    phone_number = Column(String, nullable=True)


class PostVote(Base):
    __tablename__ = "post_votes"
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey(
        "Users.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    create_at_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))

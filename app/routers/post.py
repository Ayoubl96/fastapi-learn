from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import Optional, List
from .. import models, schemas, oauth2
from ..database import get_db
from sqlalchemy.sql import or_
from sqlalchemy import func

router = APIRouter(
    prefix="/post",
    tags=['Post']
)


@router.get("s", response_model=List[schemas.PostOut])
def get_post(
        db: Session = Depends(get_db),
        limit: int = 10,
        skip: int = 0,
        search: Optional[str] = "",
        current_user: int = Depends(oauth2.get_current_user,
                                    )
):
    posts = db.query(models.Post, func.count(models.PostVote.post_id).label("votes")).join(
        models.PostVote, models.PostVote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.owner_id == current_user.id,
        or_(
            models.Post.title.contains(search),
            models.Post.content.contains(search)
        )
    ).limit(limit).offset(skip).all()

    return posts


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(
        id: int, db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)
):
    post = db.query(models.Post, func.count(models.PostVote.post_id).label("votes")).join(
        models.PostVote, models.PostVote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.owner_id == current_user.id, models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not found")
    check_user = current_user.id != post.Post.owner_id
    if check_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Operation not authorize")

    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(
        post: schemas.PostCreate, db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)
):
    title = post.title
    content = post.content
    owner = current_user.id
    if post.published:
        published = 1
    else:
        published = 0

    new_post = models.Post(
        title=title,
        content=content,
        published=published,
        owner_id=owner
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.delete("/{id}")
def delete_post(
        id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)
):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not found")
    check_user = current_user.id != post.first().owner_id
    if check_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"You cant delete the post")

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(
        id: int, up_date_post: schemas.PostCreate,
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if up_date_post.published:
        published = 1
    else:
        published = 0

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not found")
    check_user = current_user.id != post.owner_id
    if check_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"You cant edit the post")

    post_query.update({
        'title': up_date_post.title,
        'content': up_date_post.content,
        'published': published
    },
        synchronize_session=False
    )
    db.commit()

    return post_query.first()

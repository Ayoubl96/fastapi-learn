import fastapi
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, tools
from ..database import get_db

router = fastapi.APIRouter(
    prefix="/user",
    tags=['User']
)


@router.post("s/", status_code=fastapi.status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = fastapi.Depends(get_db)):
    hashed_password = tools.has_psw(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("s/", response_model=List[schemas.UserOut])
def get_users(db: Session = fastapi.Depends(get_db)):
    users = db.query(models.User).all()

    return users


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = fastapi.Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND,
                                    detail=f"User with id: {id} not found")
    return user


@router.delete("/{id}")
def delete_user(id: int, db: Session = fastapi.Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)

    if user.first() is None:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND,
                                    detail=f"user with id: {id} not found")

    user.delete(synchronize_session=False)
    db.commit()
    return fastapi.Response(status_code=fastapi.status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.UserOut)
def update_user(id: int, up_date_user: schemas.UserUpdate, db: Session = fastapi.Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()

    if user is None:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND,
                                    detail=f"user with id: {id} not found")

    hashed_old_password = str(tools.has_psw(up_date_user.old_password))

    check = tools.verify_password(str(up_date_user.old_password), user.password)
    print(check)
    if not check:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND,
                                    detail=f"La password è errata")
    user_query.update({
        'email': up_date_user.email,
        'password': hashed_old_password,
    },
        synchronize_session=False
    )
    db.commit()
    return user_query.first()

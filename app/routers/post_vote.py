from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2

router = APIRouter(
    prefix="/post-vote",
    tags=['Post Vote']
)


@router.post('', status_code=status.HTTP_201_CREATED)
def vote(postvote: schemas.PostVote,
         db: Session = Depends(database.get_db),
         current_user: int = Depends(oauth2.get_current_user)
         ):
    post = db.query(models.Post).filter(models.Post.id == postvote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')

    vote_query = db.query(models.PostVote).filter(models.PostVote.post_id == postvote.post_id,
                                                  models.PostVote.user_id == current_user.id)
    found_vote = vote_query.first()
    if postvote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.id} already voted")
        new_vote = models.PostVote(post_id=postvote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote created"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Vote deleted"}

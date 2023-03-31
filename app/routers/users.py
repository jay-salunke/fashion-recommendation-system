from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.databases.getdb import get_db
from app.databases import schemas
from app.databases import crud

router = APIRouter(prefix="/users")


@router.post('/info')
def get_info(user: schemas.User, db: Session = Depends(get_db)):
    check = crud.get_user_by_email(db=db, email=user.email)
    if not check:
        return {
            "api": "v1",
            "status": "failed",
            "description": "User Not Found"
        }
    result = crud.create_user_info(db=db, user=user)
    if not result:
        return {
            "api": "v1",
            "status": "failed",
            "description": "User Information Is alredy There"
        }
    else:
        return {
            "api": "v1",
            "status": "success",
            "description": "User Information Added Successfully"
        }
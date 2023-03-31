from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.databases import schemas
from app.databases import crud
from app.databases.getdb import get_db

router = APIRouter(prefix="/auth")


@router.post('/login')
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    result = crud.get_user_by_email(db=db, email=user.email)
    if result:
        if result.hashed_password == user.password:
            if result.age is None:
                return {
                    "api": "v1",
                    "status": "success",
                    "redirect": "true"
                }
            else:
                return {
                    "api": "v1",
                    "status": "success",
                    "redirect": "false"
                }
    else:
        return {
            "api": "v1",
            "status": "failed"
        }
    if result.hashed_password == user.password:
        if result.age is None:
            return {
                "api": "v1",
                "status": "success",
                "redirect": "true"
            }
        else:
            return {
                "api": "v1",
                "status": "success",
                "redirect": "false"
            }
    else:
        return {
            "api": "v1",
            "status": "failed"
        }


@router.post('/register')
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    result = crud.create_user(db=db, user=user)
    if result:
        return {
            "api": "v1",
            "status": "success"
        }
    else:
        return {
            "api": "v1",
            "status": "failed"
        }
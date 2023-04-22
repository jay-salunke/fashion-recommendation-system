from fastapi import APIRouter, Depends
from databases import crud
from databases.getdb import get_db
from sqlalchemy.orm import Session
router = APIRouter(prefix="/category")

@router.post("/{category}")
def items(category, db : Session= Depends(get_db)):
    if category=="ladies":
        return crud.category(category="A",db=db)
    if category=="mens":
        return crud.category(category="F",db=db)
    if category=="sport":
        return crud.category(category="S",db=db)
    if category=="divide":
        return crud.category(category="D",db=db)
    if category=="baby":
        return crud.category(category="G",db=db)
    
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from databases import schemas, crud
from databases.getdb import get_db

router = APIRouter(prefix="/items")


@router.post("/insert")
def insert_items(items: schemas.ItemBase, db: Session = Depends(get_db)):
    items = crud.creat_item(db=db, item=items)
    if items:
        return {
            "api": "v1",
            "status": "success",
            "description": "Item Added Successfully"
        }
    else:
        return {
            "api": "v1",
            "status": "failed",
            "description": "Item Already Exists"
        }

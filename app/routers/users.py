import email
from pyexpat import model
from telnetlib import SE
from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from databases.getdb import get_db
from databases import schemas
from databases import crud
from routers.auth import get_current_user

router = APIRouter(prefix="/users")


@router.post('/info')
def get_info(user=Depends(get_current_user), db: Session = Depends(get_db)):
    info = crud.get_user_by_id(db=db, user_id=user.user_id)
    return info


@router.post('/info/edit')
def edit_info(user: schemas.User, user_id=Depends(get_current_user), db: Session = Depends(get_db)):
    print(user_id)
    update_items = {k: v for k, v in user.dict().items() if v is not None}
    print(update_items)
    try:
        user = crud.get_user_by_id(db=db, user_id=user_id.user_id)
        # check password and confirm password is in update_items
        if 'password' in update_items and 'new_password' in update_items:

            if user.hashed_password != update_items['password']:
                return {
                    "api": "v1",
                    "status": "failed",
                    "description": "Password Does Not Match"
                }
            else:
                # update current password with new password in db
                update_items['hashed_password'] = update_items['new_password']
                update_items.pop('password')
                update_items.pop('new_password')
                print(update_items)
                crud.update_user_info(db=db, update_items=update_items, user_id=user.user_id)
        else:
            crud.update_user_info(db=db, update_items=update_items, user_id=user.user_id)
        return {
            "api": "v1",
            "status": "success",
            "description": "User Information Updated Successfully"
        }
    except Exception as e:
        print(e)


@router.post('/transactions')
def get_transactions(user=Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        result = user
        print(result.user_id)
        if result:
            # get all transactions for a user and return it in json format
            transactions = crud.get_transactions_by_id(db=db, id=result.user_id)
            transaction_list = []
            if transactions:
                for transaction, item in transactions:
                    transaction_data = {
                        'item_name': item.product_name,
                        'transaction_id': transaction.id,
                        'transaction_date': str(transaction.timestamp),
                        'item_name': item.product_name,
                        'item_id': item.item_id,
                        'item_price': item.price,
                        'item_description': item.description
                    }
                    transaction_list.append(transaction_data)
                return transaction_list
        return {
            "api": "v1",
            "status": "failed",
            "description": "No transactions found"
        }
    except Exception as e:
        print(e)


@router.post('/transactions/create')
def create_transactions(transactions: schemas.Transactions,
                        db: Session = Depends(get_db), user=Depends(get_current_user)):
    transactions.user_id = user.user_id
    transactions = crud.create_transactions(db=db, transaction=transactions)
    if transactions:
        return {
            "api": "v1",
            "status": "success",
            "description": "Transaction Added Successfully"
        }
    return {
        "api": "v1",
        "status": "failed",
        "description": "Error Occured"
    }


@router.get("/suggestion")
def suggest(q: str | None = None, db: Session = Depends(get_db)):
    if q:
        result = crud.suggest(db=db, query=q)
        return result
    return "Hello"

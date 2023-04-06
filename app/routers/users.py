import email
from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from databases.getdb import get_db
from databases import schemas
from databases import crud
from routers.auth import get_current_user
router = APIRouter(prefix="/users")


@router.post('/info')
def get_info(userinfo: schemas.User,email: Annotated[str, Body()], db: Session = Depends(get_db)):
    userinfo.email = email
    check = crud.get_user_by_email(db=db, email=email)
    if not check:
        return {
            "api": "v1",
            "status": "failed",
            "description": "User Not Found"
        }
    result = crud.create_user_info(db=db, user=userinfo)
    if not result:
        return {
            "api": "v1",
            "status": "failed",
            "description": "User Information Is Already There"
        }
    else:
        return {
            "api": "v1",
            "status": "success",
            "description": "User Information Added Successfully"
        }


@router.post('/transactions')
def get_transactions(email: Annotated[str, Body(embed=True)],db: Session = Depends(get_db)):
    print("hello")
    print(email)
    print("In transactions")
    result = crud.get_user_by_email(db,email)

    print(result.user_id)
    if result:
        # get all transactions for a user and return it in json format
        transactions = crud.get_transactions_by_id(db=db, id=result.user_id)
        transaction_list = []

        for transaction, item in transactions:
            transaction_data = {
                'transaction_id': transaction.id,
                'transaction_date': str(transaction.timestamp),
                'item_name': item.product_name,
                'item_id': item.item_id,
                'item_price': item.price,
                'item_description':item.description
            }
            transaction_list.append(transaction_data)
        return transaction_list

    return {
        "api": "v1",
        "status": "failed",
        "description": "No transactions found"
    }


@router.post('/transactions/create')
def create_transactions( transactions: schemas.Transactions,email: Annotated[str, Body()], db: Session = Depends(get_db)):

    user = crud.get_user_by_email(db=db, email=email)
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

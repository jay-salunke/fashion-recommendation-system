from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.databases.getdb import get_db
from app.databases import schemas
from app.databases import crud
from app.routers.auth import get_current_user
router = APIRouter(prefix="/users")


@router.post('/info')
def get_info(current, db: Session = Depends(get_db)):
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
            "description": "User Information Is Already There"
        }
    else:
        return {
            "api": "v1",
            "status": "success",
            "description": "User Information Added Successfully"
        }


@router.post('/transactions')
def get_transactions(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    print("In transactions")
    result = crud.get_user_by_email(db,current_user.email)
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
            }
            transaction_list.append(transaction_data)
        return transaction_list

    return {
        "api": "v1",
        "status": "failed",
        "description": "No transactions found"
    }


@router.post('/transactions/create')
def create_transactions(transactions: schemas.Transactions, db: Session = Depends(get_db),current = Depends(get_current_user)):
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

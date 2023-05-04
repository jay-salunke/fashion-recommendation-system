import json
from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from databases.getdb import get_db
from databases import schemas
from databases import crud
from routers.auth import get_current_token, get_current_user
from databases.crud import get_current_time
import boto3
import os
# personalize_events = boto3.client('personalize-events',
#                                   aws_access_key_id=os.environ.get(
#                                       'access_key'),
#                                   aws_secret_access_key=os.environ.get(
#                                       'secret_key'),
#                                   region_name='ap-south-1')
router = APIRouter(prefix="/users")


@router.post('/info')
def get_info(user=Depends(get_current_user), db: Session = Depends(get_db)):
    info = crud.get_user_by_id(db=db, user_id=user.user_id)
    return info


@router.post('/info/edit')
def edit_info(user: schemas.User, user_id=Depends(get_current_user), db: Session = Depends(get_db)):
    print(user_id)
    update_items = {k: v for k, v in user.dict().items() if v is not None}
    print(update_items['age'])
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
                print(update_items['age'], "hello")
                crud.update_user_info(
                    db=db, update_items=update_items, user_id=user.user_id)
        else:
            # print("Hello")
            
            # if user.age is None:
            #     print("ok")
            #     print(update_items)
            #     properties = {
            #         'clubMemberStatus': update_items['club_member_status'],
            #         'age': update_items['age'],
            #         'postalCode': update_items['postal_code']
            #     }

            #     nuser = {
            #         'userId': user.user_id,
            #         'properties': json.dumps(properties)
            #     }

            #     users = [nuser]
            #     response = personalize_events.put_users(
            #         datasetArn="arn:aws:personalize:ap-south-1:296410630894:dataset/FRS/USERS",
            #         users=users
            #     )

            crud.update_user_info(
                db=db, update_items=update_items, user_id=user.user_id)
        return {
            "api": "v1",
            "status": "success",
            "description": "User Information Updated Successfully"
        }
    except Exception as e:
        print("Exception is ",e)


@router.post('/transactions')
def get_transactions(user_id=Depends(get_current_user), db: Session = Depends(get_db)):
    print("hello")
    try:
        result = user_id
        print(result.user_id)
        if result:
            # get all transactions for a user and return it in json format
            transactions = crud.get_transactions_by_id(
                db=db, id=result.user_id)
            transaction_list = []
            if transactions:
                for transaction, item in transactions:
                    transaction_data = {
                        'item_name': item.product_name,
                        'transaction_id': transaction.id,
                        'transaction_date': str(transaction.timestamp),
                        'item_name': item.product_name,
                        'item_id': item.item_id,
                        'item_price': int(float(item.price) * 1000),
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
                        db: Session = Depends(get_db), user=Depends(get_current_user), token=Depends(get_current_token)):
    print(transactions)
    transactions.user_id = user.user_id
    transactions.timestamp = get_current_time()
    # print(token)
    # properties={
    #         "sales_channel_id": transactions.sales_channel_id
    #     }
    # response = personalize_events.put_events(
    #     trackingId='9c45f328-e9ba-4975-ad83-b61c72e7dddd',
    #     userId=transactions.user_id,
    #     sessionId=token,
        
    #     eventList=[
    #         {
    #             "sentAt": f"{get_current_time()}",
    #             "eventType": "Purchase",
    #             "itemId": f"{transactions.item_id}",
    #             "properties": json.dumps(properties)
    #         }
    #     ]

    # )
    # print(response)
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


@router.post("/addtocart")
def add_to_cart(user= Depends(get_current_user), data :Annotated[dict,Body()] = ..., db: Session = Depends(get_db)):
    crud.addtocart(user_id=user.user_id,data=data,db=db)


@router.post("/getcart")
def get_cart_items(user = Depends(get_current_user),db: Session = Depends(get_db)):
    result = crud.getcart(user_id=user.user_id,db=db)
    items =  result.item_ids['data']
    result = crud.get_items_by_item_id(db=db, item_ids=items)
    return result
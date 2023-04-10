from typing import Annotated
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.routers.auth import get_current_user
from databases import schemas, crud
import boto3
import os
from databases.getdb import get_db

router = APIRouter(prefix="/recommend")
#get access key and secret key from environment variables

personalizeRt = boto3.client('personalize-runtime',
                             aws_access_key_id=os.environ.get('access_key'),
                             aws_secret_access_key=os.environ.get('secret_key'),
                             region_name='ap-south-1')


@router.post("/bestseller")
def bestseller(user= Depends(get_current_user), db: Session = Depends(get_db)):
    response = personalizeRt.get_recommendations(
        recommenderArn='arn:aws:personalize:ap-south-1:296410630894:recommender/best',
        userId=user.user_id,
        numResults=10
    )
    return response['itemList']

@router.post("/freq")
def frequently_bought_toghether(user = Depends(get_current_user), db: Session = Depends(get_db)):
    transaction = crud.get_transactions_for_item(db=db,user_id=user.user_id)
    response = personalizeRt.get_recommendations(
        recommenderArn='arn:aws:personalize:ap-south-1:296410630894:recommender/freq',
        itemId = str(transaction.item_id),
        numResults=10
    )
    return response['itemList']

@router.post('/foryou')
def recommended_for_you(user= Depends(get_current_user), db: Session = Depends(get_db)):
    response = personalizeRt.get_recommendations(
        recommenderArn='arn:aws:personalize:ap-south-1:296410630894:recommender/you',
        userId = user.user_id,
        numResults=10
    )
    return response['itemList'] 
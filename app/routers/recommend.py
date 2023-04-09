from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from databases import schemas, crud
import boto3

from databases.getdb import get_db

router = APIRouter(prefix="/recommend")
#get access key and secret key from environment variables

personalizeRt = boto3.client('personalize-runtime',
                             aws_access_key_id=ACCESS_KEY,
                             aws_secret_access_key=SECRET_KEY,
                             region_name='ap-south-1')

#lL3ZtFGCLXV81efEsxax
@router.post("/foryou")
def recommended_for_you(user: schemas.UserBase, db: Session = Depends(get_db)):
    result = crud.get_user_by_email(db, user.email)
    response = personalizeRt.get_recommendations(
        recommenderArn='arn:aws:personalize:ap-south-1:296410630894:recommender/frequentlybough',
        userId=result.user_id,
        numResults=10
    )

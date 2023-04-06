from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from databases import schemas, crud
import boto3

from databases.getdb import get_db

router = APIRouter(prefix="/recommend")

personalizeRt = boto3.client('personalize-runtime')

#lL3ZtFGCLXV81efEsxax
@router.post("/foryou")
def recommended_for_you(user: schemas.UserBase, db: Session = Depends(get_db)):
    result = crud.get_user_by_email(db, user.email)
    response = personalizeRt.get_recommendations(
        recommenderArn='arn:aws:personalize:ap-south-1:296410630894:recommender/frequentlybough',
        userId=result.user_id,
        numResults=10
    )

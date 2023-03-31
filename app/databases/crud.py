from sqlalchemy.orm import Session
from app.databases import models, schemas


# generate random user_id that is always unique
def generate_user_id():
    import random
    import string
    user_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return user_id


def create_user(db: Session, user: schemas.UserCreate):
    # check user already exists otherwise create user
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        return False
    db_user = models.User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return True


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user_info(db: Session, user: schemas.User):
    result = get_user_by_email(db, user.email)
    if result.age is not None:
        return False
    db_user = models.User(user_id=generate_user_id(), club_member_status=user.club_member_status,
                          fashion_news_frequency=user.fashion_news_frequency, age=user.age,
                          postal_code=user.postal_code)
    hello = db_user.__dict__.copy()
    hello.pop('_sa_instance_state')
    db.query(models.User).filter(models.User.email == user.email).update(hello)
    db.commit()
    return True

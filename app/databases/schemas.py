from optparse import Option
from typing import Optional

import uvicorn
from pydantic import BaseModel

from databases.database import Base


class ItemBase(BaseModel):
    # get items from models.py along with data type
    item_id: int
    product_name: str
    product_type_no: int
    product_group_name: str
    graphical_appearance_no: int
    colour_group_code: int
    department_no: int
    index_code: str
    index_group_no: int
    section_no: int
    garment_group_no: int
    description: str
    price: str

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserInfo(UserBase):
    class Config:
        orm_mode = True


class User(BaseModel):
    email: Optional[str] = None
    name: str
    club_member_status: str
    fashion_news_frequency: str
    age: int
    postal_code: str

    class Config:
        orm_mode = True


class UserFinal(User):
    user_id: str


class Transactions(BaseModel):
    # get transactions from models.py along with data type
    user_id: Optional[str] = None
    item_id: int
    sales_channel_id: int
    timestamp: int
    event_type: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None


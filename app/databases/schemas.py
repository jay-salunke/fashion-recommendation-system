from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


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


class User(UserBase):
    club_member_status: str
    fashion_news_frequency: str
    age: int
    postal_code: str

    class Config:
        orm_mode = True


class UserFinal(User):
    user_id: str


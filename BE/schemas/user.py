from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    pseudo: str
    passw: str
    token: Optional[str]
    tokenExpi: Optional[str]
    tokenSalt: Optional[str]
    participate2023: Optional[bool]
    participate2024: Optional[bool]
    participate2025: Optional[bool]

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional

class UserLienBase(BaseModel):
    user1id : str
    user2id: str
    typeLien: int

class UserLienCreate(UserLienBase):
    pass

class UserLienUpdate(UserLienBase):
    pass

class UserLien(UserLienBase):
    id: int

    class Config:
        orm_mode = True

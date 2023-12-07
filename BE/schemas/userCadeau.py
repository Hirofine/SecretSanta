from pydantic import BaseModel
from typing import Optional

class UserCadeauBase(BaseModel):
    user1id : str
    user2id: str
    annee: int

class UserCadeauCreate(UserCadeauBase):
    pass

class UserCadeauUpdate(UserCadeauBase):
    pass

class UserCadeau(UserCadeauBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional

class UserCadeauBase(BaseModel):
    user1id : str
    user2id: str
    annee: int
    user3id: str
    user4id: str

class UserCadeauCreate(UserCadeauBase):
    pass

class UserCadeauUpdate(UserCadeauBase):
    pass

class UserCadeau(UserCadeauBase):
    id: int

    class Config:
        orm_mode = True

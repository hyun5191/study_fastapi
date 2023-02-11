from typing import Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class IserCreate(UserBase):
    password: str
    full_name:Optional[str] = None

class User(UserBase):
    username: str
    full_name: Optional[str] = None

    class config:
        orm_mode = True
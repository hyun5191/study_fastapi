from sqlalchemy import Column, string, DateTime
from sqlalchemy.sql import func
from pydantic import BaseModel

from.conn import base

class check_data_type(BaseModel):
    username: str
    password: str
    full_name: str
    data_data: str

class User(base):
    __tablename__ = "users"

    username = Column(string(16), index=True, nullable=False, primary_key=True)
    username = Column(string(100), index=True, nullable=False, primary_key=True)
    username = Column(string(20), index=True, primary_key=False)
    username = Column(DateTime(timezone=True), index=True, nullable=False, primary_key=True, server_default=func.now())
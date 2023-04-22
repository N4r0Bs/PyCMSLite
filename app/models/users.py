from sqlmodel import SQLModel, Field

from typing import Optional

class UserModel(SQLModel):
    username: str
    email: str
    password: str
    name: str


class User(UserModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    
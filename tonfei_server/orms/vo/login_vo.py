from pydantic import BaseModel


class DataBase(BaseModel):
    access_token: str
    token_type: str


class Token(BaseModel):
    data: DataBase


class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []

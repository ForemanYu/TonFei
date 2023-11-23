from pydantic import BaseModel


# 会话模型
class Item(BaseModel):
    name: str
    json: str

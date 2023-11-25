from pydantic import BaseModel


# 会话模型
class Item(BaseModel):
    name: str
    content: str

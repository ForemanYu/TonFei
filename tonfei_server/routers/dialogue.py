from fastapi import APIRouter

from tonfei_server.config.database_no_sql import collection
from tonfei_server.orms.models.dialogue import Item

router = APIRouter()


@router.post("/")
async def create_item(item: Item):
    # 将数据插入到 MongoDB
    result = await collection.insert_one(item.model_dump())
    # 返回插入的文档 ID
    return {"id": str(result.inserted_id)}


@router.get("/{item_id}")
async def get_item(item_id: str):
    # 查询指定 ID 的文档
    item = await collection.find_one({"_id": item_id})
    if item:
        return item
    else:
        return {"error": "Item not found"}


@router.put("/{item_id}")
async def update_item(item_id: str, item: Item):
    # 更新指定 ID 的文档
    result = await collection.update_one({"_id": item_id}, {"$set": item.model_dump()})
    if result.modified_count == 1:
        return {"message": "Item updated"}
    else:
        return {"error": "Item not found"}


@router.delete("/{item_id}")
async def delete_item(item_id: str):
    # 删除指定 ID 的文档
    result = await collection.delete_one({"_id": item_id})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    else:
        return {"error": "Item not found"}

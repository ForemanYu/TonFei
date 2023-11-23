from motor.motor_asyncio import AsyncIOMotorClient

# 连接到 MongoDB 调用集合操作 crud
client = AsyncIOMotorClient("mongodb://127.0.0.1:27017")  # 连接信息
db = client["tonfei"]  # 数据库名称
collection = db["dialogue"]  # 集合名称

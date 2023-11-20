# 数据库连接

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 为 SQLAlchemy 定义数据库 URL地址¶

# SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@127.0.0.1/tonfei"

# 创建 SQLAlchemy 引擎
# connect_args 仅用于SQLite，在其他数据库不需要它
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# 创建一个SessionLocal类 这个实例将是实际的数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建一个Base类 创建每个数据库模型或类
Base = declarative_base()

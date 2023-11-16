import uvicorn
from fastapi import FastAPI, Depends, Request, Response

from routers import login, items, users
from tonfei_server.config.database import engine, SessionLocal
from tonfei_server.config.dependencies import get_current_active_user
from tonfei_server.orms.models import models

# 基于SQLAlchemy模型创建数据库表
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["users"], dependencies=[Depends(get_current_active_user)])
app.include_router(items.router, prefix="/items", tags=["items"], dependencies=[Depends(get_current_active_user)])
app.include_router(login.router, prefix="/login", tags=["login"])


# 中间件
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8008, reload=True)

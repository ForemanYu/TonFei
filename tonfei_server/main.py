import uvicorn
from fastapi import FastAPI, Depends

from routers import login, items, users
from tonfei_server.config.dependencies import get_current_active_user

app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["users"], dependencies=[Depends(get_current_active_user)])
app.include_router(items.router, prefix="/items", tags=["items"], dependencies=[Depends(get_current_active_user)])
app.include_router(login.router, prefix="/login", tags=["login"])

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8008, reload=True)

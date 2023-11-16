import uvicorn
from fastapi import FastAPI, Depends

from config.dependencies import get_current_active_user
from routers import login, items, users

app = FastAPI(dependencies=[Depends(get_current_active_user)], responses={404: {"description": "Not found"}})
app.include_router(users.router)
app.include_router(items.router)
app.include_router(login.router, prefix="/login",
                   tags=["login"],
                   dependencies=None)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8008, reload=True)

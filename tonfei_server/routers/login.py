from datetime import timedelta

from fastapi import HTTPException, APIRouter

from tonfei_server.constant.constant import ACCESS_TOKEN_EXPIRE_MINUTES
from tonfei_server.orms.dto.login_dto import Login
from tonfei_server.orms.vo.login_vo import Token
from tonfei_server.routers.extensions.login import authenticate_user, create_access_token

router = APIRouter()

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


# 账号 johndoe 密码 secret
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Login):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"data": {"access_token": access_token, "token_type": "bearer"}}

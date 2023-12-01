# 全局、路由依赖项
from typing import Annotated

from fastapi import HTTPException, status, Header, Depends
from jose import JWTError, jwt
from pydantic import ValidationError

from tonfei_server.constant.constant import SECRET_KEY, ALGORITHM
from tonfei_server.orms.vo.login_vo import TokenData
from tonfei_server.routers.extensions.login import get_user, User
from tonfei_server.routers.login import fake_users_db


# 路由依赖 拦截Token认证 处理 方法
async def get_current_user(token: Annotated[str, Header()]):
    authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


# 路由依赖 拦截Token认证
async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

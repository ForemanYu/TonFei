# 依赖项

from fastapi import Depends, HTTPException, status, Header
from jose import JWTError, jwt

from tonfei_server.constant.constant import SECRET_KEY, ALGORITHM
from tonfei_server.routers.extensions.login import User


# 路由依赖 拦截Token认证 处理 方法
async def get_current_user(token: str = Header()):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭据!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = User(username=username)
    if user is None:
        raise credentials_exception
    return user


# 路由依赖 拦截Token认证
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="已禁用")
    return current_user

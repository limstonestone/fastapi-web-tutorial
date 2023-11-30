import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import jwt, JWTError
from database.connection import Settings

settings = Settings()


def create_access_token(user: str):
    payload = {"user": user, "expires": time.time() + 3600}

    token = jwt.encode(
        payload, settings.SECRET_KEY, algorithm="HS256"
    )  # 인코딩할 대상, 페이로드 사인을 위한 키, 사인/암호화 알고리즘
    return token


def verify_access_token(token: str):
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        expire = data.get("expires")  # 만료 시간 존재 확인

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplided",
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):  # 만료 여부 확인
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detiail="Token expired!"
            )
        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token"
        )

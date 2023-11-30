from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    def create_hash(self, password: str):  # 문자열 해싱 값 반환
        return pwd_context.hash(password)

    def verify_hash(self, plain_password: str, hashed_password: str):  # 패스워드 일치 여부 확인
        return pwd_context.verify(plain_password, hashed_password)

from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your-secret-key-change-this"
ALGORITHM = "HS256"

def create_access_token(username: str):
    expire = datetime.utcnow() + timedelta(hours=24)
    data = {"sub": username, "exp": expire}
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)



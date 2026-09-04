from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi import Header,HTTPException,Request 
from dotenv import load_dotenv
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
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

def verify_token(Authorization:str =Header(...) ):
    token=Authorization.replace("Bearer ", "")
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username=payload.get('sub')
        if not username:
            raise HTTPException(status_code=401,detail="invalid token")
        return username
    except:
        raise HTTPException(status_code=401,detail="Invalid token")
        
 




















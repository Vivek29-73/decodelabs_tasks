from dotenv import load_dotenv
import os
load_dotenv()

from fastapi import FastAPI
from fastapi import HTTPException

import bcrypt
import jwt

from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from database import engine
from database import SessionLocal

from models import Base
from models import User

from schemas import UserRegister
from schemas import UserLogin

from fastapi import Header

app = FastAPI()
security = HTTPBearer()

Base.metadata.create_all(bind=engine)

SECRET_KEY=os.getenv("SECRET_KEY")

@app.post("/register", status_code=201)
def register_user(user: UserRegister):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    hashed_password = bcrypt.hashpw(
        user.password.encode(),
        bcrypt.gensalt()
    )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password.decode()
    )

    db.add(new_user)

    db.commit()

    return {
        "message": "User Registered"
    }

@app.post("/login")
def login_user(user: UserLogin):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    is_valid = bcrypt.checkpw(
        user.password.encode(),
        existing_user.password.encode()
    )

    if not is_valid:

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    payload = {
        "user_id": existing_user.id,
        "email": existing_user.email
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return {
        "token": token
    }

@app.get("/profile")
def get_profile(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )

    return {
        "message": "Protected Route Accessed",
        "user": payload
    }




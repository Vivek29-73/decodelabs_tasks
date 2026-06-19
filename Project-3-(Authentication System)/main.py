from fastapi import FastAPI
from fastapi import HTTPException

import bcrypt

from database import engine
from database import SessionLocal

from models import Base
from models import User

from schemas import UserRegister

app = FastAPI()

Base.metadata.create_all(bind=engine)


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
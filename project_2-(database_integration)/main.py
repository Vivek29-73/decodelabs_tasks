from fastapi import FastAPI
from fastapi import HTTPException

from database import engine
from database import SessionLocal

from models import Base
from models import User

from schemas import UserCreate
from schemas import UserUpdate

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/users", status_code=201)
def create_user(user: UserCreate):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User Created"
    }

@app.get("/users", status_code=200)
def get_users():

    db = SessionLocal()

    users = db.query(User).all()

    return users


@app.put("/users/{user_id}", status_code=200)
def update_user(
    user_id: int,
    user: UserUpdate
):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not existing_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    existing_user.name = user.name
    existing_user.email = user.email

    db.commit()

    return {
        "message": "User Updated"
    }

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):

    db = SessionLocal()

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)

    db.commit()
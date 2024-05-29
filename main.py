from fastapi import FastAPI
from sqlmodel import SQLModel
from config import SettingsDep
from deps import UserServiceDep
from models import User
from db import engine

app = FastAPI()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/info")
def read_root(settings: SettingsDep):
    return {
        "settings": settings
    }


@app.get("/users")
def get_users(*, user_service: UserServiceDep):
    users = user_service.get_all()

    return {
        "code": 0,
        "data": {
            "users": users,
        }
    }


@app.post("/users")
def create_user(*, user_service: UserServiceDep, user: User):
    user = User.model_validate(user)
    user = user_service.create(user)
    return {
        "code": 0,
        "data": {
            "user": user,
        }
    }


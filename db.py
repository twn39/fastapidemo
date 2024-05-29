from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session
from config import get_settings


settings = get_settings()
sqlite_url = settings.DATABASE_URL
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=settings.DEBUG, connect_args=connect_args)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

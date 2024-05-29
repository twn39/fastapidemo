from sqlmodel import select
from db import SessionDep
from models import User


class UserService:
    def __init__(self, db_session: SessionDep):
        self.db_session = db_session

    def get_all(self):
        users = self.db_session.exec(select(User)).all()
        return users

    def create(self, user: User):
        self.db_session.add(user)
        self.db_session.commit()
        self.db_session.refresh(user)
        return user

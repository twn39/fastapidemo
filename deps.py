from typing import Annotated
from fastapi import Depends
from services.user_service import UserService


UserServiceDep = Annotated[UserService, Depends(UserService)]

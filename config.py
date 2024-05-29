from typing import Annotated
from fastapi import Depends
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI start application"
    DEBUG: bool = False
    DATABASE_URL: str
    DATABASE_NAME: str
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()


SettingsDep = Annotated[Settings, Depends(get_settings)]

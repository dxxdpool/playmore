from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: str = "dev"
    DATABASE_URL: str = Field(...)

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

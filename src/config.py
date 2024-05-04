from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRESQL_CONN_STRING: str

    class Config:
        env_file = ".env"


settings = Settings()

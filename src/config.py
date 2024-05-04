from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    POSTGRESQL_CONN_STRING: str
    POSTGRESQL_TEST_CONN_STRING: str
    APP_ENV: str = "dev"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

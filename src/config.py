from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_NAME: str | None = None

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')

settings = Settings()



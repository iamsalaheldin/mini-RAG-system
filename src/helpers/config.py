from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    App_Version: str
    OPENAI_API_KEY: str

    class Config:
        env_file = "src/.env"
        env_file_encoding = "utf-8"

def get_settings():
    return Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings is a Pydantic model that represents the configuration settings for the application.

    Attributes:
        algorithm (str): The algorithm used for token encoding.
        secret_key (str): The secret key used for token encoding.
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    ALGORITHM: str
    SECRET_KEY: str
    DB_URL: str


settings = Settings()
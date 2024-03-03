from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # database connection uri
    DATABASE_URI: str

    # project embeds
    PROJECT_TITLE: str
    PROJECT_VERSION: str
    PROJECT_DESCRIPTION: str

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )


settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Since this is a test task and the service is small,
    # simple aiosqlite will be enough for us.
    # There's no need to hide the database URL in a .env file in this case.
    db_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')

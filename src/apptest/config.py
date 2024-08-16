import pydantic
from sqlalchemy import URL, make_url


class DatabaseSettings(pydantic.BaseSettings):
    url: pydantic.PostgresDsn

    def get_db_url(self) -> URL:
        return make_url(self.url).set(drivername="postgresql+psycopg")

    class Config(pydantic.BaseSettings.Config):
        env_prefix = "DATABASE_"


class Settings(pydantic.BaseSettings):
    database: DatabaseSettings

    class Config(pydantic.BaseSettings.Config):
        env_nested_delimiter = "_"
        extra = pydantic.Extra.ignore

settings = Settings(".env")   
from pydantic import (
    BaseModel,
)

from pydantic_settings import BaseSettings


class DatabaseConfig(BaseModel):
    """
    Backend database configuration parameters.
    """
    dsn: str = "postgresql://test_gio:mypassword@localhost:5432/catalog_db"


class Config(BaseSettings):
    """
    API configuration parameters.
    Automatically read modifications to the configuration parameters
    from environment variables and ``.env`` file.
    """

    database: DatabaseConfig = DatabaseConfig()
    token_key: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "micro"
        env_nested_delimiter = "__"
        case_sensitive = False


config = Config()

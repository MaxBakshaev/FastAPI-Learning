from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings


BASEDIR = Path(__file__).parent.parent

DB_PATH = BASEDIR / "db.sqlite3"


class DbSettings(BaseModel):
    """Настройки БД"""

    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True
    # echo: bool = False


class Settings(BaseSettings):
    """Настройки"""

    api_v1_prefix: str = "/api/v1"
    db: DbSettings = DbSettings()
    # db_echo: bool = True


settings = Settings()

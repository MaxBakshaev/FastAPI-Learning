from pathlib import Path
from pydantic_settings import BaseSettings


BASEDIR = Path(__file__).parent.parent


class Setting(BaseSettings):
    """Настройки"""

    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{BASEDIR}/db.sqlite3"
    db_echo: bool = False
    # db_echo: bool = True


settings = Setting()

from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from core.config import settings


class DatabaseHelper:
    """Подключение к БД"""

    def __init__(self, url: str, echo: bool = False):
        """Создает движок и фабрику сессий"""
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            # связывает движок и сессию
            bind=self.engine,
            # изменения в сессии не будут автоматически отправляться в базу данных
            autoflush=False,
            # автоматическое подтверждение изменений в базе данных после каждого запроса
            autocommit=False,
            # объекты не будут устаревать, и их атрибуты будут оставаться в памяти,
            # даже если данные в базе были изменены другими сессиями
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        """Управляет сессиями"""
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session
    
    async def session_dependency(self) -> AsyncSession:
        """Создает сессию для каждого запроса"""
        async with self.session_factory() as session:
            yield session
            await session.close()
            
    async def scoped_session_dependency(self) -> AsyncSession:
        """Создает сессию для каждого запроса"""
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(url=settings.db_url, echo=settings.db_echo)

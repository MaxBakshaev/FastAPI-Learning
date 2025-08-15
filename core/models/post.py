from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .mixins import UserRelationMixin

from .base import Base


class Post(Base, UserRelationMixin):

    # _user_id_nullable: bool = False
    # _user_id_unique: bool = False
    _user_back_populates = "posts"

    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    def __str__(self):
        """Возвращает строковое представление поста"""
        return f"{self.__class__.__name__}(id={self.id}, username={self.title!r}, user_id={self.user_id})"

    def __repr__(self):
        """Возвращает строковое представление поста в списке пользователей"""
        return str(self)

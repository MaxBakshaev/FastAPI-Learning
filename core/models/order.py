from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .order_product_association import order_product_assosiation_table


if TYPE_CHECKING:
    from .product import Product


class Order(Base):

    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        # состояние на стороне сервера при создании записи
        server_default=func.now(),
        # состояние на стороне sqlalchemy
        default=datetime.utcnow,
    )
    products: Mapped[list["Product"]] = relationship(
        secondary=order_product_assosiation_table,
        back_populates="orders",
        # lazy="noload"
    )

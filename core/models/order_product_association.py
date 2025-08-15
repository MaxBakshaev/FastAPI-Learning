from sqlalchemy import Column, Integer, ForeignKey, Table, UniqueConstraint

from .base import Base


order_product_assosiation_table = Table(
    "order_product_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", ForeignKey("orders.id"), nullable=False),
    Column("product_id", ForeignKey("products.id"), nullable=False),
    UniqueConstraint("order_id", "product_id", name="idx_unique_order_product")
)
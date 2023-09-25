from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.models.base import SQLModel


class ProductModel(SQLModel):
    __tablename__ = "products"
    __table_args__ = {"schema": "public"}

    id: Mapped[int] = mapped_column("id", primary_key=True)
    sku: Mapped[str] = mapped_column("sku")
    name: Mapped[str] = mapped_column("name")
    price: Mapped[float] = mapped_column("price")
    brand: Mapped[str] = mapped_column("brand")

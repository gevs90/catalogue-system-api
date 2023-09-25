from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    sku: str
    name: str
    price: float
    brand: str


class CreateProductSchema(BaseModel):
    sku: str
    name: str
    price: float
    brand: str


class UpdateProductSchema(BaseModel):
    sku: str | None = None
    name: str | None = None
    price: float | None = None
    brand: str | None = None


class DeleteProductSchema(BaseModel):
    message: str

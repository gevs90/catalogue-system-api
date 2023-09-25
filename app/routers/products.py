from typing import List

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

from app.database.session import create_session
from app.const import (
    PRODUCTS_TAGS,
    PRODUCTS_URL,
)
from app.schemas.auth import UserSchema
from app.schemas.products import (
    ProductSchema, CreateProductSchema, UpdateProductSchema, DeleteProductSchema)
from app.services.auth import get_current_user
from app.services.products import ProductService


router = APIRouter(prefix="/" + PRODUCTS_URL, tags=PRODUCTS_TAGS)


@router.get("/", response_model=List[ProductSchema])
async def get_products(
    session: Session = Depends(create_session),
) -> List[ProductSchema]:
    """Get listing products"""

    return ProductService(session).get_products()


@router.post("/", response_model=ProductSchema)
async def create_product(
    form: CreateProductSchema,
    user: UserSchema = Depends(get_current_user),
    session: Session = Depends(create_session),
) -> ProductSchema:
    """Get listing products"""

    return ProductService(session).store_product(form)


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(
    product_id: int,
    session: Session = Depends(create_session),
) -> ProductSchema:
    """Get product by ID."""

    return ProductService(session).get_product(product_id)


@router.put("/{product_id}", response_model=ProductSchema)
async def update_product(
    product_id: int,
    form: UpdateProductSchema,
    user: UserSchema = Depends(get_current_user),
    session: Session = Depends(create_session),
) -> ProductSchema:
    """Update prodcut by ID"""

    return ProductService(session).update_product(product_id, form, user)


@router.delete("/{product_id}", response_model=DeleteProductSchema)
async def delete_products(
    product_id: int,
    user: UserSchema = Depends(get_current_user),
    session: Session = Depends(create_session),
) -> DeleteProductSchema:
    """Get listing products"""

    return ProductService(session).delete_product(product_id)

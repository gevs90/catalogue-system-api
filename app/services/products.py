from typing import List

from sqlalchemy import select
from app.exceptions import raise_with_log
from app.mail.sendgrid import send_email_to_admin

from fastapi import status

from app.models.product import ProductModel
from app.schemas.products import CreateProductSchema, ProductSchema, DeleteProductSchema
from app.services.auth import AuthDataManager
from app.services.base import (
    BaseDataManager,
    BaseService,
)


class ProductService(BaseService):
    def get_product(self, product_id: int) -> ProductSchema:
        """Get product by ID."""

        return ProductDataManager(self.session).get_product(product_id)

    def get_products(self) -> List[ProductSchema]:
        """Select products."""

        return ProductDataManager(self.session).get_products()

    def store_product(self, product: CreateProductSchema) -> ProductSchema:
        """ Store new product """
        product_model = ProductModel(
            sku=product.sku,
            name=product.name,
            price=product.price,
            brand=product.brand,
        )

        return ProductDataManager(self.session).store_product(product_model, True)

    def update_product(self, product_id: int, product: CreateProductSchema, user: any) -> ProductSchema:
        """ Update product by ID """
        saved_product = ProductDataManager(
            self.session).get_product_model(product_id)

        if product.sku:
            saved_product.sku = product.sku
        if product.name:
            saved_product.name = product.name
        if product.price:
            saved_product.price = product.price
        if product.brand:
            saved_product.brand = product.brand

        if saved_product in self.session.dirty:
            emails = AuthDataManager(self.session).get_emails_users(user)
            send_email_to_admin("Product updated at",
                                "The admin user " + user.email + " has ben updated the product " + product.sku, emails)

        updated_product = ProductDataManager(
            self.session).update_product(saved_product, True)
        return updated_product

    def delete_product(self, product_id: int) -> ProductSchema:
        """ Delete product by ID """
        saved_product = ProductDataManager(
            self.session).get_product_model(product_id)

        ProductDataManager(self.session).destroy_product(saved_product)
        return DeleteProductSchema(message="Product deleted at")


class ProductDataManager(BaseDataManager):
    def store_product(self, product: CreateProductSchema, recover: bool = False) -> ProductSchema:
        product = self.add_one(product, recover=recover)
        return ProductSchema(
            id=product.id,
            sku=product.sku,
            name=product.name,
            price=product.price,
            brand=product.brand
        )

    def update_product(self, product: any, recover: bool = False) -> ProductSchema:
        product = self.update_one(product, recover=recover)
        return ProductSchema(
            id=product.id,
            sku=product.sku,
            name=product.name,
            price=product.price,
            brand=product.brand
        )

    def destroy_product(self, product: any) -> DeleteProductSchema:
        return self.destroy_one(product)

    def get_product(self, product_id: int) -> ProductSchema:
        stmt = select(ProductModel).where(
            ProductModel.id == product_id)
        model = self.get_one(stmt)

        if not isinstance(model, ProductModel):
            raise_with_log(status.HTTP_404_NOT_FOUND, "Product not found")

        return ProductSchema(**model.to_dict())

    def get_product_model(self, product_id: int) -> ProductSchema:
        stmt = select(ProductModel).where(
            ProductModel.id == product_id)
        model = self.get_one(stmt)

        if not isinstance(model, ProductModel):
            raise_with_log(status.HTTP_404_NOT_FOUND, "Product not found")

        return model

    def get_products(self) -> List[ProductSchema]:
        schemas: List[ProductSchema] = list()

        stmt = select(ProductModel)

        for model in self.get_all(stmt):
            schemas += [ProductSchema(**model.to_dict())]

        return schemas

from http import HTTPStatus
from webargs.flaskparser import use_kwargs
from flask_apispec import marshal_with

from extensions import db
from src.utils.base_resource import BaseResource
from src.models.product_methods import ProductMethods
from src.schemas.products import (
    ProductCreateRequestSchema,
    ProductCreateResponseSchema,
    ProductDetailsResponseSchema,
    ProductListRequestSchema,
    ProductUpdateRequestSchema,
    ProductUpdateResponseSchema,
)
from src.schemas.pagination import PaginationResponseSchema


class ProductCreateResource(BaseResource):

    @use_kwargs(ProductCreateRequestSchema(), location="json")
    @marshal_with(ProductCreateResponseSchema, HTTPStatus.CREATED)
    def post(self, **kwargs):
        record = ProductMethods.create_record(kwargs)
        db.session.commit()
        return {"product_id": record.id}


class ProductDetailsResource(BaseResource):

    @marshal_with(ProductDetailsResponseSchema, HTTPStatus.OK)
    def get(self, product_id, **kwargs):
        if not (record := ProductMethods.get_record_with_id(product_id, db=db)):
            raise ValueError("Record not found for the corresponding product_id")

        return record


class ProductListResource(BaseResource):

    @use_kwargs(ProductListRequestSchema, location="querystring")
    @marshal_with(PaginationResponseSchema(ProductDetailsResponseSchema), HTTPStatus.OK)
    def get(self, **kwargs):
        return ProductMethods.get_filtered_products(kwargs, db=db)


class ProductUpdateResource(BaseResource):

    @use_kwargs(ProductUpdateRequestSchema, location="json")
    @marshal_with(ProductUpdateResponseSchema, HTTPStatus.NO_CONTENT)
    def patch(self, product_id, **kwargs):
        if not kwargs:
            raise ValueError("Please provide at- least one value to update the record.")

        if not (product := ProductMethods.get_record_with_id(product_id, db=db)):
            raise ValueError("Product not found for the corresponding product_id")

        ProductMethods.update_record_with_id(product.id, **kwargs)
        db.session.commit()
        return {"message": "Updated record"}


class ProductDeleteResource(BaseResource):

    @marshal_with(ProductUpdateResponseSchema, HTTPStatus.NO_CONTENT)
    def delete(self, product_id, **kwargs):
        if not (product := ProductMethods.get_record_with_id(product_id, db=db)):
            raise ValueError("Product not found for the corresponding product_id")

        ProductMethods.delete_record(db, product.id)
        db.session.commit()
        return {"message": "Deleted record"}

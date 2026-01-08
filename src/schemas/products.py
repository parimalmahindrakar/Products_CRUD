from marshmallow import fields, Schema, validate, validate

from src.utils.common_constants import DATETIME_FORMAT
from src.schemas.pagination import PaginationRequestSchema


class ProductCreateRequestSchema(Schema):
    product_name = fields.String(required=True, validate=[validate.Length(min=1, max=10)])
    product_type = fields.String(required=True, validate=[validate.Length(min=1, max=50)])
    price = fields.Integer(required=True, validate=validate.Range(min=1))
    stock = fields.Integer(required=True, validate=validate.Range(min=1))


class ProductCreateResponseSchema(Schema):
    product_id = fields.Integer()


class ProductDetailsResponseSchema(Schema):
    created_at = fields.DateTime(format=DATETIME_FORMAT)
    product_name = fields.String()
    product_type = fields.String()
    price = fields.Integer()
    stock = fields.Integer()


class ProductListRequestSchema(PaginationRequestSchema):
    product_name = fields.String()
    product_type = fields.String()

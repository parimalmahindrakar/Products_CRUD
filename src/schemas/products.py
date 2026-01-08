from marshmallow import fields, Schema, validate, validate


class ProductCreateRequestSchema(Schema):
    product_name = fields.String(required=True, validate=[validate.Length(min=1, max=10)])
    product_type = fields.String(required=True, validate=[validate.Length(min=1, max=50)])
    price = fields.Integer(required=True, validate=validate.Range(min=1))
    stock = fields.Integer(required=True, validate=validate.Range(min=1))


class ProductCreateResponseSchema(Schema):
    product_id = fields.Integer()

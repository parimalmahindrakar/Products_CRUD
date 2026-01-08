from marshmallow import fields, Schema, validate, pre_dump

from src.utils.common_constants import DEFAULT_PAGE_NUMBER, DEFAULT_PAGE_SIZE, PAGE_SIZE_OPTIONS


class PaginationRequestSchema(Schema):
    page_number = fields.Integer(load_default=DEFAULT_PAGE_NUMBER, validate=validate.Range(min=1))
    page_size = fields.Integer(
        load_default=DEFAULT_PAGE_SIZE, validate=validate.Range(min=1, max=PAGE_SIZE_OPTIONS[-1])
    )


class NestedPaginationMetaDataResponseSchema(Schema):
    total_records = fields.Integer(required=True, dump_only=True)
    page_size = fields.Integer(required=True, dump_only=True, dump_default=DEFAULT_PAGE_SIZE)
    page_number = fields.Integer(required=True, dump_only=True, dump_default=DEFAULT_PAGE_NUMBER)


class PaginationResponseSchema(Schema):
    meta = fields.Nested(NestedPaginationMetaDataResponseSchema, required=True)

    def __init__(self, item_schema, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["data"] = fields.List(fields.Nested(item_schema))
        self.dump_fields["data"] = self.fields["data"]
        self.dump_only = list(item_schema._declared_fields.keys())

    @pre_dump
    def convert_to_paginated_response(self, response, **kwargs):
        return {
            "data": response.items,
            "meta": {
                "total_records": response.total,
                "page_size": response.per_page,
                "page_number": response.page,
            },
        }

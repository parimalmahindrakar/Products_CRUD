from src.utils.base_model import BaseModel
from src.models.product import Product


class ProductMethods(BaseModel):
    model = Product

    @classmethod
    def get_filtered_products(cls, kwargs, db):
        filters = []
        if product_name := kwargs.get("product_name"):
            filters.append(cls.model.product_name.like(f"{product_name}%"))
        if product_type := kwargs.get("product_type"):
            filters.append(cls.model.product_type == product_type)

        query = db.session.query(cls.model).filter(*filters)
        records = cls.get_paginated_records_with_filters(
            page_number=kwargs["page_number"], page_size=kwargs["page_size"], query=query
        )
        return records

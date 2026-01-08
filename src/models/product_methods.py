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

        records = db.session.query(cls.model).filter(*filters).all()
        return records

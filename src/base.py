from src.utils.url import URLS
from src.views.products import (
    ProductCreateResource,
    ProductDetailsResource,
    ProductListResource,
    ProductUpdateResource,
    ProductDeleteResource,
)

urls = [
    URLS(ProductCreateResource, ["products/create"], name="create_product_api"),
    URLS(ProductDetailsResource, ["products/<int:product_id>/details"], name="get_product_details_api"),
    URLS(ProductListResource, ["products/list"], name="get_filtered_product_list_api"),
    URLS(ProductUpdateResource, ["products/<int:product_id>/update"], name="update_product_api"),
    URLS(ProductDeleteResource, ["products/<int:product_id>/delete"], name="delete_product_api"),
]

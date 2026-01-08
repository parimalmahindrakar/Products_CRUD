from src.utils.url import URLS
from src.views.products import ProductCreateResource, ProductDetailsResource, ProductListResource

urls = [
    URLS(ProductCreateResource, ["products/create"], name="create_product_api"),
    URLS(ProductDetailsResource, ["products/<int:product_id>/details"], name="get_product_details_api"),
    URLS(ProductListResource, ["products/list"], name="get_filtered_product_list_api"),
]

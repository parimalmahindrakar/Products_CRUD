from src.utils.url import URLS
from src.views.products import ProductCreateResource

urls = [
    URLS(ProductCreateResource, ["product/create"], name="create_product_api"),
]

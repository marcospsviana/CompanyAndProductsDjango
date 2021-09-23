from django.urls import path
from .views import list_products, create_product

app_name = "comany"
urlpatterns = [
    path("products", list_products, name="products"),
    path("create-products", create_product, name="createproducts"),
]

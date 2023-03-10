from django.urls import path
from .views import (
    shop,
    # details,
    home,
    # ProductsListView,
    ProductDetailView,
    # filter_by_kind,
    # filter_by_origin,

)
app_name = "products"

urlpatterns = [
    path("products/shop/", shop, name="shop"),
    path("", home, name="home"),
    # path("shop/", ProductsListView.as_view(), name="shop"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="details"),
    # path("kind/<int:kind_id>/", filter_by_kind, name="filter_by_kind"),
    # path("origin/<int:origin_id>/", filter_by_origin, name="filter_by_origin"),
]

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cart.forms import CartAddProductForm
from .forms import FilterByKindForm, FilterByOriginForm
from .models import Product, ProductKind, ProductOrigin


def home(request: HttpRequest):
    return render(request=request, template_name='products/home.html')


def shop(request: HttpRequest):
    main = Product.objects.select_related("kind").prefetch_related("origin").filter(archived=False).order_by(
        "price").all()
    kind = ProductKind.objects.all()
    # origin = ProductOrigin.objects.all()
    form1 = FilterByKindForm()
    if request.method == "POST":
        key = request.POST.get("choice")
        form1.is_valid()
        context = {"form": form1, "products": main.filter(kind=key), "kind": kind, "filter_by": 0}
    else:
        context = {"form": form1, "products": main, "kind": kind, "filter_by": 0}
    return render(request=request, template_name='products/shop.html', context=context)


# class ProductsListView(ListView):
#     template_name = "products/shop.html"
#     context_object_name = "products"
#
#     queryset = (
#         Product
#         .objects
#         .select_related("kind")
#         .prefetch_related("origin")
#         .filter(archived=False)
#         .filter(price__gt=1)
#         # .filter(kind=    )
#         .order_by("price")
#         .all()
#     )


class ProductDetailView(DetailView):
    template_name = "products/details.html"
    context_object_name = "product"
    cart_product_form = CartAddProductForm()
    queryset = (
        Product
        .objects
        .select_related("profile", "kind")
        .prefetch_related("origin")
    )


def about(request: HttpRequest):
    return render(request=request, template_name='products/index.html')


def article(request: HttpRequest):
    return render(request=request, template_name='products/article.html')


# def filter_by_kind(request: HttpRequest, kind_id):
#     products = Product.objects.select_related("kind").filter(archived=False).order_by("price").filter(
#         kind=kind_id).all()
#     kind = ProductKind.objects.all()
#     context = {"products": products, "kind": kind, "filter_by": kind_id}
#     return render(request=request, template_name='products/shop.html', context=context)
#
#
# def filter_by_origin(request: HttpRequest, origin_id):
#     products = Product.objects.prefetch_related("origin").filter(archived=False).order_by("price").filter(
#         origin=origin_id).all()
#     origin = ProductOrigin.objects.all()
#     context = {"products": products, "origin": origin, "filter_by": origin_id}
#     return render(request=request, template_name='products/shop.html', context=context)
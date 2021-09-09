from django.shortcuts import render
from .models import Product
# Create your views here.


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    content = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", content)

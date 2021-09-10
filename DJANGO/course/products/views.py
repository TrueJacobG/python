from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    content = {
        "form": form,
    }
    return render(request, "products/product_create.html", content)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    content = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", content)

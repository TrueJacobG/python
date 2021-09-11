from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.


def product_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
    content = {}
    return render(request, "products/product_create.html", content)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    content = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", content)

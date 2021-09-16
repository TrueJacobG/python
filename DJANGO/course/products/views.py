from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm


def product_create_view(request):
    initial_data = {
        'title': "This is initial title"
    }
    # now you can edit 1 id in your data base
    obj = Product.objects.get(id=1)
    # \/ -> initial=initial_data
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    content = {
        'form': form,
    }
    return render(request, "products/product_create.html", content)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form,
#     }
#     return render(request, "products/product_create.html", context)


def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)

from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, contact_view
from .views import product_detail_view, product_create_view, product_list_view, product_delete_view

app_name = 'products'

urlpatterns = [
    path('<int:id>/', product_detail_view, name="product-detail"),
    path('<int:id>/delete/', product_delete_view, name="product-delete"),
    path('', product_list_view, name="product-list"),
    path('create/', product_create_view, name="product-create"),
]

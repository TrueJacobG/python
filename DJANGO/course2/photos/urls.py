from django.urls import path
from .views import PhotosListView

app_name = 'photos'
urlpatterns = [
    path('', PhotosListView.as_view(), name='photos-list-view'),
]

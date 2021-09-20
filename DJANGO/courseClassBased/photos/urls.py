from django.urls import path
from .views import PhotosListView, PhotosDetailView, PhotosCreateView, PhotosUpdateView

app_name = 'photos'
urlpatterns = [
    path('', PhotosListView.as_view(), name='photos-list-view'),
    path('<int:id>/', PhotosDetailView.as_view(), name='photos-detail'),
    path('create/', PhotosCreateView.as_view(), name='photos-create'),
    path('<int:id>/update/', PhotosUpdateView.as_view(), name='photos-update'),
]

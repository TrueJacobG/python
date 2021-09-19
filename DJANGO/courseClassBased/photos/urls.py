from django.urls import path
from .views import PhotosListView, PhotosDetailView

app_name = 'photos'
urlpatterns = [
    path('', PhotosListView.as_view(), name='photos-list-view'),
    path('<int:id>/', PhotosDetailView.as_view(), name='photos-detail')
]

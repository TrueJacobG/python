from django.urls import path
from .views import PhotosListView, PhotosDetailView, PhotosCreateView, PhotosUpdateView, PhotosDeleteView, PhotosDetailViewRAW, PhotosListViewRAW, PhotosCreateViewRAW

app_name = 'photos'
urlpatterns = [
    path('', PhotosListViewRAW.as_view(), name='photos-list-view'),
    path('<int:id>/', PhotosDetailViewRAW.as_view(), name='photos-detail'),
    path('create/', PhotosCreateViewRAW.as_view(), name='photos-create'),
    path('<int:id>/update/', PhotosUpdateView.as_view(), name='photos-update'),
    path('<int:id>/delete/', PhotosDeleteView.as_view(), name='photos-delete'),
]

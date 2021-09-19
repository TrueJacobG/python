from django.shortcuts import render, get_object_or_404
from .models import Photo

from django.views.generic import (
    CreateView, DeleteView, ListView, UpdateView, DetailView
)


class PhotosListView(ListView):
    template_name = 'photos/list.html'
    queryset = Photo.objects.all()


class PhotosDetailView(DetailView):
    template_name = 'photos/detail.html'

    def get_object(self):
        my_id = self.kwargs.get("id")
        return get_object_or_404(Photo, id=my_id)

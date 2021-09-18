from django.shortcuts import render
from .models import Photo

from django.views.generic import (
    CreateView, DeleteView, ListView, UpdateView, DetailView
)


class PhotosListView(ListView):
    template_name = 'photos/list.html'
    queryset = Photo.objects.all()

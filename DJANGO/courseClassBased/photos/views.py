from django.shortcuts import render, get_object_or_404
from .models import Photo

from django.views.generic import (
    CreateView, DeleteView, ListView, UpdateView, DetailView
)

from .forms import PhotoModelForm


class PhotosListView(ListView):
    template_name = 'photos/list.html'
    queryset = Photo.objects.all()


class PhotosDetailView(DetailView):
    template_name = 'photos/detail.html'

    def get_object(self):
        my_id = self.kwargs.get("id")
        return get_object_or_404(Photo, id=my_id)


class PhotosCreateView(CreateView):
    template_name = 'photos/create.html'
    form_class = PhotoModelForm
    queryset = Photo.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return "/"


class PhotosUpdateView(UpdateView):
    template_name = 'photos/create.html'
    form_class = PhotoModelForm
    queryset = Photo.objects.all()

    def get_object(self):
        my_id = self.kwargs.get("id")
        return get_object_or_404(Photo, id=my_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return "/"

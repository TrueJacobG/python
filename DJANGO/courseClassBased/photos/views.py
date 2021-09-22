from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Photo

from django.views.generic import (
    CreateView, DeleteView, ListView, UpdateView, DetailView
)
from django.views import View
from .forms import PhotoModelForm


class PhotosListView(ListView):
    template_name = 'photos/list.html'
    queryset = Photo.objects.all()


class PhotosListViewRAW(View):
    template_name = 'photos/list.html'
    queryset = Photo.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {
            "object_list": self.get_queryset()
        }
        return render(request, self.template_name, context)


class PhotosDetailView(DetailView):
    template_name = 'photos/detail.html'

    def get_object(self):
        my_id = self.kwargs.get("id")
        return get_object_or_404(Photo, id=my_id)


class PhotosDetailViewRAW(View):
    template_name = 'photos/detail.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Photo, id=id)
            context["object"] = obj
        return render(request, self.template_name, context)


class PhotosCreateView(CreateView):
    template_name = 'photos/create.html'
    form_class = PhotoModelForm
    queryset = Photo.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return "/"


class PhotosCreateViewRAW(View):
    template_name = 'photos/create.html'

    def get(self, request, *args, **kwargs):
        form = PhotoModelForm()
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = PhotoModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = PhotoModelForm()
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)


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


class PhotosDeleteView(DeleteView):
    template_name = 'photos/delete.html'

    def get_object(self):
        my_id = self.kwargs.get("id")
        return get_object_or_404(Photo, id=my_id)

    def get_success_url(self):
        return reverse('photos:photos-list-view')

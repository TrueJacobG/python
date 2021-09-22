from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeView(View):
    # def method - if form then post
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})


def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home.html', context)

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    my_context = {
        "my_title": "main page - home",
        "my_list": [1, 2, 3],
    }
    return render(request, "home.html", my_context)


def contact_view(request, *args, **kwargs):
    # print(request.user)
    # return HttpResponse("<h1>Contact here :D</h1>")
    my_context = {
        "my_title": "Contact Page - Contact",
        "my_number": "000-000-000",
    }
    return render(request, "contact.html", my_context)

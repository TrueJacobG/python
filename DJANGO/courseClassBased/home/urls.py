from django.urls import path
from .views import home_view, HomeView

app_name = ""
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # path("", home_view, name="home")
]

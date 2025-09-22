from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about-the-project/", views.AboutView.as_view(), name="about"),
]

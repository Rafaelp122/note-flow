from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("", views.NotesListView.as_view(), name="notes_list"),
]

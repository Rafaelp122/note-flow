from django.views.generic import ListView

from .models import Note


class NotesListView(ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"

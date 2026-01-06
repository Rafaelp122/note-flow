from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Note


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

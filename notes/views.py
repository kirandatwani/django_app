from django.views import generic
from django.urls import reverse_lazy
from .models import Note

class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'notes_list'

    def get_queryset(self):
        """Return the all notes."""
        return Note.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'notes/create.html'
    model = Note
    fields = ['message']
    success_url = reverse_lazy('notes:index') # more robust than hardcoding to /notes/; directs user to index view after creating a note

class UpdateView(generic.edit.UpdateView):
    template_name = 'notes/update.html'
    model = Note
    fields = ['message']
    success_url = reverse_lazy('notes:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'notes/delete.html' # override default of notes/note_confirm_delete.html
    model = Note
    success_url = reverse_lazy('notes:index')

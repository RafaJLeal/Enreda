from rest_framework import viewsets

from note.models import Note
from note.serializer import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all().prefetch_related('users')
	serializer_class = NoteSerializer

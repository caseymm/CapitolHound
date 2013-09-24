# Create your views here.
from searchExample.models import Note, NoteSegment
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

from searchExample.forms import NotesSearchForm
from searchExample.query import NotesQuery


def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    context = {
        'notes': notes,
    }
    return render_to_response('notes.html', {'notes': notes})
    #return render(request, 'home', context)

def note(request, pk):
    #this isn't right
    note = get_object_or_404(Note, id=pk)
    notesegment = get_object_or_404(NoteSegment, id=pk)
    all_segments = list(note.notesegment_set.all())
    #all_segments = NoteSegment.objects.all()
    
    context = {
        'note': note,
        'notesegment': notesegment,
        'all_segments': all_segments,
    }
    return render(request, "searchExample/note.html", context)


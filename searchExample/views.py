# Create your views here.
from searchExample.models import Note, NoteSegment
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

from searchExample.forms import NotesSearchForm
#from searchExample.query import NotesQuery
#from searchExample.utils import BorkHighlighter


def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    all_notes = Note.objects.all()
    context = {
        'notes': notes,
        'all_notes': all_notes,
    }
    #return render_to_response('notes.html', {'notes': notes})
    return render(request, 'searchExample/notes.html', context)

def note(request, pk):
    #form = NotesSearchForm(request.GET)
    #notes = form.search()
    note = get_object_or_404(Note, id=pk)
    notesegment = get_object_or_404(NoteSegment, id=pk)
    all_segments = list(note.notesegment_set.all())
   
    context = {
        'notes': notes,
        'note': note,
        'notesegment': notesegment,
        'all_segments': all_segments,
    }
    return render(request, "searchExample/note.html", context)

#def note_list(request, pk):
#    note = get_object_or_404(Note, id=pk)
#    all_notes = Note.objects.all()
#    return render(request, "../haystackExample/templates/base.html", {'all_notes': all_notes})



# Create your views here.
from searchExample.models import Note, NoteSegment
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

#from django.shortcuts import render

#def home(request):
    #context = {'message': 'Here\'s the message from the views file'}
    #return render(request, "base.html", context)

from django.shortcuts import render_to_response

from searchExample.forms import NotesSearchForm


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
    
    context = {
        'note': note,
        'notesegment': notesegment,
    }
    return render(request, "searchExample/note.html", context)

#def notesegment(request, pk):
#    notesegment= get_object_or_404(NoteSegment)
#    
#    context = {
#       'notesegment': notesegment,
#    }
#    return render(request, "searchExample/note.html", context)
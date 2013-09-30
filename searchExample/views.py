# Create your views here.

from searchExample.models import Note, NoteSegment
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

from searchExample.forms import NotesSearchForm#
#from searchExample.query import NotesQuery
#from searchExample.utils import BorkHighlighter
import urllib
from urllib import urlparse


def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    #all_notes = Note.objects.all()
    context = {
        'notes': notes,
        #'allnotes': allnotes,
    }
    #return render_to_response('notes.html', {'notes': notes})
    return render(request, "searchExample/notes.html", context)

def note(request, pk):
    #this isn't right
    note = get_object_or_404(Note, id=pk)
    #all_notes = Note.objects.all()
    notesegment = get_object_or_404(NoteSegment, id=pk)
    all_segments = list(note.notesegment_set.all())
    #all_segments = NoteSegment.objects.all()
    
    
    
    pageURL = request.get_full_path()
    urlData = urlparse(pageURL)
    theQuery = urlData.query.strip('=')
    
    
    context = {
        'tempvar': theQuery,
        'note': note,
        'notesegment': notesegment,
        'all_segments': all_segments,
    }
    return render(request, "searchExample/note.html", context)

#def note_list(request, pk):
#    note = get_object_or_404(Note, id=pk)
#    all_notes = Note.objects.all()
#    return render(request, "../haystackExample/templates/base.html", {'all_notes': all_notes})


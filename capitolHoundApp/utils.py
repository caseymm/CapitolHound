# In ``myapp/utils.py``...
#from haystack.utils import Highlighter
#from capitolHoundApp.forms import NotesSearchForm
#from capitolHoundApp.models import Note, NoteSegment

#class BorkHighlighter(Highlighter):
#    def find_window(self, highlight_locations):
#        their_start, their_end = super(ShowMoreTextHighlighter, self).find_window(highlight_locations)
#        # perform some clever operations here to find an earlier start location
#        my_start = their_start/2 # or just do something simple
#        return (my_start, their_end)
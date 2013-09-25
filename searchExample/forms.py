from haystack.forms import SearchForm
#from haystack.query import SearchQuerySet

class NotesSearchForm(SearchForm):

    def no_query_found(self):
        query = self.searchqueryset.all()
        return query 

#from haystack.forms import HighlightedModelSearchForm
#from django import forms
#from searchExample.models import Note, NoteSegment

#class NotesSearchForm(HighlightedModelSearchForm):
    #project = forms.ModelChoiceField(queryset=NoteSegment.objects.all(), required=False)

    #def search(self):
        #lQuerySet = super(NotesSearchForm, self).search()

        #if self.cleaned_data['project']:
            #lQuerySet = lQuerySet.filter(project=self.cleaned_data['project'])

        #return lQuerySet

from haystack.forms import SearchForm
#from haystack.query import SearchQuerySet



class NotesSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()


#not currently using

from haystack.query import SearchQuerySet
from haystack.utils import Highlighter

class NotesQuery(SearchQuerySet):
    def no_query_found(self):
        all_results = SearchQuerySet(self).all()
        #sqs = SearchQuerySet().filter(content='foo').highlight()
        sqs = SearchQuerySet().filter(content=all_results).highlight()
        highlighter = Highlighter(search_query)
        result = sqs[0]
        result.highlighted['text'][0]
        print highlighter.highlight(sqs[0].text)
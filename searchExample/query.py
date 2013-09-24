from haystack.query import SearchQuerySet

class NotesQuery(SearchQuerySet):
    def no_query_found(self):
        all_results = SearchQuerySet(self).all()
        #sqs = SearchQuerySet().filter(content='foo').highlight()
        sqs = SearchQuerySet().all().highlight()
        result = sqs[0]
        result.highlighted['text'][0]
from django.core.management.base import NoArgsCommand, CommandError
from haystack.query import SearchQuerySet
from django.db import connection
from searchExample.models import Note, NoteSegment, UserProfile, SaveThisSearch
import datetime

# your custom command must reference the base management classes like this:
class Command(NoArgsCommand):
    # it's useful to describe what the function does:
    help = 'Search'
    
    def handle_noargs(self,**options):
        try:
            self.auto_search()
        except Exception, e:
            print e
        finally:
            connection.close()

    def auto_search(self):
        ###excludes notes before this date
        for e in NoteSegment.objects.exclude(timestamp__lt="2013-12-01 00:00"):
            #all_results = SearchQuerySet().all()
            sqs = SearchQuerySet().auto_query('senate').values_list("title", flat=True)
            #result = sqs.exclude(pub_date__gte=datetime.date(2008, 1, 1), pub_date__lt=datetime.date(2013, 12, 9))
            print(sqs)
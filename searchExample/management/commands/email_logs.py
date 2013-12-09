#!/usr/bin/env python
from django.core.management.base import NoArgsCommand, CommandError
from django.contrib.auth.models import User
from searchExample.models import Note, NoteSegment, UserProfile, SaveThisSearch
from django.db import connection
from haystack.query import SearchQuerySet
import datetime

# your custom command must reference the base management classes like this:
class Command(NoArgsCommand):
    # it's useful to describe what the function does:
    help = 'Saves email logs'
    
    def handle_noargs(self,**options):
        try:
            self.save_email_logs()
        except Exception, e:
            print e
        finally:
            connection.close()

    def save_email_logs(self):
        for e in Note.objects.exclude(timestamp__lt="2013-12-01 00:00"):
            for user in User.objects.all():
                self.stdout.write(user.username)
                for e in SaveThisSearch.objects.all().filter(user=user):
                    print (e.saved_searches)
                    
                    sqs = SearchQuerySet().auto_query(e.saved_searches).values_list("title", flat=True)
                    #result = sqs.exclude(pub_date__gte=datetime.date(2008, 1, 1), pub_date__lt=datetime.date(2013, 12, 9))
                    print(sqs)

                
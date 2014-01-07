#!/usr/bin/env python
from django.core.management.base import NoArgsCommand, CommandError
from django.contrib.auth.models import User
from capitolHoundApp.models import Note, NoteSegment, UserProfile, SaveThisSearch, EmailLogs
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
        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d 00:00")
        for user in User.objects.all():
            self.stdout.write(user.username)
            for e in SaveThisSearch.objects.all().filter(user=user):
                user_searches = e.saved_searches
                for e in Note.objects.exclude(timestamp__lt=today):
                
                    print (user_searches)
                    
                    #sqs = SearchQuerySet().auto_query(e.saved_searches).values_list("title", flat=True)
                    sqs = SearchQuerySet().auto_query(user_searches).count()
                    print(sqs)
                    
                    if sqs > 0:
                        link_to_result = "<a href=\'http://capitolhound.com/search/?q=" + user_searches + "\'><b>" + user_searches + "</b></a>"
                        print(link_to_result)                        
                        
                        todays_log = EmailLogs.objects.create(user = user, saved_alert_term = user_searches, saved_alert_link = link_to_result)
                        print("saved the email log")

                
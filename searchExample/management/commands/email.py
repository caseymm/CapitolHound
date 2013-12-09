#!/usr/bin/env python
from django.core.management.base import NoArgsCommand, CommandError
from django.contrib.auth.models import User
from django.shortcuts import render
from searchExample.models import Note, NoteSegment, UserProfile, SaveThisSearch
from django.core.mail import EmailMessage
from django.db import connection
#from django.template.loader import get_template
#from django.template import Context


# your custom command must reference the base management classes like this:
class Command(NoArgsCommand):
    # it's useful to describe what the function does:
    help = 'Sends daily email with subscribed alerts'
    
    def handle_noargs(self,**options):
        try:
            self.send_email_alerts()
        except Exception, e:
            print e
        finally:
            connection.close()

    def send_email_alerts(self):
        for user in User.objects.all():
            self.stdout.write("got users")
            
            subject = 'Today\'s Alerts'
            from_email="Capitol Hound Alerts <alerts@capitolhound.com>"
            terms = SaveThisSearch.objects.all().filter(user=user).values_list('saved_searches', flat=True)
            text = 'Hi %s, here are your alerts: %s.' % (user.username, ', '.join(terms))
            
            self.stdout.write("gets here")
            msg = EmailMessage(subject, text, from_email, [user.email])
            msg.send()
                                    
        self.stdout.write("sending complete")
                    
                    
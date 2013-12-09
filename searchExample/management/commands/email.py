#!/usr/bin/env python
from django.core.management.base import NoArgsCommand, CommandError
from django.contrib.auth.models import User
from django.shortcuts import render
from searchExample.models import Note, NoteSegment, UserProfile, SaveThisSearch, EmailLogs
from django.core.mail import EmailMultiAlternatives
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
            terms = EmailLogs.objects.all().filter(user=user).values_list('saved_alert_term', flat=True)
            links = EmailLogs.objects.all().filter(user=user).values_list('saved_alert_link', flat=True)
            text_content = 'Hi %s, here are your alerts for today: %s.' % (user.username, ', '.join(links))
            html_content = 'Hi %s, here are your alerts for today:<br /><b> %s </b><br />' % (user.username, ', '.join(links))
            #t = loader.get_template('registration/email.txt')
            #c = Context({
            #'saved_alert_term': 'saved_alert_term',
            #'saved_alert_link': 'saved_alert_link',
            #})
            self.stdout.write("gets here")
            msg = EmailMultiAlternatives(subject, text_content, from_email, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
                                    
        self.stdout.write("sending complete")
                    
                    
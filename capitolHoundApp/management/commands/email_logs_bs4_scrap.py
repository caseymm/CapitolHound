#!/usr/bin/env python
from django.core.management.base import NoArgsCommand, CommandError
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from capitolHoundApp.models import Note, NoteSegment, UserProfile, SaveThisSearch
from urllib2 import urlopen
from django.db import connection

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
        for user in User.objects.all():
            self.stdout.write(user.username)
            #for e in SaveThisSearch.objects.all().filter(user=user).values_list('saved_searches', flat=True):
            for e in SaveThisSearch.objects.all().filter(user=user):
                print (e.saved_searches)

                BASE_URL = "http://capitolhound.com/search/?q=" + e.saved_searches
                print(BASE_URL)
                SEARCH_URL = "http://capitolhound.com/search/"

                #def get_category_links(section_url):
                html = urlopen(BASE_URL).read()
                
                soup = BeautifulSoup(html, "lxml")
                transcript_result_list = soup.p
                ind_transcripts = transcript_result_list.find_all('span', attrs={'class': 'object_date'})
                print(ind_transcripts)
                #self.stdout.write(ind_transcripts)
                #transcript_links = [SEARCH_URL + a["href"] for a in p.findAll("a")]
                #print transcript_links
                #return transcript_links
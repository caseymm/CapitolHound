#!/usr/bin/env python
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from capitolHoundApp.models import Note, NoteSegment, UserProfile, SaveThisSearch

class Command(BaseCommand):
    args = '<transcript>'
    help = 'Parses and imports latest transcript'
    
    def handle(self, *args, **options):
        for transcript in args:
            try:
                #echo ("trying")
                self.stdout.write("trying")
                
                #Use code below when file to import is on web server :

                #import urllib2
                #import re
                #response = urllib2.urlopen("http://domainname.com/transcript.html")
                #html = response.read()
                
                
                #end server version
                
                #Use this code when file is local:
                
                with open ("transcript.html", "r") as tempFile:
                    #html=tempFile.read().replace('<p>[SPEAKER CHANGE]', '<p class="speaker_change">').replace(",", "")
                    html=tempFile.read().replace('<p>[SPEAKER CHANGE]', '<p class="speaker_change">')

                
                soup = BeautifulSoup(html)
                
                transcript_title = soup.h1;
                transcript = (soup.find_all('div', attrs={'class': 'section'}));
                
                
                transcript_header = Note.objects.create(header = transcript_title, title = transcript_title)
                #this_transcript_title.save()
                
                print(transcript_title);
                
                
                #transcript_header.save()
                print ("header saved")
                
                print Note.objects.latest('id')
                this_note = Note.objects.latest('id')
                
                for sections in transcript:
                    section_time = sections.h3;
                    section_text = sections.find_all('p');
                    
                    #print ("Section Time: %d", section_time);
                    #print ("Section Text: %d", section_text);
                    
                    each_section = NoteSegment.objects.create(note = this_note,title = "title", audio = "audio", timestamp = section_time, body = section_text)
                    #each_section_text = NoteSection.objects.create(body = section_text)
                    
                    #each_section_text.save()
                
            except Note.DoesNotExist:
                raise CommandError('didn\'t work')
        
                
        
        #each_section.save()
        #print ("section saved")
        
        #echo ("start of scrape.py")
        self.stdout.write("end of scrape.py")

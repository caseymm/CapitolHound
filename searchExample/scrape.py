#!/usr/bin/env python

from bs4 import BeautifulSoup
from django.db.searchExample.models import Note, NoteSegment, UserProfile, SaveThisSearch


#Use code below when file to import is on web server :

#import urllib2
#import re
#response = urllib2.urlopen("http://domainname.com/transcript.html")
#html = response.read()




#end server version

#Use this code when file is local:

with open ("transcript.html", "r") as tempFile:
    html=tempFile.read().replace('<p>[SPEAKER CHANGE]', '<p class="speaker_change">');

#print html;



soup = BeautifulSoup(html)

transcript_title = soup.h1;
transcript = (soup.find_all('div', attrs={'class': 'section'}));

this_transcript_title = Note.objects.get(title = transcript_title)
this_transcript_title.save()

print(transcript_title);




for segments in transcript:
    segment_time = segments.h3;
    segment_text = segments.find_all('p');
    
    print ("Segment Time: %d", segment_time);
    print ("Segment Text: %d", segment_text);
    
    each_segment_time = NoteSegment.objects.get(timestamp = segment_time)
    each_segment_text = NoteSegment.objects.get(body = segment_text)
    
    each_segment_time.save()
    each_segment_text.save()
    

#print ("Segment Text: %d", segment_text);


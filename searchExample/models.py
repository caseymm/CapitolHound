from django.db import models
from django.contrib.auth.models import User
import datetime

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d 00:00")


class Note(models.Model):
    header = models.CharField(max_length=1000)
    meta = models.TextField()
    title = models.CharField(max_length=1000)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.header
        return self.meta
        return self.timestamp 

class NoteSegment(models.Model):
    note = models.ForeignKey(Note)
    title = models.CharField(max_length=1000)
    body = models.TextField()
    audio = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
        return self.body
        return self.timestamp

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    # this is where I want the query strings to be saved
    topics = models.CharField(max_length=1000)
    #use with foreign key to saved searches class

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    
class SaveThisSearch(models.Model):
    #searchid = models.IntegerField(max_length=1000, primary_key=True)
    #searchid = models.CharField(max_length=1000, primary_key=True)
    user = models.ForeignKey(User)
    saved_searches = models.TextField()
    #saved_searches = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.user.username+'\'s searches'
    
class EmailLogs(models.Model):
    user = models.ForeignKey(User)
    saved_alert_term = models.TextField()
    saved_alert_link = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
        return self.user.username+'\'s email logs'+today
        return self.timestamp
    


    

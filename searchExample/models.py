from django.db import models
from django.contrib.auth.models import User


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
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
        return self.body
        return self.timestamp
    
#class User(models.Model):
    # The additional attributes we wish to include.
    #username = models.CharField(max_length=1000)
    #email = models.CharField(max_length=1000)
    #password = models.CharField(max_length=1000)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    # this is where I want the query strings to be saved
    topics = models.CharField(max_length=1000)
    #use with foreign key to saved searches class
    
    

#class SavedSearches
    #searches...

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

    

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
    
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    topics = models.CharField(max_length=1000)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
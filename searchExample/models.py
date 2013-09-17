from django.db import models
#from django.contrib.auth.models import User


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

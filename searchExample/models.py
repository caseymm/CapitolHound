from django.db import models
#from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
from django.conf.urls.defaults import patterns, url
from searchExample import views

urlpatterns = patterns('',
    url(r'^', views.notes, name='notes'),
    url(r'^(?P<pk>\d+)$', views.note, name='note'),
    )

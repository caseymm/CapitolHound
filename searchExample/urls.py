from django.conf.urls import patterns, include, url
from searchExample import views

urlpatterns = patterns('',
    url(r'^$', views.notes, name='notes'),
    #url(r'^note_content/(?P<pk>\d+)$', views.note_content, name='note_content'),
    url(r'^(?P<pk>\d+)$', views.note, name='note'),
    )
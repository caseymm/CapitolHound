from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from haystack.views import SearchView
from haystack.query import SearchQuerySet
from haystack.forms import SearchForm

from capitolHoundApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'capitolHound.views.home', name='home'),
    # url(r'^capitolHound/', include('capitolHound.foo.urls')),
    url(r'^$', views.notes, name='notes'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^email_success/$', views.email_test, name='email_test'),
    url(r'^search/$', include('haystack.urls')),
    #url(r'^$', include('haystack.urls')),
    #url(r'^', include('capitolHoundApp.urls')),
    url(r'^search/(?P<pk>\d+)$', views.note, name='note'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
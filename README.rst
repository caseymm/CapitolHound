Capitol Hound
==============

Capitol Hound is a `Reese News Lab <http://reesenewslab.org/>`_ project that will enable users to search through a database of transcripts, text and audio, from
the North Carolina General Assembly. The idea for the project originated in the summer of 2013 as a startup idea and developed by a
team of three journalism students in the fall of 2013.

About
-----

Capitol Hound is built using the django framework. The search funtionality is provided by `django-haystack <https://github.com/toastdriven/django-haystack>`_,
wich runs off of a java based search engine, `elasticsearch <http://www.elasticsearch.org/>`_.

The `live development site <http://capitolhound.com>`_ allows users to search through example transcripts, register for
an account, log in and out, and subscribe to daily alerts.

Installing haystack and elasticsearch
-------------------------------------

This project is currently running on:

* django-haystack v2
* elasticsearch 0.90.1

Requirements for haystack:

* pip install django-haystack==2.0.0
* pip install pyelasticsearch==0.5 

Requirements for elasticsearch:

* brew install elasticsearch

Elasticsearch can be launched using:

* elasticsearch -f -D es.config=/usr/local/Cellar/elasticsearch/0.90.2/config/elasticsearch.yml

If you need to wipe the db and set it up again:

From within capitolHound run:

* python manage.py sqlclear capitolHoundApp | python manage.py dbshell

Scripts
-------

scraper.py, email_logs.py, and email.py are three scripts used to import transcripts, log saved searches, and send out daily alert emails.

**scraper.py**

To run (from main capitolHound project folder where manage.py is):

* python manage.py scraper transcript.html

scraper.py is set up to scrape an html file specifically named transcript.html located in the main project folder
(same place as manage.py)

**email_logs.py**

To run:

* python manage.py email_logs

This will gather all of the terms that each user has saved to generate a list of alerts to send them

**email.py**

To run:

* python manage.py email

This will send an email to all users that will include links to the saved terms that appear in the transcript added to the
database today.


Credits
=======

This project belongs to `Reese News Lab <http://reesenewslab.org/>`_ and the `School of Journalism and Mass Communication at The University of
North Carolina at Chapel Hill <http://jomc.unc.edu/>`_.

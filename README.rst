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

Credits
=======

This project belongs to `Reese News Lab <http://reesenewslab.org/>`_ and the `School of Journalism and Mass Communication at The University of
North Carolina at Chapel Hill <http://jomc.unc.edu/>`_.

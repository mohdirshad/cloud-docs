from django.conf.urls import patterns, include, url
from notes.views import *


urlpatterns = patterns('',
     url(r'^$', Note.as_view(), name='notelist'),
     url(r'^add/$', Create_notes.as_view(), name='create'),

)

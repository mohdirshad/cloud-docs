from django.conf.urls import patterns, include, url
from notes.views import *


urlpatterns = patterns('',
     url(r'^$', Notes.as_view(), name='notelist'),
     url(r'^add/$', CreateNote.as_view(), name='create'),

)

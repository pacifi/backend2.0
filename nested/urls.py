from django.conf.urls import url
from django.urls import path

from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    url(r'^api/musicians/$', MusicianListView.as_view()),
    url(r'^api/musicians/(?P<pk>\d+)/$', MusicianView.as_view()),
    url(r'^api/albums/$', AlbumListView.as_view()),
    url(r'^api/albums/(?P<pk>\d+)/$', AlbumView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

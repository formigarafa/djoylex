from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
  url(r'^$', 'index', name="index"),
  url(r'^post/(?P<id>\d+)$', 'show', name="show"),
  url(r'^post/new/$', 'new', name="new"),
  url(r'^post/create/$', 'create', name="create"),
  url(r'^post/(?P<id>\d+)/edit/$', 'edit', name="edit"),
  url(r'^post/(?P<id>\d+)/update/$', 'update', name="update"),
  url(r'^post/(?P<id>\d+)/destroy/$', 'destroy', name="destroy"),
)
from django.conf.urls.defaults import *

urlpatterns = patterns('oauth.views',
  url(r'^facebook/step1$', 'step1'),
  url(r'^facebook/step2$', 'step2'),
  url(r'^logout$', 'logout'),
)
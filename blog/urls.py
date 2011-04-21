from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
  url(r'^$', 'index', name="index"),
  url(r'^post/(?P<id>\d+)$', 'show', name="show"),
#    url(r'^settings/$', notice_settings, name="notification_notice_settings"),
#    url(r'^(\d+)/$', single, name="notification_notice"),
#    url(r'^feed/$', feed_for_user, name="notification_feed_for_user"),
#    url(r'^mark_all_seen/$', mark_all_seen, name="notification_mark_all_seen"),
)
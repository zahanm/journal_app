
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('transcribe.views',
  url(r'^$', 'index', name='home'),
)

urlpatterns += patterns('journal.views',
  url(r'^journal/add/$', 'add'),
  url(r'^journal/(?P<journal_id>\d+)/$', 'show'),
)

urlpatterns += patterns('',
  url(r'^admin/', include(admin.site.urls)),
)

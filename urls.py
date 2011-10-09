
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('transcribe.views',
  url(r'^$', 'index', name='home'),
)

urlpatterns += patterns('journal.views',
  url(r'^(?P<journal_id>\d+)/$', 'show'),
  url(r'^add/$', 'add'),
)

urlpatterns += patterns('',
  url(r'^admin/', include(admin.site.urls)),
)


from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # url(r'^ppjournal/', include('ppjournal.foo.urls')),
  url(r'^$', 'transcribe.views.index', name='home'),
  url(r'^journal/add/$', 'journal.views.add'),
  url(r'^journal/(?P<journal_id>\d+)/$', 'journal.views.show'),

  url(r'^admin/', include(admin.site.urls)),
)

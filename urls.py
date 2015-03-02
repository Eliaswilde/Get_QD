from django.conf.urls import patterns, include, url
from django.contrib import admin
from settings import DEBUG, MEDIA_ROOT, STATIC_ROOT

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', 'main.views.demo', name='demo')
)


if DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT,
            'show_indexes': True,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': STATIC_ROOT,
            'show_indexes': True,
        }),
   )
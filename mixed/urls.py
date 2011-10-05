from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('mixed.views',
    url(r'^$', 'index', name='index'),
    url(r'^feed.xml$', 'feed', name='feed'),
)
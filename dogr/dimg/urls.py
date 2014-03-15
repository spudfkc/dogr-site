from django.conf.urls import patterns, url

from dimg import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
        url(r'^(?P<entry_id>[a-z\d]+)/$', views.detail, name='detail'),
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/home/ncc/workspace/dogr/dogr/static', 'show_indexes': True })
)




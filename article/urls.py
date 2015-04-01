from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import RSSFeed
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'article.view  s.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.home',name='home'),
    url(r'^(?P<id>\d+)','blog.views.post',name='detail'),
    url(r'^about/$','blog.views.about',name='about'),
    url(r'^archive/$','blog.views.archive',name='archive'),
    url(r'^feed/$',RSSFeed(),name='RSS'),

)

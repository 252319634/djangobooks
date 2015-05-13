from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from books import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^latest/$', views.latest_books),
)

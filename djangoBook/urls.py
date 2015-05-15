from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.conf.urls.defaults import *
from books import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^latest/$', views.latest_books),
    url(r'^time/$', views.current_datetime),
    url(r'^hello/$', views.hello),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^mypage/$', views.current_section),
)

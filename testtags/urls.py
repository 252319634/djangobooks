# -*- coding: utf-8 -*-


from django.conf.urls import patterns, include, url
from testtags import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'djangoBook.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^cut_blank/', views.cut_blank),

                       )
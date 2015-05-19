from django.conf.urls import patterns, include, url
from django.contrib import admin
import testtags

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^testtags/', include(testtags.urls)),

)
urlpatterns += patterns('books.views',

                        url(r'^$', 'current_section'),
                        url(r'^latest/$', 'latest_books'),
                        url(r'^time/$', 'current_datetime'),
                        url(r'^hello/$', 'hello'),
                        url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
                        url(r'^mypage/$', 'current_section'),
                        url(r'^meta/$', 'display_meta'),
                        url(r'^search/$', 'search'),
                        )
urlpatterns += patterns('contact.views',

                        url(r'^contact/$', 'contact'),
                        url(r'^contact/thanks/$', 'thanks'),
                        )

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'passion3.views.home', name='home'),
    # url(r'^passion3/', include('passion3.foo.urls')),

    url(r'^$', 'rants.views.blog_index', name="home"),
    url(r'^rant/(?P<slug>[-\w]+)$', 'rants.views.rant', name="rant"),
    url(r'^rant/(?P<rant>[-\w]+)/(?P<slug>[-\w]+)/$', 'rants.views.post', name="post"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

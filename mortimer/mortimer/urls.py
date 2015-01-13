from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mortimer.views.home', name='home'),
    url(r'^home/', 'mortimer.views.home'),                 # page that skips auth, for now
    url(r'^login/', 'mortimer.views.log_in', name='log_in'),
    url(r'^logout/', 'mortimer.views.logout_view', name='logout_view'),
    url(r'^authN/', 'mortimer.views.authN', name='authN'),
)


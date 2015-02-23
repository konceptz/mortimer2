from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mortimer.views.home', name='home'),
    url(r'^test/', 'mortimer.views.test'),
    url(r'^home/', 'mortimer.views.home'),
    url(r'^get_creds/', 'mortimer.views.get_creds'),
    url(r'^create/', 'mortimer.views.create_app'),
    url(r'^remove/', 'mortimer.views.remove_app'),
    url(r'^create_creds/', 'mortimer.views.create_creds'),
    url(r'^remove_creds/', 'mortimer.views.remove_creds'),
    url(r'^modify_creds/', 'mortimer.views.modify_creds'),
    url(r'^error/', 'mortimer.views.error'),
    url(r'^login/', 'mortimer.views.log_in', name='log_in'),
    url(r'^logout/', 'mortimer.views.logout_view', name='logout_view'),
    url(r'^authN/', 'mortimer.views.authN', name='authN'),
)


from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('openstack_aps_app.views',
                       url(r'^$', 'index'),
                       url(r'^instance_create/', 'instance_create'),
                       url(r'^instance_list/', 'instance_list'),
                       url(r'^tenant_create/', 'tenant_create'),
                       url(r'^tenant_list/', 'tenant_list'),
                       url(r'^quota_list/(?P<tenant_id>\w+)?$', 'quota_list'),
)

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'device/(?P<device>[\w-]+)[/?]$', views.device, name='device'),
    url(r'^device[/?]$', views.devices, name='devices'),
    url(r'device/(?P<device>[\w-]+)/stats[/?]$', views.device_stats, name='device_stats'),
    url(r'^application[/?]$', views.applications, name='applications')
]
from django.contrib import admin

from api.models import DeviceStat, Device, ApplicationGroup

admin.site.register(Device)
admin.site.register(DeviceStat)
admin.site.register(ApplicationGroup)
import datetime
import json

from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import JsonResponse

from api.models import DeviceStat, Device, ApplicationGroup


def only_get(request):
    if request.method is not 'GET':
        return HttpResponse(status=403)


def object_found(obj):
    if obj:
        return HttpResponse(to_json(obj), content_type="application/json; charset=utf-8")
    else:
        return HttpResponse(status=404)


def device(request, device=''):
    only_get(request)

    device_obj = Device.objects.get(name=device)

    return object_found([device_obj])


def device_stats(request, device=''):
    device_obj = Device.objects.get(name=device)
    stats = None

    if device_obj:
        stats = DeviceStat.objects.filter(device=device_obj.name)

    return object_found(stats)


def devices(request):
    only_get(request)

    location = request.GET.get('location')
    application = request.GET.get('application')
    devices = Device.objects.all()

    if location is not None:
        devices = devices.filter(location=str(location))
    if application is not None:
        devices = devices.filter(application=str(application))

    return object_found(devices)


def applications(request):
    only_get(request)

    return object_found(ApplicationGroup.objects.all())


def api_stats(request, start=0, end=0):
    start_datetime = datetime.datetime.fromtimestamp(int(start))
    end_datetime = datetime.datetime.fromtimestamp(int(end))

    print start_datetime, end_datetime

    stats = DeviceStat.objects.filter(timestamp__range=[start_datetime, end_datetime])
    return HttpResponse(to_json(stats))


def to_json(objects):
    return serializers.serialize('json', objects)

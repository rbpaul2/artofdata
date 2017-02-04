from __future__ import unicode_literals

from django.db import models

class ApplicationGroup(models.Model):
    name = models.CharField(max_length=50, primary_key=True, db_index=True)
    business = models.CharField(max_length=50, null=True)
    priority = models.IntegerField(null=True)  # 1-10


class Device(models.Model):
    name = models.CharField(max_length=50, primary_key=True, db_index=True)
    environment = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)

    os = models.CharField(max_length=50)
    os_eos = models.CharField(max_length=50)
    ip = models.CharField(max_length=50, null=True)

    application = models.ForeignKey(ApplicationGroup)


class DeviceStat(models.Model):

    device = models.ForeignKey(Device)

    timestamp = models.DateTimeField()
    cpu_cores = models.IntegerField()
    cpu_capcity = models.FloatField()
    cpu_usage_mhz = models.FloatField()
    cpu_usage_percent = models.FloatField()
    mem_capacity_provisioned = models.FloatField()
    mem_usage = models.FloatField()
    disk_r_throughput = models.FloatField()
    disk_w_throughput = models.FloatField()
    network_in_throughput = models.FloatField()
    network_tx_throughput = models.FloatField()

    class Meta:
        ordering = ['timestamp']

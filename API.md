# /api/application
List of Applications
~~~~
[<...>,{"model": "api.applicationgroup", "pk": 1, "fields": {"name": "app_1", "location": "Stanardsville", "business": "Food", "priority": 10}}]
~~~~


# /api/device  (optional url params: ?location={location}  ?applicaiton={application})
List of all Devices
~~~~
[<...>,{"model": "api.devicestat", "pk": 10959, "fields": {"device": "3c86e59f-13b2-4bbf-8dc2-1d69824d4533", "timestamp": "2013-06-30T22:03:24Z", "cpu_cores": 1, "cpu_capcity": 2925.999516, "cpu_usage_mhz": 19.50666344, "cpu_usage_percent": 0.6666666666666667, "mem_capacity_provisioned": 119724.0, "mem_usage": 39145.066666666666, "disk_r_throughput": 0.0, "disk_w_throughput": 0.6666666666666666, "network_in_throughput": 0.6666666666666666, "network_tx_throughput": 0.6666666666666666}}]
~~~~
# /api/device/{device_name}
Device Static Data
~~~~
{"model": "api.device", "pk": "3c86e59f-13b2-4bbf-8dc2-1d69824d4533", "fields": {"environment": "rnd", "os": "Windows 2008 R2", "os_eos": "4/1/13", "ip": "147.158.166.153", "application": 4}}
~~~~
# /api/device/{device_name}/stats/
List of stats for device
~~~~
[<...>,{"model": "api.devicestat", "pk": 150545, "fields": {"device": "6aa79220-092b-49f4-a75c-169b7524d4a9", "timestamp": "2013-08-12T13:40:46Z", "cpu_cores": 1, "cpu_capcity": 2925.99956, "cpu_usage_mhz": 3.9013327466666667, "cpu_usage_percent": 0.13333333333333333, "mem_capacity_provisioned": 156768.0, "mem_usage": 63612.53333333333, "disk_r_throughput": 0.0, "disk_w_throughput": 1.0666666666666667, "network_in_throughput": 0.0, "network_tx_throughput": 0.0}}]
~~~~

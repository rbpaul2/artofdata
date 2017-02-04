# art-of-data
GhostRed GE Digital Cincinnati Hackathon API for Art of Data


# quick start

download *db.sqlit3* file from [box](https://ge.box.com/s/c9nda7yshun1qgugtxckvcmvy8xzi0ax) and place into project root

install dependencies:
~~~~
pip install -r requirements.txt
~~~~

run server
~~~~
python manage.py runserver
~~~~

## details
1. Device: 
  * Name - Name of the Device
  * IP Address
  * Environment - Faststorage or rnd evnrionment
  * Location - pyshical geolocation
  * Operating System
  * OS End of Service Date
2. Application: Name, Business, Priority
3. Data:
  * Timestamp: number of milliseconds since 1970-01-01.
  * CPU cores: number of virtual CPU cores provisioned.
  * CPU capacity provisioned (CPU requested): the capacity of the CPUs in terms of MHZ, it equals to number of cores x speed * per core.
  * CPU usage: in terms of MHZ.
  * CPU usage: in terms of percentage
  * Memory provisioned (memory requested): the capacity of the memory of the VM in terms of KB.
  * Memory usage: the memory that is actively used in terms of KB.
  * Disk read throughput: in terms of KB/s
  * Disk write throughput: in terms of KB/s
  * Network received throughput: in terms of KB/s
  * Network transmitted throughput: in terms of KB/s

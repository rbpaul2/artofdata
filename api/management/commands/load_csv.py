import datetime
import os
import random
import socket
import struct
import uuid

import pytz
from django.core.management.base import BaseCommand

from api.models import Device, DeviceStat, ApplicationGroup


class Command(BaseCommand):
    args = 'No args needed'
    help = 'Load CSV files from nested date folders'

    app_names = ["TEST1", "TEST2"]
    business = ["Corporate", "Research", "Development", "Manufacturing", "Deployment", "Packaging", "Sales", "Human Resources", "Finance", "Regulation", "Legal", "Operations", "IT", "Marketing", "Engineering"]
    locations = ["Warner", "Lyon", "Willow Run", "Conyersville", "Mount Baker", "Farmington Lake", "Martins Corner",
                 "Willaha", "Center", "Spring City", "Mittenlane", "East Waterford", "Coltman", "Scottsville", "Hebron",
                 "Longview", "Emerson", "North Knoxville", "Momford Landing", "Ipswich", "Storms", "Kalauao", "Farwell",
                 "Brentwood Village", "Wilhelm Park", "Bannister Acres", "Bent Pine", "Mitchell", "Social Circle",
                 "Kreutzberg", "Cimarron", "Brookhaven", "Montverde Junction", "Midland City", "Sacramento",
                 "Del Rey Oaks", "Coal Creek", "Rabbitown", "Fairland", "Gaskil", "Morgan Mill", "Merrimac South",
                 "Stanardsville", "Two Brooks", "Curriers", "Skookumchuck", "Edgerton", "Slater"]
    models = ["Windows 2008 R2", "Windows 2012 R2", "Oracle Enterprise Linux", "Red Hat Enterprise Linux", "SunOS"]
    os_eol = [["4/1/13", "4/1/13", "4/1/13", "4/1/13", "4/1/13"],
              ["1/1/23", "1/1/23", "1/1/23", "1/1/23", "1/1/23"],
              ["12/1/12", "6/1/15", "2/1/19", "10/1/22", "4/1/25"],
              ["5/1/13", "8/1/16", "10/1/18", "2/1/22", "9/1/24"],
              ["11/1/11", "3/1/14", "7/1/18", "4/1/23", "6/1/25"]]

    def handle(self, *args, **options):
        """
        """

        self.apps = self.make_applications()

        self.load('fastworks', '/Users/alanplacko/Development/hackathon/fastStorage')
        self.load('rnd', '/Users/alanplacko/Development/hackathon/rnd')

    def make_applications(self):
        apps = []

        for a in range(1, 101):
            # id = uuid.uuid4().__str__().split('-')[0]
            name = 'app_' + str(a)
            app, created = ApplicationGroup.objects.get_or_create(
                name=name,
                business=self.get_random(self.business),
                priority=random.randint(1, 10)
            )
            apps.append(app)

        return apps

    def get_random(self, array):
        assert isinstance(array, list)
        return random.choice(array)

    def load(self, environment, root):
        """
        :param environment: environment the virtual machine resides in
        :param root: directory where they are stored on disc
        """

        self.csv_hash = dict()

        for name in self.load_files(root):
            self.load_csvs(environment, root + '/' + name)

    def random_ip(self):
        """return random IP address"""
        return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

    def load_csvs(self, environment, folder):
        """
        :param environment: environment the vm is pulled from
        :param folder: folder to iterate over
        :return: status of loading folders
        """
        csv_files = self.load_files(folder)

        for csv_file in csv_files:
            csv_filename = folder + '/' + csv_file

            key = os.path.basename(csv_filename).split('.')[0]
            try:
                csv_hash_key = self.csv_hash[key]
            except:
                csv_hash_key = uuid.uuid4()
                self.csv_hash[key] = csv_hash_key

            with open(csv_filename, 'rb') as file:

                model_num = random.randint(0,4)
                eos_num = random.randint(0,4)

                try:
                    device = Device.objects.get(pk=csv_hash_key)
                except:
                    device, created = Device.objects.get_or_create(
                        name=csv_hash_key,
                        location=self.get_random(self.locations),
                        environment=environment,
                        os=str(self.models[model_num]),
                        os_eos=str(self.os_eol[model_num][eos_num]),
                        ip=self.random_ip(),
                        application=self.get_random(self.apps)
                    )



                print 'adding stats to device:', device.name

                try:

                    lines = file.readlines()

                    csv_count = len(lines[1:])
                    stat_count = 0
                    stats = list()

                    for contents in lines[1:]:
                        row = contents.split(';\t')


                        ts = datetime.datetime.fromtimestamp(int(row[0]))
                        localtz = pytz.timezone('UTC')
                        ts = localtz.localize(ts)

                        stat = DeviceStat(
                            device=device,
                            timestamp=ts,
                            cpu_cores=row[1],
                            cpu_capcity=row[2],
                            cpu_usage_mhz=row[3],
                            cpu_usage_percent=row[4],
                            mem_capacity_provisioned=row[5],
                            mem_usage=row[6],
                            disk_r_throughput=row[7],
                            disk_w_throughput=row[8],
                            network_in_throughput=row[9],
                            network_tx_throughput=row[10]
                        )

                        if stat:
                            stat_count+=1
                            stats.append(stat)

                    # if stat_count < csv_count:
                    #     print 'Not all stats loaded:', csv_filename
                    #
                    # else:

                    DeviceStat.objects.bulk_create(stats, batch_size=500)
                except:
                    print 'Could not load stats for:', csv_filename


    def load_files(self, path_to_dir):
        """
        :param path_to_dir:
        :return: list of directory contents of path_to_dir
        """
        folders = os.listdir(path_to_dir)
        return [foldername for foldername in folders if not foldername.startswith('.')]

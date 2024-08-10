import time
import json
from urllib.request import urlopen
import os
import django
from django.core.management.base import BaseCommand
from earthquakes.models import Earthquake

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Starting the daemon...")
        self.get_earthquakes()
    
    def get_earthquakes(self):
        while True:
            data = json.load(urlopen(f'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson'))
            #print("____________________________")
            #print(data["features"][0]["id"])

            for feature in data["features"]:
                earthquake = feature["properties"]
                #print(earthquake)
                earthquake_check = Earthquake.objects.filter(api_id=earthquake["ids"])
                if earthquake_check.exists():
                    continue
                new_earthquake = Earthquake(api_id=earthquake["ids"], magnitude=earthquake["mag"], place=earthquake["place"], time=str(earthquake["time"]), tsunami=earthquake["tsunami"])
                new_earthquake.save()
            time.sleep(10)
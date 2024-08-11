import time
import json
from urllib.request import urlopen
import os
import django
from django.core.management.base import BaseCommand
from earthquakes.models import Earthquake
import datetime
from django.core.mail import EmailMessage, send_mail
from earthsafe.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User

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
                
                # Find the date using milliseconds after epoch, which is what is given from the api
                
                # Milliseconds since UNIX epoch
                milliseconds = earthquake["time"]

                # Convert milliseconds to seconds
                seconds = milliseconds / 1000.0

                # Create a datetime object from the UNIX epoch
                epoch = datetime.datetime(1970, 1, 1)

                # Add the seconds to the epoch
                date = epoch + datetime.timedelta(seconds=seconds)

                new_earthquake = Earthquake(api_id=earthquake["ids"], magnitude=earthquake["mag"], place=earthquake["place"], time=date, tsunami=earthquake["tsunami"])
                new_earthquake.save()

                # Generate mailing list
                mailing_list  = list(User.objects.values_list('email', flat=True))

                # Send email to all
                send_mail(
                    f"Magnitude {earthquake["mag"]} Earthquake Detected: {earthquake["place"]} at {date}",
                    "Mark yourself as safe or in need of help.",
                    EMAIL_HOST_USER,
                    mailing_list,
                    [],
                )

                #email.send()
                print("Emails sent.")

            time.sleep(10)
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import json
from datetime import date, datetime, timedelta
from urllib.request import urlopen
from .models import Earthquake, Status

# Create your views here.
def earthquakes(request):
    return render(request, "earthquakes/earthquakes.html", {
        "earthquakes": reversed(Earthquake.objects.all())
    })

def addstatus(request):
    print(request)
    if request.method == "POST" and request.user.is_authenticated:
        data = json.loads(request.body)
        if (data["status"] == "green") or (data["status"] == "yellow") or (data["status"] == "red"):
            print(data)
            earthquake = Earthquake.objects.get(id=data["earthquake_id"])
            if Status.objects.filter(earthquake=earthquake, user=request.user):
                tempquake = Status.objects.get(earthquake=earthquake, user=request.user)
                tempquake.delete()
                print("STATUS DELETED")
            userstatus = Status(user=request.user, earthquake=earthquake, status=data["status"])
            userstatus.save()
            print("STATUS ADDED")
            return HttpResponse(status=200)
    print('DID NOT PASS')
    return HttpResponse(status=500)

def earthquake(request, id):
    earthquake = Earthquake.objects.get(pk=id)
    return render(request, "earthquakes/earthquake.html", {
        "statuses": earthquake.statuses.all()
    }

    )
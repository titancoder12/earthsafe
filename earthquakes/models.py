from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Earthquake(models.Model):
    id = models.AutoField(primary_key=True)
    api_id = models.CharField(max_length=11)
    magnitude = models.FloatField()
    place = models.CharField(max_length=64)
    time = models.DateTimeField()
    tsunami = models.IntegerField()

    def __str__(self):
        return f"Magnitude {self.magnitude} earthquake: {self.place} at {self.time}"

class Status(models.Model):
    earthquake = models.ForeignKey(Earthquake, on_delete=models.CASCADE, related_name="statuses")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="statuses")
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user} has status {self.status} for {self.earthquake}"
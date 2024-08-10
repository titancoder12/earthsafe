from django.db import models

# Create your models here.
class Earthquake(models.Model):
    id = models.AutoField(primary_key=True)
    api_id = models.CharField(max_length=11)
    magnitude = models.IntegerField()
    place = models.CharField(max_length=64)
    time = models.TimeField()
    tsunami = models.IntegerField()

    def __str__(self):
        return f"Magnitude {self.magnitude} earthquake in {self.place} at {self.time}"
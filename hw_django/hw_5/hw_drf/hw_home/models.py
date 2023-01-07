from django.db import models


class Sensor(models.Model):
    sensor_name = models.CharField(max_length=50)
    sensor_description = models.TextField()


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

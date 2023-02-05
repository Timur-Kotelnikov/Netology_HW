from django.contrib.auth.models import User
from django.db import models


class Adv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='WTS something!')
    description = models.TextField(blank=True)
    posted_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

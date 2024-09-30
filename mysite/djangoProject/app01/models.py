from django.db import models


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    password = models.CharField(max_length=64)
    data = models.IntegerField(null=True, blank=True)
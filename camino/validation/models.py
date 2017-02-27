from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class User(models.Model):
    username = models.CharField(max_length=200)
    classname = models.CharField(max_length=200)
    phone = models.IntegerField(default=0)
    pin = models.IntegerField(default=0)
    temp = models.BooleanField(default=True)

    def __str__(self):
        return self.username

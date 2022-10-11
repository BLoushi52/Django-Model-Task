from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Restuarants(models.Model):

    name = models.CharField(max_length=30),
    description = models.CharField(max_length=""),
    opening_time = models.TimeField(),
    closing_time = models.TimeField(),
    created_at = models.DateTimeField(),

from django.db import models
import time

# Create your models here.

class book(models.Model):
    ISBN = models.CharField(blank=False, max_length=13, null=True, unique=True)
    price = models.FloatField(null=False, blank=False, default=99.99)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.ISBN



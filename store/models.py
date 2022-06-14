from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length = 100)
    district = models.CharField(max_length = 150)
    address = models.CharField(max_length = 50)
    number = models.CharField(max_length = 20)
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 15)
    createdAt = models.DateField(default = date.today)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

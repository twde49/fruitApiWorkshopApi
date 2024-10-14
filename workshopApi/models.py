import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Fruit(models.Model):
    name = models.CharField(max_length=50,default='MissingNo')
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Season(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    UUID = models.UUIDField(default=uuid.uuid4, editable=False)

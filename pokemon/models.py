from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
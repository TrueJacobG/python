from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    isPremium = models.BooleanField(default=False)

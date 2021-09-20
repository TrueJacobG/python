from django.db import models
from django.urls import reverse

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    isPremium = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('photos:photos-detial', kwargs={'id': self.id})

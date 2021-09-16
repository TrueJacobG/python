from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    isTrue = models.BooleanField(default=True)

    def get_absolute_url(self):
        # return f"/product/{self.id}"
        return reverse("product-detail", kwargs={'id': self.id})

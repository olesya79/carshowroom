from django.conf import settings
from django.db import models


# Create your models here.

class Car(models.Model):
    user_id = models.ForeignKey('Provider', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=210)
    model = models.CharField(max_length=210)
    brand = models.CharField(max_length=210)
    provider = models.CharField(max_length=210)
    country_of_origin = models.CountryField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    characteristic = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=210)
    сompany_name = models.CharField(max_length=210)
    founder = models.CharField(max_length=210)
    email = models.CharField(max_length=210)
    additional_information = models.TextField(blank=True)

    def __str__(self):
        return self.title

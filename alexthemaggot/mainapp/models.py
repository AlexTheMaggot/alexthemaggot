from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    telegram = models.CharField(max_length=20, null=True, blank=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    viber = models.CharField(max_length=20, null=True, blank=True)
    skype = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
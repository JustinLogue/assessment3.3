from django.db import models


class widgets(models.Model):
    description = models.CharField(max_length=200)
    quantity = models.IntegerField
from django.db import models

class BatterModel(models.Model):
    name = models.CharField(max_length=35)


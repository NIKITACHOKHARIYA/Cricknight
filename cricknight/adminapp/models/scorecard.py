from django.db import models

class Scorecard(models.Model):
    name = models.CharField(max_length=35)
from django.db import models

class Bowler(models.Model):
    name = models.CharField(max_length=35)
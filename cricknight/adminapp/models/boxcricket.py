from django.db import models

class BoxCricket(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
from django.db import models

class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35)
    description = models.TextField()

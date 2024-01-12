from django.db import models
from .player import Player

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=35)
    captain_name = models.CharField(max_length=35)
    username=models.ForeignKey(Player,on_delete=models.CASCADE,default=1)



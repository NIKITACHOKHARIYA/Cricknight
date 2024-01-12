from django.db import models
from .user import User
class Player(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    player_id = models.IntegerField(max_length=35)
    name = models.CharField(max_length=35)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    # def __str__(self):
    #     return self.username


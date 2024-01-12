from django.db import models

class User(models.Model):
    #user_id = models.IntegerField(max_length=3)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=30,primary_key=True,unique=True)
    password = models.CharField(max_length=8)
    email = models.EmailField()
    contact = models.IntegerField()
    def __str__(self):
        return self.username


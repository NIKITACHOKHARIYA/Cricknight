from django.db import models
class Ground(models.Model):
    ground_id = models.AutoField(primary_key=True)
    ground_name = models.CharField(max_length=35)
    #description = models.CharField(max_length=35)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=35)
    #contact = models.IntegerField(max_length=10)
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ground_img/',blank=True)



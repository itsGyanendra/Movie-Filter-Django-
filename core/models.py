from django.db import models

# Create your models here.



class movie(models.Model):
    Title = models.CharField(max_length=120)
    Year = models.IntegerField(default=0)
    Rating = models.DecimalField(max_digits=3, decimal_places=1)
    
    
    
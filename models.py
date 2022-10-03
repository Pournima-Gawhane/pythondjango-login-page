from django.db import models

# Create your models here.
class User_detail(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height =models.DecimalField(max_digits=16, decimal_places=4)
    weight =models.DecimalField(max_digits=16, decimal_places=4)


    def __str__(self):
        
        return self.fullname
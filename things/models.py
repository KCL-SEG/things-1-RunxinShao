from django.db import models

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


# Create your models here.
class Thing(models.Model):
    name = models.TextField(unique = True,blank = False, max_length = 30)
    description = models.TextField(unique = False,blank = True, max_length = 120)
    quantity = models.IntegerField(unique = False,validators=[MinValueValidator(0,message = 'can not less than 0'),MaxValueValidator(100,message = 'can not bigger than 100')]
    )

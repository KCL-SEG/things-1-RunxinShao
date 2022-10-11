from django.db import models

# Create your models here.
class Thing():
    name = models.TextField(unique = True,blank = False, max_length = 30)
    description = models.TextField(unique = False,blank = True, max_length = 120)
    quantity = models.IntegerField(unique = False,validators=[MinValueValidator(
    0,message = 'can not less than 0')]
    validators=[MaxValueValidators(100,message = 'can not bigger than 100')]
    )

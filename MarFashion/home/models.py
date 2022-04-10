#from turtle import ondrag
from django.db import models
from django.templatetags.static import static
from django.contrib.auth.models import User
from platformdirs import user_cache_dir


class Clothes(models.Model):

    idCloth = models.IntegerField()  # 1:hats 2:dresses 3:shoes 4:bags
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50)  
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="clothes")


class ClothesType(models.Model):
    TYPE_CHOICES = [
        ('Hats', 'H'),
        ('Dresses', 'D'),
        ('Shoes', 'S'),
        ('Bags', 'B'),
    ]
    id = models.IntegerField(primary_key=True)
    typeCloth = models.CharField(max_length=50, choices=TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clothesType")
    
    def __str__(self):
        return self.typeCloth


from django.db import models
from django.templatetags.static import static


class Clothes(models.Model):
    idCloth = models.IntegerField()  # 1:hats 2:dresses 3:shoes 4:bags
    type = models.CharField(max_length=50)  # imgURL ex:hat1, shoes1
    price = models.DecimalField(max_digits=5, decimal_places=2)


class ClothesType(models.Model):
    TYPE_CHOICES = [
        ('Hats', 'H'),
        ('Dresses', 'D'),
        ('Shoes', 'S'),
        ('Bags', 'B'),
    ]
    id = models.IntegerField(primary_key=True)
    typeCloth = models.CharField(max_length=50, choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.typeCloth


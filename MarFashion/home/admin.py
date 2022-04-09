from django.contrib import admin
from .models import *




@admin.register(ClothesType)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ['id', 'typeCloth']


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ['idCloth', 'type', 'price']

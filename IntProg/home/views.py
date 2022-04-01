import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.views.generic import CreateView, DetailView, ListView
from .forms import *


#VIEWS
#TO GET THE 4 TYPES OF CLOTHES
def home(request):
    clothesType = ClothesType.objects.all
    return render(request, 'home.html', { 'clothesType': clothesType, })


#def clothes_detail(request, idCloth):
#    clothes = Clothes.objects.all.get(idCloth=idCloth)
#    return render(request, 'clothes_detail.html', {
#        'clothes': clothes,
#    })


def clothes_detail(request, idCloth):
    clothes = Clothes.objects.filter(idCloth=idCloth)
    return render(request, 'clothes_detail.html', {
        'clothes': clothes,
    })


def clothesCart(request, type):
    clothesCart = Clothes.objects.filter(type=type)
    return render(request, 'clothesCart.html', {
        'clothesCart': clothesCart,
    })


class itemAdd(CreateView):
    model = Clothes
    success_url ='/'
    form_class = itemAdd



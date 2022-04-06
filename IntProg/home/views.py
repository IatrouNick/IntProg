from ast import Or
from audioop import add
from ctypes import Union
import re
from typing import List
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from numpy import append
# Create your views here.
from .models import *
from django.views.generic import CreateView, DetailView, ListView , UpdateView
from django.views.generic.edit import CreateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic.edit import DeleteView

class SignupView(CreateView):
    form_class =UserCreationForm
    template_name = 'home/signup.html'
    success_url = "/"

    def get(self,request, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args,**kwargs)






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

class itemDelete(DeleteView):
    model = Clothes
    success_url = '/list'
    template_name = 'home/clothes_deleteView.html'


class itemAdd(CreateView):
    model = Clothes
    success_url = '/'
    form_class = items

class itemList(ListView):
    model = Clothes


class itemUpdate(UpdateView):
    model = Clothes
    success_url = '/'
    form_class = items


class itemDetail(DetailView):
    model = Clothes
    template_name = 'home/clothes_detailView.html' 
    context_object_data = 'clothes'
    

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

def searchView(request):
    if request.method =="POST":
        searched = request.POST.get('searched')
        clothesSearched = Clothes.objects.filter(Q(type__contains=searched) | Q(price__contains=searched))
        return render(request, 'search.html',
            {'searched':searched,
             'clothesSearched':clothesSearched})
    else:
        return render(request, 'search.html',{})
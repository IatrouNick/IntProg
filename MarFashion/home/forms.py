from ast import Constant
from dataclasses import fields
from multiprocessing.sharedctypes import Value
from tkinter import Tk
from turtle import title
from xml.dom import ValidationErr
from django import forms
from .models import *
from django.core.exceptions import ValidationError






class items(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = {'idCloth','type','price','user' }
        
        widgets = {
            'idCloth': forms.TextInput(attrs={'class': 'form-control mb-2 ', 'style': 'width:200px'}),
            'type': forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:200px'}),
            'price': forms.TextInput(attrs={'class': 'form-control mb-2' ,'style': 'width:100px'}),
            'user': forms.Textarea(attrs={'class': 'form-control mb-2', 'style': 'width:100px'}),
            'user': forms.HiddenInput(),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['user'] = '1'

    def clean_self(self):
        idCloth = self.cleaned_data['idCloth']
         

        if 'Django' not in idCloth:
            raise forms.ValidationError('Please insert an id')
        return idCloth

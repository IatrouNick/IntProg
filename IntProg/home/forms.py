from dataclasses import fields
from tkinter import Widget
from turtle import title
from xml.dom import ValidationErr
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class itemAdd(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = {'idCloth','type','price' }
        widgets = {
            'idCloth': forms.TextInput(attrs={'class': 'form-control mb-2 ', 'style': 'width:200px'}),
            'type': forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:200px'}),
            'price': forms.TextInput(attrs={'class': 'form-control mb-2' ,'style': 'width:100px'})

        }

    def clean_self(self):
        idCloth = self.cleaned_data['idCloth']
        if 'Django' not in idCloth:
            raise forms.ValidationError('Please insert an id')
        return idCloth

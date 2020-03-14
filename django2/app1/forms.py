from django import forms
from django.forms import ModelForm
from app1.models import *


class Form(ModelForm):
    class Meta:
        model=dbtest
        fields=['name','major','age','grade','gender'] # '__all__'도 가능
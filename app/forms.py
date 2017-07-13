#!/usr/bin/python
# coding: utf-8

from django.forms import ModelForm
#from django import forms
from app.models import Moment
from django.db import models


#KIND_CHOICES=(
    #('python','python'),
    #('java','java'),
#)

class MomentForm(ModelForm):
    #content = models.CharField(max_length=300)
    #user_name = models.CharField(max_length=20,default='unkown_name')
    #kind = models.CharField(max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0])#
    class Meta:
        model = Moment
        fields = ('content','user_name','kind')
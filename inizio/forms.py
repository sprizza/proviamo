#!usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import Inizio

class PostForm(forms.ModelForm):
    class Meta:
        model = Inizio
        fields = ('titolo', 'posizione', 'contenuto',)



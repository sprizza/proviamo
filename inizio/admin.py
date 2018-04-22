# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Inizio

class InizioModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'data'] #funzone restituzione titolo
    list_filter = ['data'] #filtro per ricerca per data
    search_fields = ['titolo', 'contenuto'] #ricerca per titolo e contenuto
    prepopulated_fields = {'slug': ('titolo',)}

    class Meta:
        model = Inizio

admin.site.register(Inizio, InizioModelAdmin)

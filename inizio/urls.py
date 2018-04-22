#!usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.admindocs import views

from django.views.generic import ListView, DetailView
from .models import Inizio


urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset = Inizio.objects.all().order_by("-data"),
        template_name = "lista_post.html",
        paginate_by = 4), name = "lista"),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = Inizio,
        template_name = "singolo.html"), name = "singolo"),

    url(r'^post/$',ListView.as_view(
        queryset = Inizio.objects.all().order_by("post_edit"),
        template_name = "post_edit.html"), name = "post_edit"),


    url(r'^gioco/$', ListView.as_view(
        queryset = Inizio.objects.all().order_by("gioco"),
        template_name = "gioco.html"), name = "gioco"),


]



# ^(?P<id>\d+)/(?P<slug>[\w-]+)/$

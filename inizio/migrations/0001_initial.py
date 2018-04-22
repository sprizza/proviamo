# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inizio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=120)),
                ('contenuto', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readbooks', '0004_auto_20160803_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publishers',
            field=models.ManyToManyField(blank=True, to='readbooks.Publisher'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-20 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190820_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='tousers',
            field=models.TextField(max_length=10),
        ),
    ]

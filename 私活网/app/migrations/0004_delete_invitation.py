# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-20 06:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190820_1418'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Invitation',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-28 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tractor',
            new_name='Machinery',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-21 01:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='create_time',
            new_name='created_time',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-24 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minutes', '0004_minutesdocument_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minutesdocument',
            name='groups',
        ),
    ]

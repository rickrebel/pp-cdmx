# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-08-27 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_account', '0008_ppimage_error_cell'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppimage',
            name='vision_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]

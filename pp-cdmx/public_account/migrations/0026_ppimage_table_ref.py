# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-19 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_account', '0025_publicaccount_suburb_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppimage',
            name='table_ref',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-19 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_account', '0024_publicaccount_match_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaccount',
            name='suburb_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
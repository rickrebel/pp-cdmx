# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-08-21 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20200812_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalproject',
            name='variation',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Variacion'),
        ),
    ]

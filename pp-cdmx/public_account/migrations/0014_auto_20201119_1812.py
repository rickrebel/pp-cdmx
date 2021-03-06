# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-11-20 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_account', '0013_publicaccount_orphan_rows'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaccount',
            name='ignore_columns',
            field=models.CharField(blank=True, help_text='columnas a ignorar para la alineacion horizontal', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='publicaccount',
            name='unreadable',
            field=models.CharField(blank=True, choices=[('bajo', 'bajo'), ('media', 'media'), ('alto', 'alto')], max_length=50, null=True, verbose_name='Nivel de ilegibilidad'),
        ),
    ]

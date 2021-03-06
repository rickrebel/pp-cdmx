# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-11-14 01:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public_account', '0012_auto_20200903_1734'),
        ('project', '0014_auto_20200830_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='anomalyfinalproject',
            name='public_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='public_account.PublicAccount'),
        ),
        migrations.AlterField(
            model_name='anomalyfinalproject',
            name='final_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.FinalProject'),
        ),
    ]

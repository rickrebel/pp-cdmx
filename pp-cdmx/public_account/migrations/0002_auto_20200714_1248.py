# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-07-14 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaccount',
            name='original_pdf',
            field=models.FileField(blank=True, null=True, upload_to='public_account', verbose_name='PDF original'),
        ),
        migrations.AlterField(
            model_name='publicaccount',
            name='pages',
            field=models.TextField(blank=True, null=True, verbose_name='Paginas'),
        ),
        migrations.AlterField(
            model_name='publicaccount',
            name='period_pp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.PeriodPP', verbose_name='Periodo PP'),
        ),
        migrations.AlterField(
            model_name='publicaccount',
            name='townhall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geographic.TownHall', verbose_name='Alcaldia'),
        ),
    ]

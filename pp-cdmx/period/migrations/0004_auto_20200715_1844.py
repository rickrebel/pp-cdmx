# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-07-15 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0003_auto_20200715_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodpp',
            name='pdf_iecm',
            field=models.FileField(blank=True, null=True, upload_to='period_pp', verbose_name='Archivo PDF del IECM'),
        ),
    ]

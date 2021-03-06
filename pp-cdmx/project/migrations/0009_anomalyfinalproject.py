# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-07-16 00:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0005_anomaly'),
        ('project', '0008_auto_20200715_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnomalyFinalProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anomaly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classification.Anomaly')),
                ('final_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.FinalProject')),
            ],
            options={
                'verbose_name': 'Anomal\xeda y Proyecto Final',
                'verbose_name_plural': 'Anomal\xeda y Proyecto Final',
            },
        ),
    ]

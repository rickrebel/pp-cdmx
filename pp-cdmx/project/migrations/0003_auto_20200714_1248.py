# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-07-14 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200714_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalproject',
            name='approuved',
            field=models.FloatField(blank=True, null=True, verbose_name='Aprobado'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='assigned',
            field=models.FloatField(blank=True, null=True, verbose_name='Asignado'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='category_cp',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Categoria CP'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='description_cp',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion CP'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='excecuted',
            field=models.FloatField(blank=True, null=True, verbose_name='Ejecutado'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='final_name',
            field=models.TextField(blank=True, null=True, verbose_name='Nombre Final'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='modified',
            field=models.FloatField(blank=True, null=True, verbose_name='Modificado'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='observation',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='period_pp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.PeriodPP', verbose_name='Periodo PP'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='progress',
            field=models.IntegerField(blank=True, null=True, verbose_name='Progreso'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project', verbose_name='Proyecto'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='suburb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geographic.Suburb', verbose_name='Colonia'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='total_votes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total de Votos'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='user_validation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario validador'),
        ),
        migrations.AlterField(
            model_name='finalproject',
            name='validated',
            field=models.BooleanField(default=False, verbose_name='Validado'),
        ),
        migrations.AlterField(
            model_name='project',
            name='category_iedf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classification.CategoryIEDF', verbose_name='Categoria IEDF'),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_winer',
            field=models.BooleanField(default=False, verbose_name='Es el ganador'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name_iedf',
            field=models.CharField(max_length=255, verbose_name='Nombre del IEFD'),
        ),
        migrations.AlterField(
            model_name='project',
            name='period_pp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.PeriodPP', verbose_name='Periodo PP'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.IntegerField(verbose_name='ID del Proyecto'),
        ),
        migrations.AlterField(
            model_name='project',
            name='suburb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geographic.Suburb', verbose_name='Colonia'),
        ),
        migrations.AlterField(
            model_name='project',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Votos'),
        ),
    ]

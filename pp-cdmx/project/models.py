# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from geographic.models import Suburb

from period.models import PeriodPP
from classification.models import CategoryIEDF

from django.contrib.auth.models import User


class Project(models.Model):
    suburb = models.ForeignKey(Suburb, verbose_name=u"Colonia")
    period_pp = models.ForeignKey(PeriodPP, verbose_name=u"Periodo PP")
    name_iedf = models.CharField(
        max_length=255,
        verbose_name=u"Nombre del IEFD")
    project_id = models.IntegerField(verbose_name=u"ID del Proyecto")
    category_iedf = models.ForeignKey(
        CategoryIEDF,
        blank=True,
        null=True,
        verbose_name=u"Categoria IEDF")
    votes = models.IntegerField(default=0, verbose_name=u"Votos")
    is_winer = models.BooleanField(
        default=False, verbose_name=u"Es el ganador")

    class Meta:
        verbose_name = "Proyecto de Presupuesto"
        verbose_name_plural = "Proyectos de Presupuestos"

    def __unicode__(self):
        return self.name_iedf


class FinalProject(models.Model):
    suburb = models.ForeignKey(Suburb, verbose_name=u"Colonia")
    period_pp = models.ForeignKey(PeriodPP, verbose_name=u"Periodo PP")
    project = models.ForeignKey(
        Project,
        blank=True,
        null=True,
        verbose_name=u"Proyecto")
    total_votes = models.IntegerField(
        blank=True, null=True, verbose_name=u"Total de Votos")
    description_cp = models.TextField(
        blank=True, null=True, verbose_name=u"Descripcion CP")
    final_name = models.TextField(
        blank=True,
        null=True,
        verbose_name=u"Nombre Final")
    category_cp = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=u"Categoria CP")
    # category_ollin
    # subcategory

    # Ammounts
    assigned = models.FloatField(
        blank=True, null=True, verbose_name=u"Asignado")
    approuved = models.FloatField(
        blank=True, null=True, verbose_name=u"Aprobado")
    modified = models.FloatField(
        blank=True,
        null=True,
        verbose_name=u"Modificado")
    excecuted = models.FloatField(
        blank=True, null=True, verbose_name=u"Ejecutado")
    progress = models.IntegerField(
        blank=True, null=True, verbose_name=u"Progreso")

    # Observations
    observation = models.TextField(
        blank=True, null=True, verbose_name=u"Observaciones")
    validated = models.BooleanField(default=False, verbose_name=u"Validado")
    user_validation = models.ForeignKey(
        User, blank=True, null=True, verbose_name=u"Usuario validador")
    # original_page

    class Meta:
        verbose_name = "Proyecto Final en la Cuenta Publica"
        verbose_name_plural = "Proyectos Finales en la Cuenta Publica"

    def __unicode__(self):
        return self.project

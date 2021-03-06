# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CategoryIECM, Anomaly


admin.site.register(CategoryIECM)


class AnomalyAdmin(admin.ModelAdmin):
    model = Anomaly
    list_display = ["name", "is_public"]    
    list_filter = ["is_public"]
admin.site.register(Anomaly, AnomalyAdmin)

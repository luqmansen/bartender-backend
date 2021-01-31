from pprint import pprint

from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from egg_report.models import Cage, Report

SKIP_DISPLAY = ['created_at']


class BaseAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    ordering = ('id',)
    list_per_page = 10
    list_display = []
    readonly_fields = ['created_at']


@admin.register(Cage)
class CageAdmin(BaseAdmin):
    list_display = [f.name for f in Cage._meta.fields if f.name not in SKIP_DISPLAY]
    list_editable = [f for f in list_display if f != 'id']
    readonly_fields = []


@admin.register(Report)
class ReportAdmin(BaseAdmin):
    list_display = [f.name for f in Report._meta.fields]


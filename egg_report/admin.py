from pprint import pprint

from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from egg_report.models import CageNum, Report

SKIP_DISPLAY = ['created_at']


class BaseAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    ordering = ('id',)
    list_per_page = 10
    list_display = []
    readonly_fields = ['created_at']


@admin.register(CageNum)
class CageAdmin(BaseAdmin):
    list_display = [f.name for f in CageNum._meta.fields if f.name not in SKIP_DISPLAY]
    list_editable = [f for f in list_display if f is not 'id']
    readonly_fields = []


@admin.register(Report)
class ReportAdmin(BaseAdmin):
    list_display = [f.name for f in Report._meta.fields]


from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from api.models import TestModel


class BaseAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    ordering = ('id',)
    list_per_page = 10
    list_display = []
    readonly_fields = ['created_at', 'updated_at']


@admin.register(TestModel)
class TestAdmin(BaseAdmin):
    list_display = [f.name for f in TestModel._meta.fields]
    readonly_fields = []

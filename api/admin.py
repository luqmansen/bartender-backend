from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from django_summernote.admin import SummernoteModelAdmin
from api.models import Gallery, Article


TITLE = "Website Eduwisata"

admin.site.site_header = TITLE
admin.site.site_title = TITLE
admin.site.index_title = TITLE


class BaseAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    ordering = ('id',)
    list_per_page = 10
    list_display = []
    readonly_fields = ['created_at']


@admin.register(Gallery)
class GalleryAdmin(BaseAdmin):
    list_display = [f.name for f in Gallery._meta.fields]
    readonly_fields = []


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    readonly_fields = ('slug',)

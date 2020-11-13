from django.contrib import admin
from django.utils.html import format_html
from djangoql.admin import DjangoQLSearchMixin
from django_summernote.admin import SummernoteModelAdmin
from api.models import Gallery, Article, TourismPacket

TITLE = "Website Eduwisata"
SKIP_DISPLAY = ['created_at']

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
    list_display = [f.name for f in Gallery._meta.fields if f.name not in SKIP_DISPLAY]
    list_display += ['preview_image']
    readonly_fields = []

    def preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="300"/>')

    preview_image.short_description = "Image"


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    readonly_fields = ('slug',)


@admin.register(TourismPacket)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

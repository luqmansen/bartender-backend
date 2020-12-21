from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from djangoql.admin import DjangoQLSearchMixin

from api.models import Gallery, Content, TourismPackage

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
    list_display += ['image_prev']
    readonly_fields = ['image_prev']
    display = True


@admin.register(Content)
class ContentAdmin(SummernoteModelAdmin, BaseAdmin):
    summernote_fields = '__all__'
    readonly_fields = ('slug', 'image_prev', 'qr_code', 'qr_code_preview')
    display = False
    list_display = ['title']


@admin.register(TourismPackage)
class TourPackageAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

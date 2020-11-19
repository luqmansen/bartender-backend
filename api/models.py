from django.db import models
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
from djmoney.models.fields import MoneyField

from api.utils import unique_slug_generator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelImage(BaseModel):
    image_field = 'image'
    scale = 'w_400,c_scale'

    class Meta:
        abstract = True

    def image_prev(self):
        if getattr(self, self.image_field):
            url = getattr(getattr(self, self.image_field), 'url').split(sep='/')
            url.insert(6, self.scale)
            return mark_safe('<img src="{}" />'.format("/".join(url)))
        return '(No Image)'

    image_prev.short_description = 'Image Preview'
    image_prev.allow_tags = True


class Gallery(BaseModelImage):
    file_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/gallery/', null=False)

    class Meta:
        verbose_name = 'Galeri Gambar'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.file_name)


class Article(BaseModelImage):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(upload_to='images/article/', null=False)
    content = models.TextField()
    slug = models.SlugField(max_length=40, null=True, blank=True)
    image_field = 'header_image'

    class Meta:
        verbose_name = 'Artikel'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class TourismPackage(BaseModel):
    title = models.CharField(max_length=100)
    price = MoneyField(default_currency='IDR', max_digits=10, decimal_places=0)
    content = models.TextField()

    class Meta:
        verbose_name = 'Paket Wisata'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Article)

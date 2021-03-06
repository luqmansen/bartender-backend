import os

from django.db import models
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
from djmoney.models.fields import MoneyField

from api.utils import unique_slug_generator, generate_qr


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def image_prev(image_url, scale='w_400,c_scale'):
    # specifically for cloudinary url
    url = image_url.split(sep='/')
    url.insert(6, scale)
    return mark_safe('<img src="{}" />'.format("/".join(url)))


class BaseModelImage(BaseModel):
    image_field = 'image'
    scale = 'w_400,c_scale'

    class Meta:
        abstract = True

    def image_prev(self):
        if getattr(self, self.image_field):
            url = getattr(getattr(self, self.image_field), 'url')
            return image_prev(url)
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


class Content(BaseModelImage):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(upload_to='images/content/', null=False)
    gallery_image_1 = models.ImageField(upload_to='images/content/', null=True, blank=True)
    gallery_image_2 = models.ImageField(upload_to='images/content/', null=True, blank=True)
    gallery_image_3 = models.ImageField(upload_to='images/content/', null=True, blank=True)

    fun_fact = models.TextField(default=None)
    content = models.TextField()
    slug = models.SlugField(max_length=40, null=True, blank=True)
    qr_code = models.ImageField(upload_to='images/content/', null=False)
    image_field = 'header_image'

    def qr_code_preview(self):
        return image_prev(self.qr_code.url)

    qr_code_preview.short_description = 'Image Preview'
    qr_code_preview.allow_tags = True

    class Meta:
        verbose_name = 'Konten'
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


def pre_save_receiver(sender, instance: Content, *args, **kwargs):
    if not instance.slug:
        slug = unique_slug_generator(instance)
        instance.slug = slug
        instance.header_image.name = '_'.join([slug, instance.header_image.name])
        instance.qr_code = generate_qr('/'.join([os.getenv('FE_HOST'), 'content', instance.slug]))


pre_save.connect(pre_save_receiver, sender=Content)

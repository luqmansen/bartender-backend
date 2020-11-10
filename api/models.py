from django.db import models
from django.db.models.signals import pre_save

from api.utils import unique_slug_generator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Gallery(BaseModel):
    file_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/gallery/', null=False)

    class Meta:
        verbose_name = 'Galeri Gambar'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.file_name)


class Article(BaseModel):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(upload_to='images/article/', null=False)
    content = models.TextField()
    slug = models.SlugField(max_length=40, null=True, blank=True)

    class Meta:
        verbose_name = 'Artikel'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Article)

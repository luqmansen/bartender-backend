from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Gallery(BaseModel):
    file_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/gallery/', blank=True)

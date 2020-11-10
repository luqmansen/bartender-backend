from rest_framework import serializers

from api.models import Gallery


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at']
        model = Gallery

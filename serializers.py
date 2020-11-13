from rest_framework import serializers

from api.models import Gallery, Article, TourismPacket


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at']
        model = Gallery


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at']
        model = Article


class TourismPacketSerializers(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at']
        model = TourismPacket

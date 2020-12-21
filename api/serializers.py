from django.contrib.humanize.templatetags.humanize import intcomma
from rest_framework import serializers

from api.models import Gallery, Content, TourismPackage


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at']
        model = Gallery


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at']
        model = Content


class TourismPackageSerializers(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        exclude = ['created_at']
        model = TourismPackage

    @staticmethod
    def get_price(obj):
        return intcomma(obj.price)
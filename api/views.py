from rest_framework import viewsets

from api.models import Gallery
from serializers import GallerySerializers


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers


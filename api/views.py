from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from rest_framework.response import Response

from api.models import Gallery, Content, TourismPackage
from api.serializers import GallerySerializers, ArticleSerializers, TourismPackageSerializers


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers


class ContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ArticleSerializers

    def retrieve(self, request, *args, **kwargs):
        objs = get_object_or_404(self.queryset, slug=kwargs['slug'])
        return Response(self.serializer_class(objs).data)


class TourismPackageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TourismPackage.objects.all()
    serializer_class = TourismPackageSerializers

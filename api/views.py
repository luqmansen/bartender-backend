from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from rest_framework.response import Response

from api.models import Gallery, Article
from serializers import GallerySerializers, ArticleSerializers


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

    def retrieve(self, request, *args, **kwargs):
        objs = get_object_or_404(self.queryset, slug=kwargs['slug'])
        return Response(self.serializer_class(objs).data)



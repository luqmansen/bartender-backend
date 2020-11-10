from django.urls import path

from api.views import GalleryViewSet

gallery_list = GalleryViewSet.as_view({
    'get' : 'list'
})

urlpatterns = [
    path('gallery/', gallery_list),
]

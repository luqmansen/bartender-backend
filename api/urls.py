from django.urls import path
from django.views.decorators.cache import cache_page

from api.views import GalleryViewSet, ContentViewSet, TourismPackageViewSet

gallery_list = GalleryViewSet.as_view({'get': 'list'})
article_list = ContentViewSet.as_view({'get': 'list'})
article_detail = ContentViewSet.as_view({'get': 'retrieve'})
tourism_package_list = TourismPackageViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('gallery/', cache_page(60)(gallery_list)),
    path('article/', cache_page(60)(article_list), name='article-list'),
    path('article/<str:slug>/', cache_page(60)(article_detail), name='article-detail'),
    path('tourpackage/', cache_page(60)(tourism_package_list))
]

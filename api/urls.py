from django.urls import path

from api.views import GalleryViewSet, ArticleViewSet, TourismPackageViewSet

gallery_list = GalleryViewSet.as_view({'get': 'list'})
article_list = ArticleViewSet.as_view({'get': 'list'})
article_detail = ArticleViewSet.as_view({'get': 'retrieve'})
tourism_package_list = TourismPackageViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('gallery/', gallery_list),
    path('article/', article_list, name='article-list'),
    path('article/<str:slug>/', article_detail, name='article-detail'),
    path('tourpackage/', tourism_package_list)
]

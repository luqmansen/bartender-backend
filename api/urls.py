from django.urls import path

from api.views import GalleryViewSet, ArticleViewSet

gallery_list = GalleryViewSet.as_view({'get': 'list'})
article_list = ArticleViewSet.as_view({'get': 'list'})
article_detail = ArticleViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('gallery/', gallery_list),
    path('article/', article_list, name='article-list'),
    path('article/<str:slug>/', article_detail, name='article-detail')
]

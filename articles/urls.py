from django.urls import path
from .views import (ArticlesView,
                    ArticleDeleteView,
                    ArticleDetailView,
                    ArticleUpdateView,
                    ArticleCreate)


urlpatterns = [
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
    path('new/',ArticleCreate.as_view(),name='article_new'),
    path('',ArticlesView.as_view(),name='article_list')
]
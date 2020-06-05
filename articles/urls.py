from django.urls import path
from .views import (
    ArticleView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView
)

urlpatterns = [
    path('new', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/detail', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticleView.as_view(), name='article_list'),
]
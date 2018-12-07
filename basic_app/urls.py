from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:pk>', views.article_view, name='article'),
    path('article-create', views.ArticleCreateView.as_view(), name='article-create'),
    path('', views.ArticleListView.as_view(), name='home'),
]

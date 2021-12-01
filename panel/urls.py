from django.urls import path

from .views import ArticleListView
from . import views

urlpatterns = [
    path('', views.panel, name="panel"),
    path('news/list/', ArticleListView.as_view(), name="article_lists"),
    path('news/add/', views.news_add, name="article_add"),
]

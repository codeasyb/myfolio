from django.urls import path

from .views import ArticleListView
from . import views

urlpatterns = [
    path('', views.panel, name="panel"),
    path('news/list/', ArticleListView.as_view(), name="article_lists"),
    path('news/add/', views.news_add, name="article_add"),
    # path('news/del/(?P<pk>\d+)', views.news_delete, name="article_delete"),
    path('news/del/<int:pk>', views.news_delete, name="article_delete"),
]

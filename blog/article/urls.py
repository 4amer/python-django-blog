from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('/pub_article/', views.pub_article, name='pub_article')
]
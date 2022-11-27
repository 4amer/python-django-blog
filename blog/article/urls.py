from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('createPost/', views.createPost, name='createPost'),
    path('/pub_article/', views.pub_article, name='pub_article'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name="register"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="index"),
    path('profile',views.profile , name="profile"),
    path('article/<id>',views.article , name="article"),
    path('category/<name>',views.getCategory , name="topic"),
    path('login',views.getLogin , name="login"),
    path('logout',views.getLogout , name="logout"),
    path('author/<name>',views.getAuthor , name="author")
]

from django.urls import path
from . import views
app_name="blogApp"

urlpatterns = [
    path('', views.index , name="index"),
    path('profile',views.profile , name="profile"),
    path('article/<id>',views.article , name="article"),
    path('category/<name>',views.getCategory , name="topic"),
    path('login',views.getLogin , name="login"),
    path('logout',views.getLogout , name="logout"),
    path('author/<name>',views.getAuthor , name="author"),
    path('create',views.getCreatePost , name="createPost"),
    path('logged_in_profile',views.getProfile , name="logged_in_profile"),
    path('update/<id>',views.getUpdate , name="update"),
    path('delete/<id>', views.getDelete, name="delete"),
    path('registration', views.getRegistern, name="registration"),
    path('allCategory',views.getAllCategory , name="allCategory"),
    path('createCategory',views.getCreateCategory , name="createCategory"),
]

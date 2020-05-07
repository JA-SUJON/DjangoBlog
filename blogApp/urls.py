from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="index"),
    path('profile',views.profile , name="profile"),
    path('article/<id>',views.article , name="article"),
]

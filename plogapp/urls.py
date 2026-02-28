from django.urls import path
from .views import postList , post_details

urlpatterns = [
    path("",postList,name="home"),
    path("post/<int:pk>/",post_details , name="post_details")
]




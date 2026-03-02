# urls for functiion based view
"""
from django.urls import path
from .views import postList , post_details

urlpatterns = [
    path("",postList,name="home"),
    path("post/<int:pk>/",post_details , name="post_details")
]
"""

#converting the code with class based view

from django.urls import path
from .views import (postListView, detailPostView, postCreateView, postupdate,deletePost)

urlpatterns = [
    path("post/<int:pk>/", detailPostView.as_view(), name="post_details"),
    path("", postListView.as_view(), name="home"),
    path("post/new/",postCreateView.as_view(), name="new_post"),
    path("post/<int:pk>/edit/",postupdate.as_view(),name="post_update"),
    path("post/<int:pk>/delete/",deletePost.as_view(),name="delete_post")
]




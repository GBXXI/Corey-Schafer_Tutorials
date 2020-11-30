
from django.urls import path

from blog import views
from blog.views import (PostCreateView, PostDetailView, PostListView, PostDeleteView,
                        PostUpdateView, UserPostListView)

urlpatterns = [
    # Since we want it to be the blog homepage we leave the string, blank.
    path("", PostListView.as_view(), name="blog-home"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("user/<str:username>/", UserPostListView.as_view(), name="user-post"),
    path("about", views.about, name="blog-about"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.PostList.as_view(), name="blog"),
    path("post_create/", views.PostCreate.as_view(), name="post_create"),
    path(
        "post_detail/<slug:slug>/",
        views.PostDetail.as_view(),
        name="post_detail",
    ),
    path("post_edit/<slug:slug>", views.PostEdit.as_view(), name="post_edit"),
    path(
        "post_delete/<slug:slug>/delete",
        views.PostDelete.as_view(),
        name="post_delete",
    ),
]

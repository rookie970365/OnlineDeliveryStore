from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.posts, name="posts"),
    path("post/<int:pk>/", views.post, name="post"),
    # path("post/", views.post, name="post"),
    path("tag/<int:tag_id>/", views.filter_by_tag, name="filter_by_tag"),
]
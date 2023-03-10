from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from blog.models import Post, Tag


def posts(request: HttpRequest):
    posts = Post.objects.select_related("author").prefetch_related("tag").all()
    tags = Tag.objects.all()
    context = {"posts": posts, "tags": tags, "filter_by": 0}
    return render(request=request, template_name='blog/posts.html', context=context)


def post(request: HttpRequest, pk: int):
    post_single = get_object_or_404(Post.objects.select_related("author").prefetch_related("tag"), pk=pk)
    context = {"post": post_single}
    return render(request=request, template_name='blog/post_single.html', context=context)

# def post(request: HttpRequest):
#     return render(request=request, template_name='blog/post_single.html')


def filter_by_tag(request: HttpRequest, tag_id):
    posts = Post.objects.prefetch_related("tag").filter(tag=tag_id).all()
    tags = Tag.objects.all()
    context = {"posts": posts, "tags": tags, "filter_by": tag_id}
    return render(request=request, template_name='blog/posts.html', context=context)

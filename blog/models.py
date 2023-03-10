from django.db import models
from typing import TYPE_CHECKING
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    text = models.TextField()
    author = models.ForeignKey("blog.Author", on_delete=models.PROTECT, related_name="post")
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField("blog.Tag", related_name="post")
    # image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('-created', )
        verbose_name_plural = 'Posts'

    if TYPE_CHECKING:
        objects: models.Manager

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.pk, ])


class Author(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:filter_by_tag', kwargs={'tag_id': self.pk})


from django.db import models
from typing import TYPE_CHECKING

from django.urls import reverse


class ProductKind(models.Model):
    name = models.CharField(max_length=64)
    # slug = models.SlugField(max_length=64, unique=True)
    # class Meta:
    #     ordering = ('name')
    #     verbose_name_plural = 'Kinds'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:filter_by_kind', kwargs={'kind_id': self.pk})


class Product(models.Model):
    kind = models.ForeignKey(ProductKind, on_delete=models.PROTECT, related_name="product")
    name = models.CharField(max_length=64)
    # slug = models.SlugField(max_length=64, unique=True)
    # image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    # price = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    origin = models.ManyToManyField("products.ProductOrigin", related_name="product")
    # profile = models.OneToOneField("products.ProductProfile", on_delete=models.CASCADE, related_name="product_profile")
    description = models.TextField(blank=True, null=False)
    # available = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ('name')
    #     verbose_name_plural = 'Products'

    if TYPE_CHECKING:
        objects: models.Manager

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:details', args=[self.pk, ])


class ProductProfile(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="profile")
    degree_of_roast = models.CharField(max_length=64)
    preparation_method = models.TextField(blank=True, null=False)

    def __str__(self):
        return f"Recommended coffee preparation methods: {self.preparation_method}"


class ProductOrigin(models.Model):
    origin = models.CharField(max_length=64)

    def __str__(self):
        return self.origin

    def get_absolute_url(self):
        return reverse('products:filter_by_origin', kwargs={'origin_id': self.pk})

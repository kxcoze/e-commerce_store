from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    # icon = ...
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    category = TreeForeignKey(
        Category, related_name="product_category", on_delete=models.CASCADE, null=True
    )
    price = models.IntegerField(null=False)
    amount = models.PositiveIntegerField(null=False)
    image_path = models.ImageField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    reviews = models.ManyToManyField("users.User", through="Review")

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vote = models.PositiveSmallIntegerField()
    comment = models.TextField()

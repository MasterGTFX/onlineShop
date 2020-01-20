from django.db import models
import os


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    add_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return "[ID:{}] {}".format(self.id, self.name)


def get_image_path(instance, filename):
    return os.path.join('media/images', filename)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    add_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return "[ID:{}] {}".format(self.id, self.name)


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    product_count = models.IntegerField(default=1, blank=False)


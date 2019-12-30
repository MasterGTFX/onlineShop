from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "[ID:{}] {}".format(self.id, self.name)

from django.db import models
from accounts.models import CustomUser  # Import your CustomUser model

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    product_img = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=100)
    count = models.IntegerField()
    product_available = models.BooleanField(default=True)
    shop_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
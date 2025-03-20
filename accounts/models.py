from django.contrib.auth.models import AbstractUser
from django.db import models

class ShopCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('shop_owner', 'Shop Owner'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # New field: Shop owners must select a category
    shop_category = models.ForeignKey(
        ShopCategory, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.username

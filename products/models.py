from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    product_img = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=100)  # Assuming category is a text field
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # Example: Rating out of 5.0
    product_review = models.TextField()
    count = models.IntegerField()
    product_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


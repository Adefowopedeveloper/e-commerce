from django.db import models
from django.contrib.auth.models import User  # Correctly imported User model

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=225, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Changed 'date' to 'created_at'

    def __str__(self): 
        return self.name  # Returns the category name for better admin panel display

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product/', null=True, blank=True)  # Allows empty uploads
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  # Returns the product name for better admin panel display

# Order Model
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # Status field added
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order by {self.user.username} - {self.product.name} (Quantity: {self.quantity})"

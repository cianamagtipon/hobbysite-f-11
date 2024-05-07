from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='merchstore_profile')
    display_name = models.CharField(max_length=63)
    email = models.EmailField()

    def __str__(self):
        return self.display_name

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='products'
    )
    owner = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE,
        null=True 
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('On sale', 'On sale'),
        ('Out of stock', 'Out of stock')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchstore:detail', args=[self.pk])
    
    class Meta:
        ordering = ['name']

class Transaction(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    STATUS_CHOICES = [
        ('On cart', 'On cart'),
        ('To Pay', 'To Pay'),
        ('To Ship', 'To Ship'),
        ('To Receive', 'To Receive'),
        ('Delivered', 'Delivered')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On cart')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.buyer.display_name}"

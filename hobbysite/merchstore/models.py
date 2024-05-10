from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from user_management.models import Profile
from user_management import models as user_models

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
        user_models.Profile, 
        on_delete=models.CASCADE,
        null=True 
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
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
    buyer = models.ForeignKey(
        user_models.Profile, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='buyer'
    )
    product = models.ForeignKey(
        'Product', 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='purchased_product'
    )
    amount = models.PositiveIntegerField()
    cart = "ON CART"
    pay = "TO PAY"
    ship = "TO SHIP"
    receive = "TO RECEIVE"
    delivered = "DELIVERED"
    STATUS_CHOICES = [
        ('On cart', 'On cart'),
        ('To Pay', 'To Pay'),
        ('To Ship', 'To Ship'),
        ('To Receive', 'To Receive'),
        ('Delivered', 'Delivered')
    ]
    status = models.CharField(max_length=20, 
                              choices=STATUS_CHOICES, 
                              default='On cart'
                              )
    created_on = models.DateTimeField(auto_now_add=True)

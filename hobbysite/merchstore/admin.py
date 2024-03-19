from django.contrib import admin
from .models import ProductType, Product


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = ()
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = ()
from django.contrib import admin
from .models import ProductType, Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)

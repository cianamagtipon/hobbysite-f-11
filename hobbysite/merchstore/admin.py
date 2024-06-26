from django.contrib import admin
from .models import ProductType, Product, Transaction


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = ()
    
    search_fields = ["name"]
    list_display = ["name"]
    
    fieldsets = [("Details", {"fields": ("name", "description")})]
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = ()
    
    search_fields = ["name"]
    list_display = ["name", "owner", "product_type", "price", "stock"]

    fieldsets = [("Details", {"fields": [("name", "owner", "description", "price", "stock"), "product_type"]})]
    
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    inlines = ()
    
    search_fields = ["buyer", "product"]
    list_display = ["buyer", "product", "cart", "amount"]

    fieldsets = [("buyer", {"fields": [("product", "cart", "amount")]})]
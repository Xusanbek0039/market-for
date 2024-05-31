from django.contrib import admin
from .models import Product, Category, Review, ProductImage


class ProductImageAdmin(admin.StackedInline):
    """
    Admin inline class for managing
    ProductImage within the ProductAdmin
    """
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for managing Product instances
    """
    list_display = (
        "sku",
        "name",
        "category",
        "calculate_average_rating",
        "price",
        "image",
    )

    ordering = ("sku",)
    inlines = [ProductImageAdmin]


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for managing Category instances
    """
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)

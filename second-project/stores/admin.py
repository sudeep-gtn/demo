from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status']

    # @admin.display(ordering='inventory')
    @admin.display(ordering='inventory', description='Inventory status')
    def inventory_status(self, product):
        if (product.inventory < 30):
            return 'Low'
        return 'Ok'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
admin.site.register(models.Address)




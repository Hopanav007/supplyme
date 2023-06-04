# Register your models here.
from django.contrib import admin
from . import models
from modeltranslation.admin import TranslationAdmin

# Register your models here.
admin.site.register(models.Sub_category)
admin.site.register(models.Category)
admin.site.register(models.Region)
admin.site.register(models.Supplier)
admin.site.register(models.Branch)
admin.site.register(models.Product)
admin.site.register(models.ProductImages)
admin.site.register(models.Customer)
admin.site.register(models.Delivery_point)
admin.site.register(models.Cart)
admin.site.register(models.Cart_item)
admin.site.register(models.Order)


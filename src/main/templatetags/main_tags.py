from django import template

from main.models import Category, Product

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all() 
# @register inclu
def get_supplier_products(supplier):
    return Product.objects.filter(supplier = supplier)
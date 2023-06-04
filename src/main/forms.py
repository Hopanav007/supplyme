from django import forms

from .models import Cart_item, Supplier, Customer

class SupplierForm(forms.ModelForm):
    
    class Meta:
        model = Supplier
        fields = ("user", "title", "avatar", "phone_number", "description")

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ("user", "title", "avatar", "phone_number", "description")

class AddProductForm(forms.ModelForm):

    class Meta:
        model = Cart_item
        fields = ("cart", "product", "quantity")
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
from allauth.account.views import SignupView

from .forms import AddProductForm, CustomerForm, SupplierForm

from .models import Cart, Cart_item, Category, Product, Region, Supplier

from .tasks import send_registration_confirmation

class Regions: 
    def get_regions(self):
        return Region.objects.all()
    def get_categories(self):
        return Category.objects.all()
        

# Create your views here.

class ProductsView(Regions, ListView):
    
    model = Product
    queryset = Product.objects.all()
    # paginate_by = 1

    # def get_context_data(self, *args, **kwargs):
    #     context  = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context
        

    # def get(self, request):
    #     products = Product.objects.all()
    #     return render(request, "main/product_list.html", {"product_list" : products})
    
class ProductDetailView(Regions, DetailView):

    model = Product
    slug_field = "pk"


    # def Post(self, request):
    #     print(request.POST)
        # form = AddProductForm(request.POST)
        # if form.is_valid():
        #     form = form.save()
        #     form.save()
        # return redirect('/')
    # def get(self, request, pk):
        # product = Product.objects.get(id=pk)
        # return render(request, "main/product_detail.html", {"product" : product})

class SupplierDetailView(Regions, DetailView):

    model = Supplier
    slug_field = "pk"

class FilterProductsView(Regions, View):
    
    # paginate_by = 3

    def get(self, request, id):
        products = Product.objects.filter(category__id=id)
        return render(request, "main/product_list.html", {"product_list" : products})
    

class Search(Regions, ListView):
    
    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get("q"))
                                      
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context
    
class CustomerRegisterView(Regions, View):

    # def get_context_data(self, *args, **kwargs):
    #     context  = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
        new_cart = Cart(customer=form)
        new_cart.save()
        return redirect("/")

    def get(self, request):
        return render(request, "main/customer_register.html")
    


class SupplierRegisterView(Regions, View):

    # def get_context_data(self, *args, **kwargs):
    #     context  = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context

    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
        return redirect("/")

    def get(self, request):
        return render(request, "main/supplier_register.html")
    
    
class ChoiceView(Regions, View):

    def get(self, request):
        return render(request, "main/choice.html")
    
    
class CartView(Regions, View):

    def get(self, request, pk):
        cart = Cart.objects.get(id=pk)
        return render(request, "main/cart_detail.html", {"cart" : cart})
    
class CartItemView(Regions, View):
    def post(self, request):
        form = AddProductForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
        else:
            print('some error')
        return redirect('/')


        
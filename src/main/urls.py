from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductsView.as_view(), name='home'),
    path("filter/<int:id>", views.FilterProductsView.as_view(), name="filter"),
    path("search", views.Search.as_view(), name="search"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name='product_detail'),
    path("suppliers/<int:pk>/", views.SupplierDetailView.as_view(), name='supplier_detail'),   
    path('customer/register/', views.CustomerRegisterView.as_view(), name='customer_register'),
    path('supplier/register/', views.SupplierRegisterView.as_view(), name='supplier_register'),
    path('choice/', views.ChoiceView.as_view(), name='choice'),
    path('customer/cart/<int:pk>/', views.CartView.as_view(), name='customer_cart'),
    path('cart_add/', views.CartItemView.as_view(), name='add_product')

]
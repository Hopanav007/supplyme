from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Sub_category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_categories'

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    sub_category = models.ForeignKey(Sub_category, related_name='categories', on_delete=models.CASCADE)
    class Meta:

        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("Region")
        verbose_name_plural = ("Regions")

    def __str__(self):
        return self.name


class Supplier(models.Model):
    user = models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='images/profile_images')
    title = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12)
    # password = password
    description = models.TextField()
    shipping_regions = models.ManyToManyField(Region, related_name="shipping_regions")

    class Meta:
        verbose_name = ("Supplier")
        verbose_name_plural = ("Suppliers")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("supplier_detail", kwargs={"pk": self.pk})

class Branch(models.Model):

    name = models.CharField(max_length=50)
    city = models.ForeignKey(Region, related_name="cities", on_delete=models.CASCADE)
    address = models.CharField(max_length = 150)
    supplier = models.ForeignKey(Supplier, related_name="suppliers", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("branch")
        verbose_name_plural = ("branchs")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("branch_detail", kwargs={"pk": self.pk})

class Product(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    poster = models.ImageField(upload_to="images/product_posters", height_field=None, width_field=None, max_length=None, default="product_images/image_2.jpg")
    supplier = models.ForeignKey(Supplier, related_name="product_supplier", on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, related_name="branch", on_delete=models.CASCADE)
    price = models.FloatField()
    cost = models.FloatField()

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):  
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

class ProductImages(models.Model):
    image = models.ImageField(upload_to="images/product_images", height_field=None, width_field=None, max_length=None)
    product = models.ForeignKey(Product, verbose_name=(""), on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("Product Image")
        verbose_name_plural = ("Product Images")

    def __str__(self):
        return f'{self.product.name} images'

    # def get_absolute_url(self):
        # return reverse("ProductImages_detail", kwargs={"pk": self.pk})

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='images/profile_images')
    title = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12)
    # password = password
    description = models.TextField()

    class Meta:
        verbose_name = ("Customer")
        verbose_name_plural = ("Customers")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
        # return reverse("Customer_detail", kwargs={"pk": self.pk})


class Delivery_point(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(Region, related_name="city", on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    postcode = models.CharField(max_length=12)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Delivery_point")
        verbose_name_plural = ("Delivery_points")

    def __str__(self):
        return f"{self.user} address = {self.address}"

    # def get_absolute_url(self
        # return reverse("Delivery_point_detail", kwargs={"pk": self.pk})



class Cart(models.Model):

    customer = models.OneToOneField(Customer, verbose_name=(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Cart")
        verbose_name_plural = ("Carts")

    def __str__(self):
        return self.customer.title

    def get_absolute_url(self):
        return reverse("customer_cart", kwargs={"pk": self.pk})

class Cart_item(models.Model):

    cart = models.ForeignKey(Cart, related_name="usercart", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    quantity = models.IntegerField()


    class Meta:
        verbose_name = ("cart_item")
        verbose_name_plural = ("cart_items")

    def __str__(self):
        return self.product.name

    # def get_absolute_url(self):
        # return reverse("cart_item_detail", kwargs={"pk": self.pk})


class Order(models.Model):

    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    cart = models.ForeignKey(Cart, related_name="cart", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name="customer", on_delete=models.CASCADE)
    delivery_point = models.ForeignKey(Delivery_point, related_name="delivery_point", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return f'{self.customer.title} delivery point: {self.delivery_point}' 

    # def get_absolute_url(self):
        # return reverse("Order_detail", kwargs={"pk": self.pk})





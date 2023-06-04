import os
import django
import random
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SupplyMe.settings')
django.setup()
from main.models import User, Supplier, Region, Branch, Category, Product



fake = Faker()
def generate_fake_user(num_records):
    for _ in range(num_records):
        # Generate fake data
        name = fake.name()
        email = fake.email()
        password = fake.password()

        # Create a new object using the generated data
        your_object = User.objects.create(username=name, email=email, password=password)
        your_object.save()

# Call the function to generate a specified number of fake records



def generate_fake_supplier(num_records):
    for i in range(num_records):
        # Generate fake data
        user = User.objects.get(pk=i+3)
        title = fake.company()
        phone = fake.phone_number()
        description = fake.text()
        regions = Region.objects.get(pk=random.randint(1, 2))


        # Create a new object using the generated data
        your_object = Supplier.objects.create(user = user, title = title, phone_number = phone, description = description)
        your_object.shipping_regions.add(regions)
        your_object.save()



def generate_fake_branch(num_records):
    for i in range(num_records):
        # Generate fake data
        supplier = Supplier.objects.get(pk=i+3)
        name = fake.address()
        regions = Region.objects.get(pk=random.randint(1, 2))


        # Create a new object using the generated data
        your_object = Branch.objects.create(name = name, supplier = supplier, address = name, city = regions)
        your_object.save()


def generate_fake_product(num_records):
    for i in range(num_records):
        # Generate fake data
        name = fake.ean(length=8)
        description = fake.text()
        price = random.randint(100, 2000)
        category = Category.objects.get(pk = random.randint(1,6))
        supplier = Supplier.objects.get(pk = random.randint(3,28))
        branch = Branch.objects.get(supplier = supplier)

        your_object = Product.objects.create(name = name, description = description, price = price, cost =price, category = category, supplier = supplier, branch = branch)
        your_object.save()

generate_fake_user(100)  # Generate 100 fake records
generate_fake_supplier(90)
generate_fake_branch(25)
generate_fake_product(100)
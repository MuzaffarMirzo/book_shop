from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLE_CHOICES = (
        ('client', 'client'),
        ('users', 'users'),
        ('seller', 'seller '),
    )

    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    user_role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='client')

    def str(self):
        return self.username

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def str(self):
        return f'{self.user.first_name}'


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def str(self):
        return f'{self.user.first_name}'
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='product_images', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.price * self.quantity

class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name

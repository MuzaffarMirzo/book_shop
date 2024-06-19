from django.contrib import admin
from .models import User, Client, Seller, Product,Category,Cart

admin.site.register([User,Client,Seller,Product,Category,Cart])

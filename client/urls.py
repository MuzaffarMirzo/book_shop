from django.urls import path
from .views import (HomeView,ProductDetailView,CartDeteilView,category_books, delete_cart,ProductSallerView,CreateBookView)

app_name='client'

urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('product/<int:product_id>/', ProductDetailView.as_view() ,name='deteil'),
    path('category/<int:category_id>/',category_books, name='category_books'),
    path('cart-deteil/', CartDeteilView.as_view(), name='cart_deteil'),
    path('seller-deteil/', ProductSallerView.as_view(), name='dashboard_seller'),
    path('delete-cart/<int:id>/',delete_cart, name='delete_cart'),
    path('add-book/', CreateBookView.as_view(), name='add_book'),

    
   
    
    
]





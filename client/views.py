from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from users.models import Product,Cart,Category
from users.models import User,Product
from users.peremissions import AdminRequiredMixin,SellerRequiredMixin
from users.forms import UpdateUserForm, AddBookForm


class UsersdashView(View):

    def get(self, request):
        user = User.objects.all()
        return render(request, 'dashboard.html', {'users': user})


class HomeView(View):
    def get(self, request):
        product = Product.objects.all()
        categorys=Category.objects.all()
        
        products = Product.objects.filter(in_stock=True)
        cart=Cart.objects.count()
        return render(request, 'client/home.html', context={'products': products,'product': product, 'cart': cart,'categorys':categorys })
def category_books(request, category_id):
    categorys=Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    product = category.products.all()
    return render(request, 'client/home.html', {'product': product, 'categorys': categorys})
    
class ProductDetailView(View):
    def get(self, request, product_id):
        categorys=Category.objects.all()
        product=get_object_or_404(Product, id=product_id)
        cart=Cart.objects.count()
        return render(request, 'client/deteil.html', context={'product': product, 'cart': cart, 'categorys': categorys})
    def post(self, request,product_id):
        product=get_object_or_404(Product, id=product_id)
        quantity=int(request.POST['cart'])
        if Cart.objects.filter(product=product).exists():
            cart=Cart.objects.filter(product=product).first()
            cart.quantity+=quantity
            cart.save()
        else:
            cart=Cart()
            cart.product=product
            cart.quantity=quantity
            cart.save()
        return redirect('client:home')
    

class CartDeteilView(View):
    def get(self, request):
        categorys=Category.objects.all()
        products=Cart.objects.all()
        cart=Cart.objects.count()
        return render(request, 'client/cart_deteil.html', {'products':products, 'cart':cart, 'categorys':categorys})
    


class UpdateUserView(AdminRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UpdateUserForm(instance=user)  
        return render(request, 'create.html', { 'form': form})
        

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():


            form.save()
            return redirect('dashboard')
        return render(request, 'create.html', {'form': form})

def delete(request, id):
    delet = get_object_or_404(User, id=id)
    delet.delete()
    return redirect('dashboard')


def deleteproduct(request, id):
    delet = get_object_or_404(Product, id=id)
    delet.delete()
    return redirect('client:home')



def delete_cart(request, id):
    delet = get_object_or_404(Cart, id=id)
    delet.delete()
    return redirect('client:home')



class ProductSallerView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'dashboard_seller.html', {'product': product})
    
class CreateBookView(SellerRequiredMixin, View):
    def get(self, request):
        form = AddBookForm()
        return render(request, 'add_book.html', context={"form":form})
    
    def post(self, request):
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client:home')
        return render(request, 'add_book.html', {'form': form})

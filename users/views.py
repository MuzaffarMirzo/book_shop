from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .peremissions import AdminRequiredMixin
from .models import User,Seller,Client
from django.db.models import Q


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        form = LoginForm()
        return render(request, 'login.html', {'form': form})


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'student':
                new_student = Client()
                new_student.user = user
                new_student.save()

            return redirect('/')
        return render(request, 'register.html', {'form': form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('client:home')
    




# class ProfileView(LoginRequiredMixin, View):
#     def get(self, request):
#         return render(request, 'profile.html')
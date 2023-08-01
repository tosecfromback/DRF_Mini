from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
# from .forms import LoginForm, RegisterForm

# Create your views here.
### User index
class UserIndex(View):
    def get(self, request):
        context = {
            'title' : 'User Index'
        }
        return render(request, 'user/user_index.html', context)
    def post(self, request):
        pass


### User login
class UserLogin(View):
    def get(self, request):
        context = {
            'title' : 'User Login'
        }
        return render(request, 'user/user_login.html', context)
    def post(self, request):
        pass


### User logout
class UserLogout(View):
    def get(self, request):
        context = {
            'title' : 'User Logout'
        }
        return render(request, 'user/user_logout.html', context)
    def post(self, request):
        pass


### User register
class UserRegister(View):
    def get(self, request):
        context = {
            'title' : 'User Register'
        }
        return render(request, 'user/user_register.html', context)
    def post(self, request):
        pass


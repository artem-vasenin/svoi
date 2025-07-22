from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'my_auth/login.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/shop/products')

        return render(request, 'my_auth/login.html', {'error': 'User is not found'})

class RegView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'my_auth/registration.html')

@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/auth/login')


from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'my_auth/login.html')

class RegView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'my_auth/registration.html')

@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/auth/login')


from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest

class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'my_auth/login.html')

class RegView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'my_auth/registration.html')


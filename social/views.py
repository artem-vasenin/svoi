from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpRequest

class DashboardView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return render(request, 'social/dashboard.html')
        return redirect('/auth/')

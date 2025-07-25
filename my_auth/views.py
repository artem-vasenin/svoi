from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy

from .forms import CustomRegForm
from .models import Profile

class RegView(FormView):
    template_name = 'my_auth/registration.html'
    form_class = CustomRegForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(
            user=user,
            phone=form.cleaned_data['phone'],
            birthday=form.cleaned_data['birthday'],
            reason=form.cleaned_data['reason'],
        )
        return super().form_valid(form)

@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/auth')


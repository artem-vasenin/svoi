from django.urls import path
from django.contrib.auth.views import LoginView

from .views import RegView, logout_view
from .forms import CustomLoginForm

app_name = 'my_auth'

urlpatterns = [
    path('', LoginView.as_view(
        template_name='my_auth/login.html',
        redirect_authenticated_user=True,
        authentication_form=CustomLoginForm,
    ), name='login'),
    path('registration/', RegView.as_view(), name='registration'),
    path('logout/', logout_view, name='logout'),
]
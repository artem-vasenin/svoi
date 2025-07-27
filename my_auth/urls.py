from django.urls import path
from django.contrib.auth.views import LoginView

from .views import RegView, logout_view, CodeView
from .forms import CustomLoginForm

app_name = 'my_auth'

urlpatterns = [
    path('', LoginView.as_view(
        template_name='my_auth/login.html',
        redirect_authenticated_user=True,
        authentication_form=CustomLoginForm,
    ), name='login'),
    path('registration/', RegView.as_view(), name='registration'),
    path('code/', CodeView.as_view(), name='code'),
    path('logout/', logout_view, name='logout'),
]
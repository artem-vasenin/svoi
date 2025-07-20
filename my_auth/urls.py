from django.urls import path

from .views import LoginView, RegView, logout_view

app_name = 'my_auth'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('registration/', RegView.as_view(), name='registration'),
    path('logout/', logout_view, name='logout'),
]
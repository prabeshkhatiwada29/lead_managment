from django.urls import path
from .views.auth_views import renderRegisterForm, renderLoginForm , forget_password


app_name = 'accounts'

urlpatterns = [
    path('register/', renderRegisterForm, name='register'),
    path('login/', renderLoginForm, name='login'),

    path('forget/', forget_password, name='forget_password'),

]

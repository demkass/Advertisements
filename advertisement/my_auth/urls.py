from django.urls import path
from .views import *

urlpatterns = [
    path('register', reg_view, name='reg'), # Регистрация 
    path('profile', profile_view, name='prof'), # Профиль
    path('login', login_view, name='log'), # Войти
    path('logout', logout_view, name='logout') # Выйти
]
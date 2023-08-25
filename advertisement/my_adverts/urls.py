from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('index.html', index, name='main_page2'),
    path('top-sellers.html', topSellers, name='top-sellers'),
    path('advertisement-post.html', advertisement_post, name='adv-post'),
    path('register.html', register, name='reg'),
    path('login.html', login, name='log'),
    path('profile.html', profile, name='prof'),
    path('advertisement.html', advertisement_detail, name='adv-detail'),
    path('login.html', logout_view, name='logout')
]
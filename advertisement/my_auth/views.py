from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm

def reg_view(request): # Регистрация 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('prof')  
    else:
        form = UserCreationForm()
    return render(request, 'app_auth/register.html', {'form': form})

@login_required(login_url=reverse_lazy('log')) # Профиль
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request): # Войти
    redirect_url = reverse('prof')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error": "Пользователь не найден."})

def logout_view(request): # Выйти
    logout(request)
    return redirect(reverse('log'))
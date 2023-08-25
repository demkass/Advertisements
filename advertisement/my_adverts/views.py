from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement

def index (request):
    adverts = Advertisement.objects.all()
    context = {'adverts': adverts}
    return render(request,'app_adverts/index.html', context)

def topSellers (request):
    return render(request,'app_adverts/top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main_page2')
            return redirect(url)
    else:
        form = AdvertisementForm()  
    context = {'form': form}
    return render(request, 'app_adverts/advertisement-post.html', context)

def register (request):
    return render(request,'app_auth/register.html')

def login (request):
    return render(request,'app_auth/login.html')

def profile (request):
    return render(request,'app_auth/profile.html')

def advertisement_detail (request):
    return render(request,'app_adverts/advertisement.html')

def logout_view (request):
    return render(request,'app_adverts/login.html')
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'core/home.html')

def about_us_view(request):
    return render(request, 'core/about_us.html')

def login_view(request):
    return render(request, 'core/login.html')

def register_view(request):
    return render(request, 'core/register.html')

def contact_view(request):
    return render(request, 'core/contact.html')
from django.shortcuts import render
from cursos.models import Course
from blog.models import Post

# Create your views here.
def home_view(request):
    context = {
        'courses': Course.objects.filter(show_home=True),
        'posts': Post.objects.filter(show_home=True)
    }
    return render(request, 'core/home.html', context)

def about_us_view(request):
    return render(request, 'core/about_us.html')

def login_view(request):
    return render(request, 'core/login.html')

def register_view(request):
    return render(request, 'core/register.html')

def contact_view(request):
    return render(request, 'core/contact.html')
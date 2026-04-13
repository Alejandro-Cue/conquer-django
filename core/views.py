from django.shortcuts import render
from cursos.models import Course
from blog.models import Post
from conquerblocks.forms import ContactForm
from django.core.mail import send_mail
from core.models import Contact

# from .forms import ContactForm

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
    if request.POST:
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            email = formulario.cleaned_data.get('email')
            comentario = formulario.cleaned_data.get('comentario')
            message_content = f'Nombre: {nombre}, Email: {email}, Comentario: {comentario}'

            Contact.objects.create(
                nombre=nombre,
                email=email,
                comentario=comentario
            )

            success = send_mail(
                "Formulario de contacto de mi web",
                message_content,
                "alejcue@gmail.com",
                ["alejcue@gmail.com"],
                fail_silently=False,
                
            )

            context = {
                'form': ContactForm(),
                'success': True
            }
            return render(request, 'core/contact.html', context)
        else:
            context = {
                'form': formulario
            }
            return render(request, 'core/contact.html', context)

    formulario = ContactForm()
    context = {
        'form': formulario
    }
    return render(request, 'core/contact.html', context)
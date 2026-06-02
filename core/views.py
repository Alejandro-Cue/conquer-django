from django.shortcuts import render
from cursos.models import Course
from blog.models import Post
from conquerblocks.forms import ContactForm, LoginForm, UserRegisterForm
from django.core.mail import send_mail
from core.models import Contact
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
# from .forms import ContactForm
from django.contrib.auth.models import User

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
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('core:home'))
            else:
                context = {
                    'form': form,
                    'error': True,
                    'error_message': 'Credenciales inválidas. Por favor, inténtalo de nuevo.',
                }
                return render(request, 'core/login.html', context)
        else:
            context = {
                'form': form,
                'error': True,
                'error_message': 'Credenciales inválidas. Por favor, inténtalo de nuevo.',
            }
            return render(request, 'core/login.html', context)
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'core/login.html', context)
    
def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))

def register_view(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password1
                
            )
            user.save()
            context = {
                'msg': 'Usuario registrado exitosamente. Ahora puedes iniciar sesión.'
            }
            return render(request, 'core/register.html', context)
        else:
            context = {
                'form': form,
                'error': True,
                'error_message': 'Usuario no válido.',
            }
            return render(request, 'core/register.html', context)
    
    formulario_vacio = UserRegisterForm()
    context = {
        'form': formulario_vacio
    }
    return render(request, 'core/register.html', context)

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
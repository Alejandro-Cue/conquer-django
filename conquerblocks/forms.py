from django import forms
from django.contrib.auth.password_validation import validate_password

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo Electrónico')
    comentario = forms.CharField(widget=forms.Textarea, label='Comentario')

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and '@' not in email:
            raise forms.ValidationError('El correo electrónico no es válido.')
        return email
    

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Nombre de Usuario'
    )
    password = forms.CharField(
        widget=forms.PasswordInput, 
        label='Contraseña'
    )

class UserRegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Nombre de Usuario'
    )
    first_name= forms.CharField(
        max_length=30,
        label='Nombre'
    )
    last_name= forms.CharField(
        max_length=30,
        label='Apellidos'
    )
    email = forms.EmailField(
        label='Correo Electrónico',
        max_length=150
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        required=False, 
        label='Contraseña',
        help_text='Si no se establece contraseña se generará una automáticamente.'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        required=False, 
        label='Confirmar Contraseña',
        help_text='Repite la contraseña.'
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != '' and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        
        if password2 != '':
            validate_password(password2)
        return password2

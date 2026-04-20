from django.urls import path
from .views import home_view, about_us_view, login_view, register_view, contact_view, logout_view

app_name = 'core'

urlpatterns = [
    path('', home_view, name='home'),
    path('about_us/', about_us_view, name='about_us'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('contact/', contact_view, name='contact'),
    path('logout/', logout_view, name='logout'),
]

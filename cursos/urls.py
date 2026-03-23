from django.urls import path, include
from .views import cursos_list_view, cursos_detail_view

app_name = 'cursos'

urlpatterns = [
    path('', cursos_list_view, name='cursos_list'),
    path('<int:id>/', cursos_detail_view, name='cursos_detail'),
]
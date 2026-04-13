from django.shortcuts import render
from .models import Course

# Create your views here.
def cursos_list_view(request):
    all_courses = Course.objects.all()
    context = {
        'courses': all_courses
    }
    return render(request, 'cursos/cursos_list.html', context)

def cursos_detail_view(request, id):
    course = Course.objects.get(pk=id)
    context = {
        'course': course
    }
    return render(request, 'cursos/cursos_detail.html', context)


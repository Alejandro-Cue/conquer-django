from django.shortcuts import render
from .models import Course
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cursos_list_view(request):
    all_courses = Course.objects.all()
    context = {
        'courses': all_courses
    }
    return render(request, 'cursos/cursos_list.html', context)

@login_required
def cursos_detail_view(request, id):
    course = Course.objects.get(pk=id)
    context = {
        'course': course
    }
    return render(request, 'cursos/cursos_detail.html', context)


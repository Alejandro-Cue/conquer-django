from django.shortcuts import render

# Create your views here.
def cursos_list_view(request):
    return render(request, 'cursos/cursos_list.html')

def cursos_detail_view(request, id):
    return render(request, 'cursos/cursos_detail.html')
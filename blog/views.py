from django.shortcuts import render

# Create your views here.
def blog_list_view(request):
    return render(request, 'blog/blog_list.html')

def blog_detail_view(request, id):
    return render(request, 'blog/blog_detail.html', {'id': id})
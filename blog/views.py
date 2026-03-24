from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_list_view(request):
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail_view(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'post': post
    }
    return render(request, 'blog/blog_detail.html', context)
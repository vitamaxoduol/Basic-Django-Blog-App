from django.shortcuts import render
from .models import BlogPost


def blog_list(request):
    posts = BlogPost.objects.all().order_by('published_date')
    return render(request, 'blog/blog_list.html', {'posts': posts})

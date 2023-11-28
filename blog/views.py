from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import BlogPostSerializer


class BlogPostListView(ListView):
    # posts = BlogPost.objects.all().order_by('published_date')
    # return render(request, 'blog/blog_list.html', {'posts': posts})

    model = BlogPost
    template_name = 'blogpost_list.html'
    
    
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'
    
class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_create.html'
    success_url = reverse_lazy('blogpost_list')
    
class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model =  BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_update.html'
    success_url = reverse_lazy('blogpost_list')
    
class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = "blogpost_delete.html"
    success_url = reverse_lazy('blogpost_list')
    
class BlogPostViewSet(viewsets.ModelsViewSet):
    queryset = BlogPost.objects.all()
    serializers_class = BlogPostSerializer
    
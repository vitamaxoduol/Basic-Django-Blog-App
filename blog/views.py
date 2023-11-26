from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm
from django.urls import reverse_lazy


class BlogPostListView(ListView):
    # posts = BlogPost.objects.all().order_by('published_date')
    # return render(request, 'blog/blog_list.html', {'posts': posts})

    model = BlogPost
    template_name = 'blogpost_list.html'
    
    
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'
    
class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_create.html'
    success_url = reverse_lazy('blogpost_list')
    
class BlogPostUpdateView(UpdateView):
    model =  BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_update.html'
    success_url = reverse_lazy('blogpost_list')
    
class BlogPostDeleteView(DeleteView):
    models = BlogPost
    template_name = "blogpost_delete.html"
    success_url = reverse_lazy('blogpost_list')
    
from django.urls import path, include
from .views import (BlogPostCreateView, BlogPostListView, 
                    BlogPostUpdateView, BlogPostDetailView, 
                    BlogPostDeleteView)
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register(r'post', views.BlogPostViewSet)



urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('post/new', BlogPostCreateView.as_view(), name='blogpost_new'),
    path('post/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('post/<int:pk>/delete', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('api', include(router.urls)),
    
]

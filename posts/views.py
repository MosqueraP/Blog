from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post, PostView, Like, Comment

from posts.models import Post

# Create your views here.

# vista ListView mustra todos los contenidos del modelo
class PostLisView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post

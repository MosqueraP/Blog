from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post, PostView, Like, Comment
from posts.forms import PostForm

# Create your views here.

# vista ListView mustra todos los contenidos del modelo
class PostLisView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/' # redireccionar a la misma vista en la que se invoca
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'create'
        })
        return context

# Actualizar
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/' # redireccionar a la misma vista en la que se invoca

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/' # redireccionar a la misma vista en la que se invoca

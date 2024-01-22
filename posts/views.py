# from typing import Any
from typing import Any
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post, PostView, Like, Comment
from posts.forms import PostForm, CommentForm

# Create your views here.

# vista ListView mustra todos los contenidos del modelo
class PostLisView(ListView):
    model = Post
    

    
class PostDetailView(DetailView):
    model = Post

    # funcionalidad para crear comentarios
    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid:
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context

    # visualizar las vista de los post, si el user es autenticado
    def get_object(self, **kwargs):
        object=super().get_object(**kwargs)

        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)
                        
        return object

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/' # redireccionar a la misma vista en la que se invoca
    

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

# Funcionalidad de los likes
def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
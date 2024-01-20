from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission # usuario base
from django.shortcuts import reverse

# Create your models here.

class User(AbstractUser):
    pass
    
    def __str__(self):
        return self.username
    


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
        
    @property
    def get_comment_count(self):
        return self.comment_set.all().count() # contar commentarios en los post
    
    @property
    def get_view_count(self):
        return self.postview_set.all().count() # contar commentarios en los post
    
    @property
    def get_like_count(self):
        return self.like_set.all().count() # contar commentarios en los post
    



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) # tiempo de creacion comentarios 
    content = models.TextField()
    
    def __str__(self):
        return self.user.username # quien hizo el comentario
    

# fecha de creacion del post
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) # tiempo de creacion comentarios 

    def __str__(self):
        return self.user.username # quien hizo el comentario

#ver los like y quien lo ha creado
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username # quien hizo el comentario


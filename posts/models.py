from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    content = models.TextField()
    image = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    # autor = models.Foreinkey()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    #user = models.Foreinkey()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) # tiempo de creacion comentarios 
    content = models.TextField()
    
    def __str__(self):
        return self.user.username # quien hizo el comentario
    
# fecha de creacion del post
class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) # tiempo de creacion comentarios 

    def __str__(self):
        return self.user.username # quien hizo el comentario

#ver los like y quien lo ha creado
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username # quien hizo el comentario


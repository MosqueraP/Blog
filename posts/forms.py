from django import forms
from posts.models import Post, Comment

# formulario para crear y actualizar post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__') # traer todos los campos de la clase Post

# formulario para crear y actualizar el conetnido de comentasrios
class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))

    class Meta:
        model = Comment
        fields = ('content', ) #tupla # traer el campo de la clase Comment


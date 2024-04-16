from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import Comment, CommentLike, Blog, Tag

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'content')


class CommentLikeForm(forms.ModelForm):
    class Meta:
        model = CommentLike
        fields = ['user']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
